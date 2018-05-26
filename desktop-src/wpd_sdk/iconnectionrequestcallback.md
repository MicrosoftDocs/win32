---
Description: Defines a single callback method.
ms.assetid: 579f7a29-cd98-4d97-9f8e-9b786897df1c
title: IConnectionRequestCallback interface
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IConnectionRequestCallback interface

The **IConnectionRequestCallback** interface defines a single callback method. A Windows Portable Devices (WPD) application implements this optional Component Object Model (COM) interface to receive notifications about completed requests and to cancel pending requests. The requests are sent using the[**IPortableDeviceConnector::Connect**](/windows/win32/portabledeviceconnectapi/nf-portabledeviceconnectapi-iportabledeviceconnector-connect?branch=master) and [**IPortableDeviceConnector::Disconnect**](/windows/win32/portabledeviceconnectapi/nf-portabledeviceconnectapi-iportabledeviceconnector-disconnect?branch=master) methods.

## Members

The **IConnectionRequestCallback** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **IConnectionRequestCallback** also has these types of members:

-   [Methods](#methods)

### Methods

The **IConnectionRequestCallback** interface has these methods.



| Method                                                      | Description                                                                           |
|:------------------------------------------------------------|:--------------------------------------------------------------------------------------|
| [**OnComplete**](iconnectionrequestcallback-oncomplete.md) | Notifies an application that a previously scheduled request has completed.<br/> |



 

## Requirements



|                                     |                                                                                                                                                                        |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                                                                                             |
| Minimum supported server<br/> | None supported<br/>                                                                                                                                              |
| Header<br/>                   | <dl> <dt>Devpkey.h; </dt> <dt>Portabledeviceconnectapi.h</dt> </dl> |
| IDL<br/>                      | <dl> <dt>Portabledeviceconnectapi.idl</dt> </dl>                                                                |
| Library<br/>                  | <dl> <dt>PortableDeviceGuids.lib</dt> </dl>                                                                     |



 

 




