---
title: IWmsPresentationDevice interface
description: Displays screen data on a monitor that is connected to the MultiPoint station.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f59c323c-95f7-46c6-999b-68de9b9e3f5c
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- IWmsPresentationDevice interface
- IWmsPresentationDevice interface, described
topic_type:
- apiref
api_name:
- IWmsPresentationDevice
api_location:
- WmsStationPresenter.idl
api_type:
- COM
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IWmsPresentationDevice interface

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Displays screen data on a monitor that is connected to the MultiPoint station.

## Members

The **IWmsPresentationDevice** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IWmsPresentationDevice** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWmsPresentationDevice** interface has these methods.



| Method                                                                          | Description                                                                                                                                                                       |
|:--------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateStationPresenter**](iwmspresentationdevice-createstationpresenter.md) | Creates a [**IWmsStationPresenter**](iwmsstationpresenter.md) instance for an input device, and then displays the cursor at the specified coordinates on the monitor.<br/> |
| [**GetDimensions**](iwmspresentationdevice-getdimensions.md)                   | Retrieves the dimensions of a monitor screen, in pixels.<br/>                                                                                                               |
| [**GetInstanceId**](iwmspresentationdevice-getinstanceid.md)                   | Retrieves the unique ID of the monitor.<br/>                                                                                                                                |
| [**OnError**](iwmspresentationdevice-onerror.md)                               | Called by MultiPoint Services when an **IWmsPresentationDevice** method returns an error.<br/>                                                                              |



 

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| IDL<br/>                      | <dl> <dt>WmsStationPresenter.idl</dt> </dl> |
| IID<br/>                      | IID\_IWmsPresentationDevice is defined as 3fa4b1eb-eb6c-455e-a7ae-0861a26c8fc4<br/>          |



## See also

<dl> <dt>

[**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509)
</dt> <dt>

[MultiPoint Interfaces](multipoint-interfaces.md)
</dt> </dl>

 

 





