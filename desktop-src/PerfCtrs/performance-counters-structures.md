---
description: You use the following structures when working with performance data.
ms.assetid: 97118b64-3a2f-49c0-92e7-324df08bdb12
title: Performance Counters Structures
ms.topic: article
ms.date: 08/17/2020
---

# Performance Counters Structures

You use the following structures when working with performance data.

For information about the functions that are available for working with performance counters, see [Performance Counters Functions](performance-counters-functions.md).

## Performance Data Helper (PDH) structures

Consumers that use the [Performance Data Helper (PDH)](using-the-pdh-functions-to-consume-counter-data.md) functions use the following structures:

- [**PDH\_BROWSE\_DLG\_CONFIG**](/windows/win32/api/pdh/ns-pdh-pdh_browse_dlg_config_a)
- [**PDH\_BROWSE\_DLG\_CONFIG\_H**](/windows/win32/api/pdh/ns-pdh-pdh_browse_dlg_config_ha)
- [**PDH\_COUNTER\_INFO**](/windows/desktop/api/Pdh/ns-pdh-pdh_counter_info_a)
- [**PDH\_COUNTER\_PATH\_ELEMENTS**](/windows/desktop/api/Pdh/ns-pdh-pdh_counter_path_elements_a)
- [**PDH\_DATA\_ITEM\_PATH\_ELEMENTS**](/windows/desktop/api/Pdh/ns-pdh-pdh_data_item_path_elements_a)
- [**PDH\_FMT\_COUNTERVALUE**](/windows/desktop/api/Pdh/ns-pdh-pdh_fmt_countervalue)
- [**PDH\_FMT\_COUNTERVALUE\_ITEM**](/windows/desktop/api/Pdh/ns-pdh-pdh_fmt_countervalue_item_a)
- [**PDH\_RAW\_COUNTER**](/windows/desktop/api/Pdh/ns-pdh-pdh_raw_counter)
- [**PDH\_RAW\_COUNTER\_ITEM**](/windows/desktop/api/Pdh/ns-pdh-pdh_raw_counter_item_a)
- [**PDH\_RAW\_LOG\_RECORD**](/windows/desktop/api/Pdh/ns-pdh-pdh_raw_log_record)
- [**PDH\_STATISTICS**](/windows/desktop/api/Pdh/ns-pdh-pdh_statistics)
- [**PDH\_TIME\_INFO**](/windows/desktop/api/Pdh/ns-pdh-pdh_time_info)

## PerfLib V2 Consumer structures

Consumers that use the [PerfLib V2 Consumer](using-the-perflib-functions-to-consume-counter-data.md) functions use the following structures:

- [**PERF\_COUNTER\_DATA**](/windows/desktop/api/Perflib/ns-perflib-perf_counter_data)
- [**PERF\_COUNTER\_HEADER**](/windows/desktop/api/Perflib/ns-perflib-perf_counter_header)
- [**PERF\_COUNTER\_IDENTIFIER**](/windows/desktop/api/Perflib/ns-perflib-perf_counter_identifier)
- [**PERF\_COUNTER\_REG\_INFO**](/windows/desktop/api/Perflib/ns-perflib-perf_counter_reg_info)
- [**PERF\_COUNTERSET\_REG\_INFO**](/windows/desktop/api/Perflib/ns-perflib-perf_counterset_reg_info)
- [**PERF\_DATA\_HEADER**](/windows/desktop/api/Perflib/ns-perflib-perf_data_header)
- [**PERF\_INSTANCE\_HEADER**](/windows/desktop/api/Perflib/ns-perflib-perf_instance_header)
- [**PERF\_MULTI\_COUNTERS**](/windows/desktop/api/Perflib/ns-perflib-perf_multi_counters)
- [**PERF\_MULTI\_INSTANCES**](/windows/desktop/api/Perflib/ns-perflib-perf_multi_instances)
- [**PERF\_STRING\_BUFFER\_HEADER**](/windows/win32/api/perflib/ns-perflib-perf_string_buffer_header)
- [**PERF\_STRING\_COUNTER\_HEADER**](/windows/win32/api/perflib/ns-perflib-perf_string_counter_header)

## PerfLib V2 Provider structures

[V2 performance data providers](providing-counter-data-using-version-2-0.md) use the following structures:

- [**PERF\_COUNTER\_IDENTITY**](/windows/desktop/api/Perflib/ns-perflib-perf_counter_identity)
- [**PERF\_COUNTER\_INFO**](/windows/desktop/api/Perflib/ns-perflib-perf_counter_info)
- [**PERF\_COUNTERSET\_INFO**](/windows/desktop/api/Perflib/ns-perflib-perf_counterset_info)
- [**PERF\_COUNTERSET\_INSTANCE**](/windows/desktop/api/Perflib/ns-perflib-perf_counterset_instance)
- [**PERF\_PROVIDER\_CONTEXT**](/windows/win32/api/perflib/ns-perflib-perf_provider_context)

## Performance DLL structures

[Performance extension DLL providers](providing-counter-data-using-a-performance-dll.md) and [consumers that use the registry functions to consume counter data](using-the-registry-functions-to-consume-counter-data.md) use the following structures:

- [**PERF\_COUNTER\_BLOCK**](/windows/desktop/api/Winperf/ns-winperf-perf_counter_block)
- [**PERF\_COUNTER\_DEFINITION**](/windows/desktop/api/Winperf/ns-winperf-perf_counter_definition)
- [**PERF\_DATA\_BLOCK**](/windows/desktop/api/Winperf/ns-winperf-perf_data_block)
- [**PERF\_INSTANCE\_DEFINITION**](/windows/desktop/api/Winperf/ns-winperf-perf_instance_definition)
- [**PERF\_OBJECT\_TYPE**](/windows/desktop/api/Winperf/ns-winperf-perf_object_type)
