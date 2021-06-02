---
description: The DVDAdm.GetParentalLevel method retrieves the parental level that was last saved to the registry.
ms.assetid: 2aadcf41-2c65-4f3a-8ce8-0fc9aa580ad9
title: GetParentalLevel Method
ms.topic: reference
ms.date: 05/31/2018
---

# GetParentalLevel Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `DVDAdm.GetParentalLevel` method retrieves the parental level that was last saved to the registry.

``` syntax
[ iParentalLevel = ] DVD.DVDAdm.GetParentalLevel()
```

## Return Value

Returns an Integer from 1 through 8 indicating the default parental level.

## Remarks

The parental level this method retrieves is not necessarily the same level currently stored in the MSWebDVD control; to get the level currently stored in the control, call the [**GetPlayerParentalLevel**](getplayerparentallevel-method.md) method. A value of -1 indicates that parental management is disabled.

## See also

<dl> <dt>

[MSDVDAdm Object](msdvdadm-object.md)
</dt> </dl>

 

 



