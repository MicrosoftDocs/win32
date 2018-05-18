---
title: IWmsCustomPresenterPlugin GetPresentationDeviceForHub method
description: Requests that a third-party device present screen data for a USB hub.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '74e295c5-e549-42a2-aebd-1b04744705d9'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["GetPresentationDeviceForHub method", "GetPresentationDeviceForHub method, IWmsCustomPresenterPlugin interface", "IWmsCustomPresenterPlugin interface, GetPresentationDeviceForHub method"]
topic_type:
- apiref
api_name:
- IWmsCustomPresenterPlugin.GetPresentationDeviceForHub
api_location:
- WmsStationPresenter.idl
api_type:
- COM
---

# IWmsCustomPresenterPlugin::GetPresentationDeviceForHub method

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Requests that a third-party device present screen data for a USB hub.

## Syntax


```C++
HRESULT GetPresentationDeviceForHub(
  [in]  BSTR                   bstrUsbHubDeviceInstanceId,
  [out] IWmsPresentationDevice **ppPresentationDevice
);
```



## Parameters

<dl> <dt>

*bstrUsbHubDeviceInstanceId* \[in\]
</dt> <dd>

The ID of the USB hub that is connected to the device.

</dd> <dt>

*ppPresentationDevice* \[out\]
</dt> <dd>

Retrieves a pointer to a pointer to the device that is to present the screen data. To prevent the device from presenting screen data, set this parameter to **NULL**.

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

[**IWmsPresentationDevice**](iwmspresentationdevice.md)
</dt> </dl>

 

 





