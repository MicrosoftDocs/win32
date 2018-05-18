---
title: IWmsStationMousePresenter interface
description: Retrieves mouse cursor updates from a MultiPoint station.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5e5b8e50-257e-41a2-80ab-866e40a7547e'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["IWmsStationMousePresenter interface", "IWmsStationMousePresenter interface, described"]
topic_type:
- apiref
api_name:
- IWmsStationMousePresenter
api_location:
- WmsStationPresenter.idl
api_type:
- COM
---

# IWmsStationMousePresenter interface

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Retrieves mouse cursor updates from a MultiPoint station.

## Members

The **IWmsStationMousePresenter** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IWmsStationMousePresenter** also has these types of members:

-   [Methods](#methods)

### Methods

The **IWmsStationMousePresenter** interface has these methods.



| Method                                                         | Description                                                                                             |
|:---------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------|
| [**OnError**](iwmsstationmousepresenter-onerror.md)           | Called by MultiPoint Services when an **IWmsStationMousePresenter** method returns an error.<br/> |
| [**SetCursor**](iwmsstationmousepresenter-setcursor.md)       | Updates the shape of the mouse cursor.<br/>                                                       |
| [**SetCursorPos**](iwmsstationmousepresenter-setcursorpos.md) | Updates the position of the mouse cursor.<br/>                                                    |
| [**ShowCursor**](iwmsstationmousepresenter-showcursor.md)     | Displays or hides the mouse cursor.<br/>                                                          |



 

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| IDL<br/>                      | <dl> <dt>WmsStationPresenter.idl</dt> </dl> |
| IID<br/>                      | IID\_IWmsStationMousePresenter is defined as a391f331-00f0-4204-9d09-f926917233b0<br/>       |



## See also

<dl> <dt>

[**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509)
</dt> <dt>

[MultiPoint Services Interfaces](multipoint-interfaces.md)
</dt> </dl>

 

 





