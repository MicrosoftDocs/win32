---
Description: 'This section describes the new features that were added to Performance Counters for each release.'
ms.assetid: '14bdae6c-9dcd-401e-8c43-5391e00cf7e3'
title: 'What's New'
---

# What's New

This section describes the new features that were added to Performance Counters for each release.

## Windows 7 and Windows Server 2008 R2

The following features were added in this release:

-   The [CTRPP](ctrpp.md) usage was changed to improve and simplify code generation. The tool now generates only a header and resource file. If you want to old code generation behavior (not recommended), you can use the new **-legacy** argument.

    You must now specify the new **-o** and **-rc** arguments that specify the name and location of the header and resource file, respectively.

    You can use the optional new **-prefix** argument to specify a string to add to the beginning of global variables and functions defined in the generated header file.

    If you have to update your counters manifest, using the new code generation eliminates the need to merge your previous callback implementation with the new generated code since the callbacks are no longer included in the generated code.

-   Added the **symbol** attribute to the following manifest elements:
    -   [**provider**](https://msdn.microsoft.com/library/windows/desktop/ee781352)
    -   [**counterSet**](https://msdn.microsoft.com/library/windows/desktop/ee781342)
    -   [**counter**](https://msdn.microsoft.com/library/windows/desktop/ee781346)

    The **symbol** attribute is required for [**provider**](https://msdn.microsoft.com/library/windows/desktop/ee781352) and [**counterSet**](https://msdn.microsoft.com/library/windows/desktop/ee781342), and is optional for [**counter**](https://msdn.microsoft.com/library/windows/desktop/ee781346). The attribute lets you provide a symbolic name that you can use to reference each element when calling the provider functions (for example, you can use the counter set symbolic name when calling [**PerfCreateInstance**](perfcreateinstance.md)).

## Windows Vista

The Performance Counters architecture for providing counter data was completely changed for this release. Previously, you used an INI file to define your counter data and you implemented a performance DLL to provide the data when a consumer requested it. The new architecture uses a manifest to define the counter data and injects a thread into your process that collects the counter data directly from your application; all your application does is define and set the counter values and the system handles providing the values to the consumer. For complete details, see [Providing Counter Data Using Version 2.0](providing-counter-data-using-version-2-0.md).

Note that you can still use a performance DLL to provide counter data in Windows Vista but you are encouraged to use the new architecture instead.

The following functions were added for this release:

-   [*ControlCallback*](controlcallback-perflibv2.md)
-   [**PerfCreateInstance**](perfcreateinstance.md)
-   [**PerfDeleteInstance**](perfdeleteinstance.md)
-   [**PerfQueryInstance**](perfqueryinstance.md)
-   [**PerfSetCounterSetInfo**](perfsetcountersetinfo.md)
-   [**PerfSetULongCounterValue**](perfsetulongcountervalue.md)
-   [**PerfSetULongLongCounterValue**](perfsetulonglongcountervalue.md)
-   [**PerfSetCounterRefValue**](perfsetcounterrefvalue.md)
-   [**PerfStartProvider**](perfstartprovider.md)
-   [**PerfStopProvider**](perfstopprovider.md)

The following structures were added for this release:

-   [**PERF\_COUNTER\_IDENTITY**](perf-counter-identity.md)
-   [**PERF\_COUNTER\_INFO**](perf-counter-info.md)
-   [**PERF\_COUNTERSET\_INFO**](perf-counterset-info.md)
-   [**PERF\_COUNTERSET\_INSTANCE**](perf-counterset-instance.md)

For a list of the XML elements that you use in your manifest to define your counters, see [Performance Counters Schema](performance-counters-schema.md).

For information on the CTRPP pre-processor tool that parses your manifest and generates the code that you use as the starting point for your provider, see [CTRPP](ctrpp.md).

 

 



