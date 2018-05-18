---
Description: 'The Stop method stops playback.'
ms.assetid: 'ede19f02-6eda-42da-a108-06d78dc2e8a9'
title: Stop Method
---

# Stop Method

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

 

 



