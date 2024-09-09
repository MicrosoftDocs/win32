---
title: Timing (Direct3D 12 Graphics)
description: This section covers querying timestamps, and calibrating the GPU and CPU timestamp counters.
ms.assetid: CC1E5BAB-4363-43FF-BF5B-6C9AEBECD6CA
ms.topic: article
ms.date: 05/31/2018
---

# Timing (Direct3D 12 Graphics)

This section covers querying timestamps, and calibrating the GPU and CPU timestamp counters.

## Timestamp frequency

Your application can query the GPU timestamp frequency on a per-command queue basis (refer to the [**ID3D12CommandQueue::GetTimestampFrequency**](/windows/win32/api/d3d12/nf-d3d12-id3d12commandqueue-gettimestampfrequency) method).

The returned frequency is measured in Hz (ticks/sec). If the specified command queue doesn't support timestamps (see the table in the [Queries](queries.md) section), then this API fails (and returns **E_FAIL**). [**D3D12_COMMAND_LIST_TYPE_DIRECT**](/windows/win32/api/d3d12/ne-d3d12-d3d12_command_list_type) and [**D3D12_COMMAND_LIST_TYPE_COMPUTE**](/windows/win32/api/d3d12/ne-d3d12-d3d12_command_list_type) always support timestamps. [**D3D12_COMMAND_LIST_TYPE_COPY**](/windows/win32/api/d3d12/ne-d3d12-d3d12_command_list_type) optionally supports timestamps if the [**D3D12_FEATURE_DATA_D3D12_OPTIONS3::CopyQueueTimestampQueriesSupported**](/windows/win32/api/d3d12/ns-d3d12-d3d12_feature_data_d3d12_options3) member is **TRUE**.

## Timestamp calibration

D3D12 enables applications to correlate results obtained from timestamp queries with results obtained from calling `QueryPerformanceCounter`. This is enabled by the call [**ID3D12CommandQueue::GetClockCalibration**](/windows/desktop/api/d3d12/nf-d3d12-id3d12commandqueue-getclockcalibration).

A timestamp is sampled by the GPU at the moment that the GPU is finished with all of the preceding workload. It's the same behavior adopted by Direct3D 11 (see [D3D11_QUERY_TIMESTAMP](https://microsoft.github.io/DirectX-Specs/d3d/archive/D3D11_3_FunctionalSpec.htm#20.4.3%20D3D11_QUERY_TIMESTAMP) in the Direct3D 11.3 Functional Specification on GitHub). That means that timestamp queries are a bottom-of-pipe (BOP) operation in Direct3D 12.

[**GetClockCalibration**](/windows/desktop/api/d3d12/nf-d3d12-id3d12commandqueue-getclockcalibration) samples the GPU timestamp counter for a given command queue and samples the CPU counter via `QueryPerformanceCounter` at nearly the same time. Again this API fails (returning E\_FAIL) if the specified command queue does not support timestamps (see the table in the [Queries](queries.md) topic).

Note that GPU and CPU timestamp counters are not necessarily directly related to the clock speed of these processors, but instead work from timestamp ticks.

## Timestamp queries

You can obtain timestamps as part of a command list (rather than a CPU-side call on a command queue) via timestamp queries. (See [Queries](queries.md) for more information about queries in general). 

All timestamp queries use the type [**D3D12_QUERY_TYPE_TIMESTAMP**](/windows/win32/api/d3d12/ne-d3d12-d3d12_query_type) for the actual query. However, due to hardware limitations, [**D3D12_COMMAND_LIST_TYPE_DIRECT**](/windows/win32/api/d3d12/ne-d3d12-d3d12_command_list_type) and [**D3D12_COMMAND_LIST_TYPE_COMPUTE**](/windows/win32/api/d3d12/ne-d3d12-d3d12_command_list_type) use a different [**D3D12_QUERY_HEAP_TYPE**](/windows/win32/api/d3d12/ne-d3d12-d3d12_query_heap_type) from the one that [**D3D12_COMMAND_LIST_TYPE_COPY**](/windows/win32/api/d3d12/ne-d3d12-d3d12_command_list_type) uses.

Direct and compute queues use [**D3D12_QUERY_HEAP_TYPE_TIMESTAMP**](/windows/win32/api/d3d12/ne-d3d12-d3d12_query_heap_type).

Copy queues use [**D3D12_QUERY_HEAP_TYPE_COPY_QUEUE_TIMESTAMP**](/windows/win32/api/d3d12/ne-d3d12-d3d12_query_heap_type).

Copy queue queries are supported only if the [**D3D12_FEATURE_DATA_D3D12_OPTIONS3::CopyQueueTimestampQueriesSupported**](/windows/win32/api/d3d12/ns-d3d12-d3d12_feature_data_d3d12_options3) member is **TRUE**.

Timestamp queries, once resolved via [**ID3D12GraphicsCommandList::ResolveQueryData**](/windows/win32/api/d3d12/nf-d3d12-id3d12graphicscommandlist-resolvequerydata), are a 
**UINT64** that represents ticks, as is returned by [**ID3D12CommandQueue::GetClockCalibration**](/windows/win32/api/d3d12/nf-d3d12-id3d12commandqueue-getclockcalibration), and as such it must be divided by the queue frequency to get the length in seconds.

> [!IMPORTANT]
> For accuracy, use floating-point arithmetic when calculating second or millisecond intervals of timestamps. For example, use `queriedTicks / (double)Frequency` instead of `queriedTicks / Frequency`.

## Related topics

<dl> <dt>

[Counters and Queries](counters-and-queries.md)
</dt> <dt>

[**ID3D12Device::SetStablePowerState**](/windows/desktop/api/d3d12/nf-d3d12-id3d12device-setstablepowerstate)
</dt> <dt>

[**ID3D12Object::SetName**](/windows/desktop/api/d3d12/nf-d3d12-id3d12object-setname)
</dt> <dt>

[**ID3DUserDefinedAnnotation**](/windows/desktop/api/d3d11_1/nn-d3d11_1-id3duserdefinedannotation)
</dt> <dt>

[Performance Measurement](performance-measurement.md)
</dt> </dl>
