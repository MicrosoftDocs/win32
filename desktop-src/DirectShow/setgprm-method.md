---
description: The SetGPRM method sets the specified general parameter register to the specified value.
ms.assetid: ded28f2a-5e40-4f76-9ed4-de10296529e1
title: SetGPRM Method
ms.topic: reference
ms.date: 05/31/2018
---

# SetGPRM Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `SetGPRM` method sets the specified general parameter register to the specified value.

``` syntax
MSWebDVD.SetGPRM(iIndex, nValue)
```

## Parameters

<dl> <dt>

<span id="iIndex"></span><span id="iindex"></span><span id="IINDEX"></span>*iIndex*
</dt> <dd>

Specifies the general parameter register to set as an Integer. The Integer value must range from 0 through 15.

</dd> <dt>

<span id="nValue"></span><span id="nvalue"></span><span id="NVALUE"></span>*nValue*
</dt> <dd>

Specifies the new value for the register as an Integer.

</dd> </dl>

## Remarks

General parameter registers, or GPRMs, are 16-bit registers that each disc can use in unique ways for temporary data storage. A player application does not need to access these registers for any standard playback or navigation control using the **MSWebDVD** object. This method is provided for player applications implementing advanced functionality. Do not attempt to modify the GPRMs directly unless you have a thorough knowledge of the DVD specification and the ways in which the GPRMs are used on the particular disc to be played. Changing these values can result in unpredictable behavior.

 

 



