---
description: The SelectAndActivateButton method selects and activates the specified button.
ms.assetid: fa6239ea-0478-41f1-9515-d67a7fad11db
title: SelectAndActivateButton Method
ms.topic: reference
ms.date: 05/31/2018
---

# SelectAndActivateButton Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `SelectAndActivateButton` method selects and activates the specified button.

``` syntax
MSWebDVD.SelectAndActivateButton(iButton)
```

## Parameters

<dl> <dt>

<span id="iButton"></span><span id="ibutton"></span><span id="IBUTTON"></span>*iButton*
</dt> <dd>

Specifies the button as an Integer.

</dd> </dl>

## Return Value

No return value.

## Remarks

Use this method when implementing custom mouse handling after setting [**DisableAutoMouseProcessing**](disableautomouseprocessing-property.md) to **true**.

This method highlights the specified button and activate it automatically.

## See also

<dl> <dt>

[**ButtonsAvailable**](buttonsavailable-property.md)
</dt> <dt>

[**CurrentButton**](currentbutton-property.md)
</dt> <dt>

[**ActivateButton**](activatebutton-method.md)
</dt> <dt>

[**GetButtonAtPosition**](getbuttonatposition-method.md)
</dt> <dt>

[**GetButtonRect**](getbuttonrect-method.md)
</dt> <dt>

[**SelectAtPosition**](selectatposition-method.md)
</dt> </dl>

 

 



