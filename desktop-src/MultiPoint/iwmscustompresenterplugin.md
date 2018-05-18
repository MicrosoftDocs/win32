---
title: IWmsCustomPresenterPlugin interface
description: Retrieves a custom input device that is connected to a MultiPoint station.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'bcef5b3d-ba6a-4aaa-9ddd-a25f9586d088'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["IWmsCustomPresenterPlugin interface", "IWmsCustomPresenterPlugin interface, described"]
topic_type:
- apiref
api_name:
- IWmsCustomPresenterPlugin
api_location:
- WmsStationPresenter.idl
api_type:
- COM
---

# IWmsCustomPresenterPlugin interface

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Retrieves a custom input device that is connected to a MultiPoint station.

## Members

The **IWmsCustomPresenterPlugin** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IWmsCustomPresenterPlugin** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWmsCustomPresenterPlugin** interface has these methods.



| Method                                                                                       | Description                                                                                             |
|:---------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------|
| [**GetPresentationDeviceForHub**](iwmscustompresenterplugin-getpresentationdeviceforhub.md) | Requests that a third-party device present screen data for a USB hub.<br/>                        |
| [**OnError**](iwmscustompresenterplugin-onerror.md)                                         | Called by MultiPoint Services when an **IWmsCustomPresenterPlugin** method returns an error.<br/> |



 

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| IDL<br/>                      | <dl> <dt>WmsStationPresenter.idl</dt> </dl> |
| IID<br/>                      | IID\_IWmsCustomPresenterPlugin is defined as 3110a841-1256-4c62-ad83-ef72a529c5b5<br/>       |



## See also

<dl> <dt>

[**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509)
</dt> <dt>

[MultiPoint Services Interfaces](multipoint-interfaces.md)
</dt> </dl>

 

 





