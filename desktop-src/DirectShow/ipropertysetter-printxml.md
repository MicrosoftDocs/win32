---
description: The PrintXML method converts property data into an XML string.
ms.assetid: 24638489-b5ed-4bdd-b40e-6d61c0db1533
title: IPropertySetter::PrintXML method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPropertySetter.PrintXML
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IPropertySetter::PrintXML method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `PrintXML` method converts property data into an XML string.

## Syntax


```C++
HRESULT PrintXML(
  [out] char *pszXML,
  [in]  int  cbXML,
  [out] int  *pcbPrinted,
  [in]  int  indent
);
```



## Parameters

<dl> <dt>

*pszXML* \[out\]
</dt> <dd>

Pointer to a buffer that receives the XML string.

</dd> <dt>

*cbXML* \[in\]
</dt> <dd>

Size of the buffer pointed to by *pszXML*, in bytes.

</dd> <dt>

*pcbPrinted* \[out\]
</dt> <dd>

Pointer to a variable that receives the length of the XML string. Can be **NULL**.

</dd> <dt>

*indent* \[in\]
</dt> <dd>

Number of indent levels for the outermost tag.

</dd> </dl>

## Return value

Returns S\_OK if successful. Otherwise, returns an **HRESULT** value indicating the cause of the error. If the XML string is longer than the buffer, the method returns E\_OUTOFMEMORY.

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

[**IPropertySetter Interface**](ipropertysetter.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




