---
description: This topic lists structures that are used with processes, threads, processors, job objects, and user-mode scheduling (UMS).
ms.assetid: dbb50193-4c67-494e-9c46-2ac3106fac9a
title: Process and Thread Structures
ms.topic: article
ms.date: 05/31/2018
---

# Process and Thread Structures

This topic lists structures that are used with processes, threads, processors, job objects, and user-mode scheduling (UMS).

## Process and Thread Structures

The following structures are used with processes and threads:

-   [**APP\_MEMORY\_INFORMATION**](/windows/win32/api/processthreadsapi/ns-processthreadsapi-app_memory_information)
-   [**AR\_STATE**](/windows/win32/api/winuser/ne-winuser-ar_state)
-   [**CACHE\_DESCRIPTOR**](/windows/desktop/api/WinNT/ns-winnt-cache_descriptor)
-   [**IO\_COUNTERS**](/windows/desktop/api/WinNT/ns-winnt-io_counters)
-   [**ORIENTATION\_PREFERENCE**](/windows/desktop/api/WinUser/ne-winuser-orientation_preference)
-   [**PEB**](/windows/desktop/api/Winternl/ns-winternl-peb)
-   [**PEB\_LDR\_DATA**](/windows/desktop/api/Winternl/ns-winternl-peb_ldr_data)
-   [**PROCESS\_INFORMATION**](/windows/win32/api/processthreadsapi/ns-processthreadsapi-process_information)
-   [**PROCESS\_MEMORY\_EXHAUSTION\_INFO**](/windows/win32/api/processthreadsapi/ns-processthreadsapi-process_memory_exhaustion_info)
-   [**PROCESS\_MITIGATION\_ASLR\_POLICY**](/windows/desktop/api/WinNT/ns-winnt-process_mitigation_aslr_policy)
-   [**PROCESS\_MITIGATION\_BINARY\_SIGNATURE\_POLICY**](/windows/desktop/api/WinNT/ns-winnt-process_mitigation_binary_signature_policy)
-   [**PROCESS\_MITIGATION\_CONTROL\_FLOW\_GUARD\_POLICY**](/windows/desktop/api/WinNT/ns-winnt-process_mitigation_control_flow_guard_policy)
-   [**PROCESS\_MITIGATION\_DEP\_POLICY**](/windows/desktop/api/WinNT/ns-winnt-process_mitigation_dep_policy)
-   [**PROCESS\_MITIGATION\_DYNAMIC\_CODE\_POLICY**](/windows/desktop/api/WinNT/ns-winnt-process_mitigation_dynamic_code_policy)
-   [**PROCESS\_MITIGATION\_EXTENSION\_POINT\_DISABLE\_POLICY**](/windows/desktop/api/winnt/ns-winnt-process_mitigation_extension_point_disable_policy)
-   [**PROCESS\_MITIGATION\_FONT\_DISABLE\_POLICY**](/windows/desktop/api/WinNT/ns-winnt-process_mitigation_font_disable_policy)
-   [**PROCESS\_MITIGATION\_IMAGE\_LOAD\_POLICY**](/windows/desktop/api/WinNT/ns-winnt-process_mitigation_image_load_policy)
-   [**PROCESS\_MITIGATION\_STRICT\_HANDLE\_CHECK\_POLICY**](/windows/desktop/api/WinNT/ns-winnt-process_mitigation_strict_handle_check_policy)
-   [**PROCESS\_MITIGATION\_SYSTEM\_CALL\_DISABLE\_POLICY**](/windows/desktop/api/WinNT/ns-winnt-process_mitigation_system_call_disable_policy)
-   [**RTL\_USER\_PROCESS\_PARAMETERS**](/windows/desktop/api/Winternl/ns-winternl-rtl_user_process_parameters)
-   [**STARTUPINFO**](/windows/win32/api/processthreadsapi/ns-processthreadsapi-startupinfoa)
-   [**STARTUPINFOEX**](/windows/desktop/api/WinBase/ns-winbase-startupinfoexa)
-   [**TEB**](/windows/desktop/api/Winternl/ns-winternl-teb)

## Processor Structures

The following structures are used with processors and processor groups:

-   [**CACHE\_RELATIONSHIP**](/windows/desktop/api/WinNT/ns-winnt-cache_relationship)
-   [**GROUP\_AFFINITY**](/windows/desktop/api/WinNT/ns-winnt-group_affinity)
-   [**GROUP\_RELATIONSHIP**](/windows/desktop/api/WinNT/ns-winnt-group_relationship)
-   [**NUMA\_NODE\_RELATIONSHIP**](/windows/desktop/api/WinNT/ns-winnt-numa_node_relationship)
-   [**PROCESSOR\_GROUP\_INFO**](/windows/desktop/api/WinNT/ns-winnt-processor_group_info)
-   [**PROCESSOR\_NUMBER**](/windows/desktop/api/WinNT/ns-winnt-processor_number)
-   [**PROCESSOR\_RELATIONSHIP**](/windows/desktop/api/WinNT/ne-winnt-logical_processor_relationship)
-   [**SYSTEM\_CPU\_SET\_INFORMATION**](/windows/desktop/api/winnt/ns-winnt-system_cpu_set_information)
-   [**SYSTEM\_LOGICAL\_PROCESSOR\_INFORMATION**](/windows/desktop/api/WinNT/ns-winnt-system_logical_processor_information)
-   [**SYSTEM\_LOGICAL\_PROCESSOR\_INFORMATION\_EX**](/windows/desktop/api/WinNT/ns-winnt-system_logical_processor_information_ex)

## Dispatcher Queue Structure

The following structure is used to create a [DispatcherQueueController](/uwp/api/windows.system.dispatcherqueuecontroller).

-   [**DispatcherQueueOptions**](/windows/desktop/api/DispatcherQueue/ns-dispatcherqueue-dispatcherqueueoptions)

## Job Object Structures

The following structures are used with job objects:

-   [**JOBOBJECT\_ASSOCIATE\_COMPLETION\_PORT**](/windows/desktop/api/WinNT/ns-winnt-jobobject_associate_completion_port)
-   [**JOBOBJECT\_BASIC\_ACCOUNTING\_INFORMATION**](/windows/desktop/api/WinNT/ns-winnt-jobobject_basic_accounting_information)
-   [**JOBOBJECT\_BASIC\_AND\_IO\_ACCOUNTING\_INFORMATION**](/windows/desktop/api/WinNT/ns-winnt-jobobject_basic_and_io_accounting_information)
-   [**JOBOBJECT\_BASIC\_LIMIT\_INFORMATION**](/windows/desktop/api/WinNT/ns-winnt-jobobject_basic_limit_information)
-   [**JOBOBJECT\_BASIC\_PROCESS\_ID\_LIST**](/windows/desktop/api/WinNT/ns-winnt-jobobject_basic_process_id_list)
-   [**JOBOBJECT\_BASIC\_UI\_RESTRICTIONS**](/windows/desktop/api/WinNT/ns-winnt-jobobject_basic_ui_restrictions)
-   [**JOBOBJECT\_END\_OF\_JOB\_TIME\_INFORMATION**](/windows/desktop/api/WinNT/ns-winnt-jobobject_end_of_job_time_information)
-   [**JOBOBJECT\_EXTENDED\_LIMIT\_INFORMATION**](/windows/desktop/api/WinNT/ns-winnt-jobobject_extended_limit_information)
-   [**JOBOBJECT\_SECURITY\_LIMIT\_INFORMATION**](/windows/desktop/api/WinNT/ns-winnt-jobobject_security_limit_information)

## User-Mode Scheduling Structures

The following structures are used with UMS:

-   [**UMS\_CREATE\_THREAD\_ATTRIBUTES**](/windows/desktop/api/WinNT/ns-winnt-ums_create_thread_attributes)
-   [**UMS\_SCHEDULER\_STARTUP\_INFO**](/windows/desktop/api/WinBase/ns-winbase-ums_scheduler_startup_info)
-   [**UMS\_SYSTEM\_THREAD\_INFORMATION**](/windows/desktop/api/WinBase/ns-winbase-ums_system_thread_information)

 

 
