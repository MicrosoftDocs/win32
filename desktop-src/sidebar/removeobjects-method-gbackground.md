---
title: background.removeObjects method
description: Removes all g text and g image elements added to the gadget background using the addTextObject and addImageObject methods.
ms.assetid: '5f915fe1-2930-45ea-ac8c-747127fee1f5'
keywords: ["removeObjects method Windows Sidebar", "removeObjects method Windows Sidebar , background object", "background object Windows Sidebar , removeObjects method"]
topic_type:
- apiref
api_name:
- background.removeObjects
api_location:
- Sidebar.Exe
api_type:
- COM
---

# background.removeObjects method

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Removes all [**g:text**](gtext.md) and [**g:image**](image-element.md) elements added to the gadget background using the [**addTextObject**](addtextobject-method-gbackground.md) and [**addImageObject**](addimageobject-method-gbackground.md) methods.

## Syntax


```JScript
iRetVal = background.removeObjects()
```



## Parameters

This method has no parameters.

## Remarks

The initial background image is unaffected.

## Examples

The following example demonstrates how to add both [**g:text**](gtext.md) and [**g:image**](image-element.md) elements to a [**g:background**](background-element.md) and then remove them using the **removeObjects** method


```JScript
\\ Add g:text and g:image elements to the g:background element.
\\ imgBackground is the value of the 'id' attribute for the g:background element.
var imgGlow = imgBackground.addImageObject("file://img.png", 0, 0);
var txtShadow = imgBackground.addTextObject("test", "Verdana", 25, "Red", 50, 50);

\\ Remove all text and image elements, leaving the initial background image unchanged.
imgBackground.removeObjects();
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Wbemcli.h</dt> </dl>                           |
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

 

 





