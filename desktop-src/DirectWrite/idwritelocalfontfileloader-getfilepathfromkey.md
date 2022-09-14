---
title: IDWriteLocalFontFileLoader GetFilePathFromKey method
description: Obtains the absolute font file path from the font file reference key.
ms.assetid: a61cfe80-100d-4813-b04f-a39f626893dd
keywords:
- GetFilePathFromKey method Direct Write
- GetFilePathFromKey method Direct Write , IDWriteLocalFontFileLoader interface
- IDWriteLocalFontFileLoader interface Direct Write , GetFilePathFromKey method
topic_type:
- apiref
api_name:
- IDWriteLocalFontFileLoader.GetFilePathFromKey
api_location:
- dwrite.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IDWriteLocalFontFileLoader::GetFilePathFromKey method

Obtains the absolute font file path from the font file reference key.

## Syntax


```C++
virtual HRESULT GetFilePathFromKey(
  [in]  const void   *fontFileReferenceKey,
              UINT32 fontFileReferenceKeySize,
  [out]       WCHAR  *filePath,
              UINT32 filePathSize
) = 0;
```



## Parameters

<dl> <dt>

*fontFileReferenceKey* \[in\]
</dt> <dd>

Type: **const void\***

The font file reference key that uniquely identifies the local font file within the scope of the font loader being used.

</dd> <dt>

*fontFileReferenceKeySize* 
</dt> <dd>

Type: **UINT32**

The size of font file reference key in bytes.

</dd> <dt>

*filePath* \[out\]
</dt> <dd>

Type: **WCHAR\***

The character array that receives the local file path.

</dd> <dt>

*filePathSize* 
</dt> <dd>

Type: **UINT32**

The length of the file path character array.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>Dwrite.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>Dwrite.dll</dt> </dl> |



## See also

<dl> <dt>

[**IDWriteLocalFontFileLoader**](idwritelocalfontfileloader.md)
</dt> </dl>

 

 





