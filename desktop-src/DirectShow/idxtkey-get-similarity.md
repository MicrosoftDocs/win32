---
description: The get\_Similarity method retrieves the range of color data that becomes transparent. At higher values, a wider range of similar colors is transparent. This property applies only when the key type is DXTKEY\_RGB or DXTKEY\_NONRED.
ms.assetid: ddf82759-fe71-4e06-b73c-c450b7cce43d
title: IDxtKey::get_Similarity method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDxtKey.get_Similarity
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IDxtKey::get\_Similarity method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `get_Similarity` method retrieves the range of color data that becomes transparent. At higher values, a wider range of similar colors is transparent. This property applies only when the key type is DXTKEY\_RGB or DXTKEY\_NONRED.

## Syntax


```C++
HRESULT get_Similarity(
  [out, retval] int *pVal
);
```



## Parameters

<dl> <dt>

*pVal* \[out, retval\]
</dt> <dd>

Receives the similarity value.

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

[**IDxtKey::get\_KeyType**](idxtkey-get-keytype.md)
</dt> </dl>

 

 




