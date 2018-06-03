---
title: IWmsStationPresenter2 GetMousePresenter method
description: Retrieves an interface pointer to the mouse to use for the MultiPoint station. This method was inherited from the IWmsStationPresenter interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: C4AC262C-F8EB-4EE9-91C5-1AB078135F03
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- GetMousePresenter method
- GetMousePresenter method, IWmsStationPresenter2 interface
- IWmsStationPresenter2 interface, GetMousePresenter method
topic_type:
- apiref
api_name:
- IWmsStationPresenter2.GetMousePresenter
api_location:
- WmsStationPresenter.idl
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IWmsStationPresenter2::GetMousePresenter method

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Retrieves an interface pointer to the mouse to use for the MultiPoint station. This method was inherited from the [**IWmsStationPresenter**](iwmsstationpresenter.md) interface.

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
| IID<br/>                      | IID\_IWmsStationPresenter2 is defined as 5c03282a-b68f-476a-ace8-e0736a9d1260<br/>           |



## See also

<dl> <dt>

[**IWmsStationPresenter2**](iwmsstationpresenter2.md)
</dt> <dt>

[**IWmsStationMousePresenter**](iwmsstationmousepresenter.md)
</dt> </dl>

 

 





