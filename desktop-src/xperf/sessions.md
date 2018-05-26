---
title: Sessions
description: Sessions
ms.assetid: 692d51d8-d3ea-46fe-bb85-4810cab765aa
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Sessions

Windows Performance Analyzer extends ETW logging session to capture trace data. An ETW logging session is a collection of in-memory buffers, typically non-paged, that is managed by the kernel and accepts events via the ETW Provider API. At any time an in-use buffer is assigned to each processor. ETW event generation and buffering is lock free to allow events to be logged from any type of code. Every time EventWrite() is called, space is reserved in the in-use buffer allocated to the processor on which the calling thread is running; then the event header and user data are copied into that space. When the buffer becomes full, it is flushed to the logging session's log file and/or the real time streaming consumer, and a free buffer is assigned to that processor. If the logging throughput exceeds the ability of the flusher to free up buffers - for instance, because the disk write throughput is lower than the incoming event throughput - at some point all available buffer space in the logging session might become unavailable, determining EventWrite to fail with ERROR\_NOT\_ENOUGH\_MEMORY and lose the event data. In such cases, the EventsLost property of the logging session is incremented, so that the data loss is surfaced to consumers. Logging sessions are very flexible and can be configured with a wide range of options. Properly configured logging sessions will prevent the loss of data. This can be a process of trial and error. These are the various parameters that allow for greater control.

<dl> <dt>

<span id="Sequential_vs._Circular_vs._Buffering"></span><span id="sequential_vs._circular_vs._buffering"></span><span id="SEQUENTIAL_VS._CIRCULAR_VS._BUFFERING"></span>Sequential vs. Circular vs. Buffering
</dt> <dd>

A logging session typically has a 1-1 relationship with a logging file. These files can be either circular, think black-box, or sequential, think constantly expanding array. Buffering mode is the exception to this rule, which most of the time has not relation with a file. Buffering mode is an in-memory circular session, the content of which can be snapshot to a trace file in on request; the content of the in-memory buffer space is not flushed on snapshot. Buffering mode sessions and circular log files are great for being left on all the time, being especially useful if you don't know when the behavior of interest will occur. Choose buffering mode whenever the required circular buffer space is small enough to be kept in memory and circular log files for scenarios requiring more storage space before a wrap occurs. Sequential log files are best used when the scenario is controlled, for instance for regression testing and when the occurrence of the behavior of interest is easier to predict.

</dd> <dt>

<span id="Number_of_Buffers"></span><span id="number_of_buffers"></span><span id="NUMBER_OF_BUFFERS"></span>Number of Buffers
</dt> <dd>

The number of buffers is a key determinant of capacity in a logging session. If too many buffers are configured memory (usually non-paged pool) is wasted. If too few buffers are configured large numbers of events might be lost. In order to help keep the right balance two knobs are provided to adjust the number of buffers. Each logging session has a minimum and a maximum number of buffers associated with it. The minimum number of buffers represents the smallest possible footprint of the session. It is best to get this number right, because events may be lost as additional buffers are added.

</dd> <dt>

<span id="Buffer_Size"></span><span id="buffer_size"></span><span id="BUFFER_SIZE"></span>Buffer Size
</dt> <dd>

Almost as important as the number of Buffers, along with which it controls memory usage. There are two more aspects controlled or influenced by buffer size. The former regards disk I/O efficiency. Very small buffer sizes could reduce the I/O write efficiency. With current disks, it is recommended that buffer size is kept at minimum 64k or 128kB to ensure good write performance and thus reduced disk overhead and probability of lost events. Another aspect controlled by buffer size is related to event size. The size of your buffers determines the maximum size of any event that can be traced. It's pretty rare to have a single event be so large that it can't fit in a buffer. But should this value be artificially low or should an event be unusually large it will never get traced. As a result this is an important knob to be aware of. Currently, ETW limits the largest event size to a little under 64kB. If the buffer size is at or above 128kB no events will be lost because of buffer size; 64kB buffers will lose only events tightly approaching the valid event size limit close to 64kB, so most of the time 64kB buffers are ok as well.

</dd> <dt>

<span id="Clock_Type"></span><span id="clock_type"></span><span id="CLOCK_TYPE"></span>Clock Type
</dt> <dd>

Each logging session can use one of three different clocks to provide Event Timestamps. The primary difference between the three is in resolution and expense to retrieve.The three types are Cycle (CPU Cycle Resolution), PerfCounter (Performance Frequency resolution, which could be 100 nanosecond or better), SystemTime (10 millisecond resolution). If you intend to merge multiple logs the same clock must be used for all logs. Currently, PerfCounter is the default clock type for Windows Vista and later operating systems; SystemTime was the default in pre-Vista operating systems. We strongly recommend all performance traces are taken with PerfCounter.

</dd> <dt>

<span id="Stack_traces"></span><span id="stack_traces"></span><span id="STACK_TRACES"></span>Stack traces
</dt> <dd>

Starting with Windows Vista, stack walking can be enabled for certain kernel events. When stackwalking is enabled for a trigger kernel event, for each trigger event logged one or more additional events are logged containing fragments of the code stack from where the event was fired. When combined with symbols on the processing side this extends analysis using system events to correlate back into the code context that triggered the corresponding event, from up in kernel mode to deep inside applications. This is a very powerful tool.

</dd> <dt>

<span id="Logger_Name_Log_File_Name"></span><span id="logger_name_log_file_name"></span><span id="LOGGER_NAME_LOG_FILE_NAME"></span>Logger Name/Log File Name
</dt> <dd>

Both of these strings are configurable on creation of a logger. The only thing that really needs to be said about this is that the strings must be unique to the system. There can only be one logging session with a given name on a system. The logging session also requires exclusive write access to the log file and that cannot be shared between loggers, so it's best for that to also be unique. The non-"NT Kernel Provider" events can be configured in one or more sessions based on quality of service requirements and all "NT Kernel Provider" events must be in their own session which must be named "NT Kernel Logger". If you want all of your events in one file that can be done after the fact; see the section on merging in the Consumer bit below.

</dd> <dt>

<span id="Special_Logger_Types"></span><span id="special_logger_types"></span><span id="SPECIAL_LOGGER_TYPES"></span>Special Logger Types
</dt> <dd>

There are 2 special kinds of logger. The first is the Process Private logger; this logger type can only be used to log events coming from within a given process. This is primarily useful because it is the only way to collect heap or critical section tracing. The other special logger is the "NT Kernel Logger." This is a singleton logger that is the only logger that is allowed to collect certain kernel events. No other logger may use that name.

</dd> <dt>

<span id="Providers"></span><span id="providers"></span><span id="PROVIDERS"></span>Providers
</dt> <dd>

Logging sessions collect a defined set of providers. This is probably the most important item that is configured on a per-session basis. A provider is only turned on based on the session name for which it is enabled. Most providers can have a many to many relationship with sessions. Some providers can only log to special providers, for example "NT Kernel Provider" events to the kernel logger, or heap events to process private loggers. Most people only use a fraction of the providers available on the system. Over time, you will develop your own "core set."

</dd> </dl>

 

 




