---
description: The PreferredSubpictureStream property retrieves the preferred subpicture stream for the current viewing session.
ms.assetid: 9c15dc6f-c016-41bf-b03d-e8e5415215ae
title: PreferredSubpictureStream Property
ms.topic: reference
ms.date: 05/31/2018
---

# PreferredSubpictureStream Property

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `PreferredSubpictureStream` property retrieves the preferred subpicture stream for the current viewing session.

``` syntax
[iStream = ] MSWebDVD.PreferredSubpictureStream
```

## Return Value

Returns an Integer value representing the current preferred subpicture stream in the system registry.

## Remarks

The preferred subpicture stream is set with [MSDVDAdm](msdvdadm-object.md) object's [**DefaultSubpictureLCID**](defaultsubpicturelcid-property.md).

 

 



