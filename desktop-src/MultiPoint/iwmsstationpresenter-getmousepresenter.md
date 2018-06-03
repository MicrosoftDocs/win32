---
title: IWmsStationPresenter GetMousePresenter method
description: Retrieves an interface pointer to the mouse to use for the MultiPoint station.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e4adef0d-1713-437a-92e0-42be04afad54
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- GetMousePresenter method
- GetMousePresenter method, IWmsStationPresenter interface
- IWmsStationPresenter interface, GetMousePresenter method
topic_type:
- apiref
api_name:
- IWmsStationPresenter.GetMousePresenter
api_location:
- WmsStationPresenter.idl
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IWmsStationPresenter::GetMousePresenter method

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Retrieves an interface pointer to the mouse to use for the MultiPoint station.

## Syntax


```C++
HRESULT GetMousePresenter(
  [out] IWmsStationMousePresenter **ppMousePresenter
);
```



## Parameters

<dl> <dt>

*ppMousePresenter* \[out\]
</dt> <dd>

On successful return, receives a pointer to the interface pointer that represents the mouse.

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
</dt> <dt>

[**IWmsStationMousePresenter**](iwmsstationmousepresenter.md)
</dt> </dl>

 

 





