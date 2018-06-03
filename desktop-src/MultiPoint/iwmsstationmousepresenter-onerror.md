---
title: IWmsStationMousePresenter OnError method
description: Called by MultiPoint Services when an IWmsStationMousePresenter method returns an error.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c8d9d38d-e035-456d-ac13-da19c9d49a0f
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- OnError method
- OnError method, IWmsStationMousePresenter interface
- IWmsStationMousePresenter interface, OnError method
topic_type:
- apiref
api_name:
- IWmsStationMousePresenter.OnError
api_location:
- WmsStationPresenter.idl
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IWmsStationMousePresenter::OnError method

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Called by MultiPoint Services when an [**IWmsStationMousePresenter**](iwmsstationmousepresenter.md) method returns an error.

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
| IID<br/>                      | IID\_IWmsStationMousePresenter is defined as a391f331-00f0-4204-9d09-f926917233b0<br/>       |



## See also

<dl> <dt>

[**IWmsStationMousePresenter**](iwmsstationmousepresenter.md)
</dt> <dt>

[**WmsCustomPresenterErrorCode**](wmscustompresentererrorcode.md)
</dt> </dl>

 

 





