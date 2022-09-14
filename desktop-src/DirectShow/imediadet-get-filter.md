---
description: The get\_Filter method retrieves a pointer to the source filter currently used by the media detector.
ms.assetid: 23d603c1-445d-425a-973e-7bfe0a2d19f2
title: IMediaDet::get_Filter method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMediaDet.get_Filter
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IMediaDet::get\_Filter method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `get_Filter` method retrieves a pointer to the source filter currently used by the media detector.

## Syntax


```C++
HRESULT get_Filter(
  [out, retval] IUnknown **ppVal
);
```



## Parameters

<dl> <dt>

*ppVal* \[out, retval\]
</dt> <dd>

Receives a pointer to the filter's **IUnknown** interface. If no source filter is in use, the value is set to **NULL**.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

When the method returns, if *\*ppVal* is not **NULL**, the **IUnknown** interface has an outstanding reference count. Release the interface when you are finished using it.

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

 

 




