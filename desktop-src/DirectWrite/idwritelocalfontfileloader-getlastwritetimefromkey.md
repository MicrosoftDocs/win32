---
title: IDWriteLocalFontFileLoader GetLastWriteTimeFromKey method
description: Obtains the last write time of the file from the font file reference key.
ms.assetid: ce7f5321-8ad8-4412-a54c-7102790e99c0
keywords:
- GetLastWriteTimeFromKey method Direct Write
- GetLastWriteTimeFromKey method Direct Write , IDWriteLocalFontFileLoader interface
- IDWriteLocalFontFileLoader interface Direct Write , GetLastWriteTimeFromKey method
topic_type:
- apiref
api_name:
- IDWriteLocalFontFileLoader.GetLastWriteTimeFromKey
api_location:
- dwrite.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IDWriteLocalFontFileLoader::GetLastWriteTimeFromKey method

Obtains the last write time of the file from the font file reference key.

## Syntax


```C++
virtual HRESULT GetLastWriteTimeFromKey(
  [in]  const void     *fontFileReferenceKey,
              UINT32   fontFileReferenceKeySize,
  [out]       FILETIME *lastWriteTime
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

*lastWriteTime* \[out\]
</dt> <dd>

Type: **FILETIME\***

The time of the last font file modification.

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

 

 





