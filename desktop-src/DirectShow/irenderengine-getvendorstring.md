---
description: The GetVendorString method retrieves the name of the vendor. For the render engine objects that are provided by DirectShow, the vendor string is &\#0034;Microsoft Corporation&\#0034;.
ms.assetid: d0a4c525-67dc-419a-b4d6-8cd51888fd8a
title: IRenderEngine::GetVendorString method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IRenderEngine.GetVendorString
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IRenderEngine::GetVendorString method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `GetVendorString` method retrieves the name of the vendor. For the render engine objects that are provided by DirectShow, the vendor string is "Microsoft Corporation".

## Syntax


```C++
HRESULT GetVendorString(
  [out, retval] BSTR *pVendorID
);
```



## Parameters

<dl> <dt>

*pVendorID* \[out, retval\]
</dt> <dd>

Receives a **BSTR** containing the vendor string.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The method allocates memory for the string. The application must call **SysFreeString** to free the memory.

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

[**IRenderEngine Interface**](irenderengine.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




