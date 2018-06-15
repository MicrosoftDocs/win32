---
title: IDWriteFontFallbackBuilder interface
description: Allows you to create Unicode font fallback mappings and create a font fall back object from those mappings.
ms.assetid: 462AC12E-C856-4D8F-83AF-FAC3221425C2
keywords:
- IDWriteFontFallbackBuilder interface Direct Write
- IDWriteFontFallbackBuilder interface Direct Write , described
topic_type:
- apiref
api_name:
- IDWriteFontFallbackBuilder
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

# IDWriteFontFallbackBuilder interface

Allows you to create Unicode font fallback mappings and create a font fall back object from those mappings.

## Members

The **IDWriteFontFallbackBuilder** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IDWriteFontFallbackBuilder** also has these types of members:

-   [Methods](#methods)

### Methods

The **IDWriteFontFallbackBuilder** interface has these methods.



| Method                                                                      | Description                                                                                  |
|:----------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------|
| [**AddMapping**](idwritefontfallbackbuilder-addmapping.md)                 | Appends a single mapping to the list. Call this once for each additional mapping.<br/> |
| [**AddMappings**](https://msdn.microsoft.com/en-us/library/Dn280478(v=VS.85).aspx)               | Add all the mappings from an existing font fallback object.<br/>                       |
| [**CreateFontFallback**](https://msdn.microsoft.com/en-us/library/Dn280479(v=VS.85).aspx) | Creates the finalized fallback object from the mappings added.<br/>                    |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps \| UWP apps\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps \| UWP apps\]<br/>                          |
| Minimum supported phone<br/>  | Windows Phone 8.1 \[Windows Phone Silverlight 8.1 and Windows Runtime apps\]<br/> |
| Library<br/>                  | <dl> <dt>Dwrite.lib</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Dwrite.dll</dt> </dl>   |



 

 





