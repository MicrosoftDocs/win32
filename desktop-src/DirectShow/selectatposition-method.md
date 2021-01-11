---
description: The SelectAtPosition method selects the menu button at the specified mouse pointer coordinates.
ms.assetid: 005ec550-e04c-4dae-aa5d-d79afefe48ed
title: SelectAtPosition Method
ms.topic: reference
ms.date: 05/31/2018
---

# SelectAtPosition Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `SelectAtPosition` method selects the menu button at the specified mouse pointer coordinates.

``` syntax
MSWebDVD.SelectAtPosition(xPos, yPos)
```

## Parameters

<dl> <dt>

<span id="xPos"></span><span id="xpos"></span><span id="XPOS"></span>*xPos*
</dt> <dd>

Specifies the x-coordinate as an Integer.

</dd> <dt>

<span id="yPos"></span><span id="ypos"></span><span id="YPOS"></span>*yPos*
</dt> <dd>

Specifies the y-coordinate as an Integer.

</dd> </dl>

## Return Value

No return value.

## Remarks

Use this method when implementing custom mouse handling after setting [**DisableAutoMouseProcessing**](disableautomouseprocessing-property.md) to **true**.

Selecting merely highlights the button. To send the command associated with a button that has been selected, call [**ActivateButton**](activatebutton-method.md).

## See also

<dl> <dt>

[**ButtonsAvailable**](buttonsavailable-property.md)
</dt> <dt>

[**CurrentButton**](currentbutton-property.md)
</dt> <dt>

[**GetButtonAtPosition**](getbuttonatposition-method.md)
</dt> <dt>

[**GetButtonRect**](getbuttonrect-method.md)
</dt> <dt>

[**SelectAndActivateButton**](selectandactivatebutton-method.md)
</dt> </dl>

 

 



