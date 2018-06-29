---
Description: Information relating to a periodic capture state.
ms.assetid: 6C032D97-4B37-48D2-BD1A-35B8BA48B8AB
title: TRACE\_PERIODIC\_CAPTURE\_STATE\_INFO structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TRACE_PERIODIC_CAPTURE_STATE_INFO
api_type: 
- HeaderDef
api_location: 
- Evntrace.h
---

# TRACE\_PERIODIC\_CAPTURE\_STATE\_INFO structure

Information relating to a periodic capture state.

## Syntax


```C++
typedef struct _TRACE_PERIODIC_CAPTURE_STATE_INFO {
  ULONG  CaptureStateFrequencyInSeconds;
  USHORT ProviderCount;
  USHORT Reserved;
} TRACE_PERIODIC_CAPTURE_STATE_INFO, *PTRACE_PERIODIC_CAPTURE_STATE_INFO;
```



## Members

<dl> <dt>

**CaptureStateFrequencyInSeconds**
</dt> <dd>

The frequency of state captures in seconds.

</dd> <dt>

**ProviderCount**
</dt> <dd>

The number of providers.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for future use.

</dd> </dl>

## Remarks

Periodic capture state is a way to allow capture state notifications to be routinely sent to providers. When this is enabled, notifications will only be sent to provider registrations that have been previously enabled to the current session. Each provider can define its own response (if any) to a notification. Note that events logged by the provider in response to a notification will be sent to every ETW session that the provider is enabled to, similar to a manually requested capture state.

To use periodic capture state:

-   Allocate a buffer of type **TRACE\_PERIODIC\_CAPTURE\_STATE\_INFO**. The size of the buffer should be: sizeof(**TRACE\_PERIODIC\_CAPTURE\_STATE\_INFO**) + (x \* sizeof(GUID)), where x is the number of providers you would like to enable.
-   Call [**TraceQueryInformation**](tracequeryinformation.md) using **TracePeriodicCaptureStateInfo** for the [**TRACE\_INFO\_CLASS**](trace-info-class.md) enumeration. Pass the buffer and its size as the *TraceInformation* and *InformationLength* parameters of **TraceQueryInformation**.
-   Set **CaptureStateFrequencyInSeconds** from **TRACE\_PERIODIC\_CAPTURE\_STATE\_INFO** to the minimum frequency supported by the version of Windows. This value may change in the future, so hard coding it is not recommended. If the frequency is below the minimum, the call to [**TraceSetInformation**](tracesetinformation.md) will fail.
-   Set the **ProviderCount** from **TRACE\_PERIODIC\_CAPTURE\_STATE\_INFO** to the number of provider GUIDs being passed.
-   Add the GUIDs of each provider after the end of the **TRACE\_PERIODIC\_CAPTURE\_STATE\_INFO** structure. This uses the extra space allocated from (x \* sizeof(GUID) from the first step.
-   Call [**TraceSetInformation**](tracesetinformation.md) using **TracePeriodicCaptureStateListInfo** from the [**TRACE\_INFO\_CLASS**](trace-info-class.md) enumeration.
-   To turn periodic capture state off, call [**TraceSetInformation**](tracesetinformation.md) again with **TracePeriodicCaptureStateListInfo** from the [**TRACE\_INFO\_CLASS**](trace-info-class.md), NULL for the **TraceInformation**, and 0 as the **InformationLength**.

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Evntrace.h</dt> </dl> |



 

 




