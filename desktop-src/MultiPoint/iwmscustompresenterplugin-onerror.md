---
title: IWmsCustomPresenterPlugin OnError method
description: Called by MultiPoint Services when an IWmsCustomPresenterPlugin method returns an error.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ace6d271-e93e-4ecf-b89e-6e385137a40f'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["OnError method", "OnError method, IWmsCustomPresenterPlugin interface", "IWmsCustomPresenterPlugin interface, OnError method"]
topic_type:
- apiref
api_name:
- IWmsCustomPresenterPlugin.OnError
api_location:
- WmsStationPresenter.idl
api_type:
- COM
---

# IWmsCustomPresenterPlugin::OnError method

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Called by MultiPoint Services when an [**IWmsCustomPresenterPlugin**](iwmscustompresenterplugin.md) method returns an error.

## Syntax


```C++
HRESULT OnError(
  [in] WmsCustomPresenterErrorCode eError
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
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| IDL<br/>                      | <dl> <dt>WmsStationPresenter.idl</dt> </dl> |
| IID<br/>                      | IID\_IWmsCustomPresenterPlugin is defined as 3110a841-1256-4c62-ad83-ef72a529c5b5<br/>       |



## See also

<dl> <dt>

[**IWmsCustomPresenterPlugin**](iwmscustompresenterplugin.md)
</dt> <dt>

[**WmsCustomPresenterErrorCode**](wmscustompresentererrorcode.md)
</dt> </dl>

 

 





