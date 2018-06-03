---
Description: Enables or disables the specified event trace provider.
ms.assetid: 3aceffb6-614f-4cad-bbec-f181f0cbdbff
title: EnableTraceEx2 function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# EnableTraceEx2 function

The **EnableTraceEx2** function enables or disables the specified event trace provider.

This function supersedes the [**EnableTraceEx**](enabletraceex-func.md) function.

## Syntax


```C++
ULONG EnableTraceEx2(
  _In_     TRACEHANDLE              TraceHandle,
  _In_     LPCGUID                  ProviderId,
  _In_     ULONG                    ControlCode,
  _In_     UCHAR                    Level,
  _In_     ULONGLONG                MatchAnyKeyword,
  _In_     ULONGLONG                MatchAllKeyword,
  _In_     ULONG                    Timeout,
  _In_opt_ PENABLE_TRACE_PARAMETERS EnableParameters
);
```



## Parameters

<dl> <dt>

*TraceHandle* \[in\]
</dt> <dd>

A handle of the event tracing session to which you want to enable or disable the provider. The [**StartTrace**](starttrace.md) function returns this handle.

</dd> <dt>

*ProviderId* \[in\]
</dt> <dd>

A GUID of the event trace provider that you want to enable or disable.

</dd> <dt>

*ControlCode* \[in\]
</dt> <dd>

You can specify one of the following control codes:



| Value                                                                                                                                                                                                                              | Meaning                                                                                                                                                                                    |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="EVENT_CONTROL_CODE_DISABLE_PROVIDER"></span><span id="event_control_code_disable_provider"></span><dl> <dt>**EVENT\_CONTROL\_CODE\_DISABLE\_PROVIDER**</dt> </dl> | Disables the provider.<br/>                                                                                                                                                          |
| <span id="EVENT_CONTROL_CODE_ENABLE_PROVIDER"></span><span id="event_control_code_enable_provider"></span><dl> <dt>**EVENT\_CONTROL\_CODE\_ENABLE\_PROVIDER**</dt> </dl>    | Enables the provider. The session receives events when the provider is registered.<br/>                                                                                              |
| <span id="EVENT_CONTROL_CODE_CAPTURE_STATE"></span><span id="event_control_code_capture_state"></span><dl> <dt>**EVENT\_CONTROL\_CODE\_CAPTURE\_STATE**</dt> </dl>          | Requests that the provider log its state information. First you would enable the provider and then call **EnableTraceEx2** with this control code to capture state information.<br/> |



 

</dd> <dt>

*Level* \[in\]
</dt> <dd>

A provider-defined value that specifies the level of detail included in the event. Specify one of the following levels that are defined in the *Winmeta.h* header file. Higher numbers imply that you get lower levels as well. For example, if you specify TRACE\_LEVEL\_WARNING, you also receive all warning, error, and critical events.



| Value                                                                                                                                                                                                                                               | Meaning                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <span id="TRACE_LEVEL_CRITICAL"></span><span id="trace_level_critical"></span><dl> <dt>**TRACE\_LEVEL\_CRITICAL**</dt> <dt>1</dt> </dl>          | Abnormal exit or termination events<br/>           |
| <span id="TRACE_LEVEL_ERROR"></span><span id="trace_level_error"></span><dl> <dt>**TRACE\_LEVEL\_ERROR**</dt> <dt>2</dt> </dl>                   | Severe error events<br/>                           |
| <span id="TRACE_LEVEL_WARNING"></span><span id="trace_level_warning"></span><dl> <dt>**TRACE\_LEVEL\_WARNING**</dt> <dt>3</dt> </dl>             | Warning events such as allocation failures<br/>    |
| <span id="TRACE_LEVEL_INFORMATION"></span><span id="trace_level_information"></span><dl> <dt>**TRACE\_LEVEL\_INFORMATION**</dt> <dt>4</dt> </dl> | Non-error events such as entry or exit events<br/> |
| <span id="TRACE_LEVEL_VERBOSE"></span><span id="trace_level_verbose"></span><dl> <dt>**TRACE\_LEVEL\_VERBOSE**</dt> <dt>5</dt> </dl>             | Detailed trace events<br/>                         |



 

</dd> <dt>

*MatchAnyKeyword* \[in\]
</dt> <dd>

A bitmask of keywords that determine the category of events that you want the provider to write. The provider writes the event if any of the event's keyword bits match any of the bits set in this mask. See Remarks.

</dd> <dt>

*MatchAllKeyword* \[in\]
</dt> <dd>

This bitmask is optional. This mask further restricts the category of events that you want the provider to write. If the event's keyword meets the *MatchAnyKeyword* condition, the provider will write the event only if all of the bits in this mask exist in the event's keyword. This mask is not used if *MatchAnyKeyword* is zero. See Remarks.

</dd> <dt>

*Timeout* \[in\]
</dt> <dd>

Set to zero to enable the trace asynchronously; this is the default. If the timeout value is zero, this function calls the provider's enable callback and returns immediately. To enable the trace synchronously, specify a timeout value, in milliseconds. If you specify a timeout value, this function calls the provider's enable callback and waits until the callback exits or the timeout expires. To wait forever, set to INFINITE.

</dd> <dt>

*EnableParameters* \[in, optional\]
</dt> <dd>

The trace parameters used to enable the provider. For details, see [**ENABLE\_TRACE\_PARAMETERS**](enable-trace-parameters.md) and [**ENABLE\_TRACE\_PARAMETERS\_V1**](enable-trace-parameters-v1.md).

</dd> </dl>

## Return value

If the function is successful, the return value is **ERROR\_SUCCESS**.

If the function fails, the return value is one of the [system error codes](https://msdn.microsoft.com/windows/desktop/4a3a8feb-a05f-4614-8f04-1f507da7e5b7). The following table includes some common errors and their causes.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><dl> <dt><strong>ERROR_INVALID_PARAMETER</strong></dt> </dl></td>
<td>A parameter is incorrect. <br/> This can occur if any of the following are true:<br/>
<ul>
<li>The <em>ProviderId</em> is <strong>NULL</strong>.</li>
<li>The <em>TraceHandle</em> is <strong>NULL</strong>.</li>
</ul></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>ERROR_TIMEOUT</strong></dt> </dl></td>
<td>The timeout value expired before the enable callback completed. For details, see the <em>Timeout</em> parameter.<br/></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>ERROR_INVALID_FUNCTION</strong></dt> </dl></td>
<td>You cannot update the level when the provider is not registered.<br/></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>ERROR_NO_SYSTEM_RESOURCES</strong> </dt> </dl></td>
<td>Exceeded the number of trace sessions that can enable the provider.<br/></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>ERROR_ACCESS_DENIED</strong></dt> </dl></td>
<td>Only users with administrative privileges, users in the <em>Performance Log Users</em> group, and services running as <em>LocalSystem</em>, <em>LocalService</em>, or <em>NetworkService</em> can enable trace providers. To grant a restricted user the ability to enable a trace provider, add them to the <em>Performance Log Users</em> group or see [<strong>EventAccessControl</strong>](/windows/desktop/api/Evntcons/nf-evntcons-eventaccesscontrol).<br/> <strong>Windows XP and Windows 2000:</strong> Anyone can enable a trace provider.<br/></td>
</tr>
</tbody>
</table>



 

## Remarks

Event trace controllers call this function.

The provider defines its interpretation of being enabled or disabled. Typically, if a provider has been enabled, it generates events, but while it is disabled, it does not.

Event Tracing for Windows (ETW) supports several categories of filtering.

-   Schematized filtering - This is the traditional filtering setup also called provider-side filtering. The controller defines a custom set of filters as a binary object that is passed to the provider in the [**EnableTrace**](enabletrace.md) call. It is incumbent on the controller and provider to define and interpret these filters and the controller should only log applicable events. This requires a close coupling of the controller and provider since the type and format of the binary object of what can be filtered is not defined. The [**TdhEnumerateProviderFilters**](/windows/desktop/api/Tdh/nf-tdh-tdhenumerateproviderfilters) function can be used to retrieve the filters defined in a manifest.
-   Scope filtering - Certain providers are enabled or not enabled to a session based on whether or not they meet the criteria specified by the scope filters. There are several types of scope filters that allow filtering based on the event ID, the process ID (PID), executable filename, the app ID, and the app package name. This feature is supported on Windows 8.1,Windows Server 2012 R2, and later.
-   Stackwalk filtering - This notifies ETW to only perform a stack walk for a given set of event IDs. This feature is supported on Windows 8.1,Windows Server 2012 R2, and later.
-   Event payload filtering - For manifest providers, events can be filtered on-the-fly based on whether or not they satisfy a logical expression based on one or more predicates.

Every time **EnableTraceEx2** is called, the filters for the provider in that session are replaced by the new parameters defined by the parameters passed to the **EnableTraceEx2** function. Multiple filters passed in a single **EnableTraceEx2** call can be combined with an additive effect. To disable filtering and thereby enable all providers/events in the logging session, call **EnableTraceEx2** with the *EnableParameters* parameter pointed to an [**ENABLE\_TRACE\_PARAMETERS**](enable-trace-parameters.md) structure with the **FilterDescCount** member set to 0.

Each filter passed to the **EnableTraceEx2** function is specified by a **Type** member in the [**EVENT\_FILTER\_DESCRIPTOR**](/windows/desktop/api/Evntprov/ns-evntprov-_event_filter_descriptor). An array of **EVENT\_FILTER\_DESCRIPTOR** structures is passed in the [**ENABLE\_TRACE\_PARAMETERS**](enable-trace-parameters.md) structure passed in the **EnableParameters** parameter to the **EnableTraceEx2** function.

Each type of filter (a specific **Type** member) may only appear once in a call to the **EnableTraceEx2** function, however, some filter types allow multiple conditions to be included in a single filter. The maximum number of filters that can be included in a call to **EnableTraceEx2** is set by **MAX\_EVENT\_FILTERS\_COUNT** defined to be 8 in the *Evntprov.h* header file.

Each filter type has its own size or entity limits based on the specific **Type** member in the [**EVENT\_FILTER\_DESCRIPTOR**](/windows/desktop/api/Evntprov/ns-evntprov-_event_filter_descriptor) structure. The list below indicates these limits.



| Term                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="EVENT_FILTER_TYPE_SCHEMATIZED"></span><span id="event_filter_type_schematized"></span>**EVENT\_FILTER\_TYPE\_SCHEMATIZED**<br/>              | <dl> <dt>Filter size limit: **MAX\_EVENT\_FILTER\_DATA\_SIZE** (1024)</dt> <dt>Number of elements allowed: Defined by provider and controller</dt> </dl>                                                                   |
| <span id="EVENT_FILTER_TYPE_PID"></span><span id="event_filter_type_pid"></span>**EVENT\_FILTER\_TYPE\_PID**<br/>                                      | <dl> <dt>Filter size limit: **MAX\_EVENT\_FILTER\_DATA\_SIZE** (1024)</dt> <dt>Number of elements allowed: **MAX\_EVENT\_FILTER\_PID\_COUNT** (8) </dt> </dl>                                                              |
| <span id="EVENT_FILTER_TYPE_EXECUTABLE_NAME"></span><span id="event_filter_type_executable_name"></span>**EVENT\_FILTER\_TYPE\_EXECUTABLE\_NAME**<br/> | <dl> <dt>Filter size limit: **MAX\_EVENT\_FILTER\_DATA\_SIZE** (1024)</dt> <dt>Number of elements allowed: A single string that can contain multiple executable file names separated by semicolons. </dt> </dl>            |
| <span id="EVENT_FILTER_TYPE_PACKAGE_ID"></span><span id="event_filter_type_package_id"></span>**EVENT\_FILTER\_TYPE\_PACKAGE\_ID**<br/>                | <dl> <dt>Filter size limit: **MAX\_EVENT\_FILTER\_DATA\_SIZE** (1024)</dt> <dt>Number of elements allowed: A single string that can contain multiple package IDs separated by semicolons.</dt> </dl>                       |
| <span id="EVENT_FILTER_TYPE_PACKAGE_APP_ID"></span><span id="event_filter_type_package_app_id"></span>**EVENT\_FILTER\_TYPE\_PACKAGE\_APP\_ID**<br/>   | <dl> <dt>Filter size limit: **MAX\_EVENT\_FILTER\_DATA\_SIZE** (1024)</dt> <dt>Number of elements allowed: A single string that can contain multiple package relative app IDs (PRAIDs) separated by semicolons.</dt> </dl> |
| <span id="EVENT_FILTER_TYPE_PAYLOAD"></span><span id="event_filter_type_payload"></span>**EVENT\_FILTER\_TYPE\_PAYLOAD**<br/>                          | <dl> <dt>Filter size limit: 1**MAX\_EVENT\_FILTER\_PAYLOAD\_SIZE** (4096)</dt> <dt>Number of elements allowed: 1</dt> </dl>                                                                                                |
| <span id="EVENT_FILTER_TYPE_EVENT_ID"></span><span id="event_filter_type_event_id"></span>**EVENT\_FILTER\_TYPE\_EVENT\_ID**<br/>                      | <dl> <dt>Filter size limit: Not defined</dt> <dt>Number of elements allowed: **MAX\_EVENT\_FILTER\_EVENT\_ID\_COUNT** (64)</dt> </dl>                                                                                      |
| <span id="EVENT_FILTER_TYPE_STACKWALK"></span><span id="event_filter_type_stackwalk"></span>**EVENT\_FILTER\_TYPE\_STACKWALK**<br/>                    | <dl> <dt>Filter size limit: Not defined</dt> <dt>Number of elements allowed: **MAX\_EVENT\_FILTER\_EVENT\_ID\_COUNT** (64)</dt> </dl>                                                                                      |



 

To include all events that a provider provides, set *MatchAnyKeyword* to zero (for a [manifest-based](https://www.bing.com/search?q=manifest-based) provider or [TraceLogging](https://msdn.microsoft.com/windows/desktop/8C6A9E91-98F9-4D6B-A937-A22BA7CEB1E4) provider and 0xFFFFFFFF for a [classic](https://www.bing.com/search?q=classic) provider). To include specific events, set the *MatchAnyKeyword* mask to those specific events. To indicate that you wish to enable a Provider Group, use the EVENT\_ENABLE\_PROPERTY\_PROVIDER\_GROUP flag on the **EnableProperty** member of *EnableParameters*. For example, if the provider defines an event for its initialization and cleanup routines (set keyword bit 0), an event for its file operations (set keyword bit 1), and an event for its calculation operations (set keyword bit 2), you can set *MatchAnyKeyword* to 5 to receive initialization and cleanup events and calculation events.

If the provider defines more complex event keywords, for example, the provider defines an event that sets bit 0 for read and bit 1 for local access and a second event that sets bit 0 for read and bit 2 for remote access, you could set MatchAnyKeyword to 1 to receive all read events, or you could set MatchAnykeyword to 1 and MatchAllKeywords to 3 to receive local reads only.

If an event's keyword is zero, the provider will write the event to the session, regardless of the *MatchAnyKeyword* and *MatchAllKeyword* masks.

When you call **EnableTraceEx2** the provider may or may not be registered. If the provider is registered, ETW calls the provider's callback function, if it implements one, and the session begins receiving events. If the provider is not registered, ETW will call the provider's callback function when it registers itself, if it implements one, and the session will begin receiving events. If the provider is not registered, the provider's callback function will not receive the source ID or filter data. You can call **EnableTraceEx2** one time to enable a provider before the provider registers itself.

If the provider is registered and already enabled to your session, you can also use this function to update the *Level*, *MatchAnyKeyword*, *MatchAllKeyword* parameters, and the **EnableProperty** and **EnableFilterDesc** members of *EnableParameters*.

On Windows 8.1,Windows Server 2012 R2, and later, event payload , scope, and stack walk filters can be used by the **EnableTraceEx2** function and the [**ENABLE\_TRACE\_PARAMETERS**](enable-trace-parameters.md) and [**EVENT\_FILTER\_DESCRIPTOR**](/windows/desktop/api/Evntprov/ns-evntprov-_event_filter_descriptor) structures to filter on specific conditions in a logger session. For more information on event payload filters, see the [**TdhCreatePayloadFilter**](/windows/desktop/api/Tdh/nf-tdh-tdhcreatepayloadfilter), and [**TdhAggregatePayloadFilters**](/windows/desktop/api/Tdh/nf-tdh-tdhaggregatepayloadfilters) functions and the **ENABLE\_TRACE\_PARAMETERS**, **EVENT\_FILTER\_DESCRIPTOR**, and [**PAYLOAD\_FILTER\_PREDICATE**](/windows/desktop/api/Tdh/ns-tdh-_payload_filter_predicate) structures.

You do not call **EnableTraceEx2** to enable kernel providers. To enable kernel providers, set the **EnableFlags** member of [**EVENT\_TRACE\_PROPERTIES**](event-trace-properties.md) which you then pass to [**StartTrace**](starttrace.md). The **StartTrace** function enables the selected kernel providers.

Up to eight trace sessions can enable and receive events from the same [manifest-based](https://www.bing.com/search?q=manifest-based) provider or [TraceLogging](https://msdn.microsoft.com/windows/desktop/8C6A9E91-98F9-4D6B-A937-A22BA7CEB1E4) provider; however, only one trace session can enable a [classic](https://www.bing.com/search?q=classic) provider. If more than one session tried to enable a classic provider, the first session would stop receiving events when the second session enabled the same provider. For example, if Session A enabled Provider 1 and then Session B enabled Provider 1, only Session B would receive events from Provider 1.

The provider remains enabled for the session until the session disables the provider. If the application that started the session ends without disabling the provider, the provider remains enabled.

To determine the level and keywords used to enable a manifest-based provider, use one of the following commands:

-   Logman query providers &lt;provider-name&gt;
-   Wevtutil gp &lt;provider-name&gt;

For classic providers, it is up to the provider to document and make available to potential controllers the severity levels or enable flags that it supports. If the provider wants to be enabled by any controller, the provider should accept 0 for the severity level and enable flags and interpret 0 as a request to perform default logging (whatever that may be).

If you use **EnableTraceEx2** to enable a classic provider, the following translation occurs:

-   The *Level* parameter is the same as setting the *EnableLevel* parameter in [**EnableTrace**](enabletrace.md).
-   The *MatchAnyKeyword* is the same as setting the *EnableFlag* parameter in [**EnableTrace**](enabletrace.md) except that the keyword value is truncated from a ULONGLONG to a ULONG value.
-   In the [*ControlCallback*](controlcallback.md) callback, the provider can call [**GetTraceEnableLevel**](gettraceenablelevel.md) to get the level and [**GetTraceEnableFlags**](gettraceenableflags.md) to get the enable flag.
-   The other parameter are not used.

If **EnableTraceEx2** returns **ERROR\_INVALID\_PARAMETER** when enabling filtering, you can turn on tracing to view debugging messages about the failure. This requires a checked build.

## Examples

The following example shows you how to use the **EnableTraceEx2** with payload filters using the [**TdhCreatePayloadFilter**](/windows/desktop/api/Tdh/nf-tdh-tdhcreatepayloadfilter) and [**TdhAggregatePayloadFilters**](/windows/desktop/api/Tdh/nf-tdh-tdhaggregatepayloadfilters) functions to filter on specific conditions in a logger session.


```C++
#define INITGUID  
#include <windows.h>  
#include <stdlib.h>  
#include <stdio.h>  
#include <strsafe.h>  
#include <evntrace.h>  
#include <tdh.h>  
  
#define MAXIMUM_SESSION_NAME 1024  
  
#define PATH_TO_MANIFEST_FILE L"c:\\ExampleManifest.man"  
  
  
//  
// The following definitions would be found in the include file generated by  
// message compiler from the manifest file.  
//    
//+  
// Provider Example-Provider Event Count 2  
//+  EXTERN_C __declspec(selectany) const GUID EXAMPLE_PROVIDER = {0x37a59b93, 0xbb25, 0x4cee, {0x97, 0xaa, 0x8b, 0x6a, 0xcd, 0xc, 0x4d, 0xf8}};  
  
//  
// Event Descriptors  
//  
EXTERN_C __declspec(selectany) const EVENT_DESCRIPTOR Example_Event_1 = {0x1, 0x0, 0x0, 0x1, 0x0, 0x0, 0x0};  
#define Example_Event_1_value 0x1  
EXTERN_C __declspec(selectany) const EVENT_DESCRIPTOR Example_Event_2 = {0x2, 0x0, 0x0, 0x1, 0x0, 0x0, 0x0};  
#define Example_Event_2_value 0x2  
  
//  
// (End of snippet from include file)  
//    
  
// Allocate an EVENT_TRACE_PROPERTIES structure and set the needed logging session properties
PEVENT_TRACE_PROPERTIES AllocateTraceProperties (  
    _In_opt_ PWSTR LoggerName,  
    _In_opt_ PWSTR LogFileName  
    )  
{  
    PEVENT_TRACE_PROPERTIES TraceProperties = NULL;  
    ULONG BufferSize;  
  
    BufferSize = sizeof(EVENT_TRACE_PROPERTIES) +   
        (MAXIMUM_SESSION_NAME + MAX_PATH) * sizeof(WCHAR);  
  
    TraceProperties = (PEVENT_TRACE_PROPERTIES)malloc(BufferSize);    
    if (TraceProperties == NULL) {  
        wprintf(L"Unable to allocate %d bytes for properties structure.\n", BufferSize);  
        goto Exit;  
    }  
  
    //      
    // Set the session properties.      
    //    
    ZeroMemory(TraceProperties, BufferSize);  
    TraceProperties->Wnode.BufferSize = BufferSize;  
    TraceProperties->Wnode.Flags = WNODE_FLAG_TRACED_GUID;  
    TraceProperties->LoggerNameOffset = sizeof(EVENT_TRACE_PROPERTIES);  
    TraceProperties->LogFileNameOffset = sizeof(EVENT_TRACE_PROPERTIES) +   
        (MAXIMUM_SESSION_NAME * sizeof(WCHAR));   
  
    if (LoggerName != NULL) {  
        StringCchCopy((LPWSTR)((PCHAR)TraceProperties + TraceProperties->LoggerNameOffset),   
                      MAXIMUM_SESSION_NAME,  
                      LoggerName);  
    }  
  
    if (LogFileName != NULL) {  
        StringCchCopy((LPWSTR)((PCHAR)TraceProperties + TraceProperties->LogFileNameOffset),   
                      MAX_PATH,   
                      LogFileName);  
    }  
  
Exit:  
    return TraceProperties;  
}  

// Free the EVENT_TRACE_PROPERTIES structure previously allocated
VOID FreeTraceProperties (  
    _In_ PEVENT_TRACE_PROPERTIES TraceProperties  
    )  
{  
    free(TraceProperties);  
    return;  
}  

// Set the values needed in a PAYLOAD_FILTER_PREDICATE for a single payload filter  
FORCEINLINE VOID PayloadPredicateCreate(  
    _Out_ PPAYLOAD_FILTER_PREDICATE Predicate,  
    _In_ LPWSTR FieldName,  
    USHORT CompareOp,  
    LPWSTR Value  
)  
{  
    Predicate->FieldName = FieldName;  
    Predicate->CompareOp = CompareOp;  
    Predicate->Value = Value;  
    return;  
}  
  
int __cdecl wmain()  
{  
    UINT i;  
    PVOID EventFilters[2];  
    EVENT_FILTER_DESCRIPTOR FilterDescriptor;  
    UINT PredicateCount;  
    PAYLOAD_FILTER_PREDICATE Predicates[3];  
    ULONG FilterCount;  
    ULONG Status = ERROR_SUCCESS;  
    TRACEHANDLE SessionHandle = 0;  
    PEVENT_TRACE_PROPERTIES TraceProperties;  
    BOOLEAN TraceStarted = FALSE;  
    PWSTR LoggerName = L"MyTrace";  
    ENABLE_TRACE_PARAMETERS EnableParameters;  
  
    ZeroMemory(EventFilters, sizeof(EventFilters));  
    ZeroMemory(Predicates, sizeof(Predicates));  
    TraceProperties = NULL;  
    FilterCount = 0;  
  
    //      
    // Load the manifest for the provider      
    //    
    Status = TdhLoadManifest(PATH_TO_MANIFEST_FILE);  
    if (Status != ERROR_SUCCESS) {  
        wprintf(L"TdhCreatePayloadFilter() failed with %lu\n", Status);  
        goto Exit;  
    }  
  
    //      
    // Create predicates that match the following high-level expression:      
    //      
    // INCLUDE Example_Event_1 IF      
    //     Example_Event_1.Initiator == "User" AND      
    //     7 <= Example_Event_1.Level <= 16      
    //        
    PredicateCount = 0;  
  
    PayloadPredicateCreate(&amp;Predicates[PredicateCount++],  
                           L"Initiator",  
                           PAYLOADFIELD_IS,  
                           L"User");  
  
    PayloadPredicateCreate(&amp;Predicates[PredicateCount++],  
                           L"Level",  
                           PAYLOADFIELD_BETWEEN,  
                           L"7,16");  
  
    Status = TdhCreatePayloadFilter(&amp;EXAMPLE_PROVIDER,  
                                    &amp;Example_Event_1,  
                                    FALSE,      // Match all predicates (AND)                                      PredicateCount,  
                                    Predicates,  
                                    &amp;EventFilters[FilterCount++]);  
    if (Status != ERROR_SUCCESS) {  
        wprintf(L"TdhCreatePayloadFilter() failed with %lu\n", Status);  
        goto Exit;  
    }  
  
    //      
    // Create predicates that match the following high-level expression:      
    // INCLUDE Example_Event_2 IF      
    //      Example_Event_2.Title CONTAINS "UNI" OR      
    //      Example_Event_2.InstanceId == {0E95CFBC-58D4-44BA-BE40-E63A853536DF} OR      
    //      Example_Event_2.ErrorCode != 0      //    
    PredicateCount = 0;  
  
    PayloadPredicateCreate(&amp;Predicates[PredicateCount++],  
                           L"Title",  
                           PAYLOADFIELD_CONTAINS,  
                           L"UNI");  
  
    PayloadPredicateCreate(&amp;Predicates[PredicateCount++],  
                           L"InstanceId",  
                           PAYLOADFIELD_IS,  
                           L" {0E95CFBC-58D4-44BA-BE40-E63A853536DF}");  
  
    PayloadPredicateCreate(&amp;Predicates[PredicateCount++],  
                           L"ErrorCode",  
                           PAYLOADFIELD_NE,  
                           L"0");  
  
    Status = TdhCreatePayloadFilter(&amp;EXAMPLE_PROVIDER,  
                                    &amp;Example_Event_2,  
                                    FALSE,      // Match any predicates (OR)                                      PredicateCount,  
                                    Predicates,  
                                    &amp;EventFilters[FilterCount++]);  
    if (Status != ERROR_SUCCESS) {  
        wprintf(L"TdhCreatePayloadFilter() failed with %lu\n", Status);  
        goto Exit;  
    }  
  
    //      
    // Combine the interim filters into a final filter descriptor.      
    //    
    Status = TdhAggregatePayloadFilters(FilterCount,  
                                        EventFilters,  
                                        NULL,  
                                        &amp;FilterDescriptor);  
    if (Status != ERROR_SUCCESS) {  
        wprintf(L"TdhAggregatePayloadFilters() failed with %lu\n", Status);  
        goto Exit;  
    }  
  
    //      
    // Clean up the interim filters      
    //    
    for (i = 0; i < FilterCount; i++) {  
  
        Status = TdhDeletePayloadFilter(&amp;EventFilters[i]);  
        if (Status != ERROR_SUCCESS) {  
            wprintf(L"TdhDeletePayloadFilter() failed with %lu\n", Status);  
            goto Exit;  
        }  
    }  
  
  
  
    //      
    // Create a new trace session      
    //    
    //      
    // Allocate EVENT_TRACE_PROPERTIES structure and perform some      
    // basic initialization.       
    //      
    // N.B. LoggerName will be populated during StartTrace call.      
    //    
    TraceProperties = AllocateTraceProperties(NULL, L"SystemTrace.etl");  
    if (TraceProperties == NULL) {  
        Status = ERROR_OUTOFMEMORY;  
        goto Exit;  
    }  
  
    TraceProperties->LogFileMode = EVENT_TRACE_FILE_MODE_SEQUENTIAL | EVENT_TRACE_SYSTEM_LOGGER_MODE;  
    TraceProperties->MaximumFileSize = 100; // Limit file size to 100MB max      
    TraceProperties->BufferSize = 512; // Use 512KB trace buffers      
    TraceProperties->MinimumBuffers = 8;  
    TraceProperties->MaximumBuffers = 64;  
  
    Status = StartTrace(&amp;SessionHandle, LoggerName, TraceProperties);  
    if (Status != ERROR_SUCCESS) {  
        wprintf(L"StartTrace() failed with %lu\n", Status);  
        goto Exit;  
    }  
  
    TraceStarted = TRUE;  
  
    //      
    // Enable the provider to a trace session with filtering enabled on the      
    // provider      
    //    
    ZeroMemory(&amp;EnableParameters, sizeof(EnableParameters));  
    EnableParameters.Version = ENABLE_TRACE_PARAMETERS_VERSION_2;  
    EnableParameters.EnableFilterDesc = &amp;FilterDescriptor;  
    EnableParameters.FilterDescCount = 1;  
  
    Status = EnableTraceEx2(SessionHandle,  
                            &amp;EXAMPLE_PROVIDER,  
                            EVENT_CONTROL_CODE_ENABLE_PROVIDER,  
                            TRACE_LEVEL_VERBOSE,  
                            0,  
                            0,  
                            0,  
                            &amp;EnableParameters);  
    if (Status != ERROR_SUCCESS) {  
        wprintf(L"EnableTraceEx2() failed with %lu\n", Status);  
        goto Exit;  
    }  
  
    //      
    // Clean up the payload descriptor      
    //    
    Status = TdhCleanupPayloadEventFilterDescriptor(&amp;FilterDescriptor);  
    if (Status != ERROR_SUCCESS) {  
        wprintf(L"TdhCleanupPayloadEventFilterDescriptor() failed with %lu\n", Status);  
        goto Exit;  
    }  
  
    //      
    // Collect trace for 30 seconds      
    //    
    Sleep(30 * 1000);  
  
Exit:  
  
    //      
    // Stop tracing.      
    //    
    if (TraceStarted != FALSE) {  
        Status = ControlTrace(SessionHandle, NULL, TraceProperties, EVENT_TRACE_CONTROL_STOP);    
        if (Status != ERROR_SUCCESS) {  
            wprintf(L"StopTrace() failed with %lu\n", Status);  
        }  
    }  
  
    if (TraceProperties != NULL) {  
        FreeTraceProperties(TraceProperties);  
    }  
  
    TdhUnloadManifest(PATH_TO_MANIFEST_FILE);  
  
    return Status;  
}  
```



## Requirements



|                                     |                                                                                                                                                                                                                                                                              |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                                                                                                                                                                                                            |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                                                                                                                                                                                                               |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl>                                                                                                                                                                                        |
| Library<br/>                  | <dl> <dt>Sechost.lib on Windows 8.1 and Windows Server 2012 R2; </dt> <dt>Advapi32.lib on Windows 8, Windows Server 2012, Windows 7 and Windows Server 2008 R2</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Sechost.dll on Windows 8.1 and Windows Server 2012 R2; </dt> <dt>Advapi32.dll on Windows 8, Windows Server 2012, Windows 7 and Windows Server 2008 R2</dt> </dl> |



## See also

<dl> <dt>

[**EnableTrace**](enabletrace.md)
</dt> <dt>

[**EnableTraceEx**](enabletraceex-func.md)
</dt> <dt>

[**ENABLE\_TRACE\_PARAMETERS**](enable-trace-parameters.md)
</dt> <dt>

[**ENABLE\_TRACE\_PARAMETERS\_V1**](enable-trace-parameters-v1.md)
</dt> <dt>

[**EVENT\_FILTER\_DESCRIPTOR**](/windows/desktop/api/Evntprov/ns-evntprov-_event_filter_descriptor)
</dt> <dt>

[**GetTraceEnableFlags**](gettraceenableflags.md)
</dt> <dt>

[**GetTraceEnableLevel**](gettraceenablelevel.md)
</dt> <dt>

[**PAYLOAD\_FILTER\_PREDICATE**](/windows/desktop/api/Tdh/ns-tdh-_payload_filter_predicate)
</dt> <dt>

[**StartTrace**](starttrace.md)
</dt> <dt>

[**TdhAggregatePayloadFilters**](/windows/desktop/api/Tdh/nf-tdh-tdhaggregatepayloadfilters)
</dt> <dt>

[**TdhCreatePayloadFilter**](/windows/desktop/api/Tdh/nf-tdh-tdhcreatepayloadfilter)
</dt> <dt>

[**TdhEnumerateProviderFilters**](/windows/desktop/api/Tdh/nf-tdh-tdhenumerateproviderfilters)
</dt> </dl>

 

 




