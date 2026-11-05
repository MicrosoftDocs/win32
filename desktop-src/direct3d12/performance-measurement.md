---
title: Counters, Queries and Performance Measurement
description: The following sections describe features for use in performance testing and improvement, such as queries, counters, timing, and predication.
ms.assetid: C7AEF1A0-36FB-4026-9CCF-ED0206961A58
ms.topic: reference
ms.date: 05/31/2018
---

# Counters, Queries and Performance Measurement

The following sections describe features for use in performance testing and improvement, such as queries, counters, timing, and predication.

> [!TIP]
> Before implementing custom timestamp queries, consider using [PIX for Windows](https://devblogs.microsoft.com/pix/) for GPU profiling. PIX provides timing captures, GPU occupancy visualization, and per-draw-call cost analysis without requiring any code changes. For automated regression testing, the PIX programmatic capture API allows integration into CI pipelines.

## In this section



| Topic                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                        |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Stream-Output Counters, UAV Counters, Queries, and Predication](counters-and-queries.md)<br/> | Stream output and UAV counters operate in Direct3D 12 in a similar method to Direct3D 11, although now memory for the counters must be allocated by the app, the driver does not do it. Queries in Direct3D 12 are more different from those in Direct3D 11, with the addition of fences and other processes that remove the need for some query types.<br/> |
| [Timing](timing.md)<br/>                                                                       | This section covers querying timestamps, and calibrating the GPU and CPU timestamp counters.<br/>                                                                                                                                                                                                                                                            |
| [Predication](predication.md)<br/>                                                             | Predication is a feature that enables the GPU rather than the CPU to determine to not draw, copy or dispatch an object.<br/>                                                                                                                                                                                                                                 |



 

## Related topics

<dl> <dt>

[Direct3D 12 Programming Guide](directx-12-programming-guide.md)
</dt> </dl>

 

 





