---
Description: 'With Version 2.0, Performance Counters changed the architecture to simplify the process for providing counter data to consumers.'
ms.assetid: '37f75b15-3f52-4259-a6d9-5a1a14f88379'
title: 'Providing Counter Data Using Version 2.0'
---

# Providing Counter Data Using Version 2.0

With Version 2.0, Performance Counters changed the architecture to simplify the process for providing counter data to consumers. The new architecture uses a manifest to define the counter data and injects a thread into your process that collects the counter data directly from your application; all your application does is define and set the counter values and the system handles providing the values to the consumer.

**Steps to creating a provider**

1.  Write a manifest that defines the counter data that your provider will provide. For complete details on writing the manifest, see [Performance Counters Schema](performance-counters-schema.md).
2.  Use the tool to generate the template code that you include in your provider. The template code includes the structures that define the counter sets, the [**CounterInitialize**](counterinitialize.md) and [**CounterCleanup**](countercleanup.md) functions, and the resource strings.

    **Windows Vista:** The [**CounterInitialize**](counterinitialize.md) and [**CounterCleanup**](countercleanup.md) functions are named **PerfAutoInitialize** and **PerfAutoCleanup**, respectively. The generated code also includes the [*ControlCallback*](controlcallback-perflibv2.md) function if requested.

    Your provider must call the [**CounterInitialize**](counterinitialize.md) and [**CounterCleanup**](countercleanup.md) functions. The **CounterInitialize** calls the [**PerfStartProvider**](perfstartprovider.md) function to register the provider and also calls the [**PerfSetCounterSetInfo**](perfsetcountersetinfo.md) function to initialize the counter set. The **CounterCleanup** calls the [**PerfStopProvider**](perfstopprovider.md) function to remove the provider's registration.

3.  Include the template code from the previous step in your project and complete your provider.

    To complete the provider, you need to call the [**PerfCreateInstance**](perfcreateinstance.md) function for each instance of the counter set that you provide.

    To set the counter values, call one of the following functions:

    -   [**PerfSetULongCounterValue**](perfsetulongcountervalue.md)
    -   [**PerfSetULongLongCounterValue**](perfsetulonglongcountervalue.md)
    -   [**PerfSetCounterRefValue**](perfsetcounterrefvalue.md)

    The benefit of using [**PerfSetCounterRefValue**](perfsetcounterrefvalue.md) is that you do not have to make a function call to set or update the counter value, you simply update your local counter variable (the variable to which the reference points) and Performance Counters uses the pointer to access the counter value.

    If you do not use [**PerfSetCounterRefValue**](perfsetcounterrefvalue.md), you can use the following functions to increment or decrement the counter value:

    -   [**PerfDecrementULongCounterValue**](perfdecrementulongcountervalue.md)
    -   [**PerfDecrementULongLongCounterValue**](perfdecrementulonglongcountervalue.md)
    -   [**PerfIncrementULongCounterValue**](perfincrementulongcountervalue.md)
    -   [**PerfIncrementULongLongCounterValue**](perfincrementulonglongcountervalue.md)

    Before the provider exits, it must call the [**PerfDeleteInstance**](perfdeleteinstance.md) for each counter set instance that it created.

    If you specified the **callback** attribute in the [**provider**](https://msdn.microsoft.com/library/windows/desktop/ee781352) element in your manifest or used the **-NotificationCallback** argument when calling [CTRPP](ctrpp.md), you must implement the [*ControlCallback*](controlcallback-perflibv2.md) callback function. You pass the callback function to [**CounterInitialize**](counterinitialize.md).

    If you used the **-MemoryRoutines** when calling [CTRPP](ctrpp.md), you must implement the [*AllocateMemory*](allocatememory.md) and [*FreeMemory*](freememory.md) callback functions. You pass the callback functions to [**CounterInitialize**](counterinitialize.md).

4.  Use the LodCtr tool to write the name of the binary file that contains the localized resource strings and resource IDs to the registry. For details on using LodCtr, see [Performance Counters Schema](performance-counters-schema.md).

 

 



