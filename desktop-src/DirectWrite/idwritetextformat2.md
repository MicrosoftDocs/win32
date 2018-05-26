---
title: IDWriteTextFormat2 interface
description: Describes the font and paragraph properties used to format text, and it describes locale information.
ms.assetid: 4396d2b0-240f-ee8b-1d21-c4294fb29b51
keywords:
- IDWriteTextFormat2 interface Direct Write
- IDWriteTextFormat2 interface Direct Write , described
topic_type:
- apiref
api_name:
- IDWriteTextFormat2
api_location:
- dwrite.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IDWriteTextFormat2 interface

Describes the font and paragraph properties used to format text, and it describes locale information.

## Members

The **IDWriteTextFormat2** interface inherits from [**IDWriteTextFormat1**](idwritetextformat1.md). **IDWriteTextFormat2** also has these types of members:

-   [Methods](#methods)

### Methods

The **IDWriteTextFormat2** interface has these methods.



| Method                                                      | Description                                                                      |
|:------------------------------------------------------------|:---------------------------------------------------------------------------------|
| [**GetLineSpacing**](/windows/win32/dwrite/?branch=master) | Gets the line spacing adjustment set for a multiline text paragraph. <br/> |
| [**SetLineSpacing**](idwritetextformat2-setlinespacing.md) | Set line spacing.<br/>                                                     |



 

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

[**IDWriteTextFormat1**](idwritetextformat1.md)
</dt> </dl>

 

 





