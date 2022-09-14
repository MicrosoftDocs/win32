---
description: The DVDAdm property provides access to the MSDVDAdm object that contains methods and properties for saving application and user information.
ms.assetid: eb73a851-7118-42f3-be99-1cf356d2e37a
title: DVDAdm Property
ms.topic: reference
ms.date: 05/31/2018
---

# DVDAdm Property

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `DVDAdm` property provides access to the [MSDVDAdm](msdvdadm-object.md) object that contains methods and properties for saving application and user information.

``` syntax
        MSWebDVD.DVDAdm
```

## Remarks

This property is read-only with no default value. There is no need to create a separate reference to the **MSDVDAdm** object. To access the methods and properties of the object, use the `DVDAdm` property as shown in the following example.

## Examples


```VB
DVD.DVDAdm.DisableScreenSaver = true
```



 

 



