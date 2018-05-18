---
title: IWmsStationPresenter2 EnterIdleState method
description: Sets a MultiPoint station to an idle state, due inactive input devices. This method was inherited from the IWmsStationPresenter interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '812a59e4-46ac-4ad9-89b3-c1ad19bbd580'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["EnterIdleState method", "EnterIdleState method, IWmsStationPresenter2 interface", "IWmsStationPresenter2 interface, EnterIdleState method"]
topic_type:
- apiref
api_name:
- IWmsStationPresenter2.EnterIdleState
api_location:
- WmsStationPresenter.idl
api_type:
- COM
---

# IWmsStationPresenter2::EnterIdleState method

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Sets a MultiPoint station to an idle state, due inactive input devices. This method was inherited from the [**IWmsStationPresenter**](iwmsstationpresenter.md) interface.

## Syntax


```C++
HRESULT EnterIdleState();
```



## Parameters

This method has no parameters.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| IDL<br/>                      | <dl> <dt>WmsStationPresenter.idl</dt> </dl> |



## See also

<dl> <dt>

[**IWmsStationPresenter2**](iwmsstationpresenter2.md)
</dt> </dl>

 

 





