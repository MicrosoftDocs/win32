---
title: IWmsPresentationDevice CreateStationPresenterIWmsStationPresenter method
description: Creates a IWmsStationPresenter instance for an input device, and then displays the cursor at the specified coordinates on the monitor.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4c158e39-6eb7-4cfe-ad02-b3182c1260a7
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- CreateStationPresenterIWmsStationPresenter method
- CreateStationPresenterIWmsStationPresenter method, IWmsPresentationDevice interface
- IWmsPresentationDevice interface, CreateStationPresenterIWmsStationPresenter method
topic_type:
- apiref
api_name:
- IWmsPresentationDevice.CreateStationPresenterIWmsStationPresenter
api_location:
- WmsStationPresenter.idl
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IWmsPresentationDevice::CreateStationPresenterIWmsStationPresenter method

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Creates a [**IWmsStationPresenter**](iwmsstationpresenter.md) instance for an input device, and then displays the cursor at the specified coordinates on the monitor.

## Syntax


```C++
HRESULT CreateStationPresenterIWmsStationPresenter(
  [in]  UINT cxOffset,
  [in]  UINT cx,
  [in]  UINT cy,
  [out]      **ppPresenter
);
```



## Parameters

<dl> <dt>

*cxOffset* \[in\]
</dt> <dd>

The x-axis offset, of the cursor coordinates, in pixels.

</dd> <dt>

*cx* \[in\]
</dt> <dd>

The x-axis of the cursor coordinates.

</dd> <dt>

*cy* \[in\]
</dt> <dd>

The y-axis of the cursor coordinates.

</dd> <dt>

*ppPresenter* \[out\]
</dt> <dd>

On successful return, receives a pointer to the interface pointer that represents the input device.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| IDL<br/>                      | <dl> <dt>WmsStationPresenter.idl</dt> </dl> |
| IID<br/>                      | IID\_IWmsPresentationDevice is defined as 3fa4b1eb-eb6c-455e-a7ae-0861a26c8fc4<br/>          |



## See also

<dl> <dt>

[**IWmsPresentationDevice**](iwmspresentationdevice.md)
</dt> <dt>

[**IWmsStationPresenter**](iwmsstationpresenter.md)
</dt> </dl>

 

 





