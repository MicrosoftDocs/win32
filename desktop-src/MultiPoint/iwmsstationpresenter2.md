---
title: IWmsStationPresenter2 interface
description: Displays frame buffers from an input device that is connected to the MultiPoint station, and manages the idle notifications for the input device.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a0812a27-a24b-42cc-9321-59da261220ef'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["IWmsStationPresenter2 interface", "IWmsStationPresenter2 interface, described"]
topic_type:
- apiref
api_name:
- IWmsStationPresenter2
api_location:
- WmsStationPresenter.idl
api_type:
- COM
---

# IWmsStationPresenter2 interface

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Displays frame buffers from an input device that is connected to the MultiPoint station, and manages the idle notifications for the input device.

## Members

The **IWmsStationPresenter2** interface inherits from [**IWmsStationPresenter**](iwmsstationpresenter.md). **IWmsStationPresenter2** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWmsStationPresenter2** interface has these methods.



| Method                                                               | Description                                                                                                                                                                                           |
|:---------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**EnterIdleState**](iwmsstationpresenter2-enteridlestate.md)       | Sets a MultiPoint station to an idle state, due inactive input devices. This method was inherited from the [**IWmsStationPresenter**](iwmsstationpresenter.md) interface.<br/>                 |
| [**ExitIdleState**](iwmsstationpresenter2-exitidlestate.md)         | Removes a MultiPoint station from an idle state, due activity from input devices. This method was inherited from the [**IWmsStationPresenter**](iwmsstationpresenter.md) interface.<br/>       |
| [**GetDimensions**](iwmsstationpresenter2-getdimensions.md)         | Retrieves the dimensions of a frame buffer from the input device, in pixels. This method was inherited from the [**IWmsStationPresenter**](iwmsstationpresenter.md) interface.<br/>            |
| [**GetMousePresenter**](iwmsstationpresenter2-getmousepresenter.md) | Retrieves an interface pointer to the mouse to use for the MultiPoint station. This method was inherited from the [**IWmsStationPresenter**](iwmsstationpresenter.md) interface.<br/>          |
| [**OnError**](iwmsstationpresenter2-onerror.md)                     | Called by MultiPoint Services when an [**IWmsStationPresenter**](iwmsstationpresenter.md) method returns an error. This method was inherited from the **IWmsStationPresenter** interface.<br/> |
| [**Present**](iwmsstationpresenter2-present.md)                     | Displays an updated frame buffer from the input device. This method was inherited from the [**IWmsStationPresenter**](iwmsstationpresenter.md) interface.<br/>                                 |



 

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| IDL<br/>                      | <dl> <dt>WmsStationPresenter.idl</dt> </dl> |
| IID<br/>                      | IID\_IWmsStationPresenter2 is defined as 5c03282a-b68f-476a-ace8-e0736a9d1260<br/>           |



## See also

<dl> <dt>

[MultiPoint Services Interfaces](multipoint-interfaces.md)
</dt> <dt>

[**IWmsStationPresenter**](iwmsstationpresenter.md)
</dt> </dl>

 

 





