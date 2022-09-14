---
description: With Version 2.0, Performance Counters changed the architecture to simplify the process for providing counter data to consumers.
ms.assetid: 37f75b15-3f52-4259-a6d9-5a1a14f88379
title: Providing Counter Data Using Version 2.0
ms.topic: article
ms.date: 08/17/2020
---

# Providing Counter Data Using Version 2.0

Modern performance data providers use a manifest to define the counter data and use performance counter provider APIs to manage data within the context of the provider. Providers implemented using a manifest and performance counter provider APIs are often called **V2 providers**. Windows supports user-mode V2 providers on Windows Vista or later and kernel-mode V2 providers on Windows 7 or later.

This page describes user-mode V2 providers. For information about kernel-mode V2 providers, see [Kernel Mode Performance Monitoring](/windows-hardware/drivers/devtest/kernel-mode-performance-monitoring).

At runtime, V2 providers work as follows:

- The provider process registers itself with the Windows Performance Counter system by calling PerfStartProvider and PerfSetCounterSetInfo. The provider optionally provides a callback function that will be notified about consumer requests.
- The provider process adds or removes instances as appropriate using PerfCreateInstance and PerfDeleteInstance. The provider updates counter values when they change using PerfSet*** APIs.
- A consumer makes a request for data from a counterset. The system verifies that the caller has permissions to collect the data. The system then uses a worker thread running in the provider process to handle the request, invoking the provider's callback function if appropriate. The worker thread copies the collected data into a system-managed buffer, and the system then returns the data to the consumer.

## Steps to creating a provider

1. Write a manifest that defines the counter data that your provider will provide. For details on writing the manifest, see [Performance Counters Schema](performance-counters-schema.md).
2. Use [CTRPP](ctrpp.md) to generate the template code that you include in your provider. The template code includes the structures that define the counter sets, the [**CounterInitialize**](counterinitialize.md) and [**CounterCleanup**](countercleanup.md) functions, and the resource strings.

   Your provider must call the [**CounterInitialize**](counterinitialize.md) and [**CounterCleanup**](countercleanup.md) functions. The **CounterInitialize** calls the [**PerfStartProvider**](/windows/desktop/api/Perflib/nf-perflib-perfstartprovider) function to register the provider and also calls the [**PerfSetCounterSetInfo**](/windows/desktop/api/Perflib/nf-perflib-perfsetcountersetinfo) function to initialize the counter set. The **CounterCleanup** calls the [**PerfStopProvider**](/windows/desktop/api/Perflib/nf-perflib-perfstopprovider) function to remove the provider's registration.

3. Include the template code from the previous step in your project and complete your provider.

   To complete the provider, you need to call the [**PerfCreateInstance**](/windows/desktop/api/Perflib/nf-perflib-perfcreateinstance) function for each instance of the counter set that you provide.

   To set the counter values, call one of the following functions:

   - [**PerfSetULongCounterValue**](/windows/desktop/api/Perflib/nf-perflib-perfsetulongcountervalue)
   - [**PerfSetULongLongCounterValue**](/windows/desktop/api/Perflib/nf-perflib-perfsetulonglongcountervalue)
   - [**PerfSetCounterRefValue**](/windows/desktop/api/Perflib/nf-perflib-perfsetcounterrefvalue)

   The benefit of using [**PerfSetCounterRefValue**](/windows/desktop/api/Perflib/nf-perflib-perfsetcounterrefvalue) is that you do not have to make a function call to set or update the counter value, you simply update your local counter variable (the variable to which the reference points) and Performance Counters uses the pointer to access the counter value.

   If you do not use [**PerfSetCounterRefValue**](/windows/desktop/api/Perflib/nf-perflib-perfsetcounterrefvalue), you can use the following functions to increment or decrement the counter value:

   - [**PerfDecrementULongCounterValue**](/windows/desktop/api/Perflib/nf-perflib-perfdecrementulongcountervalue)
   - [**PerfDecrementULongLongCounterValue**](/windows/desktop/api/Perflib/nf-perflib-perfdecrementulonglongcountervalue)
   - [**PerfIncrementULongCounterValue**](/windows/desktop/api/Perflib/nf-perflib-perfincrementulongcountervalue)
   - [**PerfIncrementULongLongCounterValue**](/windows/desktop/api/Perflib/nf-perflib-perfincrementulonglongcountervalue)

   Before the provider exits, it must call the [**PerfDeleteInstance**](/windows/desktop/api/Perflib/nf-perflib-perfdeleteinstance) for each counter set instance that it created.

   If you specified the **callback** attribute in the [**provider**](/windows/desktop/PerfCtrs/performance-counters-provider--counters--element) element in your manifest or used the **-NotificationCallback** argument when calling [CTRPP](ctrpp.md), you must implement the [*ControlCallback*](/windows/desktop/api/Perflib/nc-perflib-perflibrequest) callback function. You pass the callback function to [**CounterInitialize**](counterinitialize.md).

   If you used the **-MemoryRoutines** when calling [CTRPP](ctrpp.md), you must implement the [*AllocateMemory*](/windows/desktop/api/Perflib/nc-perflib-perf_mem_alloc) and [*FreeMemory*](/windows/desktop/api/Perflib/nc-perflib-perf_mem_free) callback functions. You pass the callback functions to [**CounterInitialize**](counterinitialize.md).

4. When installing your provider, use the LodCtr tool to write the name of the binary file that contains the localized resource strings and resource IDs to the registry. For details on using LodCtr, see [Performance Counters Schema](performance-counters-schema.md).

5. When uninstalling your provider, use the UnlodCtr tool to remove your provider's information from the registry.
