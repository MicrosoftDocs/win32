---
description: The get\_StreamTypeB method retrieves a string representing the GUID of the media type for the current stream.
ms.assetid: 99ae4b52-4449-4b7c-babf-1a6cba479499
title: IMediaDet::get_StreamTypeB method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMediaDet.get_StreamTypeB
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IMediaDet::get\_StreamTypeB method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `get_StreamTypeB` method retrieves a string representing the GUID of the media type for the current stream.

## Syntax


```C++
HRESULT get_StreamTypeB(
  [out, retval] BSTR *pVal
);
```



## Parameters

<dl> <dt>

*pVal* \[out, retval\]
</dt> <dd>

Receives a string representation of the media type GUID.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The returned **BSTR** is formatted like the following: `{73647561-0000-0010-8000-00AA00389B71}`

The method allocates memory for the string. The application must call **SysFreeString** to free the memory.

Before calling this method, set the file name and stream by calling [**IMediaDet::put\_Filename**](imediadet-put-filename.md) and [**IMediaDet::put\_CurrentStream**](imediadet-put-currentstream.md).

If the media detector is in bitmap grab mode, this method returns E\_INVALIDARG. For more information, see [**IMediaDet::EnterBitmapGrabMode**](imediadet-enterbitmapgrabmode.md).

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

 

 




