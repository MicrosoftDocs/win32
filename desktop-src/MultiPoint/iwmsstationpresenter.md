---
title: IWmsStationPresenter interface
description: Displays frame buffers from an input device that is connected to the MultiPoint station.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'be25c95e-8f59-4e81-9714-bed186e9252f'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["IWmsStationPresenter interface", "IWmsStationPresenter interface, described"]
topic_type:
- apiref
api_name:
- IWmsStationPresenter
api_location:
- WmsStationPresenter.idl
api_type:
- COM
---

# IWmsStationPresenter interface

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Displays frame buffers from an input device that is connected to the MultiPoint station.

## Members

The **IWmsStationPresenter** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IWmsStationPresenter** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWmsStationPresenter** interface has these methods.



| Method                                                              | Description                                                                                        |
|:--------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------|
| [**GetDimensions**](iwmsstationpresenter-getdimensions.md)         | Retrieves the dimensions of a frame buffer from the input device, in pixels.<br/>            |
| [**GetMousePresenter**](iwmsstationpresenter-getmousepresenter.md) | Retrieves an interface pointer to the mouse to use for the MultiPoint station.<br/>          |
| [**OnError**](iwmsstationpresenter-onerror.md)                     | Called by MultiPoint Services when an **IWmsStationPresenter** method returns an error.<br/> |
| [**Present**](iwmsstationpresenter-present.md)                     | Displays an updated frame buffer from the input device.<br/>                                 |



 

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| IDL<br/>                      | <dl> <dt>WmsStationPresenter.idl</dt> </dl> |
| IID<br/>                      | IID\_IWmsStationPresenter is defined as 2e855d99-1ccb-4c17-afb0-bdc0033a383e<br/>            |



## See also

<dl> <dt>

[**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509)
</dt> <dt>

[MultiPoint Services Interfaces](multipoint-interfaces.md)
</dt> <dt>

[**IWmsStationPresenter2**](iwmsstationpresenter2.md)
</dt> </dl>

 

 





