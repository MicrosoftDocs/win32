---
description: The put\_Filename method specifies the name of the source file for the media detector to use.
ms.assetid: 37bcc7ed-d2c1-4182-b85a-03bad92c5ba7
title: IMediaDet::put_Filename method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMediaDet.put_Filename
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IMediaDet::put\_Filename method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `put_Filename` method specifies the name of the source file for the media detector to use.

Do not call this method twice on the same MediaDet object. To use this interface with more than one source file, create separate instances of the MediaDet object.

## Syntax


```C++
HRESULT put_Filename(
  [in] BSTR newVal
);
```



## Parameters

<dl> <dt>

*newVal* \[in\]
</dt> <dd>

File name of the source.

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

[**IMediaDet Interface**](imediadet.md)
</dt> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> </dl>

 

 




