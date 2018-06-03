---
title: Process Snapshotting Structures
description: The Process Snapshotting API defines the following structures.
ms.assetid: FAF68378-CA3B-41CC-9181-4B479283B8FA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Process Snapshotting Structures

The Process Snapshotting API defines the following structures.



| Structure                                                                     | Description                                                                                                                                                                        |
|-------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PSS\_ALLOCATOR**](/previous-versions/windows/desktop/api/processsnapshot/ns-processsnapshot-pss_allocator)                                       | Specifies custom functions which the Process Snapshotting functions use to allocate and free the internal walk marker structures.<br/>                                       |
| [**PSS\_AUXILIARY\_PAGE\_ENTRY**](/previous-versions/windows/desktop/api/processsnapshot/ns-processsnapshot-pss_auxiliary_page_entry)               | Holds auxiliary page entry information returned by [**PssWalkSnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psswalksnapshot).<br/>                                                                          |
| [**PSS\_AUXILIARY\_PAGES\_INFORMATION**](/previous-versions/windows/desktop/api/processsnapshot/ns-processsnapshot-pss_auxiliary_pages_information) | Holds auxiliary page entry information returned by [**PssQuerySnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-pssquerysnapshot).<br/>                                                                        |
| [**PSS\_HANDLE\_ENTRY**](/previous-versions/windows/desktop/api/processsnapshot/ns-processsnapshot-pss_handle_entry)                                | Holds information about a handle returned by [**PssWalkSnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psswalksnapshot).<br/>                                                                                |
| [**PSS\_HANDLE\_INFORMATION**](/previous-versions/windows/desktop/api/processsnapshot/ns-processsnapshot-pss_handle_information)                    | Holds handle information returned by [**PssQuerySnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-pssquerysnapshot).<br/>                                                                                      |
| [**PSS\_HANDLE\_TRACE\_INFORMATION**](/previous-versions/windows/desktop/api/processsnapshot/ns-processsnapshot-pss_handle_trace_information)       | Holds handle trace information returned by [**PssQuerySnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-pssquerysnapshot).<br/>                                                                                |
| [**PSS\_PERFORMANCE\_COUNTERS**](/previous-versions/windows/desktop/api/processsnapshot/ns-processsnapshot-pss_performance_counters)                | Holds performance counters returned by [**PssQuerySnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-pssquerysnapshot).<br/>                                                                                    |
| [**PSS\_PROCESS\_INFORMATION**](/previous-versions/windows/desktop/api/processsnapshot/ns-processsnapshot-pss_process_information)                  | Holds process information returned by [**PssQuerySnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-pssquerysnapshot).<br/>                                                                                     |
| [**PSS\_THREAD\_ENTRY**](/previous-versions/windows/desktop/api/processsnapshot/ns-processsnapshot-pss_thread_entry)                                | Holds thread information returned by [**PssWalkSnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psswalksnapshot)<br/>                                                                                         |
| [**PSS\_THREAD\_INFORMATION**](/previous-versions/windows/desktop/api/processsnapshot/ns-processsnapshot-pss_thread_information)                    | Holds thread information returned by [**PssQuerySnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-pssquerysnapshot).<br/>                                                                                      |
| [**PSS\_VA\_CLONE\_INFORMATION**](/previous-versions/windows/desktop/api/processsnapshot/ns-processsnapshot-pss_va_clone_information)               | Holds virtual address (VA) clone information returned by [**PssQuerySnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-pssquerysnapshot).<br/>                                                                  |
| [**PSS\_VA\_SPACE\_ENTRY**](/previous-versions/windows/desktop/api/processsnapshot/ns-processsnapshot-pss_va_space_entry)                           | Holds the [**MEMORY\_BASIC\_INFORMATION**](https://msdn.microsoft.com/library/windows/desktop/aa366775) returned by [**PssWalkSnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psswalksnapshot) for a virtual address (VA) region.<br/> |
| [**PSS\_VA\_SPACE\_INFORMATION**](/previous-versions/windows/desktop/api/processsnapshot/ns-processsnapshot-pss_va_space_information)               | Holds virtual address (VA) space information returned by [**PssQuerySnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-pssquerysnapshot).<br/>                                                                  |



 

 

 





