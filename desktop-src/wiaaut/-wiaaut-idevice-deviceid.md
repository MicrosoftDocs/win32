---
title: Device.DeviceID property
description: Retrieves the DeviceID (Device) for this Device.
ms.assetid: '1a92e686-942d-47db-baf1-3166815fd2c4'
keywords: ["DeviceID property WIA Automation", "DeviceID property WIA Automation , Device object", "Device object WIA Automation , DeviceID property"]
topic_type:
- apiref
api_name:
- Device.DeviceID
api_location:
- Wiaaut.h
api_type:
- COM
---

# Device.DeviceID property

Retrieves the **DeviceID (Device)** for this [**Device**](-wiaaut-device.md).

This property is read-only.

## Syntax


```VB
Property DeviceID( _
)
```



## Property value

**String** value.

## Examples

The following example shows how to display the name and ID of the selected device.


```
Dim dev 'As Device

Set dev = CommonDialog1.ShowSelectDevice

MsgBox "You selected the following device" & vbCrLf & _
       "Name:" & dev.Properties("Name").Value  & vbCrLf & _
       "DeviceID:" & dev.DeviceID
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**Device**](-wiaaut-device.md)
</dt> <dt>

[**DeviceID (DeviceInfo)**](-wiaaut-ideviceinfo-deviceid.md)
</dt> <dt>

[**OnEvent**](-wiaaut--idevicemanagerevents-onevent.md)
</dt> <dt>

[**RegisterEvent**](-wiaaut-idevicemanager-registerevent.md)
</dt> <dt>

[**RegisterPersistentEvent**](-wiaaut-idevicemanager-registerpersistentevent.md)
</dt> <dt>

[**UnregisterEvent**](-wiaaut-idevicemanager-unregisterevent.md)
</dt> <dt>

[**UnregisterPersistentEvent**](-wiaaut-idevicemanager-unregisterpersistentevent.md)
</dt> </dl>

 

 





