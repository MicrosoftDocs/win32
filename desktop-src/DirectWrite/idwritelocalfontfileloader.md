---
title: IDWriteLocalFontFileLoader interface
description: A built-in implementation of the IDWriteFontFileLoader interface, that operates on local font files and exposes local font file information from the font file reference key.
ms.assetid: acb777c8-24c6-452e-8f58-8fb2ad8c0b6c
keywords:
- IDWriteLocalFontFileLoader interface Direct Write
- IDWriteLocalFontFileLoader interface Direct Write , described
topic_type:
- apiref
api_name:
- IDWriteLocalFontFileLoader
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

# IDWriteLocalFontFileLoader interface

A built-in implementation of the [**IDWriteFontFileLoader**](/windows/win32/dwrite/?branch=master) interface, that operates on local font files and exposes local font file information from the font file reference key. Font file references created using [**CreateFontFileReference**](/windows/win32/dwrite/?branch=master) use this font file loader.

## Members

The **IDWriteLocalFontFileLoader** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IDWriteLocalFontFileLoader** also has these types of members:

-   [Methods](#methods)

### Methods

The **IDWriteLocalFontFileLoader** interface has these methods.



| Method                                                                                  | Description                                                                               |
|:----------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------|
| [**GetFilePathFromKey**](idwritelocalfontfileloader-getfilepathfromkey.md)             | Obtains the absolute font file path from the font file reference key.<br/>          |
| [**GetFilePathLengthFromKey**](idwritelocalfontfileloader-getfilepathlengthfromkey.md) | Obtains the length of the absolute file path from the font file reference key.<br/> |
| [**GetLastWriteTimeFromKey**](idwritelocalfontfileloader-getlastwritetimefromkey.md)   | Obtains the last write time of the file from the font file reference key.<br/>      |



 

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>Dwrite.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>Dwrite.dll</dt> </dl> |



 

 





