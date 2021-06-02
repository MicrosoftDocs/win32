---
description: The Stop method stops playback.
ms.assetid: 'e1ebfacc-4f33-4b4d-8e6c-1d1e1f0a22bd'
title: Stop Method (DirectShow)
ms.topic: article
ms.date: 05/31/2018
---

# Stop Method (DirectShow)

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `Stop` method stops playback.

``` syntax
MSWebDVD.Stop()
```

## Return Value

No return value.

## Remarks

If [**EnableResetOnStop**](enableresetonstop-property.md) is set to true, calling `Stop` puts the DVD Navigator, along with the rest of the filter graph, into a stopped state, which means that the next time the user presses the **Play** button, playback starts at the beginning of the disc. If **EnableResetOnStop** is set to true, playback resumes where it left off when the user issues the next **Play** command.

 

 



