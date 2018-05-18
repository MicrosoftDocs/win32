---
Description: 'Common Log File System (CLFS) uses the following abstractions to implement logging:'
ms.assetid: 'a7099979-346c-434d-8af1-6bf1d5a0512f'
title: Log Types
---

# Log Types

Common Log File System (CLFS) uses the following abstractions to implement logging:

-   A *record* is a unit of data that a client appends. Records in the active region of a log are never overwritten. Records cannot be updated or overwritten.
-   A *log stream* is a unique sequence of client records. A dedicated log has only one, unnamed, stream. A multiplexed log has one or more named streams.
-   A *physical log* is a physical set of files and attributes that store one or many log streams. These files are managed through a master file with a .blf file name extension, one for each physical log. There may be one or more additional application-specific files created by CLFS and referenced through the .blf file.
-   A *marshaling area* is a buffer that a client creates to gather log records for a log stream.

You can specify that a log hold only one stream or multiple streams. For one stream, CLFS optimizes access patterns for a dedicated log. For multiple streams, CLFS optimizes access patterns for a multiplexed log.

## Dedicated and Multiplexed Logs

A log is *dedicated* if it stores only one log stream, or *multiplexed* if it stores one or more log streams. However, after a log is created it cannot be converted from one type to the other.

A *multiplexed* log is a physical log that is shared by multiple streams. A multiplex log represents a contractual agreement between two applications or subsystems that share the same log. Each stream in a multiplexed log appears to its client owner as if it were stored in a dedicated log.

![multiplexed log streams](images/logstream-mux.png)

At any one time, only one marshaling area per stream should write to the log. If you have more than one entity writing to a stream at the same time, the log can be corrupted just like a file can be corrupted.

> \[!Important\]  
> Security is on a per-log basis. All log streams have the same security as the physical log.

 

The primary advantage of using a multiplexed log is that system I/O costs are shared across multiple streams so system performance may be better than if several dedicated logs are used on a single disk. Records and log blocks in multiplexed logs are usually written to the same disk cylinder, which minimizes seeks and reduces I/O latency.

 

 



