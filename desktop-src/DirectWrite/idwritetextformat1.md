---
title: IDWriteTextFormat1 interface
description: Describes the font and paragraph properties used to format text, and it describes locale information.
ms.assetid: 15295A17-E542-4071-AE38-02014A1235D5
keywords:
- IDWriteTextFormat1 interface Direct Write
- IDWriteTextFormat1 interface Direct Write , described
topic_type:
- apiref
api_name:
- IDWriteTextFormat1
api_location:
- dwrite.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IDWriteTextFormat1 interface

Describes the font and paragraph properties used to format text, and it describes locale information. This interface has all the same methods as [**IDWriteTextFormat**](https://msdn.microsoft.com/en-us/library/Dd316628(v=VS.85).aspx) and adds the ability for you to apply an explicit orientation.

## Members

The **IDWriteTextFormat1** interface inherits from [**IDWriteTextFormat**](https://msdn.microsoft.com/en-us/library/Dd316628(v=VS.85).aspx). **IDWriteTextFormat1** also has these types of members:

-   [Methods](#methods)

### Methods

The **IDWriteTextFormat1** interface has these methods.



| Method                                                                                | Description                                                                                                             |
|:--------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------|
| [**GetFontFallback**](https://msdn.microsoft.com/en-us/library/Dn280486(v=VS.85).aspx)                         | Gets the current fallback. If none was ever set since creating the layout, it will be nullptr.<br/>               |
| [**GetLastLineWrapping**](https://msdn.microsoft.com/en-us/library/Dn894596(v=VS.85).aspx)                 | Gets the wrapping mode of the last line.<br/>                                                                     |
| [**GetOpticalAlignment**](https://msdn.microsoft.com/en-us/library/Dn894597(v=VS.85).aspx)                 | Gets the optical margin alignment for the text format.<br/>                                                       |
| [**GetVerticalGlyphOrientation**](https://msdn.microsoft.com/en-us/library/Dn894598(v=VS.85).aspx) | Get the preferred orientation of glyphs when using a vertical reading direction.<br/>                             |
| [**SetFontFallback**](https://msdn.microsoft.com/en-us/library/Dn280487(v=VS.85).aspx)                         | Applies the custom font fallback onto the layout. If none is set, it uses the default system fallback list. <br/> |
| [**SetLastLineWrapping**](https://msdn.microsoft.com/en-us/library/Dn280490(v=VS.85).aspx)                   | Sets the wrapping mode of the last line.<br/>                                                                     |
| [**SetOpticalAlignment**](https://msdn.microsoft.com/en-us/library/Dn280488(v=VS.85).aspx)                 | Sets the optical margin alignment for the text format.<br/>                                                       |
| [**SetVerticalGlyphOrientation**](https://msdn.microsoft.com/en-us/library/Dn280489(v=VS.85).aspx) | Sets the orientation of a text format.<br/>                                                                       |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps \| UWP apps\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps \| UWP apps\]<br/>                          |
| Minimum supported phone<br/>  | Windows Phone 8.1 \[Windows Phone Silverlight 8.1 and Windows Runtime apps\]<br/> |
| Library<br/>                  | <dl> <dt>Dwrite.lib</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Dwrite.dll</dt> </dl>   |



## See also

<dl> <dt>

[**IDWriteTextFormat**](https://msdn.microsoft.com/en-us/library/Dd316628(v=VS.85).aspx)
</dt> </dl>

 

 





