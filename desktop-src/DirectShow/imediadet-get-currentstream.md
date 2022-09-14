---
description: The get\_CurrentStream method retrieves the stream number currently used by the media detector.
ms.assetid: 0f590498-e639-4b6b-be1d-f1e4a36282cb
title: IMediaDet::get_CurrentStream method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMediaDet.get_CurrentStream
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IMediaDet::get\_CurrentStream method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `get_CurrentStream` method retrieves the stream number currently used by the media detector.

## Syntax


```C++
HRESULT get_CurrentStream(
  [out, retval] long *pVal
);
```



## Parameters

<dl> <dt>

*pVal* \[out, retval\]
</dt> <dd>

Receives the current stream number.

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

 

 




