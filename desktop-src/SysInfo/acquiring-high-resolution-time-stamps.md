---
description: Windows provides APIs that you can use to acquire high-resolution time stamps or measure time intervals.
ms.assetid: D66E0FC2-3AF2-489B-B4B5-78648905B77B
title: Acquiring high-resolution time stamps
ms.topic: article
ms.date: 05/31/2018
---

# Acquiring high-resolution time stamps

Windows provides APIs that you can use to acquire high-resolution time stamps, or measure time intervals. The primary API for native code is [**QueryPerformanceCounter (QPC)**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter). For device drivers, the kernel-mode API is [**KeQueryPerformanceCounter**](/windows-hardware/drivers/ddi/content/ntifs/nf-ntifs-kequeryperformancecounter). For managed code, the [**System.Diagnostics.Stopwatch**](/previous-versions/windows/) class uses **QPC** as its precise time basis.

[**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) is independent of, and isn't synchronized to, any external time reference. To retrieve time stamps that can be synchronized to an external time reference, such as, Coordinated Universal Time (UTC) for use in high-resolution time-of-day measurements, use [**GetSystemTimePreciseAsFileTime**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemtimepreciseasfiletime).

Time stamps and time-interval measurements are an integral part of computer and network performance measurements. These performance measurement operations include the computation of response time, throughput, and latency, as well as profiling code execution. Each of these operations involves a measurement of activities that occur during a time interval that is defined by a start and an end event that can be independent of any external time-of-day reference.

[**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) is typically the best method to use to time-stamp events and measure small time intervals that occur on the same system or virtual machine. Consider using [**GetSystemTimePreciseAsFileTime**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemtimepreciseasfiletime) when you want to time-stamp events across multiple machines, provided that each machine is participating in a time synchronization scheme such as Network Time Protocol (NTP). **QPC** helps you avoid difficulties that can be encountered with other time measurement approaches, such as reading the processor’s time stamp counter (TSC) directly.

-   [QPC support in Windows versions](#qpc-support-in-windows-versions)
-   [Guidance for acquiring time stamps](#guidance-for-acquiring-time-stamps)
    -   [Virtualization](#virtualization)
    -   [Direct TSC usage](#direct-tsc-usage)
    -   [Examples for acquiring time stamps](#examples-for-acquiring-time-stamps)
-   [General FAQ about QPC and TSC](#general-faq-about-qpc-and-tsc)
-   [FAQ about programming with QPC and TSC](#faq-about-programming-with-qpc-and-tsc)
-   [Low-level hardware clock characteristics](#low-level-hardware-clock-characteristics)
    -   [Absolute Clocks and Difference Clocks](#absolute-clocks-and-difference-clocks)
    -   [Resolution, Precision, Accuracy, and Stability](#resolution-precision-accuracy-and-stability)
-   [Hardware timer info](#hardware-timer-info)

## QPC support in Windows versions

[**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) was introduced in Windows 2000 and Windows XP and has evolved to take advantage of improvements in the hardware platform and processors. Here we describe the characteristics of **QPC** on different Windows versions to help you maintain software that runs on those Windows versions.

### Windows XP and Windows 2000

[**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) is available on Windows XP and Windows 2000 and works well on most systems. However, some hardware systems' BIOS didn't indicate the hardware CPU characteristics correctly (a non-invariant TSC), and some multi-core or multi-processor systems used processors with TSCs that couldn't be synchronized across cores. Systems with flawed firmware that run these versions of Windows might not provide the same **QPC** reading on different cores if they used the TSC as the basis for **QPC**.

### Windows Vista and Windows Server 2008

All computers that shipped with Windows Vista and Windows Server 2008 used a platform counter (High Precision Event Timer (HPET)) or the ACPI Power Management Timer (PM timer) as the basis for [**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter). Such platform timers have higher access latency than the TSC and are shared between multiple processors. This limits scalability of **QPC** if it is called concurrently from multiple processors.

### Windows 7 and Windows Server 2008 R2

The majority of Windows 7 and Windows Server 2008 R2 computers have processors with constant-rate TSCs and use these counters as the basis for [**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter). TSCs are high-resolution per-processor hardware counters that can be accessed with very low latency and overhead (in the order of 10s or 100s of machine cycles, depending on the processor type). Windows 7 and Windows Server 2008 R2 use TSCs as the basis of **QPC** on single-clock domain systems where the operating system (or the hypervisor) is able to tightly synchronize the individual TSCs across all processors during system initialization. On such systems, the cost of reading the performance counter is significantly lower compared to systems that use a platform counter. Furthermore, there is no added overhead for concurrent calls and user-mode queries often bypass system calls, which further reduces overhead. On systems where the TSC is not suitable for timekeeping, Windows automatically selects a platform counter (either the HPET timer or the ACPI PM timer) as the basis for **QPC**.

### Windows 8, Windows 8.1, Windows Server 2012, and Windows Server 2012 R2

Windows 8, Windows 8.1, Windows Server 2012, and Windows Server 2012 R2 use TSCs as the basis for the performance counter. The TSC synchronization algorithm was significantly improved to better accommodate large systems with many processors. In addition, support for the new precise time-of-day API was added, which enables acquiring precise wall clock time stamps from the operating system. For more info, see [**GetSystemTimePreciseAsFileTime**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemtimepreciseasfiletime). On Windows RT and Windows 10 devices using Arm processors, the performance counter is based on either a proprietary platform counter or the system counter provided by the Arm Generic Timer if the platform is so equipped.

## Guidance for acquiring time stamps

Windows has and will continue to invest in providing a reliable and efficient performance counter. When you need time stamps with a resolution of 1 microsecond or better and you don't need the time stamps to be synchronized to an external time reference, choose [**QueryPerformanceCounter**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter), [**KeQueryPerformanceCounter**](/windows-hardware/drivers/ddi/content/ntifs/nf-ntifs-kequeryperformancecounter), or [**KeQueryInterruptTimePrecise**](/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kequeryinterrupttimeprecise). When you need UTC-synchronized time stamps with a resolution of 1 microsecond or better, choose [**GetSystemTimePreciseAsFileTime**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemtimepreciseasfiletime) or [**KeQuerySystemTimePrecise**](/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kequerysystemtimeprecise).

On a relatively small number of platforms that can't use the TSC register as the [**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) basis, for example, for reasons explained in [Hardware timer info](#hardware-timer-info), acquiring high resolution time stamps can be significantly more expensive than acquiring time stamps with lower resolution. If resolution of 10 to 16 milliseconds is sufficient, you can use [**GetTickCount64**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-gettickcount64), [**QueryInterruptTime**](/windows/desktop/api/realtimeapiset/nf-realtimeapiset-queryinterrupttime), [**QueryUnbiasedInterruptTime**](/windows/win32/api/realtimeapiset/nf-realtimeapiset-queryunbiasedinterrupttime), [**KeQueryInterruptTime**](/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kequeryinterrupttime), or [**KeQueryUnbiasedInterruptTime**](/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kequeryunbiasedinterrupttime) to obtain time stamps that aren't synchronized to an external time reference. For UTC-synchronized time stamps, use [**GetSystemTimeAsFileTime**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemtimeasfiletime) or [**KeQuerySystemTime**](/windows-hardware/drivers/ddi/wdm/nf-wdm-kequerysystemtime~r1). If higher resolution is needed, you can use [**QueryInterruptTimePrecise**](/windows/desktop/api/realtimeapiset/nf-realtimeapiset-queryinterrupttimeprecise), [**QueryUnbiasedInterruptTimePrecise**](/windows/desktop/api/realtimeapiset/nf-realtimeapiset-queryunbiasedinterrupttimeprecise), or [**KeQueryInterruptTimePrecise**](/windows-hardware/drivers/ddi/content/wdm/nf-wdm-kequeryinterrupttimeprecise) to obtain time stamps instead.

In general, the performance counter results are consistent across all processors in multi-core and multi-processor systems, even when measured on different threads or processes. Here are some exceptions to this rule:

-   Pre-Windows Vista operating systems that run on certain processors might violate this consistency because of one of these reasons:

    -   The hardware processors have a non-invariant TSC and the BIOS doesn't indicate this condition correctly.
    -   The TSC synchronization algorithm that was used wasn't suitable for systems with large numbers of processors.

-   When you compare performance counter results that are acquired from different threads, consider values that differ by ± 1 tick to have an ambiguous ordering. If the time stamps are taken from the same thread, this ± 1 tick uncertainty doesn't apply. In this context, the term tick refers to a period of time equal to 1 ÷ (the frequency of the performance counter obtained from [**QueryPerformanceFrequency**](/windows/win32/api/profileapi/nf-profileapi-queryperformancefrequency)).

When you use the performance counter on large server systems with multiple-clock domains that aren't synchronized in hardware, Windows determines that the TSC can't be used for timing purposes and selects a platform counter as the basis for [**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter). While this scenario still yields reliable time stamps, the access latency and scalability is adversely affected. Therefore, as previously stated in the preceding usage guidance, only use the APIs that provide 1 microsecond or better resolution when such resolution is necessary. The TSC is used as the basis for **QPC** on multi-clock domain systems that include hardware synchronization of all processor clock domains, as this effectively makes them function as a single clock domain system.

The frequency of the performance counter is fixed at system boot and is consistent across all processors so you only need to query the frequency from [**QueryPerformanceFrequency**](/windows/win32/api/profileapi/nf-profileapi-queryperformancefrequency) as the application initializes, and then cache the result.

### Virtualization

The performance counter is expected to work reliably on all guest virtual machines running on correctly implemented hypervisors. However, hypervisors that comply with the hypervisor version 1.0 interface and surface the reference time enlightenment can offer substantially lower overhead. For more information about hypervisor interfaces and enlightenments, see [Hypervisor Specifications](/virtualization/hyper-v-on-windows/reference/tlfs).

### Direct TSC usage

We strongly discourage using the **RDTSC** or **RDTSCP** processor instruction to directly query the TSC because you won't get reliable results on some versions of Windows, across live migrations of virtual machines, and on hardware systems without invariant or tightly synchronized TSCs. Instead, we encourage you to use [**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) to leverage the abstraction, consistency, and portability that it offers.

### Examples for acquiring time stamps

The various code examples in these sections show how to acquire time stamps.

### Using QPC in native code

This example shows how to use [**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) in C and C++ native code.


```C++
LARGE_INTEGER StartingTime, EndingTime, ElapsedMicroseconds;
LARGE_INTEGER Frequency;

QueryPerformanceFrequency(&Frequency); 
QueryPerformanceCounter(&StartingTime);

// Activity to be timed

QueryPerformanceCounter(&EndingTime);
ElapsedMicroseconds.QuadPart = EndingTime.QuadPart - StartingTime.QuadPart;


//
// We now have the elapsed number of ticks, along with the
// number of ticks-per-second. We use these values
// to convert to the number of elapsed microseconds.
// To guard against loss-of-precision, we convert
// to microseconds *before* dividing by ticks-per-second.
//

ElapsedMicroseconds.QuadPart *= 1000000;
ElapsedMicroseconds.QuadPart /= Frequency.QuadPart;
```



### Acquiring high resolution time stamps from managed code

This example shows how to use the managed code [**System.Diagnostics.Stopwatch**](/previous-versions/windows/) class.


```CSharp
using System.Diagnostics;

long StartingTime = Stopwatch.GetTimestamp();

// Activity to be timed

long EndingTime  = Stopwatch.GetTimestamp();
long ElapsedTime = EndingTime - StartingTime;

double ElapsedSeconds = ElapsedTime * (1.0 / Stopwatch.Frequency);
```



The [**System.Diagnostics.Stopwatch**](/previous-versions/windows/) class also provides several convenient methods to perform time-interval measurements.

### Using QPC from kernel mode

The Windows kernel provides kernel-mode access to the performance counter through [**KeQueryPerformanceCounter**](/windows-hardware/drivers/ddi/content/ntifs/nf-ntifs-kequeryperformancecounter) from which both the performance counter and performance frequency can be obtained. **KeQueryPerformanceCounter** is available from kernel mode only and is provided for writers of device drivers and other kernel-mode components.

This example shows how to use [**KeQueryPerformanceCounter**](/windows-hardware/drivers/ddi/content/ntifs/nf-ntifs-kequeryperformancecounter) in C and C++ kernel mode.


```C++
LARGE_INTEGER StartingTime, EndingTime, ElapsedMicroseconds;
LARGE_INTEGER Frequency;

StartingTime = KeQueryPerformanceCounter(&Frequency);

// Activity to be timed

EndingTime = KeQueryPerformanceCounter(NULL);
ElapsedMicroseconds.QuadPart = EndingTime.QuadPart - StartingTime.QuadPart;
ElapsedMicroseconds.QuadPart *= 1000000;
ElapsedMicroseconds.QuadPart /= Frequency.QuadPart;
```



## General FAQ about QPC and TSC

Here are answers to frequently-asked questions about [**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) and TSCs in general.

<dl> <dt>

<span id="Is_QueryPerformanceCounter___the_same_as_the_Win32_GetTickCount___or_________GetTickCount64___function_"></span><span id="is_queryperformancecounter___the_same_as_the_win32_gettickcount___or_________gettickcount64___function_"></span><span id="IS_QUERYPERFORMANCECOUNTER___THE_SAME_AS_THE_WIN32_GETTICKCOUNT___OR_________GETTICKCOUNT64___FUNCTION_"></span>**Is QueryPerformanceCounter() the same as the Win32 GetTickCount() or GetTickCount64() function?**
</dt> <dd>

No. [**GetTickCount**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-gettickcount) and [**GetTickCount64**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-gettickcount64) aren't related to [**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter). **GetTickCount** and **GetTickCount64** return the number of milliseconds since the system was started.

</dd> <dt>

<span id="Should_I_use_QPC_or_call_the_RDTSC__RDTSCP_instructions_directly_"></span><span id="should_i_use_qpc_or_call_the_rdtsc__rdtscp_instructions_directly_"></span><span id="SHOULD_I_USE_QPC_OR_CALL_THE_RDTSC__RDTSCP_INSTRUCTIONS_DIRECTLY_"></span>**Should I use QPC or call the RDTSC/RDTSCP instructions directly?**
</dt> <dd>

To avoid incorrectness and portability issues, we strongly encourage you to use [**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) instead of using the TSC register or the **RDTSC** or **RDTSCP** processor instructions.

</dd> <dt>

<span id="What_is_QPC_s_relation_to_an_external_time_epoch__Can_it_be_synchronized_to_an_________external_epoch_such_as_UTC_"></span><span id="what_is_qpc_s_relation_to_an_external_time_epoch__can_it_be_synchronized_to_an_________external_epoch_such_as_utc_"></span><span id="WHAT_IS_QPC_S_RELATION_TO_AN_EXTERNAL_TIME_EPOCH__CAN_IT_BE_SYNCHRONIZED_TO_AN_________EXTERNAL_EPOCH_SUCH_AS_UTC_"></span>**What is QPC’s relation to an external time epoch? Can it be synchronized to an external epoch such as UTC?**
</dt> <dd>

[**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) is based on a hardware counter that can't be synchronized to an external time reference, such as UTC. For precise time-of-day time stamps that can be synchronized to an external UTC reference, use [**GetSystemTimePreciseAsFileTime**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemtimepreciseasfiletime).

</dd> <dt>

<span id="Is_QPC_affected_by_daylight_savings_time__leap_seconds__time_zones__or_system_________time_changes_made_by_the_administrator_"></span><span id="is_qpc_affected_by_daylight_savings_time__leap_seconds__time_zones__or_system_________time_changes_made_by_the_administrator_"></span><span id="IS_QPC_AFFECTED_BY_DAYLIGHT_SAVINGS_TIME__LEAP_SECONDS__TIME_ZONES__OR_SYSTEM_________TIME_CHANGES_MADE_BY_THE_ADMINISTRATOR_"></span>**Is QPC affected by daylight savings time, leap seconds, time zones, or system time changes made by the administrator?**
</dt> <dd>

No. [**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) is completely independent of the system time and UTC.

</dd> <dt>

<span id="Is_QPC_accuracy_affected_by_processor_frequency_changes_caused_by_power_________management_or_Turbo_Boost_technology_"></span><span id="is_qpc_accuracy_affected_by_processor_frequency_changes_caused_by_power_________management_or_turbo_boost_technology_"></span><span id="IS_QPC_ACCURACY_AFFECTED_BY_PROCESSOR_FREQUENCY_CHANGES_CAUSED_BY_POWER_________MANAGEMENT_OR_TURBO_BOOST_TECHNOLOGY_"></span>**Is QPC accuracy affected by processor frequency changes caused by power management or Turbo Boost technology?**
</dt> <dd>

No. If the processor has an invariant TSC, the [**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) is not affected by these sort of changes. If the processor doesn't have an invariant TSC, **QPC** will revert to a platform hardware timer that won't be affected by processor frequency changes or Turbo Boost technology.

</dd> <dt>

<span id="Does_QPC_reliably_work_on_multi-processor_systems__multi-core_system__and_________systems_with_hyper-threading_"></span><span id="does_qpc_reliably_work_on_multi-processor_systems__multi-core_system__and_________systems_with_hyper-threading_"></span><span id="DOES_QPC_RELIABLY_WORK_ON_MULTI-PROCESSOR_SYSTEMS__MULTI-CORE_SYSTEM__AND_________SYSTEMS_WITH_HYPER-THREADING_"></span>**Does QPC reliably work on multi-processor systems, multi-core system, and systems with hyper-threading?**
</dt> <dd>

Yes.

</dd> <dt>

<span id="How_do_I_determine_and_validate_that_QPC_works_on_my_machine_"></span><span id="how_do_i_determine_and_validate_that_qpc_works_on_my_machine_"></span><span id="HOW_DO_I_DETERMINE_AND_VALIDATE_THAT_QPC_WORKS_ON_MY_MACHINE_"></span>**How do I determine and validate that QPC works on my machine?**
</dt> <dd>

You don't need to perform such checks.

</dd> <dt>

<span id="Which_processors_have_non-invariant_TSCs__How_can_I_check_if_my_system_has_a_________non-invariant_TSC_"></span><span id="which_processors_have_non-invariant_tscs__how_can_i_check_if_my_system_has_a_________non-invariant_tsc_"></span><span id="WHICH_PROCESSORS_HAVE_NON-INVARIANT_TSCS__HOW_CAN_I_CHECK_IF_MY_SYSTEM_HAS_A_________NON-INVARIANT_TSC_"></span>**Which processors have non-invariant TSCs? How can I check if my system has a non-invariant TSC?**
</dt> <dd>

You don't need to perform this check yourself. Windows operating systems perform several checks at system initialization to determine if the TSC is suitable as a basis for [**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter). However, for reference purposes, you can determine whether your processor has an invariant TSC by using one of these:

-   the Coreinfo.exe utility from Windows Sysinternals
-   checking the values returned by the CPUID instruction pertaining to the TSC characteristics
-   the processor manufacturer’s documentation

The following shows the TSC-INVARIANT info that is provided by the Windows Sysinternals Coreinfo.exe utility ([www.sysinternals.com](https://www.sysinternals.com)). An asterisk means "True".

``` syntax
> Coreinfo.exe 

Coreinfo v3.2 - Dump information on system CPU and memory topology
Copyright (C) 2008-2012 Mark Russinovich
Sysinternals - www.sysinternals.com

 <unrelated text removed>

RDTSCP          * Supports RDTSCP instruction
TSC             * Supports RDTSC instruction
TSC-DEADLINE    - Local APIC supports one-shot deadline timer
TSC-INVARIANT   * TSC runs at constant rate
```

</dd> <dt>

<span id="Does_QPC_work_reliably_on__hardware_platforms_"></span><span id="does_qpc_work_reliably_on__hardware_platforms_"></span><span id="DOES_QPC_WORK_RELIABLY_ON__HARDWARE_PLATFORMS_"></span>**Does QPC work reliably on Windows RT hardware platforms?**
</dt> <dd>

Yes.

</dd> <dt>

<span id="How_often_does_QPC_roll_over_"></span><span id="how_often_does_qpc_roll_over_"></span><span id="HOW_OFTEN_DOES_QPC_ROLL_OVER_"></span>**How often does QPC roll over?**
</dt> <dd>

Not less than 100 years from the most recent system boot, and potentially longer based on the underlying hardware timer used. For most applications, rollover isn't a concern.

</dd> <dt>

<span id="What_is_the_computational_cost_of_calling_QPC_"></span><span id="what_is_the_computational_cost_of_calling_qpc_"></span><span id="WHAT_IS_THE_COMPUTATIONAL_COST_OF_CALLING_QPC_"></span>**What is the computational cost of calling QPC?**
</dt> <dd>

The computational calling cost of [**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) is determined primarily by the underlying hardware platform. If the TSC register is used as the basis for QPC, the computational cost is determined primarily by how long the processor takes to process an **RDTSC** instruction. This time ranges from 10s of CPU cycles to several hundred CPU cycles depending upon the processor used. If the TSC can't be used, the system will select a different hardware time basis. Because these time bases are located on the motherboard (for example, on the PCI South Bridge or PCH), the per-call computational cost is higher than the TSC, and is frequently in the vicinity of 0.8 - 1.0 microseconds depending on processor speed and other hardware factors. This cost is dominated by the time required to access the hardware device on the motherboard.

</dd> <dt>

<span id="Does_QPC_require_a_kernel_transition__system_call__"></span><span id="does_qpc_require_a_kernel_transition__system_call__"></span><span id="DOES_QPC_REQUIRE_A_KERNEL_TRANSITION__SYSTEM_CALL__"></span>**Does QPC require a kernel transition (system call)?**
</dt> <dd>

A kernel transition is not required if the system can use the TSC register as the basis for [**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter). If the system must use a different time base, such as the HPET or PM timer, a system call is required.

</dd> <dt>

<span id="Is_the_performance_counter_monotonic__non-decreasing__"></span><span id="is_the_performance_counter_monotonic__non-decreasing__"></span><span id="IS_THE_PERFORMANCE_COUNTER_MONOTONIC__NON-DECREASING__"></span>**Is the performance counter monotonic (non-decreasing)?**
</dt> <dd>

Yes. QPC does not go backward.

</dd> <dt>

<span id="Can_the_performance_counter_be_used_to_order_events_in_time_"></span><span id="can_the_performance_counter_be_used_to_order_events_in_time_"></span><span id="CAN_THE_PERFORMANCE_COUNTER_BE_USED_TO_ORDER_EVENTS_IN_TIME_"></span>**Can the performance counter be used to order events in time?**
</dt> <dd>

Yes. However, when comparing performance counter results that are acquired from different threads, values that differ by ± 1 tick have an ambiguous ordering as if they had an identical time stamp.

</dd> <dt>

<span id="How_accurate_is_the_performance_counter_"></span><span id="how_accurate_is_the_performance_counter_"></span><span id="HOW_ACCURATE_IS_THE_PERFORMANCE_COUNTER_"></span>**How accurate is the performance counter?**
</dt> <dd>

The answer depends on a variety of factors. For more info, see [Low-level hardware clock characteristics](#low-level-hardware-clock-characteristics).

</dd> </dl>

## FAQ about programming with QPC and TSC

Here are answers to frequently-asked questions about programming with [**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) and TSCs.

<dl> <dt>

<span id="I_need_to_convert_the_QPC_output_to_milliseconds._How_can_I_avoid_loss_of_________precision_with_converting_to_double_or_float_"></span><span id="i_need_to_convert_the_qpc_output_to_milliseconds._how_can_i_avoid_loss_of_________precision_with_converting_to_double_or_float_"></span><span id="I_NEED_TO_CONVERT_THE_QPC_OUTPUT_TO_MILLISECONDS._HOW_CAN_I_AVOID_LOSS_OF_________PRECISION_WITH_CONVERTING_TO_DOUBLE_OR_FLOAT_"></span>**I need to convert the QPC output to milliseconds. How can I avoid loss of precision with converting to double or float?**
</dt> <dd>

There are several things to keep in mind when performing calculations on integer performance counters:

-   Integer division will lose the remainder. This can cause loss of precision in some cases.
-   Conversion between 64 bit integers and floating point (double) can cause loss of precision because the floating point mantissa can't represent all possible integral values.
-   Multiplication of 64 bit integers can result in integer overflow.

As a general principle, delay these computations and conversions as long as possible to avoid compounding the errors introduced.

</dd> <dt>

<span id="How_can_I_convert_QPC_to_100_nanosecond_ticks_so_I_can_add_it_to_a_________FILETIME_"></span><span id="how_can_i_convert_qpc_to_100_nanosecond_ticks_so_i_can_add_it_to_a_________filetime_"></span><span id="HOW_CAN_I_CONVERT_QPC_TO_100_NANOSECOND_TICKS_SO_I_CAN_ADD_IT_TO_A_________FILETIME_"></span>**How can I convert QPC to 100 nanosecond ticks so I can add it to a FILETIME?**
</dt> <dd>

A file time is a 64-bit value that represents the number of 100-nanosecond intervals that have elapsed since 12:00 A.M. January 1, 1601 Coordinated Universal Time (UTC). File times are used by Win32 API calls that return time-of-day, such as [**GetSystemTimeAsFileTime**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemtimeasfiletime) and [**GetSystemTimePreciseAsFileTime**](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemtimepreciseasfiletime). By contrast, [**QueryPerformanceCounter**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) returns values that represent time in units of 1/(the frequency of the performance counter obtained from [**QueryPerformanceFrequency**](/windows/win32/api/profileapi/nf-profileapi-queryperformancefrequency)). Conversion between the two requires calculating the ratio of the **QPC** interval and 100-nanoseconds intervals. Be careful to avoid losing precision because the values might be small (0.0000001 / 0.000000340).

</dd> <dt>

<span id="Why_is_the_time_stamp_that_is_returned_from_QPC_a_signed_integer_"></span><span id="why_is_the_time_stamp_that_is_returned_from_qpc_a_signed_integer_"></span><span id="WHY_IS_THE_TIME_STAMP_THAT_IS_RETURNED_FROM_QPC_A_SIGNED_INTEGER_"></span>**Why is the time stamp that is returned from QPC a signed integer?**
</dt> <dd>

Calculations that involve [**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) time stamps might involve subtraction. By using a signed value, you can handle calculations that might yield negative values.

</dd> <dt>

<span id="How_can_I_obtain_high_resolution_time_stamps_from_managed_code_"></span><span id="how_can_i_obtain_high_resolution_time_stamps_from_managed_code_"></span><span id="HOW_CAN_I_OBTAIN_HIGH_RESOLUTION_TIME_STAMPS_FROM_MANAGED_CODE_"></span>**How can I obtain high resolution time stamps from managed code?**
</dt> <dd>

Call the [**Stopwatch.GetTimeStamp**](/previous-versions/windows/) method from the [**System.Diagnostics.Stopwatch**](/previous-versions/windows/) class. For an example about how to use **Stopwatch.GetTimeStamp**, see [Acquiring high resolution time stamps from managed code](#acquiring-high-resolution-time-stamps-from-managed-code).

</dd> <dt>

<span id="Under_what_circumstances_does_QueryPerformanceFrequency_return_FALSE__or_________QueryPerformanceCounter_return_zero_"></span><span id="under_what_circumstances_does_queryperformancefrequency_return_false__or_________queryperformancecounter_return_zero_"></span><span id="UNDER_WHAT_CIRCUMSTANCES_DOES_QUERYPERFORMANCEFREQUENCY_RETURN_FALSE__OR_________QUERYPERFORMANCECOUNTER_RETURN_ZERO_"></span>**Under what circumstances does QueryPerformanceFrequency return FALSE, or QueryPerformanceCounter return zero?**
</dt> <dd>

This won't occur on any system that runs Windows XP or later.

</dd> <dt>

<span id="Do_I_need_to_set_the_thread_affinity_to_a_single_core_to_use_QPC_"></span><span id="do_i_need_to_set_the_thread_affinity_to_a_single_core_to_use_qpc_"></span><span id="DO_I_NEED_TO_SET_THE_THREAD_AFFINITY_TO_A_SINGLE_CORE_TO_USE_QPC_"></span>**Do I need to set the thread affinity to a single core to use QPC?**
</dt> <dd>

No. For more info, see [Guidance for acquiring time stamps](#guidance-for-acquiring-time-stamps). This scenario is neither necessary nor desirable. Performing this scenario might adversely affect your application's performance by restricting processing to one core or by creating a bottleneck on a single core if multiple threads set their affinity to the same core when calling [**QueryPerformanceCounter**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter).

</dd> </dl>

## Low-level hardware clock characteristics

These sections show low-level hardware clock characteristics.

### Absolute Clocks and Difference Clocks

Absolute clocks provide accurate time-of-day readings. They are typically based on Coordinated Universal Time (UTC) and consequently their accuracy depends in part on how well they are synchronized to an external time reference. Difference clocks measure time intervals and aren't typically based on an external time epoch. [**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) is a difference clock and isn't synchronized to an external time epoch or reference. When you use **QPC** for time-interval measurements, you typically get better accuracy than you would get by using time stamps that are derived from an absolute clock. This is because the process of synchronizing the time of an absolute clock can introduce phase and frequency shifts that increase the uncertainty of short term time-interval measurements.

### Resolution, Precision, Accuracy, and Stability

[**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) uses a hardware counter as its basis. Hardware timers consist of three parts: a tick generator, a counter that counts the ticks, and a means of retrieving the counter value. The characteristics of these three components determine the resolution, precision, accuracy, and stability of **QPC**.

If a hardware generator provides ticks at a constant rate, time intervals can be measured by simply counting these ticks. The rate at which the ticks are generated is called the frequency and expressed in Hertz (Hz). The reciprocal of the frequency is called the period or tick interval and is expressed in an appropriate International System of Units (SI) time unit (for example, second, millisecond, microsecond, or nanosecond).

![time interval](images/tick-interval.png)

The resolution of the timer is equal to the period. Resolution determines the ability to distinguish between any two time stamps and places a lower bound on the smallest time intervals that can be measured. This is sometimes called the tick resolution.

Digital measurement of time introduces a measurements uncertainty of ± 1 tick because the digital counter advances in discrete steps, while time is continuously advancing. This uncertainty is called a quantization error. For typical time-interval measurements, this effect can often be ignored because the quantizing error is much smaller than the time interval being measured.

![digital time measurement](images/digital-time-measure.png)

However, if the period being measured is small and approaches the resolution of the timer, you will need to consider this quantizing error. The size of the error introduced is that of one clock period.

The following two diagrams illustrate the impact of the ± 1 tick uncertainty by using a timer with a resolution of 1 time unit.

![tick uncertainty](images/tick-uncertainty.png)

[**QueryPerformanceFrequency**](/windows/win32/api/profileapi/nf-profileapi-queryperformancefrequency) returns the frequency of [**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter), and the period and resolution are equal to the reciprocal of this value. The performance counter frequency that **QueryPerformanceFrequency** returns is determined during system initialization and doesn't change while the system is running.

> [!Note]  
> Often [**QueryPerformanceFrequency**](/windows/win32/api/profileapi/nf-profileapi-queryperformancefrequency) doesn't return the actual frequency of the hardware tick generator. For example, in some older versions of Windows, **QueryPerformanceFrequency** returns the TSC frequency divided by 1024; and when running under a [hypervisor](https://msdn.microsoft.com/library/Ff542584(v=VS.85).aspx) that implements the [hypervisor version 1.0 interface](https://msdn.microsoft.com/library/Ff541458(v=VS.85).aspx) (or always in some newer versions of Windows), the performance counter frequency is fixed to 10 MHz. As a result, don't assume that **QueryPerformanceFrequency** will return a value derived from the hardware frequency.

 

[**QueryPerformanceCounter**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) reads the performance counter and returns the total number of ticks that have occurred since the Windows operating system was started, including the time when the machine was in a sleep state such as standby, hibernate, or connected standby.

These examples show how to calculate the tick interval and resolution and how to convert the tick count into a time value.

<dl> <dt>

<span id="Example_1"></span><span id="example_1"></span><span id="EXAMPLE_1"></span>**Example 1**
</dt> <dd>

[**QueryPerformanceFrequency**](/windows/win32/api/profileapi/nf-profileapi-queryperformancefrequency) returns the value 3,125,000 on a particular machine. What is the tick interval and resolution of [**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) measurements on this machine? The tick interval, or period, is the reciprocal of 3,125,000, which is 0.000000320 (320 nanoseconds). Therefore, each tick represents the passing of 320 nanoseconds. Time intervals smaller than 320 nanoseconds can't be measured on this machine.

Tick Interval = 1/(Performance Frequency)

Tick Interval = 1/3,125,000 = 320 ns

</dd> <dt>

<span id="Example_2"></span><span id="example_2"></span><span id="EXAMPLE_2"></span>**Example 2**
</dt> <dd>

On the same machine as the preceding example, the difference of the values returned from two successive calls to [**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) is 5. How much time has elapsed between the two calls? 5 ticks multiplied by 320 nanoseconds yields 1.6 microseconds.

ElapsedTime = Ticks \* Tick Interval

ElapsedTime = 5 \* 320 ns = 1.6 μs

</dd> </dl>

It takes time to access (read) the tick counter from software, and this access time can reduce the precision of the of the time measurement. This is because the minimum interval time (the smallest time interval that can be measured) is the larger of the resolution and the access time.

Precision = MAX \[ Resolution, AccessTime\]

For example, consider a hypothetical hardware timer with a 100 nanosecond resolution and an 800 nanosecond access time. This might be the case if the platform timer were used instead of the TSC register as the basis of [**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter). Thus, the precision would be 800 nanoseconds not 100 nanoseconds as shown in this calculation.

Precision = MAX \[800 ns,100 ns\] = 800 ns

These two figures depict this effect.

![qpc access time](images/qpc-access-time.png)

If the access time is greater than the resolution, don't try to improve the precision by guessing. In other words, it's an error to assume that the time stamp is taken precisely in the middle, or at the beginning or the end of the call.

By contrast, consider the following example in which the [**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) access time is only 20 nanoseconds and the hardware clock resolution is 100 nanoseconds. This might be the case if the TSC register was used as the basis for **QPC**. Here the precision is limited by the clock resolution.

![qpc precision](images/qpc-precision.png)

In practice, you can find time sources for which the time required to read the counter is larger or smaller than the resolution. In either case, the precision will be the larger of the two.

This table provides info on the approximate resolution, access time, and precision of a variety of clocks. Note that some of the values will vary with different processors, hardware platforms, and processor speeds.



| Clock Source                                                      | Nominal Clock Frequency | Clock Resolution    | Access Time (Typical) | Precision       |
|-------------------------------------------------------------------|-------------------------|---------------------|-----------------------|-----------------|
| PC RTC                                                            | 64 Hz                   | 15.625 milliseconds | N/A                   | N/A             |
| Query performance counter using TSC with a 3 GHz processor clock  | 3 MHz                   | 333 nanoseconds     | 30 nanoseconds        | 333 nanoseconds |
| **RDTSC** machine instruction on a system with a 3 GHz cycle time | 3 GHz                   | 333 picoseconds     | 30 nanoseconds        | 30 nanoseconds  |



 

Because [**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) uses a hardware counter, when you understand some basic characteristics of hardware counters, you gain understanding about the capabilities and limitations of **QPC**.

The most commonly used hardware tick generator is a crystal oscillator. The crystal is a small piece of quartz or other ceramic material that exhibits piezoelectric characteristics that provide an inexpensive frequency reference with excellent stability and accuracy. This frequency is used to generate the ticks counted by the clock.

The accuracy of a timer refers to the degree of conformity to a true or standard value. This depends primarily on the crystal oscillator’s ability to provide ticks at the specified frequency. If the frequency of oscillation is too high, the clock will 'run fast', and measured intervals will appear longer than they really are; and if the frequency is too low, the clock will 'run slow', and measured intervals will appear shorter than they really are.

For typical time-interval measurements for short duration (for example, response time measurements, network latency measurements, and so on), the accuracy of the hardware oscillator is usually sufficient. However, for some measurements the oscillator frequency accuracy becomes important, particularly for long time intervals or when you want to compare measurements taken on different machines. The remainder of this section explores the effects of the oscillator accuracy.

The crystals' frequency of oscillation is set during the manufacturing process and is specified by the manufacturer in terms of a specified frequency plus or minus a manufacturing tolerance expressed in 'parts per million' (ppm), called the maximum frequency offset. A crystal with a specified frequency of 1,000,000 Hz and a maximum frequency offset of ± 10 ppm would be within specification limits if its actual frequency were between 999,990 Hz and 1,000,010 Hz.

By substituting the phrase parts per million with microseconds per second, we can apply this frequency offset error to time-interval measurements. An oscillator with a + 10 ppm offset would have an error of 10 microseconds per second. Accordingly, when measuring a 1 second interval, it would run fast and measure a 1 second interval as 0.999990 seconds.

A convenient reference is that a frequency error of 100 ppm causes an error of 8.64 seconds after 24 hours. This table presents the measurement uncertainty due to the accumulated error for longer time intervals.



| Time interval duration | Measurement uncertainty due to accumulated error with +/- 10 PPM frequency tolerance |
|------------------------|--------------------------------------------------------------------------------------|
| 1 microsecond          | ± 10 picoseconds (10-12)                                                             |
| 1 millisecond          | ± 10 nanoseconds (10-9)                                                              |
| 1 second               | ± 10 microseconds                                                                    |
| 1 hour                 | ± 60 microseconds                                                                    |
| 1 day                  | ± 0.86 seconds                                                                       |
| 1 week                 | ± 6.08 seconds                                                                       |



 

The preceding table shows that for small time intervals the frequency offset error can often be ignored. However for long time intervals, even a small frequency offset can result in a substantial measurement uncertainty.

Crystal oscillators that are used in personal computers and servers are typically manufactured with a frequency tolerance of ± 30 to 50 parts per million, and rarely, crystals can be off by as much as 500 ppm. Although crystals with much tighter frequency offset tolerances are available, they are more expensive and thus are not used in most computers.

To reduce the adverse effects of this frequency offset error, recent versions of Windows, particularly Windows 8, use multiple hardware timers to detect the frequency offset and compensate for it to the extent possible. This calibration process is performed when Windows is started.

As the following examples show, the frequency offset error of a hardware clock influences the achievable accuracy, and the resolution of the clock can be less important.

![frequency offset error influences achievable accuracy](images/freq-offset-error.png)

<dl> <dt>

<span id="Example_1"></span><span id="example_1"></span><span id="EXAMPLE_1"></span>**Example 1**
</dt> <dd>

Suppose you perform time-interval measurements by using a 1 MHz oscillator, which has a resolution of 1 microsecond, and a maximum frequency offset error of ±50 ppm. Now, let us suppose the offset is exactly +50 ppm. This means that the actual frequency would be 1,000,050 Hz. If we measured a time interval of 24 hours, our measurement would be 4.3 seconds too short (23:59:55.700000 measured versus 24:00:00.000000 actual).

Seconds in a day = 86400

Frequency offset error = 50 ppm = 0.00005

86,400 seconds \* 0.00005 = 4.3 seconds

</dd> <dt>

<span id="Example_2"></span><span id="example_2"></span><span id="EXAMPLE_2"></span>**Example 2**
</dt> <dd>

Suppose the processor TSC clock is controlled by a crystal oscillator and has specified frequency of 3 GHz. This means that the resolution would be 1/3,000,000,000 or about 333 picoseconds. Assume the crystal used to control the processor clock has a frequency tolerance of ±50 ppm and is actually +50 ppm. In spite of the impressive resolution, a time-interval measurement of 24 hours will still be 4.3 seconds too short. (23:59:55.7000000000 measured versus 24:00:00.0000000000 actual).

Seconds in a day = 86400

Frequency offset error = 50 ppm = 0.00005

86,400 seconds \* 0.00005 = 4.3 seconds

This shows that a high resolution TSC clock doesn't necessarily provide more accurate measurements than a lower resolution clock.

</dd> <dt>

<span id="Example_3"></span><span id="example_3"></span><span id="EXAMPLE_3"></span>**Example 3**
</dt> <dd>

Consider using two different computers to measure the same 24 hour time interval. Both computers have an oscillator with a maximum frequency offset of ± 50 ppm. How far apart can the measurement of the same time interval on these two systems be? As in the previous examples, ± 50 ppm yields a maximum error of ± 4.3 seconds after 24 hours. If one system runs 4.3 seconds fast, and the other 4.3 seconds slow, the maximum error after 24 hours could be 8.6 seconds.

Seconds in a day = 86400

Frequency offset error = ±50 ppm = ±0.00005

±(86,400 seconds \* 0.00005) = ±4.3 seconds

Maximum offset between the two systems = 8.6 seconds

In summary, the frequency offset error becomes increasingly important when measuring long time intervals and when comparing measurements between different systems.

The stability of a timer describes whether the tick frequency changes over time, for example as the result of temperatures changes. Quartz crystals used as the tick generators on computers will exhibit small changes in frequency as a function of temperature. The error caused by thermal drift is typically small compared to the frequency offset error for common temperature ranges. However, designers of software for portable equipment or equipment subject to large temperature fluctuations might need to consider this effect.

</dd> </dl>

## Hardware timer info

<dl> <dt>

**TSC Register (x86 and x64)**
</dt> <dd>

All modern Intel and AMD processors contain a TSC register that is a 64-bit register that increases at a high rate, typically equal to the processor clock. The value of this counter can be read through the **RDTSC** or **RDTSCP** machine instructions, providing very low access time and computational cost in the order of tens or hundreds of machine cycles, depending upon the processor.

Although the TSC register seems like an ideal time stamp mechanism, here are circumstances in which it can't function reliably for timekeeping purposes:

-   Not all processors have usable TSC registers, so using the TSC register in software directly creates a portability problem. (Windows will select an alternative time source for [**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) in this case, which avoids the portability problem.)
-   Some processors can vary the frequency of the TSC clock or stop the advancement of the TSC register, which makes the TSC unsuitable for timing purposes on these processors. These processors are said to have non-invariant TSC registers. (Windows will automatically detect this, and select an alternative time source for [**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter)).
-   Even if a virtualization host has a usable TSC, live migration of running virtual machines when the target virtualization host does not have or utilize hardware assisted TSC scaling can result in a change in TSC frequency that is visible to guests. (It is expected that if this type of live migration is possible for a guest, that the hypervisor clears the invariant TSC feature bit in CPUID.)
-   On multi-processor or multi-core systems, some processors and systems are unable to synchronize the clocks on each core to the same value. (Windows will automatically detect this, and select an alternative time source for [**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter)).
-   On some large multi-processor systems, you might not be able to synchronize the processor clocks to the same value even if the processor has an invariant TSC. (Windows will automatically detect this, and select an alternative time source for [**QPC**](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter)).
-   Some processors will execute instructions out of order. This can result in incorrect cycle counts when **RDTSC** is used to time instruction sequences because the **RDTSC** instruction might be executed at a different time than specified in your program. The **RDTSCP** instruction has been introduced on some processors in response to this problem.

Like other timers, the TSC is based on a crystal oscillator whose exact frequency is not known in advance and that has a frequency offset error. Thus before it can be used, it must be calibrated using another timing reference.

During system initialization, Windows checks if the TSC is suitable for timing purposes and performs the necessary frequency calibration and core synchronization.

</dd> <dt>

**PM Clock (x86 and x64)**
</dt> <dd>

The ACPI timer, also known as the PM clock, was added to the system architecture to provide reliable time stamps independently of the processors speed. Because this was the single goal of this timer, it provides a time stamp in a single clock cycle, but it doesn't provide any other functionality.

</dd> <dt>

**HPET Timer (x86 and x64)**
</dt> <dd>

The High Precision Event Timer (HPET) was developed jointly by Intel and Microsoft to meet the timing requirements of multimedia and other time-sensitive applications. Unlike the TSC, which is a per-processor resource, the HPET is a shared, platform-wide resource, though a system may have multiple HPETs. HPET support has been in Windows since Windows Vista, and Windows 7 and Windows 8 Hardware Logo certification requires HPET support in the hardware platform.

</dd> <dt>

**GIT Timer (Arm)**
</dt> <dd>

Arm-based platforms do not have a TSC, HPET, or PM clock as there is on Intel- or AMD-based platforms. Instead, Arm processors provide the Generic Timer (sometimes called the Generic Interval Timer, or GIT) which contains a System Counter register (e.g. CNTVCT_EL0). The Generic Timer System Counter is a fixed-frequency platform-wide time source. It begins at zero at start-up and increases at a high rate. In Armv8.6 or higher, this is defined as exactly 1 GHz, but should be determined by reading the clock frequency register which is set by early boot firmware. For more details, see the chapter "The Generic Timer in AArch64 state" in "Arm Architecture Reference Manual for A-profile architecture" (DDI 0487).

</dd> <dt>

**Cycle Counter (Arm)**
</dt> <dd>

Arm-based platforms provide a Performance Monitors Cycle Counter register (e.g. PMCCNTR_EL0). This counter counts processor clock cycles. It is non-invariant and its units may not be correlated to real time. It is not advised to use this register to obtain timestamps.

</dd> </dl>
