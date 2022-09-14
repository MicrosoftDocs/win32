---
description: The WindowlessActivation property initializes the MSWebDVD object at design time for either windowed or windowless mode.
ms.assetid: 290a9459-154a-4ec7-a013-d696e6b27341
title: WindowlessActivation Property
ms.topic: reference
ms.date: 05/31/2018
---

# WindowlessActivation Property

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `WindowlessActivation` property initializes the **MSWebDVD** object at design time for either windowed or windowless mode.

``` syntax
[ bWindowless = ] MSWebDVD.WindowlessActivation
```

## Return Value

Returns whether the object is in windowed mode as a Boolean.

## Remarks

This property is read/write with a default value of true. Therefore, you only need to set this property if you are running the **MSWebDVD** object in a windowed container. When contained in a Web page in Microsoft® Internet Explorer, **MSWebDVD** is always in windowless mode, and you don't need to set this property.

 

 



