---
description: The put\_Similarity method specifies the range of color data that becomes transparent. At higher values, a wider range of similar colors is transparent. This property applies only when the key type is DXTKEY\_RGB or DXTKEY\_NONRED.
ms.assetid: f033b226-f36d-4288-b17e-e173546caee1
title: IDxtKey::put_Similarity method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDxtKey.put_Similarity
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IDxtKey::put\_Similarity method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `put_Similarity` method specifies the range of color data that becomes transparent. At higher values, a wider range of similar colors is transparent. This property applies only when the key type is DXTKEY\_RGB or DXTKEY\_NONRED.

## Syntax


```C++
HRESULT put_Similarity(
  [in] int newVal
);
```



## Parameters

<dl> <dt>

*newVal* \[in\]
</dt> <dd>

Specifies the similarity value. The valid range is from 0 to 100.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[**IDxtKey Interface**](idxtkey.md)
</dt> <dt>

[**IDxtKey::put\_KeyType**](idxtkey-put-keytype.md)
</dt> </dl>

 

 




