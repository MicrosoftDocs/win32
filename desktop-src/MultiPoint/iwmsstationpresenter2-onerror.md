---
title: IWmsStationPresenter2 OnError method
description: Called by MultiPoint Services when an IWmsStationPresenter method returns an error. This method was inherited from the IWmsStationPresenter interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: F4A86C4E-633E-4FA3-A470-36EC9FC085ED
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- OnError method
- OnError method, IWmsStationPresenter2 interface
- IWmsStationPresenter2 interface, OnError method
topic_type:
- apiref
api_name:
- IWmsStationPresenter2.OnError
api_location:
- WmsStationPresenter.idl
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IWmsStationPresenter2::OnError method

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Called by MultiPoint Services when an [**IWmsStationPresenter**](iwmsstationpresenter.md) method returns an error. This method was inherited from the **IWmsStationPresenter** interface.

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
| IID<br/>                      | IID\_IWmsStationPresenter2 is defined as 5c03282a-b68f-476a-ace8-e0736a9d1260<br/>           |



## See also

<dl> <dt>

[**IWmsStationPresenter2**](iwmsstationpresenter2.md)
</dt> <dt>

[**WmsCustomPresenterErrorCode**](wmscustompresentererrorcode.md)
</dt> </dl>

 

 





