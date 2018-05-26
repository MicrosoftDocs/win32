---
title: text.addShadow method
description: Adds a shadow effect to a g text element.
ms.assetid: 23976431-629b-4534-bef0-56c19693ef39
keywords:
- addShadow method Windows Sidebar
- addShadow method Windows Sidebar , text object
- text object Windows Sidebar , addShadow method
topic_type:
- apiref
api_name:
- text.addShadow
api_location:
- Sidebar.Exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# text.addShadow method

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Adds a shadow effect to a [**g:text**](gtext.md) element.

## Syntax


```JScript
iRetVal = text.addShadow(
  strColor,
  intRadius,
  intAlpha,
  intDeltaX,
  intDeltaY
)
```



## Parameters

<dl> <dt>

*strColor* \[in\]
</dt> <dd>

A named Windows color (such as "Black") or a color in the format "Color(Alpha, R, G, B)" where the `Alpha`, `R`, `G`, and `B` values can range from 0 to 255.

> [!Note]  
> If using the "Color(Alpha, R, G, B)" specification, the `Alpha` value is superfluous. The transparency of the shadow is set using the intAlpha parameter of [**addShadow**](addshadow-method-gbackground.md) described below.

 

</dd> <dt>

*intRadius* \[in\]
</dt> <dd>

An integer that specifies the radius (or boundary), in pixels, that the shadow effect extends outward from the edge of the target element.

</dd> <dt>

*intAlpha* \[in\]
</dt> <dd>

An integer that sets the transparency of the shadow effect. The value can range from 0 (transparent) to 100 (opaque).

</dd> <dt>

*intDeltaX* \[in\]
</dt> <dd>

The offset, in pixels, from the leftmost edge of the target element.

</dd> <dt>

*intDeltaY* \[in\]
</dt> <dd>

The offset, in pixels, from the rightmost edge of the target element.

</dd> </dl>

## Remarks

The opacity of the target element must be set to a value of at least 1 for the shadow effect to be visible.

## Examples

The following example demonstrates how to add a shadow effect to a [**g:text**](gtext.md) element.


```JScript
\\ imgBackground is the value of the 'id' attribute for the g:background element.
var txtShadow = imgBackground.addTextObject("test", "Verdana", 25, "Red", 50, 50);
txtShadow.addShadow("Color(255, 255, 0, 0)", 50, 25, 0, 0);
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**image**](image-element.md)
</dt> <dt>

[**text**](gtext.md)
</dt> </dl>

 

 





