---
description: The following example shows how to consume event data using the TdhGetProperty function.
ms.assetid: 16b36718-087f-4be9-9ca2-fc083358017b
title: Using TdhGetProperty to Consume Event Data
ms.topic: article
ms.date: 05/31/2018
---

# Using TdhGetProperty to Consume Event Data

The following example shows how to consume event data using the [**TdhGetProperty**](/windows/win32/api/tdh/nf-tdh-tdhgetproperty) function.

> [!IMPORTANT]
> TdhGetProperty is not recommended for new code.
>
> - For non-WPP events, extracting property values using TdhGetProperty is very inefficient, as it requires scanning the event's properties each time the TdhGetProperty API is called. Refer to [the TdhFormatProperty sample](./using-tdhformatproperty-to-consume-event-data.md) for a more efficient pattern for reading property values.
> - For WPP events, the TdhGetWppProperty and TdhGetWppMessage APIs are more flexible than TdhGetProperty. For example, the TdhGetWpp\* APIs can load WPP decoding information from PDB files. Consider using TdhGetWppProperty or TdhGetWppMessage instead of TdhGetProperty when decoding WPP events.

```C++
/*
Sample for decoding ETW events using TdhGetProperty.

IMPORTANT: TdhGetProperty is not recommended for new code.

- Extracting property values from non-WPP events using TdhGetProperty is very
  inefficient, as it requires scanning the event's properties each time the
  TdhGetProperty API is called. Refer to the TdhFormatProperty sample for a
  more efficient pattern for reading property values.
- The TdhGetWppProperty and TdhGetWppMessage APIs are more efficient and more
  flexible than TdhGetProperty. For example, the TdhGetWpp* APIs can load WPP
  decoding information from PDB files. Consider using TdhGetWppProperty or
  TdhGetWppMessage instead of TdhGetProperty when decoding WPP events.

This sample demonstrates the following:

- How to process events from ETL files using OpenTrace and ProcessTrace.
- How to get TRACE_EVENT_INFO data for an event using TdhGetEventInformation.
- How to format a WPP message using TdhGetProperty.
- How to extract property values from non-WPP events using TdhGetProperty.
- How to format map (enum) values using the EVENT_MAP_INFO data returned by
  TdhGetEventMapInformation.
*/

#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN 1 // Exclude rarely-used APIs from <windows.h>
#endif

#include <windows.h>

#define INITGUID // Ensure that EventTraceGuid is defined.
#include <evntrace.h>
#undef INITGUID

#include <sddl.h> // ConvertSidToStringSid
#include <tdh.h>
#include <vector>

#include <wchar.h> // wprintf
#include <stdlib.h> // _byteswap_ushort

#pragma comment(lib, "tdh.lib") // Link against TDH.dll

// Support building this sample using older versions of the Windows SDK:
#define EventNameOffset                       ActivityIDNameOffset
#define EventAttributesOffset                 RelatedActivityIDNameOffset
#define TDH_INTYPE_MANIFEST_COUNTEDSTRING     static_cast<_TDH_IN_TYPE>(22)
#define TDH_INTYPE_MANIFEST_COUNTEDANSISTRING static_cast<_TDH_IN_TYPE>(23)
#define TDH_INTYPE_MANIFEST_COUNTEDBINARY     static_cast<_TDH_IN_TYPE>(25)
#define TDH_OUTTYPE_CODE_POINTER              static_cast<_TDH_OUT_TYPE>(37)

/*
Decodes event data using TdhGetEventInformation and TdhGetProperty. Prints the
event information to stdout.

We use a context object so we can reuse buffers instead of allocating new
buffers and freeing them for each event.
*/
class DecoderContext
{
public:

    /*
    Initialize the decoder context.
    Sets up the TDH_CONTEXT array that will be used for decoding.
    */
    explicit DecoderContext(
        _In_opt_ LPCWSTR szTmfSearchPath)
    {
        TDH_CONTEXT* p = m_tdhContext;

        if (szTmfSearchPath != nullptr)
        {
            p->ParameterValue = reinterpret_cast<UINT_PTR>(szTmfSearchPath);
            p->ParameterType = TDH_CONTEXT_WPP_TMFSEARCHPATH;
            p->ParameterSize = 0;
            p += 1;
        }

        m_tdhContextCount = static_cast<BYTE>(p - m_tdhContext);
    }

    /*
    Decode and print the data for an event.
    Might throw an exception for out-of-memory conditions. Caller should catch
    the exception before returning from the ProcessTrace callback.
    */
    void PrintEventRecord(
        _In_ EVENT_RECORD* pEventRecord)
    {
        if (pEventRecord->EventHeader.EventDescriptor.Opcode == EVENT_TRACE_TYPE_INFO &&
            pEventRecord->EventHeader.ProviderId == EventTraceGuid)
        {
            /*
            The first event in every ETL file contains the data from the file header.
            This is the same data as was returned in the EVENT_TRACE_LOGFILEW by
            OpenTrace. Since we've already seen this information, we'll skip this
            event.
            */
            return;
        }

        // Reset state to process a new event.
        m_indentLevel = 1;
        m_pEvent = pEventRecord;
        m_pdd.clear();

        // There is a lot of information available in the event even without decoding,
        // including timestamp, PID, TID, provider ID, activity ID, and the raw data.

        // Show the event timestamp.
        PrintFileTime(reinterpret_cast<FILETIME const&>(m_pEvent->EventHeader.TimeStamp));

        if (IsWppEvent())
        {
            // The PrintEvent method works correctly for WPP events, but it
            // generates fairly verbose output. Treat WPP events as a special
            // case and generate more compact output for them.
            PrintWppEvent();
        }
        else
        {
            PrintEvent();
        }
    }

private:

    /*
    Print the primary properties for a WPP event.
    */
    void PrintWppEvent()
    {
        /*
        TDH supports a set of known properties for WPP events:
        - "Version": UINT32 (usually 0)
        - "TraceGuid": GUID
        - "GuidName": UNICODESTRING (module name)
        - "GuidTypeName": UNICODESTRING (source file name and line number)
        - "ThreadId": UINT32
        - "SystemTime": SYSTEMTIME
        - "UserTime": UINT32
        - "KernelTime": UINT32
        - "SequenceNum": UINT32
        - "ProcessId": UINT32
        - "CpuNumber": UINT32
        - "Indent": UINT32
        - "FlagsName": UNICODESTRING
        - "LevelName": UNICODESTRING
        - "FunctionName": UNICODESTRING
        - "ComponentName": UNICODESTRING
        - "SubComponentName": UNICODESTRING
        - "FormattedString": UNICODESTRING
        - "RawSystemTime": FILETIME
        - "ProviderGuid": GUID (usually 0)
        */

        // Since WPP events always have the same properties, there is no need
        // to query TdhGetEventInformation to find the list of properties.
        // We'll just use TdhGetProperty to get the properties we need.
        wprintf(L" ");
        PrintWppStringProperty(L"GuidName"); // Module name (WPP's "CurrentDir" variable)
        wprintf(L" ");
        PrintWppStringProperty(L"GuidTypeName"); // Source code file name + line number
        wprintf(L" ");
        PrintWppStringProperty(L"FunctionName");
        wprintf(L"\n");
        PrintIndent();
        PrintWppStringProperty(L"FormattedString");
        wprintf(L"\n");
    }

    /*
    Print the value of the given UNICODESTRING property.
    */
    void PrintWppStringProperty(_In_z_ LPCWSTR szPropertyName)
    {
        // Assume that the property name corresponds to a UNICODESTRING property.
        // Assume that the PROPERTY_DATA_DESCRIPTOR stack is empty.

        // Put the property name onto the stack.
        PushPdd(szPropertyName);

        // Call TdhGetProperty using a the current PROPERTY_DATA_DESCRIPTOR
        // stack (should have just one item on the stack right now). If
        // successful, put the property data into m_propertyBuffer.
        ULONG status = GetProperty();

        // Clear the PROPERTY_DATA_DESCRIPTOR stack.
        PopPdd();

        if (status != ERROR_SUCCESS)
        {
            wprintf(L"[TdhGetProperty(%ls) error %u]", szPropertyName, status);
        }
        else
        {
            // Print the FormattedString property data (nul-terminated
            // wchar_t string).
            wprintf(L"%ls", reinterpret_cast<LPCWSTR>(m_propertyBuffer.data()));
        }
    }

    /*
    Use TdhGetEventInformation to obtain information about this event
    (including the names and types of the event's properties). Print some
    basic information about the event (provider name, event name), then print
    each property (using TdhGetProperty to read each property value).
    */
    void PrintEvent()
    {
        ULONG status;
        ULONG cb;

        // Try to get event decoding information from TDH.
        cb = static_cast<ULONG>(m_teiBuffer.size());
        status = TdhGetEventInformation(
            m_pEvent,
            m_tdhContextCount,
            m_tdhContextCount ? m_tdhContext : nullptr,
            reinterpret_cast<TRACE_EVENT_INFO*>(m_teiBuffer.data()),
            &cb);
        if (status == ERROR_INSUFFICIENT_BUFFER)
        {
            m_teiBuffer.resize(cb);
            status = TdhGetEventInformation(
                m_pEvent,
                m_tdhContextCount,
                m_tdhContextCount ? m_tdhContext : nullptr,
                reinterpret_cast<TRACE_EVENT_INFO*>(m_teiBuffer.data()),
                &cb);
        }

        if (status != ERROR_SUCCESS)
        {
            // TdhGetEventInformation failed so there isn't a lot we can do.
            // The provider ID might be helpful in tracking down the right
            // manifest or TMF path.
            wprintf(L" ");
            PrintGuid(m_pEvent->EventHeader.ProviderId);
            wprintf(L"\n");
        }
        else
        {
            // TDH found decoding information. Print some basic info about the event,
            // then format the event contents.

            TRACE_EVENT_INFO const* const pTei =
                reinterpret_cast<TRACE_EVENT_INFO const*>(m_teiBuffer.data());

            if (pTei->ProviderNameOffset != 0)
            {
                // Event has a provider name -- show it.
                wprintf(L" %ls", TeiString(pTei->ProviderNameOffset));
            }
            else
            {
                // No provider name so print the provider ID.
                wprintf(L" ");
                PrintGuid(m_pEvent->EventHeader.ProviderId);
            }

            // Show core important event properties - try to show some kind of "event name".
            if (pTei->DecodingSource == DecodingSourceWbem ||
                pTei->DecodingSource == DecodingSourceWPP)
            {
                // OpcodeName is usually the best "event name" property for WBEM/WPP events.
                if (pTei->OpcodeNameOffset != 0)
                {
                    wprintf(L" %ls", TeiString(pTei->OpcodeNameOffset));
                }

                wprintf(L"\n");
            }
            else
            {
                if (pTei->EventNameOffset != 0)
                {
                    // Event has an EventName, so print it.
                    wprintf(L" %ls", TeiString(pTei->EventNameOffset));
                }
                else if (pTei->TaskNameOffset != 0)
                {
                    // EventName is a recent addition, so not all events have it.
                    // Many events use TaskName as an event identifier, so print it if present.
                    wprintf(L" %ls", TeiString(pTei->TaskNameOffset));
                }

                wprintf(L"\n");

                // Show EventAttributes if available.
                if (pTei->EventAttributesOffset != 0)
                {
                    PrintIndent();
                    wprintf(L"EventAttributes: %ls\n", TeiString(pTei->EventAttributesOffset));
                }
            }

            if (IsStringEvent())
            {
                // The event was written using EventWriteString.
                // We'll handle it later.
            }
            else
            {
                // The event is a MOF, manifest, or TraceLogging event.

                // To help resolve PropertyParamCount and PropertyParamLength,
                // we will record the values of all integer properties as we
                // reach them. Before we start, clear out any old values and
                // resize the vector with room for the new values.
                m_integerValues.clear();
                m_integerValues.resize(pTei->PropertyCount);

                // Recursively print the event's properties.
                PrintProperties(0, pTei->TopLevelPropertyCount);
            }
        }

        if (IsStringEvent())
        {
            // The event was written using EventWriteString.
            // We can print it whether or not we have decoding information.
            LPCWSTR pchData = static_cast<LPCWSTR>(m_pEvent->UserData);
            unsigned cchData = m_pEvent->UserDataLength / 2;
            PrintIndent();

            // It's probably nul-terminated, but just in case, limit to cchData chars.
            wprintf(L"%.*ls\n", cchData, pchData);
        }
    }

    /*
    Prints out the values of properties from begin..end.
    Called by PrintEventRecord for the top-level properties.
    If there are structures, this will be called recursively for the child
    properties.
    */
    void PrintProperties(unsigned propBegin, unsigned propEnd)
    {
        TRACE_EVENT_INFO const* const pTei =
            reinterpret_cast<TRACE_EVENT_INFO const*>(m_teiBuffer.data());

        for (unsigned propIndex = propBegin; propIndex != propEnd; propIndex += 1)
        {
            EVENT_PROPERTY_INFO const& epi = pTei->EventPropertyInfoArray[propIndex];

            PrintIndent();

            // Print the property's name.
            wprintf(L"%ls:", epi.NameOffset ? TeiString(epi.NameOffset) : L"(noname)");

            // The array of PROPERTY_DATA_DESCRIPTORs that we pass to
            // TdhGetProperty makes a path that describes the property
            // we want to access. If the property is a top-level property,
            // we only need one PROPERTY_DATA_DESCRIPTOR to identify it.
            // If we want to access a child property (nested within a
            // structure), we need to provide a full path from the top-
            // level property to the child property, with one
            // PROPERTY_DATA_DESCRIPTOR for each level of nesting.
            // To create this path, we have a stack of
            // PROPERTY_DATA_DESCRIPTORs.

            // Add the property to the stack of PROPERTY_DATA_DESCRIPTORs
            // that will be used when we call TdhGetProperty. For top-level
            // properties, there will be only one PROPERTY_DATA_DESCRIPTOR in
            // the stack, but for child properties there may be two or more.
            unsigned const pddIndex = PushPdd(epi.NameOffset ? TeiString(epi.NameOffset) : L"");
            m_indentLevel += 1;

            // We recorded the values of all previous integer properties just
            // in case we need to determine the array count for a variable-size
            // array (PropertyParamCount).
            USHORT const arrayCount =
                (epi.Flags & PropertyParamCount)
                ? m_integerValues[epi.countPropertyIndex] // Look up the value of a previous property
                : epi.count;

            // Note that PropertyParamFixedCount is a new flag and is ignored
            // by many decoders. Without the PropertyParamFixedCount flag,
            // decoders will assume that a property is an array if it has
            // either a count parameter or a fixed count other than 1. The
            // PropertyParamFixedCount flag allows for fixed-count arrays with
            // one element to be propertly decoded as arrays.
            bool isArray =
                1 != arrayCount ||
                0 != (epi.Flags & (PropertyParamCount | PropertyParamFixedCount));
            if (isArray)
            {
                wprintf(L" Array[%u]\n", arrayCount);
            }

            // Treat non-array properties as arrays with one element.
            for (unsigned arrayIndex = 0; arrayIndex != arrayCount; arrayIndex += 1)
            {
                m_pdd[pddIndex].ArrayIndex = arrayIndex;

                if (isArray)
                {
                    // Print a name for the array element.
                    PrintIndent();
                    wprintf(L"%ls[%lu]:",
                        epi.NameOffset ? TeiString(epi.NameOffset) : L"(noname)",
                        arrayIndex);
                }

                if (epi.Flags & PropertyStruct)
                {
                    // If this property is a struct, recurse and print the child
                    // properties.
                    wprintf(L"\n");
                    PrintProperties(
                        epi.structType.StructStartIndex,
                        epi.structType.StructStartIndex + epi.structType.NumOfStructMembers);
                    continue;
                }

                // Call TdhGetProperty using the PROPERTY_DATA_DESCRIPTORs that are
                // currently on our PROPERTY_DATA_DESCRIPTOR stack. If successful,
                // put the property data into m_propertyBuffer.
                ULONG status = GetProperty();
                if (status != ERROR_SUCCESS)
                {
                    wprintf(L" TdhGetProperty error %u\n", status);
                    continue;
                }

                if (!isArray)
                {
                    // If the property is an integer, save it in case we need it later
                    // to resolve a PropertyParamCount reference.
                    USHORT& integerValue = m_integerValues[propIndex];
                    void const* pData = m_propertyBuffer.data();
                    switch (epi.nonStructType.InType)
                    {
                    case TDH_INTYPE_UINT8:
                    case TDH_INTYPE_INT8:
                        integerValue = *static_cast<UINT8 const*>(pData);
                        break;
                    case TDH_INTYPE_INT16:
                    case TDH_INTYPE_UINT16:
                    case TDH_INTYPE_INT32:
                    case TDH_INTYPE_UINT32:
                    case TDH_INTYPE_HEXINT32:
                        integerValue = *static_cast<UINT16 const*>(pData);
                        break;
                    }
                }

                wprintf(L" ");

                // Print the data in m_propertyBuffer.
                PrintPropertyValue(
                    epi.nonStructType.InType,
                    epi.nonStructType.OutType,
                    epi.nonStructType.MapNameOffset);
                wprintf(L"\n");
            }

            PopPdd();
            m_indentLevel -= 1;
        }
    }

    /*
    Prints the data in m_propertyBuffer.

    For details on valid intype and outtype values, refer to winmeta.xml and
    tdh.h.

    This function assumes that m_propertyBuffer is correctly-sized for the
    data type. For example, it assumes that when inType is UINT32,
    m_propertyBuffer.size() == 4.
    */
    void PrintPropertyValue(USHORT inType, USHORT outType, unsigned mapNameOffset)
    {
        void* const pData = m_propertyBuffer.data();
        unsigned const cData = static_cast<unsigned>(m_propertyBuffer.size());

        switch (inType)
        {
        case TDH_INTYPE_UNICODESTRING:
        case TDH_INTYPE_NONNULLTERMINATEDSTRING: // WBEM, deprecated

            /*
            Note that the UNICODESTRING type may or may not be nul-terminated.
            If the property has a non-zero length, has a PropertyParamLength
            flag, or has a PropertyParamFixedLength flag, then the length is
            the length of the string (in characters). Otherwise, the string is
            nul-terminated. This sample does not distinguish between these
            cases and prints to the end of the buffer or the nul, whichever
            comes first. (This behavior also works well for the
            NONNULLTERMINATEDSTRING type.)
            */

            // Valid outtypes: string, xml, json
            wprintf(L"%.*ls", cData / 2, static_cast<LPCWSTR>(pData));
            break;

        case TDH_INTYPE_ANSISTRING:
        case TDH_INTYPE_NONNULLTERMINATEDANSISTRING: // WBEM, deprecated

            /*
            Like UNICODESTRING, the ANSISTRING type may or may not be
            nul-terminated based on the flags and length.

            This sample does not distinguish between the possible encodings
            used by the ANSISTRING data types. In particular, data using the
            xml, json, or utf8 outtype should be treated as utf-8, while data
            using the string or default outtype is treated as using an
            unspecified code page (typically the decoding machine's default
            code page is used).
            */

            // Valid outtypes: string, xml, json, utf8
            wprintf(L"%.*hs", cData, static_cast<LPCSTR>(pData));
            break;

        case TDH_INTYPE_INT8:

            // Valid outtypes: byte, string
            switch (outType)
            {
            default:
                wprintf(L"%i", *static_cast<signed char*>(pData));
                break;
            case TDH_OUTTYPE_STRING:
                wprintf(L"%c", *static_cast<unsigned char*>(pData));
                break;
            }
            break;

        case TDH_INTYPE_UINT8:

            // UINT8 properties might have an associated map.
            if (mapNameOffset != 0 &&
                PrintMapString(mapNameOffset, *static_cast<unsigned char*>(pData)))
            {
                break;
            }

            // Valid outtypes: unsignedByte, HexInt8, boolean, string
            switch (outType)
            {
            default: // treat boolean as integer
                wprintf(L"%u", *static_cast<unsigned char*>(pData));
                break;
            case TDH_OUTTYPE_HEXINT8:
                wprintf(L"0x%x", *static_cast<unsigned char*>(pData));
                break;
            case TDH_OUTTYPE_STRING:
                wprintf(L"%hc", *static_cast<unsigned char*>(pData));
                break;
            }
            break;

        case TDH_INTYPE_INT16:

            // Valid outtypes: short
            wprintf(L"%i", *static_cast<short*>(pData));
            break;

        case TDH_INTYPE_UINT16:

            // UINT16 properties might have an associated map.
            if (mapNameOffset != 0 &&
                PrintMapString(mapNameOffset, *static_cast<unsigned short*>(pData)))
            {
                break;
            }

            // Valid outtypes: unsignedShort, port, HexInt16, string
            switch (outType)
            {
            default:
                wprintf(L"%u", *static_cast<unsigned short*>(pData));
                break;
            case TDH_OUTTYPE_PORT:
                wprintf(L"%u", _byteswap_ushort(*static_cast<unsigned short*>(pData)));
                break;
            case TDH_OUTTYPE_HEXINT16:
                wprintf(L"0x%x", *static_cast<unsigned short*>(pData));
                break;
            case TDH_OUTTYPE_STRING:
                wprintf(L"%lc", *static_cast<unsigned short*>(pData));
                break;
            }
            break;

        case TDH_INTYPE_INT32:

            // Valid outtypes: int, hresult
            switch (outType)
            {
            default:
                wprintf(L"%i", *static_cast<int*>(pData));
                break;
            case TDH_OUTTYPE_HRESULT:
                wprintf(L"0x%x", *reinterpret_cast<unsigned*>(m_propertyBuffer.data()));
                break;
            }
            break;

        case TDH_INTYPE_UINT32:

            // UINT32 properties might have an associated map.
            if (mapNameOffset != 0 &&
                PrintMapString(mapNameOffset, *static_cast<unsigned*>(pData)))
            {
                break;
            }

            // Valid outtypes: unsignedInt, PID, TID, IPv4, ETWTIME, ErrorCode, Win32Error,
            // NTSTATUS, HexInt32, CodePointer
            switch (outType)
            {
            default:
                wprintf(L"%u", *static_cast<unsigned*>(pData));
                break;
            case TDH_OUTTYPE_HEXINT32:
            case TDH_OUTTYPE_ERRORCODE:
            case TDH_OUTTYPE_HRESULT:
            case TDH_OUTTYPE_NTSTATUS:
            case TDH_OUTTYPE_CODE_POINTER:
                wprintf(L"0x%x", *static_cast<unsigned*>(pData));
                break;
            case TDH_OUTTYPE_IPV4:
                wprintf(L"%u.%u.%u.%u",
                    static_cast<BYTE*>(pData)[0],
                    static_cast<BYTE*>(pData)[1],
                    static_cast<BYTE*>(pData)[2],
                    static_cast<BYTE*>(pData)[3]);
                break;
            }
            break;

        case TDH_INTYPE_INT64:

            // Valid outtypes: long
            wprintf(L"%lli", *static_cast<__int64*>(pData));
            break;

        case TDH_INTYPE_UINT64:

            // Valid outtypes: unsignedLong, ETWTIME, HexInt64, CodePointer
            switch (outType)
            {
            default:
                wprintf(L"%llu", *static_cast<unsigned __int64*>(pData));
                break;
            case TDH_OUTTYPE_HEXINT64:
            case TDH_OUTTYPE_CODE_POINTER:
                wprintf(L"0x%llx", *static_cast<unsigned __int64*>(pData));
                break;
            }
            break;

        case TDH_INTYPE_FLOAT:

            // Valid outtypes: float
            wprintf(L"%f", *static_cast<float*>(pData));
            break;

        case TDH_INTYPE_DOUBLE:

            // Valid outtypes: double
            wprintf(L"%f", *static_cast<double*>(pData));
            break;

        case TDH_INTYPE_BOOLEAN:

            // Valid outtypes: boolean
            wprintf(L"%u", *static_cast<unsigned*>(pData)); // 4-byte BOOL type
            break;

        case TDH_INTYPE_BINARY:

            // Valid outtypes: hexBinary, IPv6, SocketAddress, Pkcs7WithTypeInfo
            switch (outType)
            {
            default:
                PrintHexBinary(pData, cData);
                break;
            case TDH_OUTTYPE_IPV6:
                PrintIPv6(pData, cData);
                break;
            }
            break;

        case TDH_INTYPE_GUID:

            // Valid outtypes: guid
            PrintGuid(*static_cast<GUID*>(pData));
            break;

        case TDH_INTYPE_POINTER:

            // Valid outtypes: HexInt64, CodePointer, long, unsignedLong
            // Assume that TdhGetProperty has correctly determined size.
            switch (outType)
            {
            default:
                if (cData == 8)
                {
                    wprintf(L"0x%llx", *static_cast<unsigned __int64*>(pData));
                }
                else
                {
                    wprintf(L"0x%x", *static_cast<unsigned*>(pData));
                }
                break;
            case TDH_OUTTYPE_LONG:
                if (cData == 8)
                {
                    wprintf(L"%lli", *static_cast<__int64*>(pData));
                }
                else
                {
                    wprintf(L"%i", *static_cast<int*>(pData));
                }
                break;
            case TDH_OUTTYPE_UNSIGNEDLONG:
                if (cData == 8)
                {
                    wprintf(L"%llu", *static_cast<unsigned __int64*>(pData));
                }
                else
                {
                    wprintf(L"%u", *static_cast<unsigned*>(pData));
                }
                break;
            }
            break;

        case TDH_INTYPE_FILETIME:

            // Valid outtypes: dateTime, DateTimeCultureInsensitive
            PrintFileTime(*static_cast<FILETIME*>(pData));
            break;

        case TDH_INTYPE_SYSTEMTIME:

            // Valid outtypes: dateTime, DateTimeCultureInsensitive
            PrintSystemTime(*static_cast<SYSTEMTIME*>(pData));
            break;

        case TDH_INTYPE_SID:

            // Valid outtypes: string
            PrintSid(pData, cData);
            break;

        case TDH_INTYPE_HEXINT32:

            // HEXINT32 properties might have an associated map.
            if (mapNameOffset != 0 &&
                PrintMapString(mapNameOffset, *static_cast<unsigned*>(pData)))
            {
                break;
            }

            // Valid outtypes: HexInt32, ErrorCode, Win32Error, NTSTATUS, CodePointer
            wprintf(L"0x%x", *static_cast<unsigned*>(pData));
            break;

        case TDH_INTYPE_HEXINT64:

            // Valid outtypes: HexInt64, CodePointer
            wprintf(L"0x%llx", *static_cast<unsigned __int64*>(pData));
            break;

        case TDH_INTYPE_MANIFEST_COUNTEDSTRING: // Added in Windows 10 2018 Fall update
        case TDH_INTYPE_COUNTEDSTRING: // WBEM
        case TDH_INTYPE_REVERSEDCOUNTEDSTRING: // WBEM, deprecated

            // Valid outtypes: string, xml, json
            if (cData >= 2) // Assume first 2 bytes are bytecount.
            {
                wprintf(L"%.*ls", (cData / 2) - 1, static_cast<LPCWSTR>(pData) + 1);
            }
            break;

        case TDH_INTYPE_MANIFEST_COUNTEDANSISTRING: // Added in Windows 10 2018 Fall update
        case TDH_INTYPE_COUNTEDANSISTRING: // WBEM
        case TDH_INTYPE_REVERSEDCOUNTEDANSISTRING: // WBEM, deprecated

            // Valid outtypes: string, xml, json, utf8
            if (cData >= 2) // Assume first 2 bytes are bytecount.
            {
                wprintf(L"%.*hs", cData - 2, static_cast<LPCSTR>(pData) + 2);
            }
            break;

        case TDH_INTYPE_MANIFEST_COUNTEDBINARY: // Added in Windows 10 2018 Fall update

            // Valid outtypes: hexBinary, IPv6, SocketAddress, Pkcs7WithTypeInfo
            if (cData >= 2) // Assume first 2 bytes are bytecount.
            {
                switch (outType)
                {
                default:
                    PrintHexBinary(static_cast<BYTE*>(pData) + 2, cData - 2);
                    break;
                case TDH_OUTTYPE_IPV6:
                    PrintIPv6(static_cast<BYTE*>(pData) + 2, cData - 2);
                    break;
                }
            }
            break;

        case TDH_INTYPE_UNICODECHAR: // WBEM

            wprintf(L"%lc", *static_cast<unsigned short*>(pData));
            break;

        case TDH_INTYPE_ANSICHAR: // WBEM

            wprintf(L"%hc", *static_cast<unsigned char*>(pData));
            break;

        case TDH_INTYPE_SIZET: // WBEM

            if (cData == 8)
            {
                wprintf(L"%llu", *static_cast<unsigned __int64*>(pData));
            }
            else
            {
                wprintf(L"%u", *static_cast<unsigned*>(pData));
            }
            break;

        case TDH_INTYPE_HEXDUMP: // WBEM, deprecated

            if (cData >= 4) // Assume first 4 bytes are bytecount.
            {
                PrintHexBinary(static_cast<BYTE*>(pData) + 4, cData - 4);
            }
            break;

        case TDH_INTYPE_WBEMSID: // WBEM, deprecated
        {
            // A WBEM SID is actually a TOKEN_USER structure followed
            // by the SID. The TOKEN_USER structure is 2 * pointerSize.
            unsigned const cbTokenUser =
                m_pEvent->EventHeader.Flags & EVENT_HEADER_FLAG_32_BIT_HEADER
                ? 2 * 4
                : m_pEvent->EventHeader.Flags & EVENT_HEADER_FLAG_64_BIT_HEADER
                ? 2 * 8
                : 2 * sizeof(void*);
            if (cData > cbTokenUser)
            {
                // Skip the TOKEN_USER.
                PrintSid(static_cast<BYTE*>(pData) + cbTokenUser, cData - cbTokenUser);
            }
            else
            {
                PrintHexBinary(pData, cData);
            }
            break;
        }
        default:

            // Unknown intype. Treat as binary.
            wprintf(L"InType=%u ", inType);
            PrintHexBinary(pData, cData);
            break;
        }
    }

    bool PrintMapString(ULONG mapNameOffset, ULONG value)
    {
        bool matched = false;

        ULONG cb = static_cast<ULONG>(m_mapBuffer.size());
        ULONG status = TdhGetEventMapInformation(
            m_pEvent,
            const_cast<LPWSTR>(TeiString(mapNameOffset)),
            reinterpret_cast<EVENT_MAP_INFO*>(m_mapBuffer.data()),
            &cb);
        if (status == ERROR_INSUFFICIENT_BUFFER)
        {
            m_mapBuffer.reserve(cb);
            m_mapBuffer.resize(m_mapBuffer.capacity());
            status = TdhGetEventMapInformation(
                m_pEvent,
                const_cast<LPWSTR>(TeiString(mapNameOffset)),
                reinterpret_cast<EVENT_MAP_INFO*>(m_mapBuffer.data()),
                &cb);
        }

        if (status == ERROR_SUCCESS)
        {
            EVENT_MAP_INFO const* pMapInfo = reinterpret_cast<EVENT_MAP_INFO*>(m_mapBuffer.data());

            if ((pMapInfo->Flag & EVENTMAP_INFO_FLAG_MANIFEST_VALUEMAP) != 0 ||
                ((pMapInfo->Flag & EVENTMAP_INFO_FLAG_WBEM_VALUEMAP) != 0 &&
                (pMapInfo->Flag & ~EVENTMAP_INFO_FLAG_WBEM_VALUEMAP) != EVENTMAP_INFO_FLAG_WBEM_FLAG))
            {
                if ((pMapInfo->Flag & EVENTMAP_INFO_FLAG_WBEM_NO_MAP) == 0)
                {
                    for (ULONG i = 0; i != pMapInfo->EntryCount; i += 1)
                    {
                        if (pMapInfo->MapEntryArray[i].Value == value)
                        {
                            wprintf(L"%ls", MapString(pMapInfo, i));
                            matched = true;
                            break;
                        }
                    }
                }
                else if (value < pMapInfo->EntryCount)
                {
                    wprintf(L"%ls", MapString(pMapInfo, value));
                    matched = true;
                }
            }
            else if (
                (pMapInfo->Flag & EVENTMAP_INFO_FLAG_MANIFEST_BITMAP) != 0 ||
                (pMapInfo->Flag & EVENTMAP_INFO_FLAG_WBEM_BITMAP) != 0 ||
                ((pMapInfo->Flag & EVENTMAP_INFO_FLAG_WBEM_VALUEMAP) != 0 &&
                (pMapInfo->Flag & ~EVENTMAP_INFO_FLAG_WBEM_VALUEMAP) == EVENTMAP_INFO_FLAG_WBEM_FLAG))
            {
                ULONG matchedBits = 0;
                if ((pMapInfo->Flag & EVENTMAP_INFO_FLAG_WBEM_NO_MAP) == 0)
                {
                    for (ULONG i = 0; i != pMapInfo->EntryCount; i += 1)
                    {
                        ULONG const mask = pMapInfo->MapEntryArray[i].Value;
                        if ((value & mask) == mask)
                        {
                            if (mask != 0 || value == 0)
                            {
                                wprintf(L"%hs%ls", matched ? "| " : "", MapString(pMapInfo, i));
                                matched = true;
                                matchedBits |= mask;
                            }
                        }
                    }
                }
                else
                {
                    for (ULONG i = 0; i != pMapInfo->EntryCount; i += 1)
                    {
                        ULONG const mask = 1 << i;
                        if (value & mask)
                        {
                            wprintf(L"%ls%ls", matched ? L"| " : L"", MapString(pMapInfo, i));
                            matched = true;
                            matchedBits |= mask;
                        }
                    }
                }

                // Print any unused bits.
                if (matched && matchedBits != value)
                {
                    wprintf(L"| 0x%x", value ^ matchedBits);
                }
            }
        }

        return matched;
    }

    void PrintGuid(GUID const& g)
    {
        wprintf(L"{%08x-%04x-%04x-%02x%02x-%02x%02x%02x%02x%02x%02x}",
            g.Data1, g.Data2, g.Data3, g.Data4[0], g.Data4[1], g.Data4[2],
            g.Data4[3], g.Data4[4], g.Data4[5], g.Data4[6], g.Data4[7]);
    }

    void PrintFileTime(FILETIME const& ft)
    {
        SYSTEMTIME st = {};
        FileTimeToSystemTime(&ft, &st);
        PrintSystemTime(st);
    }

    void PrintSystemTime(SYSTEMTIME const& st)
    {
        wprintf(L"%04u-%02u-%02uT%02u:%02u:%02u.%03uZ",
            st.wYear,
            st.wMonth,
            st.wDay,
            st.wHour,
            st.wMinute,
            st.wSecond,
            st.wMilliseconds);
    }

    void PrintIPv6(_In_bytecount_(cb) void const* p, unsigned cb)
    {
        if (cb == 16)
        {
            // Simple (greedy, non-canonical) formatting for IPv6 addresses.

            UINT16 const* const pw = static_cast<UINT16 const*>(p);
            unsigned i;

            // Initial state: we haven't seen a 0:0 yet.

            for (i = 0;; i += 1)
            {
                if (i == 7)
                {
                    // No 0:0 in the address.
                    wprintf(L"%x", _byteswap_ushort(pw[i]));
                    return;
                }

                if (pw[i] == 0 && pw[i + 1] == 0)
                {
                    // Found a 0:0
                    if (i == 0)
                    {
                        wprintf(L":");
                    }

                    i += 2;
                    break;
                }

                wprintf(L"%x:", _byteswap_ushort(pw[i]));
            }

            // We've seen 0:0 and are omitting groups. Scan for a non-zero.

            for (;;)
            {
                if (i == 8)
                {
                    // Address ends with 0:0
                    wprintf(L":");
                    return;
                }

                if (pw[i] != 0)
                {
                    break;
                }

                i += 1;
            }

            for (; i != 8; i += 1)
            {
                wprintf(L":%x", _byteswap_ushort(pw[i]));
            }
        }
        else
        {
            PrintHexBinary(p, cb);
        }
    }

    void PrintHexBinary(_In_bytecount_(cb) void const* p, unsigned cb)
    {
        BYTE const* pb = static_cast<BYTE const*>(p);
        wprintf(L"0x");
        for (unsigned i = 0; i != cb; i += 1)
        {
            wprintf(L"%02x", pb[i]);
        }
    }

    void PrintSid(_In_bytecount_(cb) PSID pSid, unsigned cb)
    {
        LPWSTR szSid = nullptr;
        if (cb < 8u || // Minimum SID size is 8.
            cb < (8u + static_cast<BYTE*>(pSid)[1] * 4u) || // SID size = 8 + (4 * SubAuthorityCount)
            !ConvertSidToStringSidW(pSid, &szSid))
        {
            PrintHexBinary(pSid, cb);
        }
        else
        {
            wprintf(L"%ls", szSid);
            LocalFree(szSid);
        }
    }

    void PrintIndent()
    {
        wprintf(L"%*ls", m_indentLevel * 2, L"");
    }

    /*
    Uses the PROPERTY_DATA_DESCRIPTORs in m_pdd (controlled with PushPdd/PopPdd)
    to call TdhGetProperty. If successful, puts the property data into
    m_propertyBuffer.
    */
    ULONG GetProperty()
    {
        ULONG status;
        ULONG cb = 0;
        status = TdhGetPropertySize(
            m_pEvent,
            m_tdhContextCount,
            m_tdhContextCount ? m_tdhContext : nullptr,
            static_cast<ULONG>(m_pdd.size()),
            m_pdd.data(),
            &cb);
        if (status == ERROR_SUCCESS)
        {
            m_propertyBuffer.resize(cb);
            status = TdhGetProperty(
                m_pEvent,
                m_tdhContextCount,
                m_tdhContextCount ? m_tdhContext : nullptr,
                static_cast<ULONG>(m_pdd.size()),
                m_pdd.data(),
                cb,
                m_propertyBuffer.data());
        }

        return status;
    }

    /*
    Adds a property with the specified name to the PROPERTY_DATA_DESCRIPTOR
    stack. Returns the property's index within the m_pdd vector.
    */
    unsigned PushPdd(_In_z_ LPCWSTR szPropertyName)
    {
        unsigned index = static_cast<unsigned>(m_pdd.size());
        m_pdd.emplace_back();
        PROPERTY_DATA_DESCRIPTOR& pdd = m_pdd.back();
        pdd.PropertyName = reinterpret_cast<UINT_PTR>(szPropertyName);
        pdd.ArrayIndex = 0;
        pdd.Reserved = 0;
        return index;
    }

    /*
    Removes a property from the PROPERTY_DATA_DESCRIPTOR stack.
    */
    void PopPdd()
    {
        m_pdd.pop_back();
    }

    /*
    Returns true if the current event has the EVENT_HEADER_FLAG_STRING_ONLY
    flag set.
    */
    bool IsStringEvent() const
    {
        return (m_pEvent->EventHeader.Flags & EVENT_HEADER_FLAG_STRING_ONLY) != 0;
    }

    /*
    Returns true if the current event has the EVENT_HEADER_FLAG_TRACE_MESSAGE
    flag set.
    */
    bool IsWppEvent() const
    {
        return (m_pEvent->EventHeader.Flags & EVENT_HEADER_FLAG_TRACE_MESSAGE) != 0;
    }

    /*
    Converts a TRACE_EVENT_INFO offset (e.g. TaskNameOffset) into a string.
    */
    _Ret_z_ LPCWSTR TeiString(unsigned offset)
    {
        return reinterpret_cast<LPCWSTR>(m_teiBuffer.data() + offset);
    }

    /*
    Converts an EVENT_MAP_INFO MapEntryArray index into a string.
    */
    static _Ret_z_ LPCWSTR MapString(_In_ const EVENT_MAP_INFO* pMapInfo, unsigned index)
    {
        return reinterpret_cast<LPCWSTR>(
            reinterpret_cast<const BYTE*>(pMapInfo) + pMapInfo->MapEntryArray[index].OutputOffset);
    }

private:

    TDH_CONTEXT m_tdhContext[1]; // May contain TDH_CONTEXT_WPP_TMFSEARCHPATH.
    BYTE m_tdhContextCount;      // 1 if a TMF search path is present.
    BYTE m_indentLevel;          // How far to indent the output.
    EVENT_RECORD* m_pEvent;      // The event we're currently printing.
    std::vector<PROPERTY_DATA_DESCRIPTOR> m_pdd; // Path to the property we're currently decoding.
    std::vector<USHORT> m_integerValues; // Stored property values for resolving array lengths.
    std::vector<BYTE> m_teiBuffer; // Buffer for TRACE_EVENT_INFO data.
    std::vector<BYTE> m_propertyBuffer; // Buffer for the data returned by TdhGetProperty.
    std::vector<BYTE> m_mapBuffer; // Buffer for the data returned by TdhGetEventMapInformation.
};

/*
Parses and stores the command line options.
*/
struct DecoderSettings
{
    std::vector<LPCWSTR> etlFiles;
    std::vector<LPCWSTR> manFiles;
    std::vector<LPCWSTR> binFiles;
    LPCWSTR szTmfSearchPath;
    bool showUsage;

    DecoderSettings(
        int argc,
        _In_count_(argc) LPWSTR argv[])
        : szTmfSearchPath()
        , showUsage()
    {
        for (int i = 1; i < argc; i += 1)
        {
            LPCWSTR szArg = argv[i];
            if (szArg[0] != L'/' && szArg[0] != L'-')
            {
                etlFiles.push_back(szArg);
            }
            else if (szArg[1] == L'\0' ||
                (szArg[2] != L'\0' && szArg[2] != L':' && szArg[2] != L'='))
            {
                // Options should be /X, /X:Value, or /X=Value
                wprintf(L"ERROR: Incorrectly-formatted option: %ls\n", szArg);
                showUsage = true;
            }
            else
            {
                LPCWSTR szArgValue = &szArg[3];
                switch (szArg[1])
                {
                case L'?':
                case L'h':
                case L'H':
                    showUsage = true;
                    break;

                case L'B':
                case L'b':
                    binFiles.push_back(szArgValue);
                    break;

                case L'M':
                case L'm':
                    manFiles.push_back(szArgValue);
                    break;

                case L'T':
                case L't':
                    if (szTmfSearchPath == nullptr)
                    {
                        szTmfSearchPath = szArgValue;
                    }
                    else
                    {
                        wprintf(L"ERROR: TMF search path already set: %ls\n", szArg);
                        showUsage = true;
                    }
                    break;

                default:
                    wprintf(L"ERROR: Unrecognized option: %ls\n", szArg);
                    showUsage = true;
                    break;
                }
            }
        }

        if (!showUsage && etlFiles.empty())
        {
            wprintf(L"ERROR: No ETL files specified.\n");
            showUsage = true;
        }
    }
};

/*
Helper class to automatically close TRACEHANDLEs.
*/
class TraceHandles
{
public:

    ~TraceHandles()
    {
        CloseHandles();
    }

    void CloseHandles()
    {
        while (!handles.empty())
        {
            CloseTrace(handles.back());
            handles.pop_back();
        }
    }

    ULONG OpenTraceW(
        _Inout_ EVENT_TRACE_LOGFILEW* pLogFile)
    {
        ULONG status;

        handles.reserve(handles.size() + 1);
        TRACEHANDLE handle = ::OpenTraceW(pLogFile);
        if (handle == INVALID_PROCESSTRACE_HANDLE)
        {
            status = GetLastError();
        }
        else
        {
            handles.push_back(handle);
            status = 0;
        }

        return status;
    }

    ULONG ProcessTrace(
        _In_opt_ LPFILETIME pStartTime,
        _In_opt_ LPFILETIME pEndTime)
    {
        return ::ProcessTrace(
            handles.data(),
            static_cast<ULONG>(handles.size()),
            pStartTime,
            pEndTime);
    }

private:

    std::vector<TRACEHANDLE> handles;
};

/*
This function will be used as the EventRecordCallback function in EVENT_TRACE_LOGFILE.
It expects that the EVENT_TRACE_LOGFILE's Context pointer is set to a DecoderContext.
*/
static void WINAPI EventRecordCallback(
    _In_ EVENT_RECORD* pEventRecord)
{
    try
    {
        // We expect that the EVENT_TRACE_LOGFILE.Context pointer was set with a
        // pointer to a DecoderContext. ProcessTrace will put the Context value
        // into EVENT_RECORD.UserContext.
        DecoderContext* pContext = static_cast<DecoderContext*>(pEventRecord->UserContext);

        // The actual decoding work is done in PrintEventRecord.
        pContext->PrintEventRecord(pEventRecord);
    }
    catch (std::exception const& ex)
    {
        wprintf(L"\nERROR: %hs\n", ex.what());
    }
}

int __cdecl wmain(int argc, _In_count_(argc) LPWSTR argv[])
{
    int exitCode;

    try
    {
        DecoderSettings settings(argc, argv);
        TraceHandles handles;
        if (settings.showUsage)
        {
            wprintf(L""
                "\nUsage:"
                "\n"
                "\n  TdhGetProperty_Sample [options] filename1.etl (filename2.etl...)"
                "\n"
                "\nOptions:"
                "\n"
                "\n  -m:ManifestFile.man  Load decoding data from a manifest with TdhLoadManifest."
                "\n  -b:ResourceFile.dll  Load decoding data from a DLL with"
                "\n                       TdhLoadManifestFromBinary."
                "\n  -t:TmfSearchPath     Set the TMF search path for WPP events."
                "\n"
                "\n");
            exitCode = 1;
            goto Done;
        }

        DecoderContext context(settings.szTmfSearchPath);

        for (size_t i = 0; i != settings.manFiles.size(); i += 1)
        {
            exitCode = TdhLoadManifest(const_cast<LPWSTR>(settings.manFiles[i]));
            if (exitCode != 0)
            {
                wprintf(L"ERROR: TdhLoadManifest error %u for manifest: %ls\n",
                    exitCode,
                    settings.manFiles[i]);
                goto Done;
            }
        }

        for (size_t i = 0; i != settings.binFiles.size(); i += 1)
        {
            exitCode = TdhLoadManifestFromBinary(const_cast<LPWSTR>(settings.binFiles[i]));
            if (exitCode != 0)
            {
                wprintf(L"ERROR: TdhLoadManifestFromBinary error %u for binary: %ls\n",
                    exitCode,
                    settings.binFiles[i]);
                goto Done;
            }
        }

        for (size_t i = 0; i != settings.etlFiles.size(); i += 1)
        {
            EVENT_TRACE_LOGFILEW logFile = { const_cast<LPWSTR>(settings.etlFiles[i]) };
            logFile.ProcessTraceMode = PROCESS_TRACE_MODE_EVENT_RECORD;
            logFile.EventRecordCallback = &EventRecordCallback;
            logFile.Context = &context;

            exitCode = handles.OpenTraceW(&logFile);
            if (exitCode != 0)
            {
                wprintf(L"ERROR: OpenTraceW error %u for file: %ls\n",
                    exitCode,
                    settings.etlFiles[i]);
                goto Done;
            }

            wprintf(L"Opened: %ls\n", logFile.LogFileName);

            // Optionally print information read from the log file.
            // For example, show information about lost buffers and events.

            if (logFile.LogfileHeader.BuffersLost != 0)
            {
                wprintf(L"  **BuffersLost = %lu\n", logFile.LogfileHeader.BuffersLost);
            }

            if (logFile.LogfileHeader.EventsLost != 0)
            {
                wprintf(L"  **EventsLost = %lu\n", logFile.LogfileHeader.EventsLost);
            }
        }

        exitCode = handles.ProcessTrace(nullptr, nullptr);
        if (exitCode != 0)
        {
            wprintf(L"ERROR: ProcessTrace error %u\n",
                exitCode);
            goto Done;
        }
    }
    catch (std::exception const& ex)
    {
        wprintf(L"\nERROR: %hs\n", ex.what());
        exitCode = 1;
    }

Done:

    return exitCode;
}
```
