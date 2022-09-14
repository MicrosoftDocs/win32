---
title: System Providers
description: Enable System Trace Provider's events with EnableTraceEx2.
ms.topic: article
ms.date: 06/02/2021
---

# System Providers
 
Beginning in Windows 10 SDK build 20348, the System Trace Provider's events can be enabled in the same way that other ETW providers are, with [EnableTraceEx2](/windows/win32/api/evntrace/nf-evntrace-enabletraceex2).  The different flags and [group masks](/windows/win32/api/evntrace/ns-evntrace-event_trace_properties) associated with the System Trace Provider have been mapped to new trace providers, called System Providers, and matching keywords.  
 
Like enabling the System Trace Provider directly, the System Providers can only be enabled by a session with the [EVENT_TRACE_SYSTEM_LOGGER_MODE](./logging-mode-constants.md) set.

## System Provider reference

* [System ALPC Provider](#system-alpc-provider)
* [System Config Provider](#system-config-provider)
* [System CPU Provider](#system-cpu-provider)
* [System Hypervisor Provider](#system-hypervisor-provider)
* [System Interrupt Provider](#system-interrupt-provider)
* [System IO Provider](#system-io-provider)
* [System IO Filter Provider](#system-io-filter-provider)
* [System Lock Provider](#system-lock-provider)
* [System Memory Provider](#system-memory-provider)
* [System Object Provider](#system-object-provider)
* [System Power Provider](#system-power-provider)
* [System Process Provider](#system-process-provider)
* [System Profile Provider](#system-profile-provider)
* [System Registry Provider](#system-registry-provider)
* [System Scheduler Provider](#system-scheduler-provider)
* [System Syscall Provider](#system-syscall-provider)
* [System Timer Provider](#system-timer-provider)
 
### System ALPC Provider

Provides events related to the ALPC system.

GUID: SystemAlpcProviderGuid {fcb9baaf-e529-4980-92e9-ced1a6aadfdf}

| Keyword | Corresponding Legacy Flags and Groups |
| ------- | ------------------------------------- |
| SYSTEM_ALPC_KW_GENERAL | PERF_ALPC, EVENT_TRACE_FLAG_ALPC |
 
### System Config Provider 

Provides system configuration events.

GUID: SystemConfigProviderGuid {fef3a8b6-318d-4b67-a96a-3b0f6b8f18fe}

| Keyword | Corresponding Legacy Flags and Groups |
| ------- | ------------------------------------- |
| SYSTEM_CONFIG_KW_SYSTEM | PERF_SYSCFG_SYSTEM |
| SYSTEM_CONFIG_KW_GRAPHICS | PERF_SYSCFG_GRAPHICS |
| SYSTEM_CONFIG_KW_STORAGE | PERF_SYSCFG_STORAGE |
| SYSTEM_CONFIG_KW_NETWORK | PERF_SYSCFG_NETWORK |
| SYSTEM_CONFIG_KW_SERVICES | PERF_SYSCFG_SERVICES |
| SYSTEM_CONFIG_KW_PNP | PERF_SYSCFG_PNP |
| SYSTEM_CONFIG_KW_OPTICAL | PERF_SYSCFG_OPTICAL |
 
### System CPU Provider 

Provides events related to the CPU.

GUID: SystemCpuProviderGuid {c6c5265f-eae8-4650-aae4-9d48603d8510}

| Keyword | Corresponding Legacy Flags and Groups |
| ------- | ------------------------------------- |
| SYSTEM_CPU_KW_CONFIG | PERF_CPU_CONFIG |
| SYSTEM_CPU_KW_CACHE_FLUSH | PERF_CACHE_FLUSH |
| SYSTEM_CPU_KW_SPEC_CONTROL | PERF_SPEC_CONTROL |
 
### System Hypervisor Provider 

Provides events relating to the hypervisor.

GUID: SystemHypervisorProviderGuid {bafa072a-918a-4bed-b622-bc152097098f}

| Keyword | Corresponding Legacy Flags and Groups |
| ------- | ------------------------------------- |
| SYSTEM_HYPERVISOR_KW_PROFILE | PERF_HV_PROFILE |
| SYSTEM_HYPERVISOR_KW_CALLOUTS | PERF_HV_CALLOUTS |
| SYSTEM_HYPERVISOR_KW_VTL_CHANGE | PERF_VTL_CHANGE |
 
### System Interrupt Provider 

Provides events relating to DPCs and interrupts.

GUID: SystemInterruptProviderGuid {d4bbee17-b545-4888-858b-744169015b25}

| Keyword | Corresponding Legacy Flags and Groups |
| ------- | ------------------------------------- |
| SYSTEM_INTERRUPT_KW_GENERAL | PERF_INTERRUPT, EVENT_TRACE_FLAG_INTERRUPT |
| SYSTEM_INTERRUPT_KW_CLOCK_INTERRUPT | PERF_CLOCK_INTERRUPT |
| SYSTEM_INTERRUPT_KW_DPC | PERF_DPC, EVENT_TRACE_FLAG_DPC |
| SYSTEM_INTERRUPT_KW_DPC_QUEUE | PERF_DPC_QUEUE |
| SYSTEM_INTERRUPT_KW_WDF_DPC | PERF_WDF_DPC |
| SYSTEM_INTERRUPT_KW_WDF_INTERRUPT | PERF_WDF_INTERRUPT |
| SYSTEM_INTERRUPT_KW_IPI | PERF_IPI |
 
 
### System IO Provider 

Provides events relating to multiple kinds of IO including disk, cache, and network.

GUID: SystemIoProviderGuid {3d5c43e3-0f1c-4202-b817-174c0070dc79}

| Keyword | Corresponding Legacy Flags and Groups |
| ------- | ------------------------------------- |
| SYSTEM_IO_KW_DISK | EVENT_TRACE_FLAG_DISK_IO |
| SYSTEM_IO_KW_DISK_INIT | PERF_DISK_IO_INIT, EVENT_TRACE_FLAG_DISK_IO_INIT |
| SYSTEM_IO_KW_FILENAME | PERF_FILENAME, EVENT_TRACE_FLAG_DISK_FILE_IO |
| SYSTEM_IO_KW_SPLIT | PERF_SPLIT_IO, EVENT_TRACE_FLAG_SPLIT_IO |
| SYSTEM_IO_KW_FILE | PERF_FILE_IO, EVENT_TRACE_FLAG_FILE_IO |
| SYSTEM_IO_KW_OPTICAL | PERF_OPTICAL_IO, EVENT_TRACE_FLAG_FILE_IO_INIT |
| SYSTEM_IO_KW_OPTICAL_INIT | PERF_OPTICAL_IO_INIT |
| SYSTEM_IO_KW_DRIVERS | PERF_DRIVERS, EVENT_TRACE_FLAG_DRIVER |
| SYSTEM_IO_KW_CC | PERF_CC |
| SYSTEM_IO_KW_NETWORK | PERF_NETWORK, EVENT_TRACE_FLAG_NETWORK_TCPIP |

Note: Enabling the SYSTEM_IO_KW_DRIVERS keyword will automatically enable 
SYSTEM_IO_KW_FILENAME as well.  The SYSTEM_IO_KW_FILENAME is also automatically turned on when the System Memory Provider is enabled with the SYSTEM_MEMORY_KW_MEMORY keyword.
 
### System IO Filter Provider 

Provides events related to IO filtering including timing and failures.

GUID: SystemIoFilterProviderGuid {fbd09363-9e22-4661-b8bf-e7a34b535b8c}

| Keyword | Corresponding Legacy Flags and Groups |
| ------- | ------------------------------------- |
| SYSTEM_IOFILTER_KW_GENERAL | PERF_FLT_IO |
| SYSTEM_IOFILTER_KW_INIT | PERF_FLT_IO_INIT |
| SYSTEM_IOFILTER_KW_FASTIO | PERF_FLT_FASTIO |
| SYSTEM_IOFILTER_KW_FAILURE | PERF_FLT_IO_FAILURE |
 
### System Lock Provider 

Provides events relating to kernel locking mechanisms.

GUID: SystemLockProviderGuid {721ddfd3-dacc-4e1e-b26a-a2cb31d4705a}

| Keyword | Corresponding Legacy Flags and Groups |
| ------- | ------------------------------------- |
| SYSTEM_LOCK_KW_SPINLOCK | PERF_SPINLOCK |
| SYSTEM_LOCK_KW_SPINLOCK_COUNTERS | PERF_SPINLOCK_CNTRS |
| SYSTEM_LOCK_KW_SYNC_OBJECTS | PERF_SYNC_OBJECTS |
 
### System Memory Provider 

Provides events relating to the memory manager.

GUID: SystemMemoryProviderGuid {82958ca9-b6cd-47f8-a3a8-03ae85a4bc24}

| Keyword | Corresponding Legacy Flags and Groups |
| ------- | ------------------------------------- |
| SYSTEM_MEMORY_KW_GENERAL | PERF_MEMORY |
| SYSTEM_MEMORY_KW_HARD_FAULTS | PERF_HARD_FAULTS, EVENT_TRACE_FLAG_MEMORY_HARD_FAULTS |
| SYSTEM_MEMORY_KW_ALL_FAULTS | PERF_ALL_FAULTS, EVENT_TRACE_FLAG_MEMORY_PAGE_FAULTS |
| SYSTEM_MEMORY_KW_POOL | PERF_POOL |
| SYSTEM_MEMORY_KW_MEMINFO | PERF_MEMINFO |
| SYSTEM_MEMORY_KW_PFSECTION | PERF_PFSECTION |
| SYSTEM_MEMORY_KW_MEMINFO_WS | PERF_MEMINFO_WS |
| SYSTEM_MEMORY_KW_HEAP | PERF_HEAP |
| SYSTEM_MEMORY_KW_WS | PERF_WS |
| SYSTEM_MEMORY_KW_CONTMEM_GEN | PERF_CONTMEM_GEN |
| SYSTEM_MEMORY_KW_VIRTUAL_ALLOC | PERF_VIRTUAL_ALLOC, EVENT_TRACE_FLAG_VIRTUAL_ALLOC |
| SYSTEM_MEMORY_KW_FOOTPRINT | PERF_FOOTPRINT |
| SYSTEM_MEMORY_KW_SESSION | PERF_SESSION |
| SYSTEM_MEMORY_KW_REFSET | PERF_REFSET |
| SYSTEM_MEMORY_KW_VAMAP | PERF_VAMAP, EVENT_TRACE_FLAG_VAMAP |

Notes: 
* Enabling the SYSTEM_MEMORY_KW_MEMORY keyword will automatically enable SYSTEM_IO_KW_FILENAME on the System IO Provider as well.
* The events enabled by the SYSTEM_MEMORY_KW_POOL support a Pool Tag Filter, to selectively write events only for certain pool tags.  This is configured as a [Schematized Filter](/windows/win32/api/evntprov/ns-evntprov-event_filter_descriptor) on the System Memory Provider.  The PoolTag filter is constructed as follows:

    ```cpp
    {
    EVENT_FILTER_HEADER Header; 
    ULONG PoolTags[ETW_MAX_POOLTAG_FILTER];
    }
    ```

* The [EVENT_FILTER_HEADER](/windows/win32/api/evntprov/ns-evntprov-event_filter_header) should be initialized with Id set to SYSTEM_MEMORY_POOL_FILTER_ID and the size field set to the size of Header plus the used portion of the PoolTags array.  

* Each Pool Tag is a 4 character string that is stored as a ULONG in the filter.  
 
 
### System Object Provider 

Provides events relating to the Object Manager.

GUID: SystemObjectProviderGuid {febd7460-3d1d-47eb-af49-c9eeb1e146f2}

| Keyword | Corresponding Legacy Flags and Groups |
| ------- | ------------------------------------- |
| SYSTEM_OBJECT_KW_HANDLE | PERF_OB_HANDLE |
| SYSTEM_OBJECT_KW_OBJECT | PERF_OB_OBJECT |
 
### System Power Provider 

Provides events relating to the system's power state.

GUID: SystemPowerProviderGuid {c134884a-32d5-4488-80e5-14ed7abb8269}

| Keyword | Corresponding Legacy Flags and Groups |
| ------- | ------------------------------------- |
| SYSTEM_POWER_KW_GENERAL | PERF_POWER |
| SYSTEM_POWER_KW_HIBER_RUNDOWN | PERF_HIBER_RUNDOWN |
| SYSTEM_POWER_KW_PROCESSOR_IDLE | PERF_PROCESSOR_IDLE |
| SYSTEM_POWER_KW_IDLE_SELECTION | PERF_IDLE_SELECTION |
| SYSTEM_POWER_KW_PPM_EXIT_LATENCY | PERF_PPM_EXIT_LATENCY |
 
### System Process Provider 

Provides events relating to the process, including lifetime information, image load events, and thread related events.

GUID: SystemProcessProviderGuid {151f55dc-467d-471f-83b5-5f889d46ff66}

| Keyword | Corresponding Legacy Flags and Groups |
| ------- | ------------------------------------- |
| SYSTEM_PROCESS_KW_GENERAL | PERF_PROCESS, EVENT_TRACE_FLAG_PROCESS |
| SYSTEM_PROCESS_KW_INSWAP | PERF_PROCESS_INSWAP |
| SYSTEM_PROCESS_KW_FREEZE | PERF_PROCESS_FREEZE |
| SYSTEM_PROCESS_KW_PERF_COUNTER | PERF_PERF_COUNTER, EVENT_TRACE_FLAG_PROCESS_COUNTERS |
| SYSTEM_PROCESS_KW_WAKE_COUNTER | PERF_WAKE_COUNTER |
| SYSTEM_PROCESS_KW_WAKE_DROP | PERF_WAKE_DROP |
| SYSTEM_PROCESS_KW_WAKE_EVENT | PERF_WAKE_EVENT |
| SYSTEM_PROCESS_KW_DEBUG_EVENTS | PERF_DEBUG_EVENTS, EVENT_TRACE_FLAG_DEBUG_EVENTS |
| SYSTEM_PROCESS_KW_DBGPRINT | PERF_DBGPRINT, EVENT_TRACE_FLAG_DBGPRINT |
| SYSTEM_PROCESS_KW_JOB | PERF_JOB, EVENT_TRACE_FLAG_JOB |
| SYSTEM_PROCESS_KW_WORKER_THREAD | PERF_WORKER_THREAD |
| SYSTEM_PROCESS_KW_THREAD | PERF_THREAD, EVENT_TRACE_FLAG_THREAD |
| SYSTEM_PROCESS_KW_LOADER | PERF_LOADER, EVENT_TRACE_FLAG_IMAGE_LOAD |
 
### System Profile Provider 

Provides profiling events.

GUID: SystemProfileProviderGuid {bfeb0324-1cee-496f-a409-2ac2b48a6322}

| Keyword | Corresponding Legacy Flags and Groups |
| ------- | ------------------------------------- |
| SYSTEM_PROFILE_KW_GENERAL | PERF_PROFILE, EVENT_TRACE_FLAG_PROFILE |
| SYSTEM_PROFILE_KW_PMC_PROFILE | PERF_PMC_PROFILE |
 
### System Registry Provider 

Provides events relating to the registry.

GUID: SystemRegistryProviderGuid {16156bd9-fab4-4cfa-a232-89d1099058e3}

| Keyword | Corresponding Legacy Flags and Groups |
| ------- | ------------------------------------- |
| SYSTEM_REGISTRY_KW_GENERAL | PERF_REGISTRY, EVENT_TRACE_FLAG_REGISTRY |
| SYSTEM_REGISTRY_KW_HIVE | PERF_REG_HIVE |
| SYSTEM_REGISTRY_KW_NOTIFICATION | PERF_REG_NOTIF |
 
### System Scheduler Provider 

Provides events relating to the scheduler.

GUID: SystemSchedulerProviderGuid {599a2a76-4d91-4910-9ac7-7d33f2e97a6c}

| Keyword | Corresponding Legacy Flags and Groups |
| ------- | ------------------------------------- |
| SYSTEM_SCHEDULER_KW_XSCHEDULER | PERF_XSCHEDULER |
| SYSTEM_SCHEDULER_KW_DISPATCHER | PERF_DISPATCHER, EVENT_TRACE_FLAG_DISPATCHER |
| SYSTEM_SCHEDULER_KW_KERNEL_QUEUE | PERF_KERNEL_QUEUE |
| SYSTEM_SCHEDULER_KW_SHOULD_YIELD | PERF_SHOULD_YIELD |
| SYSTEM_SCHEDULER_KW_ANTI_STARVATION | PERF_ANTI_STARVATION |
| SYSTEM_SCHEDULER_KW_LOAD_BALANCER | PERF_LOAD_BALANCER |
| SYSTEM_SCHEDULER_KW_AFFINITY | PERF_AFFINITY |
| SYSTEM_SCHEDULER_KW_PRIORITY | PERF_PRIORITY |
| SYSTEM_SCHEDULER_KW_IDEAL_PROCESSOR | PERF_IDEAL_PROCESSOR |
| SYSTEM_SCHEDULER_KW_CONTEXT_SWITCH | PERF_CONTEXT_SWITCH, EVENT_TRACE_FLAG_CSWITCH |
 
### System Syscall Provider 

Provides events with information about system calls.

GUID: SystemSyscallProviderGuid {434286f7-6f1b-45bb-b37e-95f623046c7c}

| Keyword | Corresponding Legacy Flags and Groups |
| ------- | ------------------------------------- |
| SYSTEM_SYSCALL_KW_GENERAL | PERF_SYSCALL, EVENT_TRACE_FLAG_SYSTEMCALL |
 
### System Timer Provider 

Provides events relating to timers in the kernel.

GUID: SystemTimerProviderGuid {4f061568-e215-499f-ab2e-eda0ae890a5b}

| Keyword | Corresponding Legacy Flags and Groups |
| ------- | ------------------------------------- |
| SYSTEM_TIMER_KW_GENERAL | PERF_TIMER |
| SYSTEM_TIMER_KW_CLOCK_TIMER | PERF_CLOCK_TIMER |
 
## Remarks

This new enablement mechanism is in addition to the pre-existing methods for enabling these events.  Any code that used to work, will continue to do so.
 
The events generated by the System Trace Provider are not changing due to this new feature.  This means that the outputted events are not marked as being emitted from the individual system providers.
 
For more information on provider GUID and keyword definitions see [evntrace.h](/windows/win32/api/evntrace/).

## See Also

[Configuring and Starting a SystemTraceProvider Session](configuring-and-starting-a-systemtraceprovider-session.md)

[evntrace.h header](/windows/win32/api/evntrace/)
