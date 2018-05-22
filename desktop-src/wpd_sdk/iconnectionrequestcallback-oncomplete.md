---
Description: 'Notifies an application that a previously scheduled Connect or Disconnect request to the MTP/Bluetooth device has completed.'
ms.assetid: '1588d0ec-0d6a-4379-bfdc-4ba5fdaa4665'
title: 'IConnectionRequestCallback::OnComplete method'
---

# IConnectionRequestCallback::OnComplete method

The **OnComplete** method notifies an application that a previously scheduled Connect or Disconnect request to the MTP/Bluetooth device has completed

## Syntax


```C++
HRESULT OnComplete(
  [in] HRESULT hrStatus
);
```



## Parameters

<dl> <dt>

*hrStatus* \[in\]
</dt> <dd>

The status of the request to connect or disconnect a given device.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

An application implements the [**IConnectionRequestCallback**](iconnectionrequestcallback.md) interface to receive notifications about completed requests and to cancel pending requests.

Windows Portable Devices (WPD) calls this method to notify an application that a previously scheduled request has completed. Each request can be tracked and canceled by its application-supplied callback. Therefore, if the application needs to send multiple requests at the same time using the same [**IPortableDeviceConnector**](iportabledeviceconnector.md) object, each request should be passed a unique [**IConnectionRequestCallback**](iconnectionrequestcallback.md) object as the input parameter to the [**IPortableDeviceConnector::Connect**](iportabledeviceconnector-connect.md) and [**IPortableDeviceConnector::Disconnect**](iportabledeviceconnector-disconnect.md) methods.

## Requirements



|                                     |                                                                                                                                                                        |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                                                                                                             |
| Minimum supported server<br/> | None supported<br/>                                                                                                                                              |
| Header<br/>                   | <dl> <dt>Devpkey.h; </dt> <dt>Portabledeviceconnectapi.h</dt> </dl> |
| IDL<br/>                      | <dl> <dt>Portabledeviceconnectapi.idl</dt> </dl>                                                                |
| Library<br/>                  | <dl> <dt>PortableDeviceGuids.lib</dt> </dl>                                                                     |



## See also

<dl> <dt>

[**IConnectionRequestCallback**](iconnectionrequestcallback.md)
</dt> </dl>

 

 




