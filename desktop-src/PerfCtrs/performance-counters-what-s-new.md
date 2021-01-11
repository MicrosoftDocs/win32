---
description: This section describes the new features that were added to Performance Counters for each release.
ms.assetid: 14bdae6c-9dcd-401e-8c43-5391e00cf7e3
title: Whats New (Performance Counters)
ms.topic: article
ms.date: 05/31/2018
---

# What's New with Performance Counters

This section describes the new features that were added to Performance Counters for each release.

## Windows 7 and Windows Server 2008 R2

The [CTRPP](ctrpp.md) tool was changed to improve and simplify code generation. The tool now generates only a header and resource file. If you want to old code generation behavior (not recommended), you can use the new `-legacy` argument.

- You must now specify the new `-o` and `-rc` arguments that specify the name and location of the header and resource file, respectively.
- You can use the optional new `-prefix` argument to specify a string to add to the beginning of global variables and functions defined in the generated header file.
- If you have to update your counters manifest, using the new code generation eliminates the need to merge your previous callback implementation with the new generated code since the callbacks are no longer included in the generated code.

A new `symbol` attribute is available for the following manifest elements:

- [provider](/windows/desktop/PerfCtrs/performance-counters-provider--counters--element)
- [counterSet](/windows/desktop/PerfCtrs/performance-counters-counterset--provider--element)
- [counter](/windows/desktop/PerfCtrs/performance-counters-counter--counterset--element)

The `symbol` attribute is required for [provider](/windows/desktop/PerfCtrs/performance-counters-provider--counters--element) and [counterSet](/windows/desktop/PerfCtrs/performance-counters-counterset--provider--element), and is optional for [counter](/windows/desktop/PerfCtrs/performance-counters-counter--counterset--element). The attribute lets you provide a symbolic name that you can use to reference each element when calling the provider functions (for example, you can use the counter set symbolic name when calling [PerfCreateInstance](/windows/desktop/api/Perflib/nf-perflib-perfcreateinstance)).

## Windows Vista

The Performance Counters architecture for providing counter data was completely changed for this release.

Previously, you used an INI file to define your counter data and you implemented a performance DLL which ran in the consumer's process to provide the data when a consumer requested it. This architecture is deprecated and is not recommended for new code due to significant performance and reliability issues.

The new architecture uses a manifest to define the counter data and runs code in the provider's process to provide the data when a consumer requests it. For additional details, see [Providing Counter Data Using Version 2.0](providing-counter-data-using-version-2-0.md).

The following functions were added for this release:

- [ControlCallback](/windows/desktop/api/Perflib/nc-perflib-perflibrequest)
- [PerfCreateInstance](/windows/desktop/api/Perflib/nf-perflib-perfcreateinstance)
- [PerfDeleteInstance](/windows/desktop/api/Perflib/nf-perflib-perfdeleteinstance)
- [PerfQueryInstance](/windows/desktop/api/Perflib/nf-perflib-perfqueryinstance)
- [PerfSetCounterSetInfo](/windows/desktop/api/Perflib/nf-perflib-perfsetcountersetinfo)
- [PerfSetULongCounterValue](/windows/desktop/api/Perflib/nf-perflib-perfsetulongcountervalue)
- [PerfSetULongLongCounterValue](/windows/desktop/api/Perflib/nf-perflib-perfsetulonglongcountervalue)
- [PerfSetCounterRefValue](/windows/desktop/api/Perflib/nf-perflib-perfsetcounterrefvalue)
- [PerfStartProvider](/windows/desktop/api/Perflib/nf-perflib-perfstartprovider)
- [PerfStopProvider](/windows/desktop/api/Perflib/nf-perflib-perfstopprovider)

The following structures were added for this release:

- [PERF\_COUNTER\_IDENTITY](/windows/desktop/api/Perflib/ns-perflib-perf_counter_identity)
- [PERF\_COUNTER\_INFO](/windows/desktop/api/Perflib/ns-perflib-perf_counter_info)
- [PERF\_COUNTERSET\_INFO](/windows/desktop/api/Perflib/ns-perflib-perf_counterset_info)
- [PERF\_COUNTERSET\_INSTANCE](/windows/desktop/api/Perflib/ns-perflib-perf_counterset_instance)

For a list of the XML elements that you use in your manifest to define your counters, see [Performance Counters Schema](performance-counters-schema.md).

For information on the CTRPP pre-processor tool that parses your manifest and generates the code that you use as the starting point for your provider, see [CTRPP](ctrpp.md).
