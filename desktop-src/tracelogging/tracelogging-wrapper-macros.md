---
title: TraceLogging Wrapper Macros
description: Lists the wrapper macros for TraceLogging providers.
ms.assetid: 806F43F3-D376-4DBD-A4C5-B5F01E5D009D
ms.topic: article
ms.date: 05/31/2018
---

# TraceLogging Wrapper Macros

Lists the wrapper macros for TraceLogging providers.

In order to record events using TraceLogging providers, you need to use the
TraceLogging write macros
[**TraceLoggingWrite**](/windows/desktop/api/traceloggingprovider/nf-traceloggingprovider-traceloggingwrite)
or
[**TraceLoggingWriteActivity**](/windows/desktop/api/traceloggingprovider/nf-traceloggingprovider-traceloggingwriteactivity).
Both of these macros require you to wrap any event data in a wrapper macro.
There are several different wrapper macros for different data types. For a
complete list of TraceLogging macros, see
[TraceLogging Macros](trace-logging-macros.md).

In addition to the wrapper macros above, several macros are available for
individual data types. All of these macros have the same format as the
[TraceLoggingValue](/windows/desktop/api/traceloggingprovider/nf-traceloggingprovider-traceloggingvalue)
macro. You can use the TraceLoggingValue macro to automatically detect the
appropriate wrapper macro to use, or use the specific macro directly.

- [**TraceLoggingBinary**](/windows/desktop/api/traceloggingprovider/nf-traceloggingprovider-traceloggingbinary)
- [**TraceLoggingChannel**](/windows/desktop/api/traceloggingprovider/nf-traceloggingprovider-traceloggingchannel)
- [**TraceLoggingCustomAttribute**](/windows/desktop/api/traceloggingprovider/nf-traceloggingprovider-traceloggingcustomattribute)
- [**TraceLoggingDescription**](/windows/desktop/api/traceloggingprovider/nf-traceloggingprovider-traceloggingdescription)
- [**TraceLoggingEventTag**](/windows/desktop/api/traceloggingprovider/nf-traceloggingprovider-traceloggingeventtag)
- [**TraceLoggingKeyword**](/windows/desktop/api/traceloggingprovider/nf-traceloggingprovider-traceloggingkeyword)
- [**TraceLoggingLevel**](/windows/desktop/api/traceloggingprovider/nf-traceloggingprovider-tracelogginglevel)
- [**TraceLoggingOpcode**](/windows/desktop/api/traceloggingprovider/nf-traceloggingprovider-traceloggingopcode)
- [**TraceLoggingSocketAddress**](/windows/desktop/api/traceloggingprovider/nf-traceloggingprovider-traceloggingsocketaddress)
- [**TraceLoggingStruct**](/windows/desktop/api/traceloggingprovider/nf-traceloggingprovider-traceloggingstruct)
- [**TraceLoggingValue**](/windows/desktop/api/traceloggingprovider/nf-traceloggingprovider-traceloggingvalue)

> [!NOTE]
> [**TraceLoggingOptionGroup**](/windows/desktop/api/traceloggingprovider/nf-traceloggingprovider-traceloggingoptiongroup)
> is specifically for use inside of TRACELOGGING_DEFINE_PROVIDER.

Here are the individual wrapper macros.

- TraceLoggingInt8
- TraceLoggingUInt8
- TraceLoggingInt16
- TraceLoggingUInt16
- TraceLoggingInt32
- TraceLoggingUInt32
- TraceLoggingInt64
- TraceLoggingUInt64
- TraceLoggingFloat32
- TraceLoggingFloat64
- TraceLoggingBool
- TraceLoggingFileTime
- TraceLoggingGuid
- TraceLoggingPointer
- TraceLoggingSystemTime
- TraceLoggingHexInt8
- TraceLoggingHexUInt8
- TraceLoggingHexInt32
- TraceLoggingHexUInt32
- TraceLoggingHexInt64
- TraceLoggingHexUInt64
- TraceLoggingWchar
- TraceLoggingChar
- TraceLoggingIntPtr
- TraceLoggingUIntPtr
- TraceLoggingBoolean
- TraceLoggingHexInt16
- TraceLoggingHexUInt16
- TraceLoggingPid
- TraceLoggingTid
- TraceLoggingPort
- TraceLoggingWinError
- TraceLoggingNTStatus
- TraceLoggingHResult
- TraceLoggingSocketAddress
- TraceLoggingSid
- TraceLoggingString
- TraceLoggingWideString
- TraceLoggingCountedString
- TraceLoggingCountedWideString
- TraceLoggingAnsiString
- TraceLoggingUnicodeString
- TraceLoggingBinary(void \*data, size of the data in bytes, \[optional\] name )
  The parameters to this macro differ from those above.

If the _name_ parameter is specified, it must be a string literal (not a
variable) and may not contain any embedded null characters. If the _name_
parameter is not provided, a name is generated automatically.

The TraceLogging API also makes several macros available for arrays. These
arrays can either have a fixed length or be of a variable length, depending on
the wrapper macro you choose to use. All of these wrapper macros follow this
format.

`TraceLoggingBooleanArray(pVals, cVals, name, desc, tags)`

The parameter _pVals_ points to the array of data and _cVals_ indicates the
number of elements in the array. _cVals_ must be a constant and cannot be a
variable. As with the single value wrapper macros, _name_, **desc**, and _tags_
are optional parameters and must follow the same restrictions as explained with
the **TraceLoggingValue** macro.

- TraceLoggingInt8FixedArray
- TraceLoggingUInt8FixedArray
- TraceLoggingInt16FixedArray
- TraceLoggingUInt16FixedArray
- TraceLoggingInt32FixedArray
- TraceLoggingUInt32FixedArray
- TraceLoggingInt64FixedArray
- TraceLoggingUInt64FixedArray
- TraceLoggingFloat32FixedArray
- TraceLoggingFloat64FixedArray
- TraceLoggingBoolFixedArray
- TraceLoggingGuidFixedArray
- TraceLoggingPointerFixedArray
- TraceLoggingFileTimeFixedArray
- TraceLoggingSystemTimeFixedArray
- TraceLoggingHexInt8FixedArray
- TraceLoggingHexUInt8FixedArray
- TraceLoggingHexInt32FixedArray
- TraceLoggingHexUInt32FixedArray
- TraceLoggingHexInt64FixedArray
- TraceLoggingHexUInt64FixedArray
- TraceLoggingWcharFixedArray
- TraceLoggingCharFixedArray
- TraceLoggingIntPtrFixedArray
- TraceLoggingUIntPtrFixedArray
- TraceLoggingBooleanFixedArray
- TraceLoggingHexInt16FixedArray
- TraceLoggingHexUInt16FixedArray
- TraceLoggingInt8Array
- TraceLoggingUInt8Array
- TraceLoggingInt16Array
- TraceLoggingUInt16Array
- TraceLoggingInt32Array
- TraceLoggingUInt32Array
- TraceLoggingInt64Array
- TraceLoggingUInt64Array
- TraceLoggingFloat32Array
- TraceLoggingFloat64Array
- TraceLoggingBoolArray
- TraceLoggingGuidArray
- TraceLoggingPointerArray
- TraceLoggingFileTimeArray
- TraceLoggingSystemTimeArray
- TraceLoggingHexInt8Array
- TraceLoggingHexUInt8Array
- TraceLoggingHexInt32Array
- TraceLoggingHexUInt32Array
- TraceLoggingHexInt64Array
- TraceLoggingHexUInt64Array
- TraceLoggingWcharArray
- TraceLoggingCharArray
- TraceLoggingIntPtrArray
- TraceLoggingUIntPtrArray
- TraceLoggingBooleanArray
- TraceLoggingHexInt16Array
- TraceLoggingHexUInt16Array
