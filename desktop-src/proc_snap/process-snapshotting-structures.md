---
title: Process Snapshotting Structures
description: The Process Snapshotting API defines the following structures.
ms.assetid: FAF68378-CA3B-41CC-9181-4B479283B8FA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Process Snapshotting Structures

The Process Snapshotting API defines the following structures.



| Structure                                                                     | Description                                                                                                                                                                        |
|-------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**PSS\_ALLOCATOR**](/windows/previous-versions/processsnapshot/ns-processsnapshot-pss_allocator?branch=master)                                       | Specifies custom functions which the Process Snapshotting functions use to allocate and free the internal walk marker structures.<br/>                                       |
| [**PSS\_AUXILIARY\_PAGE\_ENTRY**](/windows/previous-versions/processsnapshot/ns-processsnapshot-pss_auxiliary_page_entry?branch=master)               | Holds auxiliary page entry information returned by [**PssWalkSnapshot**](/windows/previous-versions/processsnapshot/nf-processsnapshot-psswalksnapshot?branch=master).<br/>                                                                          |
| [**PSS\_AUXILIARY\_PAGES\_INFORMATION**](/windows/previous-versions/processsnapshot/ns-processsnapshot-pss_auxiliary_pages_information?branch=master) | Holds auxiliary page entry information returned by [**PssQuerySnapshot**](/windows/previous-versions/processsnapshot/nf-processsnapshot-pssquerysnapshot?branch=master).<br/>                                                                        |
| [**PSS\_HANDLE\_ENTRY**](/windows/previous-versions/processsnapshot/ns-processsnapshot-pss_handle_entry?branch=master)                                | Holds information about a handle returned by [**PssWalkSnapshot**](/windows/previous-versions/processsnapshot/nf-processsnapshot-psswalksnapshot?branch=master).<br/>                                                                                |
| [**PSS\_HANDLE\_INFORMATION**](/windows/previous-versions/processsnapshot/ns-processsnapshot-pss_handle_information?branch=master)                    | Holds handle information returned by [**PssQuerySnapshot**](/windows/previous-versions/processsnapshot/nf-processsnapshot-pssquerysnapshot?branch=master).<br/>                                                                                      |
| [**PSS\_HANDLE\_TRACE\_INFORMATION**](/windows/previous-versions/processsnapshot/ns-processsnapshot-pss_handle_trace_information?branch=master)       | Holds handle trace information returned by [**PssQuerySnapshot**](/windows/previous-versions/processsnapshot/nf-processsnapshot-pssquerysnapshot?branch=master).<br/>                                                                                |
| [**PSS\_PERFORMANCE\_COUNTERS**](/windows/previous-versions/processsnapshot/ns-processsnapshot-pss_performance_counters?branch=master)                | Holds performance counters returned by [**PssQuerySnapshot**](/windows/previous-versions/processsnapshot/nf-processsnapshot-pssquerysnapshot?branch=master).<br/>                                                                                    |
| [**PSS\_PROCESS\_INFORMATION**](/windows/previous-versions/processsnapshot/ns-processsnapshot-pss_process_information?branch=master)                  | Holds process information returned by [**PssQuerySnapshot**](/windows/previous-versions/processsnapshot/nf-processsnapshot-pssquerysnapshot?branch=master).<br/>                                                                                     |
| [**PSS\_THREAD\_ENTRY**](/windows/previous-versions/processsnapshot/ns-processsnapshot-pss_thread_entry?branch=master)                                | Holds thread information returned by [**PssWalkSnapshot**](/windows/previous-versions/processsnapshot/nf-processsnapshot-psswalksnapshot?branch=master)<br/>                                                                                         |
| [**PSS\_THREAD\_INFORMATION**](/windows/previous-versions/processsnapshot/ns-processsnapshot-pss_thread_information?branch=master)                    | Holds thread information returned by [**PssQuerySnapshot**](/windows/previous-versions/processsnapshot/nf-processsnapshot-pssquerysnapshot?branch=master).<br/>                                                                                      |
| [**PSS\_VA\_CLONE\_INFORMATION**](/windows/previous-versions/processsnapshot/ns-processsnapshot-pss_va_clone_information?branch=master)               | Holds virtual address (VA) clone information returned by [**PssQuerySnapshot**](/windows/previous-versions/processsnapshot/nf-processsnapshot-pssquerysnapshot?branch=master).<br/>                                                                  |
| [**PSS\_VA\_SPACE\_ENTRY**](/windows/previous-versions/processsnapshot/ns-processsnapshot-pss_va_space_entry?branch=master)                           | Holds the [**MEMORY\_BASIC\_INFORMATION**](https://msdn.microsoft.com/library/windows/desktop/aa366775) returned by [**PssWalkSnapshot**](/windows/previous-versions/processsnapshot/nf-processsnapshot-psswalksnapshot?branch=master) for a virtual address (VA) region.<br/> |
| [**PSS\_VA\_SPACE\_INFORMATION**](/windows/previous-versions/processsnapshot/ns-processsnapshot-pss_va_space_information?branch=master)               | Holds virtual address (VA) space information returned by [**PssQuerySnapshot**](/windows/previous-versions/processsnapshot/nf-processsnapshot-pssquerysnapshot?branch=master).<br/>                                                                  |



 

 

 





