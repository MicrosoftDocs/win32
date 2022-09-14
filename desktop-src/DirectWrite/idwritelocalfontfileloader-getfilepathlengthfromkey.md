---
title: IDWriteLocalFontFileLoader GetFilePathLengthFromKey method
description: Obtains the length of the absolute file path from the font file reference key.
ms.assetid: bdd84d75-5a7a-448a-a52c-0f5997ab07b9
keywords:
- GetFilePathLengthFromKey method Direct Write
- GetFilePathLengthFromKey method Direct Write , IDWriteLocalFontFileLoader interface
- IDWriteLocalFontFileLoader interface Direct Write , GetFilePathLengthFromKey method
topic_type:
- apiref
api_name:
- IDWriteLocalFontFileLoader.GetFilePathLengthFromKey
api_location:
- dwrite.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IDWriteLocalFontFileLoader::GetFilePathLengthFromKey method

Obtains the length of the absolute file path from the font file reference key.

## Syntax


```C++
HRESULT GetFilePathLengthFromKey(
  [in]  const void   *fontFileReferenceKey,
              UINT32 fontFileReferenceKeySize,
  [out]       UINT32 *filePathLength
);
```



## Parameters

<dl> <dt>

*fontFileReferenceKey* \[in\]
</dt> <dd>

Type: **const void\***

Font file reference key that uniquely identifies the local font file within the scope of the font loader being used.

</dd> <dt>

*fontFileReferenceKeySize* 
</dt> <dd>

Type: **UINT32**

Size of font file reference key in bytes.

</dd> <dt>

*filePathLength* \[out\]
</dt> <dd>

Type: **UINT32\***

Length of the file path string, not including the terminated **NULL** character.

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

 

 





