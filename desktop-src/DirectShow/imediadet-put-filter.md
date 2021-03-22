---
description: The put\_Filter method specifies a source filter for the media detector to use.
ms.assetid: 59382cb0-c472-48b8-9cc5-52f9dbc61a07
title: IMediaDet::put_Filter method (Qedit.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IMediaDet.put_Filter
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
---

# IMediaDet::put\_Filter method

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `put_Filter` method specifies a source filter for the media detector to use.

> [!IMPORTANT]
> Do not add the source filter to your own filter graph, or use a filter that is already in a filter graph. The media detector object automatically builds an internal filter graph, and putting the filter in another graph can cause unexpected results.

 

## Syntax


```C++
HRESULT put_Filter(
  [in] IUnknown *newVal
);
```



## Parameters

<dl> <dt>

*newVal* \[in\]
</dt> <dd>

Pointer to the source filter's **IUnknown** interface.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following:



| Return code                                                                                   | Description                                     |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Success.<br/>                             |
| <dl> <dt>**E\_NOINTERFACE**</dt> </dl> | *newVal* does not point to a filter.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | **NULL** pointer argument.<br/>           |



 

## Remarks

For most applications, it is simpler to call the [**IMediaDet::put\_Filename**](imediadet-put-filename.md) method with the name of a source file.

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

 

 




