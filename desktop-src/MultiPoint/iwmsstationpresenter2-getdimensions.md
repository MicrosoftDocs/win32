---
title: IWmsStationPresenter2 GetDimensions method
description: Retrieves the dimensions of a frame buffer from the input device, in pixels. This method was inherited from the IWmsStationPresenter interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: D7A754F9-0F4A-490D-A288-0304628058A7
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- GetDimensions method
- GetDimensions method, IWmsStationPresenter2 interface
- IWmsStationPresenter2 interface, GetDimensions method
topic_type:
- apiref
api_name:
- IWmsStationPresenter2.GetDimensions
api_location:
- WmsStationPresenter.idl
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IWmsStationPresenter2::GetDimensions method

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Retrieves the dimensions of a frame buffer from the input device, in pixels. This method was inherited from the [**IWmsStationPresenter**](iwmsstationpresenter.md) interface.

## Syntax


```C++
HRESULT GetDimensions(
  [out] UINT *pcx,
  [out] UINT *pcy
);
```



## Parameters

<dl> <dt>

*pcx* \[out\]
</dt> <dd>

On successful return, receives a pointer to the width of the frame buffer, in pixels.

</dd> <dt>

*pcy* \[out\]
</dt> <dd>

On successful return, receives a pointer to the height of the frame buffer, in pixels.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| IDL<br/>                      | <dl> <dt>WmsStationPresenter.idl</dt> </dl> |
| IID<br/>                      | IID\_IWmsStationPresenter2 is defined as 5c03282a-b68f-476a-ace8-e0736a9d1260<br/>           |



## See also

<dl> <dt>

[**IWmsStationPresenter2**](iwmsstationpresenter2.md)
</dt> </dl>

 

 





