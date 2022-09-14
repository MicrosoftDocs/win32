---
description: The ButtonsAvailable property retrieves the total number of buttons on the current menu.
ms.assetid: 4df3a7e7-1be4-4cc7-ad61-567f7f45811e
title: ButtonsAvailable Property
ms.topic: reference
ms.date: 05/31/2018
---

# ButtonsAvailable Property

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `ButtonsAvailable` property retrieves the total number of buttons on the current menu.

``` syntax
[ iButtons = ] MSWebDVD.ButtonsAvailable
```

## Return Value

Returns an integer value representing the number of buttons.

## Remarks

This property is read-only with no default value. Use this method when implementing custom mouse handling after setting [**DisableAutoMouseProcessing**](disableautomouseprocessing-property.md) to **true**.

Call this method to retrieve the upper limit for the range of valid button numbers.

## See also

<dl> <dt>

[**CurrentButton**](currentbutton-property.md)
</dt> <dt>

[**GetButtonAtPosition**](getbuttonatposition-method.md)
</dt> <dt>

[**GetButtonRect**](getbuttonrect-method.md)
</dt> <dt>

[**SelectAndActivateButton**](selectandactivatebutton-method.md)
</dt> <dt>

[**SelectAtPosition**](selectatposition-method.md)
</dt> </dl>

 

 



