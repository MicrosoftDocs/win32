---
title: IDWriteFactory2 GetSystemFontFallback method
description: Creates a font fallback object from the system font fallback list.
ms.assetid: 7F2BDB39-2CB4-4DB7-BBBA-74B0C07E7420
keywords:
- GetSystemFontFallback method Direct Write
- GetSystemFontFallback method Direct Write , IDWriteFactory2 interface
- IDWriteFactory2 interface Direct Write , GetSystemFontFallback method
topic_type:
- apiref
api_name:
- IDWriteFactory2.GetSystemFontFallback
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
api_location: 
---

# IDWriteFactory2::GetSystemFontFallback method

Creates a font fallback object from the system font fallback list.

## Syntax


```C++
HRESULT GetSystemFontFallback(
  [out] IDWriteFontFallback **fontFallback
);
```



## Parameters

<dl> <dt>

*fontFallback* \[out\]
</dt> <dd>

Type: **[**IDWriteFontFallback**](https://msdn.microsoft.com/en-us/library/Dn280474(v=VS.85).aspx)\*\***

Contains an address of a pointer to the newly created font fallback object.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## See also

<dl> <dt>

[**IDWriteFactory2**](idwritefactory2.md)
</dt> </dl>

 

 




