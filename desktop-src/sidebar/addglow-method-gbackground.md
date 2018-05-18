---
title: background.addGlow method
description: Adds a glow effect to the g background element.
ms.assetid: '0566b20a-2079-449a-a187-18e1defa2ccc'
keywords: ["addGlow method Windows Sidebar", "addGlow method Windows Sidebar , background object", "background object Windows Sidebar , addGlow method"]
topic_type:
- apiref
api_name:
- background.addGlow
api_location:
- Sidebar.Exe
api_type:
- COM
---

# background.addGlow method

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Adds a glow effect to the [**g:background**](background-element.md) element.

## Syntax


```JScript
iRetVal = background.addGlow(
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

The following example demonstrates how to add a glow effect to the [**g:background**](background-element.md) element.


```JScript
\\ imgBackground is the value of the 'id' attribute for the g:background element.
imgBackground.addGlow("black", 50, 50);
imgBackground.addGlow("Color(255, 255, 0, 0)",50,25);
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

 

 





