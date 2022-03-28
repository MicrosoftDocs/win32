---
title: Counters, queries, and predication
description: Stream output and UAV counters operate in Direct3D 12 in a similar method to Direct3D 11, although now memory for the counters must be allocated by the app, the driver does not do it.
ms.assetid: 8BDDAFEF-57D4-4EF5-BB0C-6C96AF557A45
ms.topic: article
ms.date: 05/31/2018
---

# Counters, queries, and predication

This topic covers stream-output counters, UAV counters, queries, and predication.

Stream output and UAV counters operate in Direct3D 12 in a similar method to Direct3D 11, although now memory for the counters must be allocated by the app, the driver does not do it. Queries in Direct3D 12 are more different from those in Direct3D 11, with the addition of fences and other processes that remove the need for some query types.

## In this section



| Topic                                                           | Description                                                                                                                                                                                  |
|-----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Stream Output Counters](stream-output-counters.md)<br/> | Stream output is the ability of the GPU to write vertices to a buffer. The stream output counters monitor progress.<br/>                                                               |
| [UAV Counters](uav-counters.md)<br/>                     | UAV counters can be used to associate a 32-bit atomic counter with an unordered-access-view (UAV).<br/>                                                                                |
| [Queries](queries.md)<br/>                               | In Direct3D 12, queries are grouped into arrays of queries called a query heap. A query heap has a type which defines the valid types of queries that can be used with that heap.<br/> |



 

## Related topics

<dl> <dt>

[Performance Measurement](performance-measurement.md)
</dt> </dl>

 

 





