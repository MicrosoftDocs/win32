---
Description: Enables the Microsoft Media Foundation HTTP byte stream to use URL monikers (also called Urlmon).
ms.assetid: 8B7D2FF7-D8A8-49E9-8CED-D37853B97A8F
title: MFPKEY_HTTP_ByteStream_Enable_Urlmon property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MFPKEY\_HTTP\_ByteStream\_Enable\_Urlmon property

Enables the Microsoft Media Foundation HTTP byte stream to use URL monikers (also called *Urlmon*).



Data type

PROPVARIANT type (vt)

PROPVARIANT member

**VARIANT\_BOOL**

VT\_BOOL

**boolVal**



## Remarks

Use this property to configure the Media Foundation HTTP byte stream. To set the property, pass an [**IPropertyStore**](https://msdn.microsoft.com/en-us/library/Bb761474(v=VS.85).aspx) pointer to the source resolver. For more information, see [Configuring a Media Source](configuring-a-media-source.md).

If the value is **VARIANT\_TRUE**, the HTTP byte stream uses Urlmon for HTTP transport. Otherwise, if the value is **VARIANT\_FALSE**, the byte stream uses WinHTTP.

The default value is **VARIANT\_TRUE** for Windows Store apps and **VARIANT\_FALSE** for Windows desktop application.

## Requirements



|                   |                                                                                    |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 




