---
title: IWmsPresentationDevice OnError method
description: Called by MultiPoint Services when an IWmsPresentationDevice method returns an error.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 34b13656-463e-485d-9ce8-3d60389d6794
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- OnError method
- OnError method, IWmsPresentationDevice interface
- IWmsPresentationDevice interface, OnError method
topic_type:
- apiref
api_name:
- IWmsPresentationDevice.OnError
api_location:
- WmsStationPresenter.idl
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IWmsPresentationDevice::OnError method

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Called by MultiPoint Services when an [**IWmsPresentationDevice**](iwmspresentationdevice.md) method returns an error.

## Syntax


```C++
HRESULT OnError(
  [in] WmsCustomPresenterErrorCode eError
);
```



## Parameters

<dl> <dt>

*eError* \[in\]
</dt> <dd>

The error code returned by the method.

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

[**WmsCustomPresenterErrorCode**](wmscustompresentererrorcode.md)
</dt> </dl>

 

 





