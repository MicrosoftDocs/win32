---
description: The SubpictureStreamsAvailable property retrieves the number of subpicture streams available in the current title.
ms.assetid: 6a6d9d15-2f56-47fc-a7bb-2cf33f384f41
title: SubpictureStreamsAvailable Property
ms.topic: reference
ms.date: 05/31/2018
---

# SubpictureStreamsAvailable Property

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `SubpictureStreamsAvailable` property retrieves the number of subpicture streams available in the current title.

``` syntax
[ iStreams = ] MSWebDVD.SubpictureStreamsAvailable
```

## Return Value

Returns the number of available streams as an Integer.

## Remarks

This property is read-only with no default value. To query each stream for its language attribute, first call this method to get the upper bound.

Stream numbering is zero-based.

 

 



