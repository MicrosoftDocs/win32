---
title: IWmsStationPresenter OnError method
description: Called by MultiPoint Services when an IWmsStationPresenter method returns an error.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 619c34f6-628a-4db3-b59d-fb53dbc89b94
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- OnError method
- OnError method, IWmsStationPresenter interface
- IWmsStationPresenter interface, OnError method
topic_type:
- apiref
api_name:
- IWmsStationPresenter.OnError
api_location:
- WmsStationPresenter.idl
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IWmsStationPresenter::OnError method

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Called by MultiPoint Services when an [**IWmsStationPresenter**](iwmsstationpresenter.md) method returns an error.

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
| IID<br/>                      | IID\_IWmsStationPresenter is defined as 2e855d99-1ccb-4c17-afb0-bdc0033a383e<br/>            |



## See also

<dl> <dt>

[**IWmsStationPresenter**](iwmsstationpresenter.md)
</dt> <dt>

[**WmsCustomPresenterErrorCode**](wmscustompresentererrorcode.md)
</dt> </dl>

 

 





