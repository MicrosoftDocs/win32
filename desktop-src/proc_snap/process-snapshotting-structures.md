---
title: Process Snapshotting Structures
description: The Process Snapshotting API defines the following structures.
ms.assetid: 'FAF68378-CA3B-41CC-9181-4B479283B8FA'
---

# Process Snapshotting Structures

The Process Snapshotting API defines the following structures.



| Structure                                                                     | Description                                                                                                                                                                        |
|-------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PSS\_ALLOCATOR**](pss-allocator.md)                                       | Specifies custom functions which the Process Snapshotting functions use to allocate and free the internal walk marker structures.<br/>                                       |
| [**PSS\_AUXILIARY\_PAGE\_ENTRY**](pss-auxiliary-page-entry.md)               | Holds auxiliary page entry information returned by [**PssWalkSnapshot**](psswalksnapshot.md).<br/>                                                                          |
| [**PSS\_AUXILIARY\_PAGES\_INFORMATION**](pss-auxiliary-pages-information.md) | Holds auxiliary page entry information returned by [**PssQuerySnapshot**](pssquerysnapshot.md).<br/>                                                                        |
| [**PSS\_HANDLE\_ENTRY**](pss-handle-entry.md)                                | Holds information about a handle returned by [**PssWalkSnapshot**](psswalksnapshot.md).<br/>                                                                                |
| [**PSS\_HANDLE\_INFORMATION**](pss-handle-information.md)                    | Holds handle information returned by [**PssQuerySnapshot**](pssquerysnapshot.md).<br/>                                                                                      |
| [**PSS\_HANDLE\_TRACE\_INFORMATION**](pss-handle-trace-information.md)       | Holds handle trace information returned by [**PssQuerySnapshot**](pssquerysnapshot.md).<br/>                                                                                |
| [**PSS\_PERFORMANCE\_COUNTERS**](pss-performance-counters.md)                | Holds performance counters returned by [**PssQuerySnapshot**](pssquerysnapshot.md).<br/>                                                                                    |
| [**PSS\_PROCESS\_INFORMATION**](pss-process-information.md)                  | Holds process information returned by [**PssQuerySnapshot**](pssquerysnapshot.md).<br/>                                                                                     |
| [**PSS\_THREAD\_ENTRY**](pss-thread-entry.md)                                | Holds thread information returned by [**PssWalkSnapshot**](psswalksnapshot.md)<br/>                                                                                         |
| [**PSS\_THREAD\_INFORMATION**](pss-thread-information.md)                    | Holds thread information returned by [**PssQuerySnapshot**](pssquerysnapshot.md).<br/>                                                                                      |
| [**PSS\_VA\_CLONE\_INFORMATION**](pss-va-clone-information.md)               | Holds virtual address (VA) clone information returned by [**PssQuerySnapshot**](pssquerysnapshot.md).<br/>                                                                  |
| [**PSS\_VA\_SPACE\_ENTRY**](pss-va-space-entry.md)                           | Holds the [**MEMORY\_BASIC\_INFORMATION**](https://msdn.microsoft.com/library/windows/desktop/aa366775) returned by [**PssWalkSnapshot**](psswalksnapshot.md) for a virtual address (VA) region.<br/> |
| [**PSS\_VA\_SPACE\_INFORMATION**](pss-va-space-information.md)               | Holds virtual address (VA) space information returned by [**PssQuerySnapshot**](pssquerysnapshot.md).<br/>                                                                  |



 

 

 





