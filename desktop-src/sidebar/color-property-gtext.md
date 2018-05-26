---
title: text.color property
description: Gets or sets the text color.
ms.assetid: b5ba7eb0-0878-4acd-acdc-c5c7435cd51f
keywords:
- color property Windows Sidebar
- color property Windows Sidebar , text object
- text object Windows Sidebar , color property
topic_type:
- apiref
api_name:
- text.color
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

# text.color property

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Gets or sets the text color.

This property is read/write.

## Syntax


```JScript
strcolor = text.color
text.color = strcolor
```



## Property value

A **String** that specifies or receives the named Windows color applied to the target element.

## Remarks

The Windows Sidebar color names match the Microsoft .NET Framework version 1.0, Windows Forms, and Microsoft Internet Explorer color names. This representation is based on UNIX X11 named color values.

The following image shows each predefined color, its name, and its hexadecimal value.

![predefined windows color names](images/reference/color-table.png)

## Examples

The following example demonstrates how to assign a color to the [**g:text**](gtext.md) element from a gadget script file.


```JScript
\\ imgBackground is the value of the 'id' attribute for the g:background element.
var txtColor = imgBackground.addTextObject("test", "Verdana", 25, "Red", intX, intY);
txtColor.color = "ForestGreen";
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

[**background**](background-element.md)
</dt> <dt>

[**image**](image-element.md)
</dt> <dt>

[**text**](gtext.md)
</dt> </dl>

 

 





