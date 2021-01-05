---
description: The GetGPRM method retrieves the specified general parameter register.
ms.assetid: 66afd2a5-6aa1-4280-93cf-dd3cfed2499d
title: GetGPRM Method
ms.topic: reference
ms.date: 05/31/2018
---

# GetGPRM Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `GetGPRM` method retrieves the specified general parameter register.

``` syntax
[ iGPRM = ] MSWebDVD.GetGPRM(iIndex)
```

## Parameters

<dl> <dt>

<span id="iIndex"></span><span id="iindex"></span><span id="IINDEX"></span>*iIndex*
</dt> <dd>

Specifies the register to retrieve as an Integer. The value must range from 0 through 15.

</dd> </dl>

## Return Value

Returns an integer value representing the specified register.

## Remarks

This method is not required for any DVD navigation or playback functionality using the **MSWebDVD** object. It is provided for those with a thorough understanding of the DVD specification who want to implement advanced features. GPRMs can be used to hold any values, so they can be freely set and read. But since GPRMs are used to store disc commands as well, changing their values using [**SetGPRM**](setgprm-method.md) can result in unpredictable behavior.

## See also

<dl> <dt>

[**SetGPRM**](setgprm-method.md)
</dt> </dl>

 

 



