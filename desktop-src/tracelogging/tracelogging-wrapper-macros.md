---
title: TraceLogging Wrapper Macros
description: Lists the wrapper macros for TraceLogging providers.
ms.assetid: 806F43F3-D376-4DBD-A4C5-B5F01E5D009D
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TraceLogging Wrapper Macros

Lists the wrapper macros for TraceLogging providers.

In order to record events using TraceLogging providers, you need to use the TraceLogging write macros [**TraceLoggingWrite**](/windows/win32/traceloggingprovider/nf-traceloggingprovider-traceloggingwrite?branch=master) or [**TraceLoggingWriteActivity**](/windows/win32/traceloggingprovider/nf-traceloggingprovider-traceloggingwriteactivity?branch=master). Both of these macros require you to wrap any event data in a wrapper macro. There are several different wrapper macros for different data types. For a complete list of TraceLogging macros, see [TraceLogging Macros](trace-logging-macros.md).

In addition to the wrapper macros above, several macros are available for individual data types. All of these macros have the same format as the [TraceLoggingValue](/windows/win32/traceloggingprovider/nf-traceloggingprovider-traceloggingvalue?branch=master) macro. You can use the TraceLoggingValue macro to automatically detect the appropriate wrapper macro to use, or use the specific macro directly.

-   [**TraceLoggingBinary**](/windows/win32/traceloggingprovider/nf-traceloggingprovider-traceloggingbinary?branch=master)
-   [**TraceLoggingChannel**](/windows/win32/traceloggingprovider/nf-traceloggingprovider-traceloggingchannel?branch=master)
-   [**TraceLoggingCustomAttribute**](/windows/win32/traceloggingprovider/nf-traceloggingprovider-traceloggingcustomattribute?branch=master)
-   [**TraceLoggingDescription**](/windows/win32/traceloggingprovider/nf-traceloggingprovider-traceloggingdescription?branch=master)
-   [**TraceLoggingEventTag**](/windows/win32/traceloggingprovider/nf-traceloggingprovider-traceloggingeventtag?branch=master)
-   [**TraceLoggingKeyword**](/windows/win32/traceloggingprovider/nf-traceloggingprovider-traceloggingkeyword?branch=master)
-   [**TraceLoggingLevel**](/windows/win32/traceloggingprovider/nf-traceloggingprovider-tracelogginglevel?branch=master)
-   [**TraceLoggingOpcode**](/windows/win32/traceloggingprovider/nf-traceloggingprovider-traceloggingopcode?branch=master)
-   [**TraceLoggingSocketAddress**](/windows/win32/traceloggingprovider/nf-traceloggingprovider-traceloggingsocketaddress?branch=master)
-   [**TraceLoggingStruct**](/windows/win32/traceloggingprovider/nf-traceloggingprovider-traceloggingstruct?branch=master)
-   [**TraceLoggingValue**](/windows/win32/traceloggingprovider/nf-traceloggingprovider-traceloggingvalue?branch=master)

> [!Note]
>
> **TraceLoggingOptionGroup** is specifically for use inside of TRACELOGGING\_DEFINE\_PROVIDER.
>
> -   [**TraceLoggingOptionGroup**](/windows/win32/traceloggingprovider/nf-traceloggingprovider-traceloggingoptiongroup?branch=master)

 

Here are the individual wrapper macros.

-   TraceLoggingInt8

-   TraceLoggingUInt8

-   TraceLoggingInt16

-   TraceLoggingUInt16

-   TraceLoggingInt32

-   TraceLoggingUInt32

-   TraceLoggingInt64

-   TraceLoggingUInt64

-   TraceLoggingFloat32

-   TraceLoggingFloat64

-   TraceLoggingBool

-   TraceLoggingFileTime

-   TraceLoggingGuid

-   TraceLoggingPointer

-   TraceLoggingSystemTime

-   TraceLoggingHexInt8

-   TraceLoggingHexUInt8

-   TraceLoggingHexInt32

-   TraceLoggingHexUInt32

-   TraceLoggingHexInt64

-   TraceLoggingHexUInt64

-   TraceLoggingWchar

-   TraceLoggingChar

-   TraceLoggingIntPtr

-   TraceLoggingUIntPtr

-   TraceLoggingBoolean

-   TraceLoggingHexInt16

-   TraceLoggingHexUInt16

-   TraceLoggingPid

-   TraceLoggingTid

-   TraceLoggingPort

-   TraceLoggingWinError

-   TraceLoggingNTStatus

-   TraceLoggingHResult

-   TraceLoggingSocketAddress

-   TraceLoggingSid

-   TraceLoggingString

-   TraceLoggingWideString

-   TraceLoggingCountedString

-   TraceLoggingCountedWideString

-   TraceLoggingAnsiString

-   TraceLoggingUnicodeString

-   TraceLoggingBinary(void \*data, size of the data in bytes, \[optional\] name ) The parameters to this macro differ from those above. If the *name* parameter is specified, it must be a string literal (not a variable) and may not contain any embedded null characters. If the *name* parameter is not provided, a name is generated automatically.

The TraceLogging API also makes several macros available for arrays. These arrays can either have a fixed length or be of a variable length, depending on the wrapper macro you choose to use. All of these wrapper macros follow this format.

`TraceLoggingBooleanArray(pVals, cVals, name, desc, tags)`

The parameter *pVals* points to the array of data and *cVals* indicates the number of elements in the array. *cVals* must be a constant and cannot be a variable. As with the single value wrapper macros, *name*, **desc**, and *tags* are optional parameters and must follow the same restrictions as explained with the **TraceLoggingValue** macro.

-   TraceLoggingInt8FixedArray

-   TraceLoggingUInt8FixedArray

-   TraceLoggingInt16FixedArray

-   TraceLoggingUInt16FixedArray

-   TraceLoggingInt32FixedArray

-   TraceLoggingUInt32FixedArray

-   TraceLoggingInt64FixedArray

-   TraceLoggingUInt64FixedArray

-   TraceLoggingFloat32FixedArray

-   TraceLoggingFloat64FixedArray

-   TraceLoggingBoolFixedArray

-   TraceLoggingGuidFixedArray

-   TraceLoggingPointerFixedArray

-   TraceLoggingFileTimeFixedArray

-   TraceLoggingSystemTimeFixedArray

-   TraceLoggingHexInt8FixedArray

-   TraceLoggingHexUInt8FixedArray

-   TraceLoggingHexInt32FixedArray

-   TraceLoggingHexUInt32FixedArray

-   TraceLoggingHexInt64FixedArray

-   TraceLoggingHexUInt64FixedArray

-   TraceLoggingWcharFixedArray

-   TraceLoggingCharFixedArray

-   TraceLoggingIntPtrFixedArray

-   TraceLoggingUIntPtrFixedArray

-   TraceLoggingBooleanFixedArray

-   TraceLoggingHexInt16FixedArray

-   TraceLoggingHexUInt16FixedArray

-   TraceLoggingInt8Array

-   TraceLoggingUInt8Array

-   TraceLoggingInt16Array

-   TraceLoggingUInt16Array

-   TraceLoggingInt32Array

-   TraceLoggingUInt32Array

-   TraceLoggingInt64Array

-   TraceLoggingUInt64Array

-   TraceLoggingFloat32Array

-   TraceLoggingFloat64Array

-   TraceLoggingBoolArray

-   TraceLoggingGuidArray

-   TraceLoggingPointerArray

-   TraceLoggingFileTimeArray

-   TraceLoggingSystemTimeArray

-   TraceLoggingHexInt8Array

-   TraceLoggingHexUInt8Array

-   TraceLoggingHexInt32Array

-   TraceLoggingHexUInt32Array

-   TraceLoggingHexInt64Array

-   TraceLoggingHexUInt64Array

-   TraceLoggingWcharArray

-   TraceLoggingCharArray

-   TraceLoggingIntPtrArray

-   TraceLoggingUIntPtrArray

-   TraceLoggingBooleanArray

-   TraceLoggingHexInt16Array

-   TraceLoggingHexUInt16Array

 

 




