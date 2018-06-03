---
title: IWmsStationPresenter GetDimensions method
description: Retrieves the dimensions of a frame buffer from the input device, in pixels.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 32e604e2-9f31-4fbc-9c95-72e0368efb18
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- GetDimensions method
- GetDimensions method, IWmsStationPresenter interface
- IWmsStationPresenter interface, GetDimensions method
topic_type:
- apiref
api_name:
- IWmsStationPresenter.GetDimensions
api_location:
- WmsStationPresenter.idl
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IWmsStationPresenter::GetDimensions method

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Retrieves the dimensions of a frame buffer from the input device, in pixels.

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
| IID<br/>                      | IID\_IWmsStationPresenter is defined as 2e855d99-1ccb-4c17-afb0-bdc0033a383e<br/>            |



## See also

<dl> <dt>

[**IWmsStationPresenter**](iwmsstationpresenter.md)
</dt> </dl>

 

 





