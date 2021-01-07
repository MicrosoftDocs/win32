---
description: Defines a single callback method.
ms.assetid: 579f7a29-cd98-4d97-9f8e-9b786897df1c
title: IConnectionRequestCallback interface (Devpkey.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IConnectionRequestCallback
api_type: 
- COM
api_location: 
- PortableDeviceGuids.lib
- PortableDeviceGuids.dll
---

# IConnectionRequestCallback interface

The **IConnectionRequestCallback** interface defines a single callback method. A Windows Portable Devices (WPD) application implements this optional Component Object Model (COM) interface to receive notifications about completed requests and to cancel pending requests. The requests are sent using the[**IPortableDeviceConnector::Connect**](/windows/desktop/api/portabledeviceconnectapi/nf-portabledeviceconnectapi-iportabledeviceconnector-connect) and [**IPortableDeviceConnector::Disconnect**](/windows/desktop/api/portabledeviceconnectapi/nf-portabledeviceconnectapi-iportabledeviceconnector-disconnect) methods.

## Members

The **IConnectionRequestCallback** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IConnectionRequestCallback** also has these types of members:

-   [Methods](#methods)

### Methods

The **IConnectionRequestCallback** interface has these methods.



| Method                                                      | Description                                                                           |
|:------------------------------------------------------------|:--------------------------------------------------------------------------------------|
| [**OnComplete**](iconnectionrequestcallback-oncomplete.md) | Notifies an application that a previously scheduled request has completed.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                                                                                             |
| Minimum supported server<br/> | None supported<br/>                                                                                                                                              |
| Header<br/>                   | <dl> <dt>Devpkey.h; </dt> <dt>Portabledeviceconnectapi.h</dt> </dl> |
| IDL<br/>                      | <dl> <dt>Portabledeviceconnectapi.idl</dt> </dl>                                                                |
| Library<br/>                  | <dl> <dt>PortableDeviceGuids.lib</dt> </dl>                                                                     |



 

