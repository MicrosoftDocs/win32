---
title: text.addGlow method
description: Adds a glow effect to a g text element.
ms.assetid: '84b22483-88bc-4d5c-a86b-b3c5a2a5e6d3'
keywords: ["addGlow method Windows Sidebar", "addGlow method Windows Sidebar , text object", "text object Windows Sidebar , addGlow method"]
topic_type:
- apiref
api_name:
- text.addGlow
api_location:
- Sidebar.Exe
api_type:
- COM
---

# text.addGlow method

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Adds a glow effect to a [**g:text**](gtext.md) element.

## Syntax


```JScript
iRetVal = text.addGlow(
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

The opacity of the target text must be set to a value of at least 1 for the glow effect to be visible.

## Examples

The following example demonstrates how to add a glow effect to a [**g:text**](gtext.md) element.


```JScript
\\ imgBackground is the value of the 'id' attribute for the g:background element.
var txtGlow = imgBackground.addTextObject("test", "Verdana", 25, "Red", 50, 50);
txtGlow.opacity = 100;
txtGlow.addGlow("black", 50, 50);
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

[**image**](image-element.md)
</dt> <dt>

[**text**](gtext.md)
</dt> </dl>

 

 





