---
title: IWmsPresentationDevice GetInstanceId method
description: Retrieves the unique ID of the monitor.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 696e95b2-04ea-40b6-bcf5-e24df1b1a8c2
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- GetInstanceId method
- GetInstanceId method, IWmsPresentationDevice interface
- IWmsPresentationDevice interface, GetInstanceId method
topic_type:
- apiref
api_name:
- IWmsPresentationDevice.GetInstanceId
api_location:
- WmsStationPresenter.idl
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IWmsPresentationDevice::GetInstanceId method

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Retrieves the unique ID of the monitor.

## Syntax


```C++
HRESULT GetInstanceId(
  [out] GUID *pInstanceId
);
```



## Parameters

<dl> <dt>

*pInstanceId* \[out\]
</dt> <dd>

On successful return, receives a pointer to the ID of the monitor.

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
</dt> </dl>

 

 





