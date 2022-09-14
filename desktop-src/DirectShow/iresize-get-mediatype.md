---
description: The get\_MediaType method returns the resizer filter's current output media type.
ms.assetid: b9900f7c-05f6-47e4-9cb0-683df2aea404
title: IResize::get_MediaType method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IResize.get_MediaType
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IResize::get\_MediaType method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `get_MediaType` method returns the resizer filter's current output media type.

## Syntax


```C++
HRESULT get_MediaType(
  [out] AM_MEDIA_TYPE *pmt
);
```



## Parameters

<dl> <dt>

*pmt* \[out\]
</dt> <dd>

Pointer to an [**AM\_MEDIA\_TYPE**](/windows/win32/api/strmif/ns-strmif-am_media_type) structure allocated by the caller. The method fills this structure with the media type. The caller must release the format block, if any.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

If the output media type has not been set, return a default media type. The filter must update its output media type when the **put\_MediaType** or **put\_Size** methods are called; the media type returned by `get_MediaType` must reflect these changes.

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Version<br/> | DirectX 9.0 or later<br/>                                                         |
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



## See also

<dl> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> <dt>

[**IResize Interface**](iresize.md)
</dt> </dl>

 

 




