---
description: The ActivateAtPosition method activates the menu button at the specified position.
ms.assetid: eddc4880-dd78-4d96-8bff-c5c883a19927
title: ActivateAtPosition Method
ms.topic: reference
ms.date: 05/31/2018
---

# ActivateAtPosition Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The ActivateAtPosition method activates the menu button at the specified position.

``` syntax
        MSWebDVD.ActivateAtPosition(xPos, yPos)
```

## Parameters

<dl> <dt>

<span id="xPos"></span><span id="xpos"></span><span id="XPOS"></span>*xPos*
</dt> <dd>

Specifies x-coordinate as an Integer.

</dd> <dt>

<span id="yPos"></span><span id="ypos"></span><span id="YPOS"></span>*yPos*
</dt> <dd>

Specifies the y-coordinate as an Integer.

</dd> </dl>

## Return Value

No return value.

## Remarks

Use this method when implementing custom mouse handling after setting [**DisableAutoMouseProcessing**](disableautomouseprocessing-property.md) to **true**.

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
</dt> <dt>

[**SelectAtPosition**](selectatposition-method.md)
</dt> </dl>

 

 



