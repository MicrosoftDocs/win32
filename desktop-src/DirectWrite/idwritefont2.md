---
title: IDWriteFont2 interface
description: Represents a physical font in a font collection.
ms.assetid: 4E3069AE-5882-4A26-A36D-BE7D7EE1B0C3
keywords:
- IDWriteFont2 interface Direct Write
- IDWriteFont2 interface Direct Write , described
topic_type:
- apiref
api_name:
- IDWriteFont2
api_location:
- dwrite.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IDWriteFont2 interface

Represents a physical font in a font collection.

This interface adds the ability to check if a color rendering path is potentially necessary.

## Members

The **IDWriteFont2** interface inherits from [**IDWriteFont1**](/windows/win32/api/dwrite_1/nn-dwrite_1-idwritefont1). **IDWriteFont2** also has these types of members:

-   [Methods](#methods)

### Methods

The **IDWriteFont2** interface has these methods.



| Method                                          | Description                                                                        |
|:------------------------------------------------|:-----------------------------------------------------------------------------------|
| [**IsColorFont**](idwritefont2-iscolorfont.md) | Enables determining if a color rendering path is potentially necessary.<br/> |



 

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

[**IDWriteFont1**](/windows/win32/api/dwrite_1/nn-dwrite_1-idwritefont1)
</dt> </dl>

 

