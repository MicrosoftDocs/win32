---
title: IDWriteTextLayout2 interface
description: Represents a block of text after it has been fully analyzed and formatted.
ms.assetid: 034D795B-016A-401E-AD75-D5B0D1E87806
keywords:
- IDWriteTextLayout2 interface Direct Write
- IDWriteTextLayout2 interface Direct Write , described
topic_type:
- apiref
api_name:
- IDWriteTextLayout2
api_location:
- dwrite.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IDWriteTextLayout2 interface

Represents a block of text after it has been fully analyzed and formatted.

## Members

The **IDWriteTextLayout2** interface inherits from [**IDWriteTextLayout1**](https://msdn.microsoft.com/en-us/library/Hh780438(v=VS.85).aspx). **IDWriteTextLayout2** also has these types of members:

-   [Methods](#methods)

### Methods

The **IDWriteTextLayout2** interface has these methods.



| Method                                                                                | Description                                                                                 |
|:--------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------|
| [**GetFontFallback**](https://msdn.microsoft.com/en-us/library/Dn482045(v=VS.85).aspx)                         | Get the current font fallback object. <br/>                                           |
| [**GetLastLineWrapping**](https://msdn.microsoft.com/en-us/library/Dn482046(v=VS.85).aspx)                 | Get whether or not the last word on the last line is wrapped.<br/>                    |
| [**GetMetrics**](idwritetextlayout2-getmetrics.md)                                   | Retrieves overall metrics for the formatted string. <br/>                             |
| [**GetOpticalAlignment**](https://msdn.microsoft.com/en-us/library/Dn482047(v=VS.85).aspx)                 | Get how the glyphs align to the edges the margin. <br/>                               |
| [**GetVerticalGlyphOrientation**](https://msdn.microsoft.com/en-us/library/Dn482048(v=VS.85).aspx) | Get the preferred orientation of glyphs when using a vertical reading direction.<br/> |
| [**SetFontFallback**](https://msdn.microsoft.com/en-us/library/Dn482049(v=VS.85).aspx)                         | Apply a custom font fallback onto layout.<br/>                                        |
| [**SetLastLineWrapping**](https://msdn.microsoft.com/en-us/library/Dn482050(v=VS.85).aspx)                 | Set whether or not the last word on the last line is wrapped. <br/>                   |
| [**SetOpticalAlignment**](https://msdn.microsoft.com/en-us/library/Dn482051(v=VS.85).aspx)                 | Set how the glyphs align to the edges the margin.<br/>                                |
| [**SetVerticalGlyphOrientation**](https://msdn.microsoft.com/en-us/library/Dn482052(v=VS.85).aspx) | Set the preferred orientation of glyphs when using a vertical reading direction.<br/> |



 

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

[**IDWriteTextLayout1**](https://msdn.microsoft.com/en-us/library/Hh780438(v=VS.85).aspx)
</dt> </dl>

 

 





