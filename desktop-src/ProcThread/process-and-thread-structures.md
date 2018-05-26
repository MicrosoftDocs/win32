---
Description: This topic lists structures that are used with processes, threads, processors, job objects, and user-mode scheduling (UMS).
ms.assetid: dbb50193-4c67-494e-9c46-2ac3106fac9a
title: Process and Thread Structures
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Process and Thread Structures

This topic lists structures that are used with processes, threads, processors, job objects, and user-mode scheduling (UMS).

## Process and Thread Structures

The following structures are used with processes and threads:

-   [**APP\_MEMORY\_INFORMATION**](app-memory-information.md)
-   [**AR\_STATE**](/windows/win32/WinUser/ne-winuser-tagar_state?branch=master)
-   [**CACHE\_DESCRIPTOR**](/windows/win32/WinNT/ns-winnt-_cache_descriptor?branch=master)
-   [**IO\_COUNTERS**](/windows/win32/WinNT/ns-winnt-_io_counters?branch=master)
-   [**ORIENTATION\_PREFERENCE**](/windows/win32/WinUser/ne-winuser-orientation_preference?branch=master)
-   [**PEB**](/windows/win32/Winternl/ns-winternl-_peb?branch=master)
-   [**PEB\_LDR\_DATA**](/windows/win32/Winternl/ns-winternl-_peb_ldr_data?branch=master)
-   [**PROCESS\_INFORMATION**](/windows/win32/WinBase/ns-processthreadsapi-_process_information?branch=master)
-   [**PROCESS\_MEMORY\_EXHAUSTION\_INFO**](process-memory-exhaustion-info.md)
-   [**PROCESS\_MITIGATION\_ASLR\_POLICY**](/windows/win32/WinNT/ns-winnt-_process_mitigation_aslr_policy?branch=master)
-   [**PROCESS\_MITIGATION\_BINARY\_SIGNATURE\_POLICY**](/windows/win32/WinNT/ns-winnt-_process_mitigation_binary_signature_policy?branch=master)
-   [**PROCESS\_MITIGATION\_CONTROL\_FLOW\_GUARD\_POLICY**](/windows/win32/WinNT/ns-winnt-_process_mitigation_control_flow_guard_policy?branch=master)
-   [**PROCESS\_MITIGATION\_DEP\_POLICY**](/windows/win32/WinNT/ns-winnt-_process_mitigation_dep_policy?branch=master)
-   [**PROCESS\_MITIGATION\_DYNAMIC\_CODE\_POLICY**](/windows/win32/WinNT/ns-winnt-_process_mitigation_dynamic_code_policy?branch=master)
-   [**PROCESS\_MITIGATION\_EXTENSION\_POINT\_DISABLE\_POLICY**](/windows/win32/winnt/ns-winnt-_process_mitigation_extension_point_disable_policy?branch=master)
-   [**PROCESS\_MITIGATION\_FONT\_DISABLE\_POLICY**](/windows/win32/WinNT/ns-winnt-_process_mitigation_font_disable_policy?branch=master)
-   [**PROCESS\_MITIGATION\_IMAGE\_LOAD\_POLICY**](/windows/win32/WinNT/ns-winnt-_process_mitigation_image_load_policy?branch=master)
-   [**PROCESS\_MITIGATION\_STRICT\_HANDLE\_CHECK\_POLICY**](/windows/win32/WinNT/ns-winnt-_process_mitigation_strict_handle_check_policy?branch=master)
-   [**PROCESS\_MITIGATION\_SYSTEM\_CALL\_DISABLE\_POLICY**](/windows/win32/WinNT/ns-winnt-_process_mitigation_system_call_disable_policy?branch=master)
-   [**RTL\_USER\_PROCESS\_PARAMETERS**](/windows/win32/Winternl/ns-winternl-_rtl_user_process_parameters?branch=master)
-   [**STARTUPINFO**](/windows/win32/WinBase/ns-processthreadsapi-_startupinfoa?branch=master)
-   [**STARTUPINFOEX**](/windows/win32/WinBase/ns-winbase-_startupinfoexa?branch=master)
-   [**TEB**](/windows/win32/Winternl/ns-winternl-_teb?branch=master)

## Processor Structures

The following structures are used with processors and processor groups:

-   [**CACHE\_RELATIONSHIP**](/windows/win32/WinNT/ns-winnt-_cache_relationship?branch=master)
-   [**GROUP\_AFFINITY**](/windows/win32/WinNT/ns-winnt-_group_affinity?branch=master)
-   [**GROUP\_RELATIONSHIP**](/windows/win32/WinNT/ns-winnt-_group_relationship?branch=master)
-   [**NUMA\_NODE\_RELATIONSHIP**](/windows/win32/WinNT/ns-winnt-_numa_node_relationship?branch=master)
-   [**PROCESSOR\_GROUP\_INFO**](/windows/win32/WinNT/ns-winnt-_processor_group_info?branch=master)
-   [**PROCESSOR\_NUMBER**](/windows/win32/WinNT/ns-winnt-_processor_number?branch=master)
-   [**PROCESSOR\_RELATIONSHIP**](/windows/win32/WinNT/ne-winnt-_logical_processor_relationship?branch=master)
-   [**SYSTEM\_CPU\_SET\_INFORMATION**](/windows/win32/winnt/ns-winnt-_system_cpu_set_information?branch=master)
-   [**SYSTEM\_LOGICAL\_PROCESSOR\_INFORMATION**](/windows/win32/WinNT/ns-winnt-_system_logical_processor_information?branch=master)
-   [**SYSTEM\_LOGICAL\_PROCESSOR\_INFORMATION\_EX**](/windows/win32/WinNT/ns-winnt-_system_logical_processor_information_ex?branch=master)

## Dispatcher Queue Structure

The following structure is used to create a [DispatcherQueueController](https://docs.microsoft.com/uwp/api/windows.system.dispatcherqueuecontroller).

-   [**DispatcherQueueOptions**](/windows/win32/DispatcherQueue/ns-dispatcherqueue-dispatcherqueueoptions?branch=master)

## Job Object Structures

The following structures are used with job objects:

-   [**JOBOBJECT\_ASSOCIATE\_COMPLETION\_PORT**](/windows/win32/WinNT/ns-winnt-_jobobject_associate_completion_port?branch=master)
-   [**JOBOBJECT\_BASIC\_ACCOUNTING\_INFORMATION**](/windows/win32/WinNT/ns-winnt-_jobobject_basic_accounting_information?branch=master)
-   [**JOBOBJECT\_BASIC\_AND\_IO\_ACCOUNTING\_INFORMATION**](/windows/win32/WinNT/ns-winnt-_jobobject_basic_and_io_accounting_information?branch=master)
-   [**JOBOBJECT\_BASIC\_LIMIT\_INFORMATION**](/windows/win32/WinNT/ns-winnt-_jobobject_basic_limit_information?branch=master)
-   [**JOBOBJECT\_BASIC\_PROCESS\_ID\_LIST**](/windows/win32/WinNT/ns-winnt-_jobobject_basic_process_id_list?branch=master)
-   [**JOBOBJECT\_BASIC\_UI\_RESTRICTIONS**](/windows/win32/WinNT/ns-winnt-_jobobject_basic_ui_restrictions?branch=master)
-   [**JOBOBJECT\_END\_OF\_JOB\_TIME\_INFORMATION**](/windows/win32/WinNT/ns-winnt-_jobobject_end_of_job_time_information?branch=master)
-   [**JOBOBJECT\_EXTENDED\_LIMIT\_INFORMATION**](/windows/win32/WinNT/ns-winnt-_jobobject_extended_limit_information?branch=master)
-   [**JOBOBJECT\_SECURITY\_LIMIT\_INFORMATION**](/windows/win32/WinNT/ns-winnt-_jobobject_security_limit_information?branch=master)

## User-Mode Scheduling Structures

The following structures are used with UMS:

-   [**UMS\_CREATE\_THREAD\_ATTRIBUTES**](/windows/win32/WinNT/ns-winnt-_ums_create_thread_attributes?branch=master)
-   [**UMS\_SCHEDULER\_STARTUP\_INFO**](/windows/win32/WinBase/ns-winbase-_ums_scheduler_startup_info?branch=master)
-   [**UMS\_SYSTEM\_THREAD\_INFORMATION**](/windows/win32/WinBase/ns-winbase-_ums_system_thread_information?branch=master)

 

 



