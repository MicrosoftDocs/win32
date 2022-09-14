---
description: Volume Envelope Effect
ms.assetid: 17b6d842-e79c-49b0-baa4-1535b4a2c6ae
title: Volume Envelope Effect
ms.topic: article
ms.date: 05/31/2018
---

# Volume Envelope Effect

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The Volume Envelope effect sets the volume on an audio stream.

Class ID (CLSID): {036A9790-C153-11D2-9EF7-006008039E37}

CLSID Variable Name: CLSID\_AudMixer

Properties



| Property | Type   | Default | Description                                                                                                           |
|----------|--------|---------|-----------------------------------------------------------------------------------------------------------------------|
| Vol      | double | 1.0     | Volume, as a percentage of the authored volume. You can produce audio fades by varying this property value over time. |



 

## Remarks

Each object in a timeline can have at most one volume envelope effect. In a composition or a group, the volume envelope is applied first, before any other audio effects, regardless of its priority. In a source or a track, the volume effect is applied according to its priority.

 

 



