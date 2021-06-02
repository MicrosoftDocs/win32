---
description: The get\_MaskName method retrieves the name of a JPEG file to be used as the wipe mask.
ms.assetid: b21913c0-4269-41f9-b2f0-ae69be9c0871
title: IDxtJpeg::get_MaskName method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDxtJpeg.get_MaskName
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IDxtJpeg::get\_MaskName method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `get_MaskName` method retrieves the name of a JPEG file to be used as the wipe mask.

## Syntax


```C++
HRESULT get_MaskName(
  [out, retval] BSTR *pVal
);
```



## Parameters

<dl> <dt>

*pVal* \[out, retval\]
</dt> <dd>

Receives the file name.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

If the wipe transition is using one of the built-in SMPTE wipes that it supports, the value of this property is an empty string.

The caller must release the returned string, using the **SysFreeString** function.

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

[**IDxtJpeg Interface**](idxtjpeg.md)
</dt> <dt>

[**IDxtJpeg::get\_MaskNum**](idxtjpeg-get-masknum.md)
</dt> </dl>

 

 




