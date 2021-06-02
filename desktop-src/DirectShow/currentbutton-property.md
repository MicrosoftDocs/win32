---
description: The CurrentButton property retrieves the number of the selected menu button.
ms.assetid: bd9720bc-068a-4f29-aa2d-1c6b550f789c
title: CurrentButton Property
ms.topic: reference
ms.date: 05/31/2018
---

# CurrentButton Property

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `CurrentButton` property retrieves the number of the selected menu button.

``` syntax
[ iButton = ] MSWebDVD.CurrentButton
```

## Return Value

Returns an integer value representing the button.

## Remarks

This property is read-only with no default value. Use this method when implementing custom mouse handling after setting [**DisableAutoMouseProcessing**](disableautomouseprocessing-property.md) to **true**.

## See also

<dl> <dt>

[**ActivateButton**](activatebutton-method.md)
</dt> <dt>

[**ButtonsAvailable**](buttonsavailable-property.md)
</dt> <dt>

[**GetButtonAtPosition**](getbuttonatposition-method.md)
</dt> <dt>

[**GetButtonRect**](getbuttonrect-method.md)
</dt> <dt>

[**SelectAndActivateButton**](selectandactivatebutton-method.md)
</dt> <dt>

[**SelectAtPosition**](selectatposition-method.md)
</dt> </dl>

 

 



