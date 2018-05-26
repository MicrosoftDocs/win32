---
Description: With Version 2.0, Performance Counters changed the architecture to simplify the process for providing counter data to consumers.
ms.assetid: 37f75b15-3f52-4259-a6d9-5a1a14f88379
title: Providing Counter Data Using Version 2.0
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Providing Counter Data Using Version 2.0

With Version 2.0, Performance Counters changed the architecture to simplify the process for providing counter data to consumers. The new architecture uses a manifest to define the counter data and injects a thread into your process that collects the counter data directly from your application; all your application does is define and set the counter values and the system handles providing the values to the consumer.

**Steps to creating a provider**

1.  Write a manifest that defines the counter data that your provider will provide. For complete details on writing the manifest, see [Performance Counters Schema](performance-counters-schema.md).
2.  Use the tool to generate the template code that you include in your provider. The template code includes the structures that define the counter sets, the [**CounterInitialize**](counterinitialize.md) and [**CounterCleanup**](countercleanup.md) functions, and the resource strings.

    **Windows Vista:** The [**CounterInitialize**](counterinitialize.md) and [**CounterCleanup**](countercleanup.md) functions are named **PerfAutoInitialize** and **PerfAutoCleanup**, respectively. The generated code also includes the [*ControlCallback*](/windows/win32/Perflib/nc-perflib-perflibrequest?branch=master) function if requested.

    Your provider must call the [**CounterInitialize**](counterinitialize.md) and [**CounterCleanup**](countercleanup.md) functions. The **CounterInitialize** calls the [**PerfStartProvider**](/windows/win32/Perflib/nf-perflib-perfstartprovider?branch=master) function to register the provider and also calls the [**PerfSetCounterSetInfo**](/windows/win32/Perflib/nf-perflib-perfsetcountersetinfo?branch=master) function to initialize the counter set. The **CounterCleanup** calls the [**PerfStopProvider**](/windows/win32/Perflib/nf-perflib-perfstopprovider?branch=master) function to remove the provider's registration.

3.  Include the template code from the previous step in your project and complete your provider.

    To complete the provider, you need to call the [**PerfCreateInstance**](/windows/win32/Perflib/nf-perflib-perfcreateinstance?branch=master) function for each instance of the counter set that you provide.

    To set the counter values, call one of the following functions:

    -   [**PerfSetULongCounterValue**](/windows/win32/Perflib/nf-perflib-perfsetulongcountervalue?branch=master)
    -   [**PerfSetULongLongCounterValue**](/windows/win32/Perflib/nf-perflib-perfsetulonglongcountervalue?branch=master)
    -   [**PerfSetCounterRefValue**](/windows/win32/Perflib/nf-perflib-perfsetcounterrefvalue?branch=master)

    The benefit of using [**PerfSetCounterRefValue**](/windows/win32/Perflib/nf-perflib-perfsetcounterrefvalue?branch=master) is that you do not have to make a function call to set or update the counter value, you simply update your local counter variable (the variable to which the reference points) and Performance Counters uses the pointer to access the counter value.

    If you do not use [**PerfSetCounterRefValue**](/windows/win32/Perflib/nf-perflib-perfsetcounterrefvalue?branch=master), you can use the following functions to increment or decrement the counter value:

    -   [**PerfDecrementULongCounterValue**](/windows/win32/Perflib/nf-perflib-perfdecrementulongcountervalue?branch=master)
    -   [**PerfDecrementULongLongCounterValue**](/windows/win32/Perflib/nf-perflib-perfdecrementulonglongcountervalue?branch=master)
    -   [**PerfIncrementULongCounterValue**](/windows/win32/Perflib/nf-perflib-perfincrementulongcountervalue?branch=master)
    -   [**PerfIncrementULongLongCounterValue**](/windows/win32/Perflib/nf-perflib-perfincrementulonglongcountervalue?branch=master)

    Before the provider exits, it must call the [**PerfDeleteInstance**](/windows/win32/Perflib/nf-perflib-perfdeleteinstance?branch=master) for each counter set instance that it created.

    If you specified the **callback** attribute in the [**provider**](https://msdn.microsoft.com/library/windows/desktop/ee781352) element in your manifest or used the **-NotificationCallback** argument when calling [CTRPP](ctrpp.md), you must implement the [*ControlCallback*](/windows/win32/Perflib/nc-perflib-perflibrequest?branch=master) callback function. You pass the callback function to [**CounterInitialize**](counterinitialize.md).

    If you used the **-MemoryRoutines** when calling [CTRPP](ctrpp.md), you must implement the [*AllocateMemory*](/windows/win32/Perflib/nc-perflib-perf_mem_alloc?branch=master) and [*FreeMemory*](/windows/win32/Perflib/nc-perflib-perf_mem_free?branch=master) callback functions. You pass the callback functions to [**CounterInitialize**](counterinitialize.md).

4.  Use the LodCtr tool to write the name of the binary file that contains the localized resource strings and resource IDs to the registry. For details on using LodCtr, see [Performance Counters Schema](performance-counters-schema.md).

 

 



