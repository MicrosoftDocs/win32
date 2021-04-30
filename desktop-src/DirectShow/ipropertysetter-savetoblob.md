---
description: The SaveToBlob method saves the property data to a persistence format.
ms.assetid: 48201192-abda-484e-bdb3-442aca52b2bf
title: IPropertySetter::SaveToBlob method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPropertySetter.SaveToBlob
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IPropertySetter::SaveToBlob method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `SaveToBlob` method saves the property data to a persistence format.

## Syntax


```C++
HRESULT SaveToBlob(
  [out] LONG *pcSize,
  [out] BYTE **ppb
);
```



## Parameters

<dl> <dt>

*pcSize* \[out\]
</dt> <dd>

Receives the size of the data, in bytes.

</dd> <dt>

*ppb* \[out\]
</dt> <dd>

Receives a pointer to an array of bytes that receives the data.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The method allocates memory for the byte array. The caller must free it, using the **CoTaskMemFree** function.

All property names and values are truncated to 40 characters in length. For this reason, XML is the preferred persistence format. See [**IXml2Dex Interface**](ixml2dex.md).

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

[**IPropertySetter Interface**](ipropertysetter.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




