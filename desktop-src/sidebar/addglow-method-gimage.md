---
title: image.addGlow method
description: Adds a glow effect to a g image element.
ms.assetid: 'e76f0195-7a5f-4833-b0d8-d81b0688f8fc'
keywords: ["addGlow method Windows Sidebar", "addGlow method Windows Sidebar , image object", "image object Windows Sidebar , addGlow method"]
topic_type:
- apiref
api_name:
- image.addGlow
api_location:
- Sidebar.Exe
api_type:
- COM
---

# image.addGlow method

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Adds a glow effect to a [**g:image**](image-element.md) element.

## Syntax


```JScript
iRetVal = image.addGlow(
  strColor,
  intRadius,
  intAlpha
)
```



## Parameters

<dl> <dt>

*strColor* \[in\]
</dt> <dd>

A named Windows color (such as "Black") or a color in the format "Color(Alpha, R, G, B)" where the `Alpha`, `R`, `G`, and `B` values can range from 0 to 255.

> [!Note]  
> If using the "Color(Alpha, R, G, B)" specification, the `Alpha` value is superfluous. The transparency of the glow is set using the intAlpha parameter of **addGlow** described below.

 

</dd> <dt>

*intRadius* \[in\]
</dt> <dd>

An integer that specifies the radius (or boundary), in pixels, that the glow effect extends outward from the edge of the target element.

</dd> <dt>

*intAlpha* \[in\]
</dt> <dd>

An integer that sets the transparency of the glow effect as a percentage from 0 (transparent) to 100 (opaque).

</dd> </dl>

## Remarks

The opacity of the target image must be set to a value of at least 1 for the glow effect to be visible.

## Examples

The following example demonstrates how to add a glow effect to a [**g:image**](image-element.md) element.


```JScript
\\ imgBackground is the value of the 'id' attribute for the g:background element.
var imgGlow = imgBackground.addImageObject("file://img.png", 0, 0);
imgGlow.addGlow("Color(255, 255, 0, 0)", 50, 25);
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**background**](background-element.md)
</dt> <dt>

[**image**](image-element.md)
</dt> <dt>

[**text**](gtext.md)
</dt> </dl>

 

 





