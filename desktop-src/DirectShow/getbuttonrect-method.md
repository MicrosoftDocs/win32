---
description: The GetButtonRect method retrieves the rectangle for the specified button, in window coordinates.
ms.assetid: 359e9483-d7ba-45b0-882b-5a4c56dc0350
title: GetButtonRect Method
ms.topic: reference
ms.date: 05/31/2018
---

# GetButtonRect Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `GetButtonRect` method retrieves the rectangle for the specified button, in window coordinates.

``` syntax
[ oButton = ] MSWebDVD.GetButtonRect(iButton)
```

## Parameters

<dl> <dt>

<span id="iButton"></span><span id="ibutton"></span><span id="IBUTTON"></span>*iButton*
</dt> <dd>

Specifies the button number as an Integer.

</dd> </dl>

## Return Value

Returns a [DVDRect](dvdrect-object.md) object that defines the rectangle.

## Remarks

Use this method when implementing custom mouse handling after setting [**DisableAutoMouseProcessing**](disableautomouseprocessing-property.md) to **true**.

## See also

<dl> <dt>

[**ButtonsAvailable**](buttonsavailable-property.md)
</dt> <dt>

[**CurrentButton**](currentbutton-property.md)
</dt> <dt>

[**ActivateButton**](activatebutton-method.md)
</dt> <dt>

[**SelectAndActivateButton**](selectandactivatebutton-method.md)
</dt> <dt>

[**SelectAtPosition**](selectatposition-method.md)
</dt> </dl>

 

 



