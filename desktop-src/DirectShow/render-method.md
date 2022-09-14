---
description: The Render method initializes the DVD filter graph.
ms.assetid: 910f1e3f-b3bb-498b-93da-3a974a3117e8
title: Render Method
ms.topic: reference
ms.date: 05/31/2018
---

# Render Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `Render` method initializes the DVD filter graph.

``` syntax
MSWebDVD.Render(iRender = 0)
```

## Parameters

<dl> <dt>

<span id="iRender"></span><span id="irender"></span><span id="IRENDER"></span>*iRender*
</dt> <dd>

Specifies an integer value indicating whether the filter graph will be destroyed and rebuilt.



| Value | Description                                                                                         |
|-------|-----------------------------------------------------------------------------------------------------|
| 0     | The filter graph will not be destroyed and rebuilt if it already exists. This is the default value. |
| 1     | The filter graph will be destroyed and rebuilt if it already exists.                                |



 

</dd> </dl>

## Return Value

No return value.

## Remarks

The `Render` method enables the **MSWebDVD** object to fully initialize the underlying DirectShow filter graph on startup. This eliminates the slight delay that otherwise occurs when the user issues the first command to play a disc or show a menu. There is no case in which `Render` needs to be called before calling any other method. For example, if the application calls [**PlayTitle**](playtitle-method.md) before the filter graph has been initialized, the **MSWebDVD** object calls `Render` automatically before attempting to play the disc.

 

 



