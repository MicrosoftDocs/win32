---
title: IDWriteColorGlyphRunEnumerator interface
description: This interface allows the application to enumerate through the color glyph runs.
ms.assetid: 649AD648-32BB-4BF4-A82F-075E93505E33
keywords:
- IDWriteColorGlyphRunEnumerator interface Direct Write
- IDWriteColorGlyphRunEnumerator interface Direct Write , described
topic_type:
- apiref
api_name:
- IDWriteColorGlyphRunEnumerator
api_location:
- dwrite.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IDWriteColorGlyphRunEnumerator interface

This interface allows the application to enumerate through the color glyph runs. The enumerator enumerates the layers in a back to front order for appropriate layering.

## Members

The **IDWriteColorGlyphRunEnumerator** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IDWriteColorGlyphRunEnumerator** also has these types of members:

-   [Methods](#methods)

### Methods

The **IDWriteColorGlyphRunEnumerator** interface has these methods.



| Method                                                                | Description                                                 |
|:----------------------------------------------------------------------|:------------------------------------------------------------|
| [**GetCurrentRun**](/windows/win32/api/dwrite_2/nf-dwrite_2-idwritecolorglyphrunenumerator-getcurrentrun) | Returns the current glyph run of the enumerator.<br/> |
| [**MoveNext**](idwritecolorglyphrunenumerator-movenext.md)           | Move to the next glyph run in the enumerator.<br/>    |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps \| UWP apps\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps \| UWP apps\]<br/>                          |
| Minimum supported phone<br/>  | Windows Phone 8.1 \[Windows Phone Silverlight 8.1 and Windows Runtime apps\]<br/> |
| Library<br/>                  | <dl> <dt>Dwrite.lib</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Dwrite.dll</dt> </dl>   |



 

