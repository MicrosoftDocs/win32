---
title: IDWriteTextLayout3 interface
description: Represents a block of text after it has been fully analyzed and formatted. | IDWriteTextLayout3 interface
ms.assetid: a7741740-9524-caf0-650b-56808abcf328
keywords:
- IDWriteTextLayout3 interface Direct Write
- IDWriteTextLayout3 interface Direct Write , described
topic_type:
- apiref
api_name:
- IDWriteTextLayout3
api_location:
- dwrite.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IDWriteTextLayout3 interface

Represents a block of text after it has been fully analyzed and formatted.

## Members

The **IDWriteTextLayout3** interface inherits from [**IDWriteTextLayout2**](idwritetextlayout2.md). **IDWriteTextLayout3** also has these types of members:

-   [Methods](#methods)

### Methods

The **IDWriteTextLayout3** interface has these methods.



| Method                                                          | Description                                                                                                                                                                                                                                                          |
|:----------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetLineMetrics**](idwritetextlayout3-getlinemetrics.md)     | Retrieves properties of each line.<br/>                                                                                                                                                                                                                        |
| [**GetLineSpacing**](idwritetextlayout3-getlinespacing.md)     | Gets line spacing information.<br/>                                                                                                                                                                                                                            |
| [**InvalidateLayout**](idwritetextlayout3-invalidatelayout.md) | Invalidates the layout, forcing layout to remeasure before calling the metrics or drawing functions. This is useful if the locality of a font changes, and layout should be redrawn, or if the size of a client implemented IDWriteInlineObject changes. <br/> |
| [**SetLineSpacing**](idwritetextlayout3-setlinespacing.md)     | Set line spacing.<br/>                                                                                                                                                                                                                                         |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps \| UWP apps\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps \| UWP apps\]<br/>                          |
| Minimum supported phone<br/>  | Windows Phone 8.1 \[Windows Phone Silverlight 8.1 and Windows Runtime apps\]<br/> |
| Library<br/>                  | <dl> <dt>Dwrite.lib</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Dwrite.dll</dt> </dl>   |



## See also

<dl> <dt>

[**IDWriteTextLayout2**](idwritetextlayout2.md)
</dt> </dl>

 

 





