---
Description: You use the following structures when working with performance data.
ms.assetid: 97118b64-3a2f-49c0-92e7-324df08bdb12
title: Performance Counters Structures
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Performance Counters Structures

You use the following structures when working with performance data.

## Consumer structures

Consumers that use the Performance Data Helper functions that consume both version 1 and version 2 performance counter data use the following structures.

-   [**PDH\_BROWSE\_DLG\_CONFIG**](/windows/win32/Pdh/ns-pdh-_browsedlgconfig_a?branch=master)
-   [**PDH\_BROWSE\_DLG\_CONFIG\_H**](/windows/win32/Pdh/ns-pdh-_browsedlgconfig_ha?branch=master)
-   [**PDH\_COUNTER\_INFO**](/windows/win32/Pdh/ns-pdh-_pdh_counter_info_a?branch=master)
-   [**PDH\_COUNTER\_PATH\_ELEMENTS**](/windows/win32/Pdh/ns-pdh-_pdh_counter_path_elements_a?branch=master)
-   [**PDH\_DATA\_ITEM\_PATH\_ELEMENTS**](/windows/win32/Pdh/ns-pdh-_pdh_data_item_path_elements_a?branch=master)
-   [**PDH\_FMT\_COUNTERVALUE**](/windows/win32/Pdh/ns-pdh-_pdh_fmt_countervalue?branch=master)
-   [**PDH\_FMT\_COUNTERVALUE\_ITEM**](/windows/win32/Pdh/ns-pdh-_pdh_fmt_countervalue_item_a?branch=master)
-   [**PDH\_RAW\_COUNTER**](/windows/win32/Pdh/ns-pdh-_pdh_raw_counter?branch=master)
-   [**PDH\_RAW\_COUNTER\_ITEM**](/windows/win32/Pdh/ns-pdh-_pdh_raw_counter_item_a?branch=master)
-   [**PDH\_RAW\_LOG\_RECORD**](/windows/win32/Pdh/ns-pdh-_pdh_raw_log_record?branch=master)
-   [**PDH\_STATISTICS**](/windows/win32/Pdh/ns-pdh-_pdh_statistics?branch=master)
-   [**PDH\_TIME\_INFO**](/windows/win32/Pdh/ns-pdh-_pdh_time_info?branch=master)

Consumers that use the nine low-level functions that can consume version 2 performance counter data use the following structures.

-   [**PERF\_COUNTER\_DATA**](/windows/win32/Perflib/ns-perflib-_perf_counter_data?branch=master)
-   [**PERF\_COUNTER\_HEADER**](/windows/win32/Perflib/ns-perflib-_perf_counter_header?branch=master)
-   [**PERF\_COUNTER\_IDENTIFIER**](/windows/win32/Perflib/ns-perflib-_perf_counter_identifier?branch=master)
-   [**PERF\_COUNTER\_REG\_INFO**](/windows/win32/Perflib/ns-perflib-_perf_counter_reg_info?branch=master)
-   [**PERF\_COUNTERSET\_REG\_INFO**](/windows/win32/Perflib/ns-perflib-_perf_counterset_reg_info?branch=master)
-   [**PERF\_DATA\_HEADER**](/windows/win32/Perflib/ns-perflib-_perf_data_header?branch=master)
-   [**PERF\_INSTANCE\_HEADER**](/windows/win32/Perflib/ns-perflib-_perf_instance_header?branch=master)
-   [**PERF\_MULTI\_COUNTERS**](/windows/win32/Perflib/ns-perflib-_perf_multi_counters?branch=master)
-   [**PERF\_MULTI\_INSTANCES**](/windows/win32/Perflib/ns-perflib-_perf_multi_instances?branch=master)
-   [**PERF\_STRING\_BUFFER\_HEADER**](/windows/win32/Perflib/ns-perflib-_string_buffer_header?branch=master)
-   [**PERF\_STRING\_COUNTER\_HEADER**](/windows/win32/Perflib/ns-perflib-_string_counter_header?branch=master)

For information about the functions that are available for working with performance counters, see [Performance Counters Functions](performance-counters-functions.md).

## Provider structures

Performance providers use the following structures.

-   [**PERF\_COUNTER\_IDENTITY**](/windows/win32/Perflib/ns-perflib-_perf_counter_identity?branch=master)
-   [**PERF\_COUNTER\_INFO**](/windows/win32/Perflib/ns-perflib-_perf_counter_info?branch=master)
-   [**PERF\_COUNTERSET\_INFO**](/windows/win32/Perflib/ns-perflib-_perf_counterset_info?branch=master)
-   [**PERF\_COUNTERSET\_INSTANCE**](/windows/win32/Perflib/ns-perflib-_perf_counterset_instance?branch=master)
-   [**PERF\_PROVIDER\_CONTEXT**](/windows/win32/Perflib/ns-perflib-_provider_context?branch=master)

Performance extension DLL providers and consumers that use the registry functions to consume counter data use the following structures.

-   [**PERF\_COUNTER\_BLOCK**](/windows/win32/Winperf/ns-winperf-_perf_counter_block?branch=master)
-   [**PERF\_COUNTER\_DEFINITION**](/windows/win32/Winperf/ns-winperf-_perf_counter_definition?branch=master)
-   [**PERF\_DATA\_BLOCK**](/windows/win32/Winperf/ns-winperf-_perf_data_block?branch=master)
-   [**PERF\_INSTANCE\_DEFINITION**](/windows/win32/Winperf/ns-winperf-_perf_instance_definition?branch=master)
-   [**PERF\_OBJECT\_TYPE**](/windows/win32/Winperf/ns-winperf-_perf_object_type?branch=master)

 

 



