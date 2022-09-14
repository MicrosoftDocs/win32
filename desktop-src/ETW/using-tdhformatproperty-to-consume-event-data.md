---
description: The following example shows how to consume event data using the TdhFormatProperty function.
ms.assetid: 5ebd500c-420e-4979-a03a-49b687464b0e
title: Using TdhFormatProperty to Consume Event Data
ms.topic: article
ms.date: 05/31/2018
---

# Using TdhFormatProperty to Consume Event Data

The following example shows how to consume event data using the [**TdhFormatProperty**](/windows/win32/api/tdh/nf-tdh-tdhformatproperty) function.

```C++
/*
Sample for decoding ETW events using TdhFormatProperty.

This sample demonstrates the following:

- How to process events from ETL files using OpenTrace and ProcessTrace.
- How to get TRACE_EVENT_INFO data for an event using TdhGetEventInformation.
- How to format a WPP message using TdhGetProperty.
- How to extract property values from non-WPP events.
- How to format property values from non-WPP events using TdhFormatProperty.
*/

#ifndef WIN32_LEAN_AND_MEAN
#define WIN32_LEAN_AND_MEAN 1 // Exclude rarely-used APIs from <windows.h>
#endif

#include <windows.h>

#define INITGUID // Ensure that EventTraceGuid is defined.
#include <evntrace.h>
#undef INITGUID

#include <tdh.h>
#include <vector>

#include <wchar.h> // wprintf

#pragma comment(lib, "tdh.lib") // Link against TDH.dll

// Support building this sample using older versions of the Windows SDK:
#define EventNameOffset        ActivityIDNameOffset
#define EventAttributesOffset  RelatedActivityIDNameOffset

/*
Decodes event data using TdhGetEventInformation and TdhFormatProperty. Prints
the event information to stdout.

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
        m_pbData = static_cast<BYTE const*>(m_pEvent->UserData);
        m_pbDataEnd = m_pbData + m_pEvent->UserDataLength;
        m_pointerSize =
            m_pEvent->EventHeader.Flags & EVENT_HEADER_FLAG_32_BIT_HEADER
            ? 4
            : m_pEvent->EventHeader.Flags & EVENT_HEADER_FLAG_64_BIT_HEADER
            ? 8
            : sizeof(void*); // Ambiguous, assume size of the decoder's pointer.

        // There is a lot of information available in the event even without decoding,
        // including timestamp, PID, TID, provider ID, activity ID, and the raw data.

        // Show the event timestamp.
        PrintFileTime(reinterpret_cast<FILETIME const&>(m_pEvent->EventHeader.TimeStamp));

        if (IsWppEvent())
        {
            PrintWppEvent();
        }
        else
        {
            PrintNonWppEvent();
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

        // Use TdhGetProperty to get the properties we need.
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
        PROPERTY_DATA_DESCRIPTOR pdd = { reinterpret_cast<UINT_PTR>(szPropertyName) };

        ULONG status;
        ULONG cb = 0;
        status = TdhGetPropertySize(
            m_pEvent,
            m_tdhContextCount,
            m_tdhContextCount ? m_tdhContext : nullptr,
            1,
            &pdd,
            &cb);
        if (status == ERROR_SUCCESS)
        {
            if (m_propertyBuffer.size() < cb / 2)
            {
                m_propertyBuffer.resize(cb / 2);
            }

            status = TdhGetProperty(
                m_pEvent,
                m_tdhContextCount,
                m_tdhContextCount ? m_tdhContext : nullptr,
                1,
                &pdd,
                cb,
                reinterpret_cast<BYTE*>(m_propertyBuffer.data()));
        }

        if (status != ERROR_SUCCESS)
        {
            wprintf(L"[TdhGetProperty(%ls) error %u]", szPropertyName, status);
        }
        else
        {
            // Print the FormattedString property data (nul-terminated
            // wchar_t string).
            wprintf(L"%ls", m_propertyBuffer.data());
        }
    }

    /*
    Use TdhGetEventInformation to obtain information about this event
    (including the names and types of the event's properties). Print some
    basic information about the event (provider name, event name), then print
    each property (using TdhFormatProperty to format each property value).
    */
    void PrintNonWppEvent()
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

            // If this property is a scalar integer, remember the value in case it
            // is needed for a subsequent property's length or count.
            if (0 == (epi.Flags & (PropertyStruct | PropertyParamCount)) &&
                epi.count == 1)
            {
                switch (epi.nonStructType.InType)
                {
                case TDH_INTYPE_INT8:
                case TDH_INTYPE_UINT8:
                    if ((m_pbDataEnd - m_pbData) >= 1)
                    {
                        m_integerValues[propIndex] = *m_pbData;
                    }
                    break;
                case TDH_INTYPE_INT16:
                case TDH_INTYPE_UINT16:
                    if ((m_pbDataEnd - m_pbData) >= 2)
                    {
                        m_integerValues[propIndex] = *reinterpret_cast<UINT16 const UNALIGNED*>(m_pbData);
                    }
                    break;
                case TDH_INTYPE_INT32:
                case TDH_INTYPE_UINT32:
                case TDH_INTYPE_HEXINT32:
                    if ((m_pbDataEnd - m_pbData) >= 4)
                    {
                        auto val = *reinterpret_cast<UINT32 const UNALIGNED*>(m_pbData);
                        m_integerValues[propIndex] = static_cast<USHORT>(val > 0xffffu ? 0xffffu : val);
                    }
                    break;
                }
            }

            PrintIndent();

            // Print the property's name.
            wprintf(L"%ls:", epi.NameOffset ? TeiString(epi.NameOffset) : L"(noname)");

            m_indentLevel += 1;

            // We recorded the values of all previous integer properties just
            // in case we need to determine the property length or count.
            USHORT const propLength =
                epi.nonStructType.OutType == TDH_OUTTYPE_IPV6 &&
                epi.nonStructType.InType == TDH_INTYPE_BINARY &&
                epi.length == 0 &&
                (epi.Flags & (PropertyParamLength | PropertyParamFixedLength)) == 0
                ? 16 // special case for incorrectly-defined IPV6 addresses
                : (epi.Flags & PropertyParamLength)
                ? m_integerValues[epi.lengthPropertyIndex] // Look up the value of a previous property
                : epi.length;
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

            PEVENT_MAP_INFO pMapInfo = nullptr;

            // Treat non-array properties as arrays with one element.
            for (unsigned arrayIndex = 0; arrayIndex != arrayCount; arrayIndex += 1)
            {
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

                // If the property has an associated map (i.e. an enumerated type),
                // try to look up the map data. (If this is an array, we only need
                // to do the lookup on the first iteration.)
                if (epi.nonStructType.MapNameOffset != 0 && arrayIndex == 0)
                {
                    switch (epi.nonStructType.InType)
                    {
                    case TDH_INTYPE_UINT8:
                    case TDH_INTYPE_UINT16:
                    case TDH_INTYPE_UINT32:
                    case TDH_INTYPE_HEXINT32:
                        if (m_mapBuffer.size() == 0)
                        {
                            m_mapBuffer.resize(sizeof(EVENT_MAP_INFO));
                        }

                        for (;;)
                        {
                            ULONG cbBuffer = static_cast<ULONG>(m_mapBuffer.size());
                            ULONG status = TdhGetEventMapInformation(
                                m_pEvent,
                                const_cast<LPWSTR>(TeiString(epi.nonStructType.MapNameOffset)),
                                reinterpret_cast<PEVENT_MAP_INFO>(m_mapBuffer.data()),
                                &cbBuffer);

                            if (status == ERROR_INSUFFICIENT_BUFFER &&
                                m_mapBuffer.size() < cbBuffer)
                            {
                                m_mapBuffer.resize(cbBuffer);
                                continue;
                            }
                            else if (status == ERROR_SUCCESS)
                            {
                                pMapInfo = reinterpret_cast<PEVENT_MAP_INFO>(m_mapBuffer.data());
                            }

                            break;
                        }
                        break;
                    }
                }

                bool useMap = pMapInfo != nullptr;

                // Loop because we may need to retry the call to TdhFormatProperty.
                for (;;)
                {
                    ULONG cbBuffer = static_cast<ULONG>(m_propertyBuffer.size() * 2);
                    USHORT cbUsed = 0;
                    ULONG status;

                    if (0 == propLength &&
                        epi.nonStructType.InType == TDH_INTYPE_NULL)
                    {
                        // TdhFormatProperty doesn't handle INTYPE_NULL.
                        if (m_propertyBuffer.empty())
                        {
                            m_propertyBuffer.push_back(0);
                        }
                        m_propertyBuffer[0] = 0;
                        status = ERROR_SUCCESS;
                    }
                    else if (
                        0 == propLength &&
                        0 != (epi.Flags & (PropertyParamLength | PropertyParamFixedLength)) &&
                        (   epi.nonStructType.InType == TDH_INTYPE_UNICODESTRING ||
                            epi.nonStructType.InType == TDH_INTYPE_ANSISTRING))
                    {
                        // TdhFormatProperty doesn't handle zero-length counted strings.
                        if (m_propertyBuffer.empty())
                        {
                            m_propertyBuffer.push_back(0);
                        }
                        m_propertyBuffer[0] = 0;
                        status = ERROR_SUCCESS;
                    }
                    else
                    {
                        status = TdhFormatProperty(
                            const_cast<TRACE_EVENT_INFO*>(pTei),
                            useMap ? pMapInfo : nullptr,
                            m_pointerSize,
                            epi.nonStructType.InType,
                            static_cast<USHORT>(
                                epi.nonStructType.OutType == TDH_OUTTYPE_NOPRINT
                                ? TDH_OUTTYPE_NULL
                                : epi.nonStructType.OutType),
                            propLength,
                            static_cast<USHORT>(m_pbDataEnd - m_pbData),
                            const_cast<PBYTE>(m_pbData),
                            &cbBuffer,
                            m_propertyBuffer.data(),
                            &cbUsed);
                    }

                    if (status == ERROR_INSUFFICIENT_BUFFER &&
                        m_propertyBuffer.size() < cbBuffer / 2)
                    {
                        // Try again with a bigger buffer.
                        m_propertyBuffer.resize(cbBuffer / 2);
                        continue;
                    }
                    else if (status == ERROR_EVT_INVALID_EVENT_DATA && useMap)
                    {
                        // If the value isn't in the map, TdhFormatProperty treats it
                        // as an error instead of just putting the number in. We'll
                        // try again with no map.
                        useMap = false;
                        continue;
                    }
                    else if (status != ERROR_SUCCESS)
                    {
                        wprintf(L" [ERROR:TdhFormatProperty:%lu]\n", status);
                    }
                    else
                    {
                        wprintf(L" %ls\n", m_propertyBuffer.data());
                        m_pbData += cbUsed;
                    }

                    break;
                }
            }

            m_indentLevel -= 1;
        }
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
        wprintf(L"%04u-%02u-%02uT%02u:%02u:%02u.%03uZ",
            st.wYear,
            st.wMonth,
            st.wDay,
            st.wHour,
            st.wMinute,
            st.wSecond,
            st.wMilliseconds);
    }

    void PrintIndent()
    {
        wprintf(L"%*ls", m_indentLevel * 2, L"");
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

private:

    TDH_CONTEXT m_tdhContext[1]; // May contain TDH_CONTEXT_WPP_TMFSEARCHPATH.
    BYTE m_tdhContextCount;  // 1 if a TMF search path is present.
    BYTE m_pointerSize;
    BYTE m_indentLevel;      // How far to indent the output.
    EVENT_RECORD* m_pEvent;      // The event we're currently printing.
    BYTE const* m_pbData;        // Position of the next byte of event data to be consumed.
    BYTE const* m_pbDataEnd;     // Position of the end of the event data.
    std::vector<USHORT> m_integerValues; // Stored property values for resolving array lengths.
    std::vector<BYTE> m_teiBuffer; // Buffer for TRACE_EVENT_INFO data.
    std::vector<wchar_t> m_propertyBuffer; // Buffer for the string returned by TdhFormatProperty.
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
                "\n  TdhFormatProperty_Sample [options] filename1.etl (filename2.etl...)"
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
