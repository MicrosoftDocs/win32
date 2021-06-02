---
description: The GetButtonAtPosition method retrieves the number of the button at the specified coordinates without selecting or activating it.
ms.assetid: ac933d0d-db2e-488f-b661-2fdc9f5acb39
title: GetButtonAtPosition Method
ms.topic: reference
ms.date: 05/31/2018
---

# GetButtonAtPosition Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `GetButtonAtPosition` method retrieves the number of the button at the specified coordinates without selecting or activating it.

``` syntax
[ iButton = ] MSWebDVD.GetButtonAtPosition(xPos, yPos)
```

## Parameters

<dl> <dt>

<span id="xPos"></span><span id="xpos"></span><span id="XPOS"></span>*xPos*
</dt> <dd>

Specifies the x-coordinate of the mouse pointer as an Integer.

</dd> <dt>

<span id="yPos"></span><span id="ypos"></span><span id="YPOS"></span>*yPos*
</dt> <dd>

Specifies the y-coordinate of the mouse pointer as an Integer.

</dd> </dl>

## Return Value

Returns an integer value specifying the button, if any, at the specified position.

## Remarks

This method returns zero if no button is present at the given coordinates. Use this method when implementing custom mouse handling after setting [**DisableAutoMouseProcessing**](disableautomouseprocessing-property.md) to **true**.

## See also

<dl> <dt>

[**ActivateButton**](activatebutton-method.md)
</dt> <dt>

[**ButtonsAvailable**](buttonsavailable-property.md)
</dt> <dt>

[**CurrentButton**](currentbutton-property.md)
</dt> <dt>

[**GetButtonRect**](getbuttonrect-method.md)
</dt> <dt>

[**SelectAndActivateButton**](selectandactivatebutton-method.md)
</dt> <dt>

[**SelectAtPosition**](selectatposition-method.md)
</dt> </dl>

 

 



