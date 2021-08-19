---
description: The AutoLogger event tracing session records events that occur early in the operating system boot process.
ms.assetid: df5a79f4-abbf-4b83-afc3-cbd14b166067
title: Configuring and Starting an AutoLogger Session
ms.topic: article
ms.date: 05/31/2018
---

# Configuring and Starting an AutoLogger Session

The AutoLogger event tracing session records events that occur early in the operating system boot process. Applications and device drivers can use the AutoLogger session to capture traces before the user logs in. Note that some device drivers, such as disk device drivers, are not loaded at the time the AutoLogger session begins.

The AutoLogger differs from the Global Logger in the following ways:

-   You can specify one or more AutoLogger sessions (the Global Logger was a single session to which everyone logged events).
-   The AutoLogger sends an enable notification to the providers when the session starts (the Global Logger did not send an enable notification to the providers, so the providers had to rely on other means to know if the Global Logger session was started in order to begin logging events).
-   The AutoLogger does not support logging NT Kernel Logger events (see the **EnableFlags** member of [**EVENT\_TRACE\_PROPERTIES**](/windows/win32/api/evntrace/ns-evntrace-event_trace_properties)). To log NT Kernel Logger events, you must use the [Global Logger](configuring-and-starting-the-global-logger-session.md).

For more information on the Global Logger seesion, see [Configuring and Starting the Global Logger Session](configuring-and-starting-the-global-logger-session.md).

> [!Note]  
> ETW supports the AutoLogger on Windows Vista and later. Use the [Global Logger](configuring-and-starting-the-global-logger-session.md) on earlier operating systems.

 

You use the registry to configure the AutoLogger session. Add the following registry key, if it is not already present:

```
HKEY_LOCAL_MACHINE
   \SYSTEM
      \CurrentControlSet
         \Control
            \WMI
               \Autologger
```

Under the **Autologger** key create a key for each AutoLogger session that you want to configure as shown in the following example.

```
HKEY_LOCAL_MACHINE
   \SYSTEM
      \CurrentControlSet
         \Control
            \WMI
               \Autologger
                  \Logger Session A
                  \Logger Session B
                  \Logger Session C
```

For each session, create a key for each provider that you want to enable to the session. Use the provider's GUID as the key.

```
HKEY_LOCAL_MACHINE
   \SYSTEM
      \CurrentControlSet
         \Control
            \WMI
               \Autologger
                  \Logger Session A
                     \{ProviderGuid1}
                     \{ProviderGuid2}
                  \Logger Session B
                  \Logger Session C
```

The following table describes the values that you can define for each AutoLogger session. You must have administrator privileges to specify these registry values. The **Start** and **Guid** value are the only values required to start the AutoLogger session; all other values have default settings that are used if the value is not present in the registry. Typically, you should use the default values. If you specify a value that ETW cannot support, ETW will override the value.




| Value | Type | Description | 
|-------|------|-------------|
| <strong>BufferSize</strong> | <strong>REG_DWORD</strong> | The size of each buffer, in kilobytes. Should be less than one megabyte. ETW uses the size of physical memory to calculate this value.<br /> | 
| <strong>ClockType</strong> | <strong>REG_DWORD</strong> | The timer to use when logging the time stamp for each event.<ul><li>1 = Performance counter value (high resolution)</li><li>2 = System timer</li><li>3 = CPU cycle counter</li></ul>For a description of each clock type, see the <strong>ClientContext</strong> member of <a href="wnode-header.md"><strong>WNODE_HEADER</strong></a>.<br /> The default value is 1 (performance counter value) on Windows Vista and later. Prior to Windows Vista, the default value is 2 (system timer).<br /> | 
| <strong>DisableRealtimePersistence</strong> | <strong>REG_DWORD</strong> | To disable real time persistence, set this value to 1. The default is 0 (enabled) for real time sessions.<br /> If real time persistence is enabled, real-time events that were not delivered by the time the computer was shutdown will be persisted. The events will then be delivered to the consumer the next time the consumer connects to the session. <br /> | 
| <strong>FileCounter</strong> | <strong>REG_DWORD</strong> | Do not set or modify this value. This value is the serial number used to increment the log file name if <strong>FileMax</strong> is specified. If the value is not valid, 1 will be assumed.<br /> | 
| <strong>FileName</strong> | <strong>REG_SZ</strong> | The fully qualified path of the log file. The path to this file must exist. The log file is a sequential log file. The path is limited to 1024 characters.<br /> If <strong>FileName</strong> is not specified, events are written to %SystemRoot%\System32\LogFiles\WMI\&lt;sessionname&gt;.etl. <br /> | 
| <strong>FileMax</strong> | <strong>REG_DWORD</strong> | The maximum number of instances of the log file that ETW creates. If the log file specified in <strong>FileName</strong> exists, ETW appends the <strong>FileCounter</strong> value to the file name. For example, if the default log file name is used, the form is %SystemRoot%\System32\LogFiles\WMI\&lt;sessionname&gt;.etl.NNNN. <br /> The first time the computer is started, the file name is &lt;sessionname&gt;.etl.0001, the second time the file name is &lt;sessionname&gt;.etl.0002, and so on. If <strong>FileMax</strong> is 3, on the fourth restart of the computer, ETW resets the counter to 1 and overwrites &lt;sessionname&gt;.etl.0001, if it exists.<br /> The maximum number of instances of the log file that are supported is 16.<br /> Do not use this feature with the <a href="logging-mode-constants.md">EVENT_TRACE_FILE_MODE_NEWFILE</a> log file mode.<br /> | 
| <strong>FlushTimer</strong> | <strong>REG_DWORD</strong> | How often, in seconds, the trace buffers are forcibly flushed. The minimum flush time is 1 second. This forced flush is in addition to the automatic flush that occurs when a buffer is full and when the trace session stops. <br /> For the case of a real-time logger, a value of zero (the default value) means that the flush time will be set to 1 second. A real-time logger is when <strong>LogFileMode</strong> is set to <strong>EVENT_TRACE_REAL_TIME_MODE</strong>.<br /> The default value is 0. By default, buffers are flushed only when they are full. <br /> | 
| <strong>Guid</strong> | <strong>REG_SZ</strong> | A string that contains a GUID that uniquely identifies the session. This value is required. | 
| <strong>LogFileMode</strong> | <strong>REG_DWORD</strong> | Specify one or more log modes. For possible values, see <a href="logging-mode-constants.md">Logging Mode Constants</a>. The default is <strong>EVENT_TRACE_FILE_MODE_SEQUENTIAL</strong>. Instead of writing to a log file, you can specify either <strong>EVENT_TRACE_BUFFERING_MODE</strong> or <strong>EVENT_TRACE_REAL_TIME_MODE</strong>.<br /> Specifying <strong>EVENT_TRACE_BUFFERING_MODE</strong> avoids the cost of flushing the contents of the session to disk when the file system becomes available. <br /> Note that using <strong>EVENT_TRACE_BUFFERING_MODE</strong> will cause the system to ignore the <strong>MaximumBuffers</strong> value, as the buffer size is instead the product of <strong>MinimumBuffers</strong> and <strong>BufferSize</strong>.<br /> AutoLogger sessions do not support the <strong>EVENT_TRACE_FILE_MODE_NEWFILE</strong> logging mode.<br /> If <strong>EVENT_TRACE_FILE_MODE_APPEND</strong> is specified, <strong>BufferSize</strong> must be explicitly provided and must be the same in both the logger and the file being appended.<br /> | 
| <strong>MaxFileSize</strong> | <strong>REG_DWORD</strong> | The maximum file size of the log file, in megabytes. The session is closed when the maximum size is reached, unless you are in circular log file mode. To specify no limit, set value to 0. The default is 100 MB, if not set. The behavior that occurs when the maximum file size is reached depends on the value of <strong>LogFileMode</strong>.<br /> | 
| <strong>MaximumBuffers</strong> | <strong>REG_DWORD</strong> | The maximum number of buffers to allocate. Typically, this value is the minimum number of buffers plus twenty. ETW uses the buffer size and the size of physical memory to calculate this value. This value must be greater than or equal to the value for <strong>MinimumBuffers</strong>.<br /> | 
| <strong>MinimumBuffers</strong> | <strong>REG_DWORD</strong> | The minimum number of buffers to allocate at startup. The minimum number of buffers that you can specify is two buffers per processor. For example, on a single processor computer, the minimum number of buffers is two.<br /> | 
| <strong>Start</strong> | <strong>REG_DWORD</strong> | To have the AutoLogger session start the next time the computer is restarted, set this value to 1; otherwise, set this value to 0.<br /> | 
| <strong>Status</strong> | <strong>REG_DWORD</strong> | The startup status of the AutoLogger. If the AutoLogger failed to start, the value of this key is the appropriate Win32 error code. If the AutoLogger successfully started, the value of this key is <strong>ERROR_SUCCESS</strong> (0).<br /> | 




 

The following table describes the values that you can define for each provider that you want to enable to your session. You must have administrator privileges to specify these registry values. If you specify a value that ETW cannot support, ETW will override the value.




| Value | Type | Description | 
|-------|------|-------------|
| <strong>Enabled</strong> | <strong>REG_DWORD</strong> | Determines if the provider is enabled. To enable the provider, set this value to 1. To disable the provider, set this value to 0. The default is 0. | 
| <strong>EnableFlags</strong> | <strong>REG_DWORD</strong> | Provider-defined value that specifies the class of events for which the provider generates events. For details, see the <em>EnableFlags</em> parameter of the <a href="/windows/win32/api/evntrace/nf-evntrace-enabletrace"><strong>EnableTrace</strong></a> function. Specify this value name if the provider does not support <strong>MatchAnyKeyword</strong> or <strong>MatchAllKeyword</strong>. | 
| <strong>EnableLevel</strong> | <strong>REG_DWORD</strong> | Provider-defined value that specifies the level of detail included in the event. For example, you can use this value to indicate the severity level of the events (informational, warning, error) that the provider generates. For a list of predefined levels, see the <em>level</em> parameter of the <a href="/windows/win32/api/evntrace/nf-evntrace-enabletraceex"><strong>EnableTraceEx</strong></a> function. | 
| <strong>EnableProperty</strong> | <strong>REG_DWORD</strong> | Use this value to include one or more of the following items in the log file:<ul><li><strong>EVENT_ENABLE_PROPERTY_SID</strong> (0x00000001) = Include in the extended data the security identifier (SID) of the user.</li><li><strong>EVENT_ENABLE_PROPERTY_TS_ID</strong> (0x00000002) = Include in the extended data the terminal session identifier.</li><li><strong>EVENT_ENABLE_PROPERTY_STACK_TRACE</strong> (0x00000004) = Include in the extended data a call stack trace for events written using <a href="/windows/desktop/api/Evntprov/nf-evntprov-eventwrite"><strong>EventWrite</strong></a>.</li><li><strong>EVENT_ENABLE_PROPERTY_IGNORE_KEYWORD_0</strong> (0x00000010) = Filters out all events that do not have a non-zero keyword specified.</li><li><strong>EVENT_ENABLE_PROPERTY_PROVIDER_GROUP</strong> (0x00000020) = Indicates that this call to <a href="/windows/win32/api/evntrace/nf-evntrace-enabletraceex2"><strong>EnableTraceEx2</strong></a> should enable a <a href="provider-traits.md">Provider Group</a> rather than an individual Event Provider.</li><li><strong>EVENT_ENABLE_PROPERTY_PROCESS_START_KEY</strong> (0x00000080) = Include the Process Start Key in the extended data.</li><li><strong>EVENT_ENABLE_PROPERTY_EVENT_KEY</strong> (0x00000100) = Include the Event Key in the extended data.</li><li><strong>EVENT_ENABLE_PROPERTY_EXCLUDE_INPRIVATE</strong> (0x00000200) = Filters out all events that are either marked as an InPrivate event or come from a process that is marked as InPrivate.</li></ul>For more information about these items, see the <strong>EnableProperty</strong> of the <a href="/windows/win32/api/evntrace/ns-evntrace-enable_trace_parameters"><strong>ENABLE_TRACE_PARAMETERS</strong></a> structure.<br /> | 
| <strong>MatchAnyKeyword</strong> | <strong>REG_QWORD</strong> | Bitmask of keywords that determine the category of events that you want the provider to write. The provider writes the event if any of the event's keyword bits match any of the bits set in this mask. To specify that the provider write all events, set this value to zero. For an example, see the Remarks section of the <a href="/windows/win32/api/evntrace/nf-evntrace-enabletraceex"><strong>EnableTraceEx</strong></a> function. | 
| <strong>MatchAllKeyword</strong> | <strong>REG_QWORD</strong> | This bitmask is optional. This mask further restricts the category of events that you want the provider to write. If the event's keyword meets the <em>MatchAnyKeyword</em> condition, the provider will write the event only if all of the bits in this mask exist in the event's keyword. This mask is not used if <em>MatchAnyKeyword</em> is zero. For an example, see the Remarks section of the <a href="/windows/win32/api/evntrace/nf-evntrace-enabletraceex"><strong>EnableTraceEx</strong></a> function. | 




 

After the registry has been modified, the AutoLogger session is started the next time the computer is restarted. The AutoLogger session calls the [**EnableTraceEx**](/windows/win32/api/evntrace/nf-evntrace-enabletraceex) function to enable the providers.

The AutoLogger sessions increase the system boot time and should be used sparingly. Services that want to capture information during the boot process should consider adding controller logic to itself instead of using the AutoLogger session.

To stop an AutoLogger session, call the [**ControlTrace**](/windows/win32/api/evntrace/nf-evntrace-controltracea) function. The session name that you pass to the function is the name of the registry key that you used to define the session in the registry.

On Windows 8.1,Windows Server 2012 R2, and later, event payload , scope, and stack walk filters can be used by the [**EnableTraceEx2**](/windows/win32/api/evntrace/nf-evntrace-enabletraceex2) function and the [**ENABLE\_TRACE\_PARAMETERS**](/windows/win32/api/evntrace/ns-evntrace-enable_trace_parameters) and [**EVENT\_FILTER\_DESCRIPTOR**](/windows/desktop/api/Evntprov/ns-evntprov-event_filter_descriptor) structures to filter on specific conditions in a logger session. For more information on event payload filters, see the [**TdhCreatePayloadFilter**](/windows/desktop/api/Tdh/nf-tdh-tdhcreatepayloadfilter), and [**TdhAggregatePayloadFilters**](/windows/desktop/api/Tdh/nf-tdh-tdhaggregatepayloadfilters) functions and the **ENABLE\_TRACE\_PARAMETERS**, **EVENT\_FILTER\_DESCRIPTOR**, and [**PAYLOAD\_FILTER\_PREDICATE**](/windows/desktop/api/Tdh/ns-tdh-payload_filter_predicate) structures.

For details on starting an event tracing session, see [Configuring and Starting an Event Tracing Session](configuring-and-starting-an-event-tracing-session.md).

For details on starting a private logger session, see [Configuring and Starting a Private Logger Session](configuring-and-starting-a-private-logger-session.md).

For details on starting an NT Kernel Logger session, see [Configuring and Starting the NT Kernel Logger Session](configuring-and-starting-the-nt-kernel-logger-session.md).

## Related topics

<dl> <dt>

[Configuring and Starting a Private Logger Session](configuring-and-starting-a-private-logger-session.md)
</dt> <dt>

[Configuring and Starting a SystemTraceProvider Session](configuring-and-starting-a-systemtraceprovider-session.md)
</dt> <dt>

[Configuring and Starting an Event Tracing Session](configuring-and-starting-an-event-tracing-session.md)
</dt> <dt>

[Configuring and Starting the NT Kernel Logger Session](configuring-and-starting-the-nt-kernel-logger-session.md)
</dt> <dt>

[**EnableTraceEx2**](/windows/win32/api/evntrace/nf-evntrace-enabletraceex2)
</dt> <dt>

[**ENABLE\_TRACE\_PARAMETERS**](/windows/win32/api/evntrace/ns-evntrace-enable_trace_parameters)
</dt> <dt>

[**EVENT\_FILTER\_DESCRIPTOR**](/windows/desktop/api/Evntprov/ns-evntprov-event_filter_descriptor)
</dt> <dt>

[**PAYLOAD\_FILTER\_PREDICATE**](/windows/desktop/api/Tdh/ns-tdh-payload_filter_predicate)
</dt> <dt>

[**TdhAggregatePayloadFilters**](/windows/desktop/api/Tdh/nf-tdh-tdhaggregatepayloadfilters)
</dt> <dt>

[**TdhCreatePayloadFilter**](/windows/desktop/api/Tdh/nf-tdh-tdhcreatepayloadfilter)
</dt> <dt>

[Updating an Event Tracing Session](updating-an-event-tracing-session.md)
</dt> </dl>
