---
description: Once you have begun an event tracing session, you can use TraceSetInformation to instruct the system to return additional event tracing data.
ms.assetid: 65CCD658-869E-40C4-83AE-34CC2720B7CB
title: Retrieving Additional Event Tracing Data
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Additional Event Tracing Data

Once you have begun an event tracing session, you can use [**TraceSetInformation**](/windows/win32/api/evntrace/nf-evntrace-tracesetinformation) to instruct the system to return additional event tracing data. The additional information will be placed in the extended data section of the relevant event trace.

The following procedure describes how to use the [**TraceSetInformation**](/windows/win32/api/evntrace/nf-evntrace-tracesetinformation) function to retrieve additional data from an event tracing session.

**To retrieve additional event tracing data**

1.  Start your session with a call to [**StartTrace**](/windows/win32/api/evntrace/nf-evntrace-starttracea).

    For more information, see [Configuring and Starting an Event Tracing Session](configuring-and-starting-an-event-tracing-session.md).

2.  Call [**TraceSetInformation**](/windows/win32/api/evntrace/nf-evntrace-tracesetinformation) to set additional event tracing data.

    use the [**EVENT\_INFO\_CLASS**](/windows/desktop/api/Evntprov/ne-evntprov-event_info_class) enumeration in the *ClassInformation* parameter to describe the additional information you wish to retrieve. The following example describes how to call [**TraceSetInformation**](/windows/win32/api/evntrace/nf-evntrace-tracesetinformation), using the session handle returned from the call to [**StartTrace**](/windows/win32/api/evntrace/nf-evntrace-starttracea), and the **TraceProviderBinaryTracking** value from **EVENT\_INFO\_CLASS**.

    ```C++
    BOOLEAN enabled = TRUE;
    Win32Error error = TraceSetInformation(
        m_sessionHandle,
        TraceProviderBinaryTracking,
        &enabled,
        sizeof(enabled));
    ```

    

3.  Alternately, you can use [**TraceQueryInformation**](/windows/win32/api/evntrace/nf-evntrace-tracequeryinformation) to retrieve information about the current event tracing session settings.

    Like [**TraceSetInformation**](/windows/win32/api/evntrace/nf-evntrace-tracesetinformation), [**TraceQueryInformation**](/windows/win32/api/evntrace/nf-evntrace-tracequeryinformation) uses the [**EVENT\_INFO\_CLASS**](/windows/desktop/api/Evntprov/ne-evntprov-event_info_class) enumeration to describe what information to retrieve from the system.

 

 
