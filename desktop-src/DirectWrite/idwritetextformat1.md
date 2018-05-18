---
title: IDWriteTextFormat1 interface
description: Describes the font and paragraph properties used to format text, and it describes locale information.
ms.assetid: '15295A17-E542-4071-AE38-02014A1235D5'
keywords: ["IDWriteTextFormat1 interface Direct Write", "IDWriteTextFormat1 interface Direct Write , described"]
topic_type:
- apiref
api_name:
- IDWriteTextFormat1
api_location:
- dwrite.dll
api_type:
- COM
---

# IDWriteTextFormat1 interface

Describes the font and paragraph properties used to format text, and it describes locale information. This interface has all the same methods as [**IDWriteTextFormat**](idwritetextformat.md) and adds the ability for you to apply an explicit orientation.

## Members

The **IDWriteTextFormat1** interface inherits from [**IDWriteTextFormat**](idwritetextformat.md). **IDWriteTextFormat1** also has these types of members:

-   [Methods](#methods)

### Methods

The **IDWriteTextFormat1** interface has these methods.



| Method                                                                                | Description                                                                                                             |
|:--------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------|
| [**GetFontFallback**](idwritetextformat1-getfontfallback.md)                         | Gets the current fallback. If none was ever set since creating the layout, it will be nullptr.<br/>               |
| [**GetLastLineWrapping**](idwritetextformat1-getlastlinewrapping.md)                 | Gets the wrapping mode of the last line.<br/>                                                                     |
| [**GetOpticalAlignment**](idwritetextformat1-getopticalalignment.md)                 | Gets the optical margin alignment for the text format.<br/>                                                       |
| [**GetVerticalGlyphOrientation**](idwritetextformat1-getverticalglyphorientation.md) | Get the preferred orientation of glyphs when using a vertical reading direction.<br/>                             |
| [**SetFontFallback**](idwritetextformat1-setfontfallback.md)                         | Applies the custom font fallback onto the layout. If none is set, it uses the default system fallback list. <br/> |
| [**SetLastLineWrapping**](idwritetextformat1-setwraponlastline.md)                   | Sets the wrapping mode of the last line.<br/>                                                                     |
| [**SetOpticalAlignment**](idwritetextformat1-setopticalalignment.md)                 | Sets the optical margin alignment for the text format.<br/>                                                       |
| [**SetVerticalGlyphOrientation**](idwritetextformat1-setverticalglyphorientation.md) | Sets the orientation of a text format.<br/>                                                                       |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps \| UWP apps\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps \| UWP apps\]<br/>                          |
| Minimum supported phone<br/>  | Windows Phone 8.1 \[Windows Phone Silverlight 8.1 and Windows Runtime apps\]<br/> |
| Library<br/>                  | <dl> <dt>Dwrite.lib</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Dwrite.dll</dt> </dl>   |



## See also

<dl> <dt>

[**IDWriteTextFormat**](idwritetextformat.md)
</dt> </dl>

 

 





