---
title: IWmsStationPresenter2 ExitIdleState method
description: Removes a MultiPoint station from an idle state, due activity from input devices. This method was inherited from the IWmsStationPresenter interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ec67142e-f430-467d-94ec-be71240849b2
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- ExitIdleState method
- ExitIdleState method, IWmsStationPresenter2 interface
- IWmsStationPresenter2 interface, ExitIdleState method
topic_type:
- apiref
api_name:
- IWmsStationPresenter2.ExitIdleState
api_location:
- WmsStationPresenter.idl
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IWmsStationPresenter2::ExitIdleState method

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Removes a MultiPoint station from an idle state, due activity from input devices. This method was inherited from the [**IWmsStationPresenter**](iwmsstationpresenter.md) interface.

## Syntax


```C++
HRESULT ExitIdleState();
```



## Parameters

This method has no parameters.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| IDL<br/>                      | <dl> <dt>WmsStationPresenter.idl</dt> </dl> |



## See also

<dl> <dt>

[**IWmsStationPresenter2**](iwmsstationpresenter2.md)
</dt> </dl>

 

 





