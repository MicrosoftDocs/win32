---
title: DeviceManager.UnregisterEvent method
description: Unregisters the specified EventID for the specified DeviceID. UnregisterEvent should only be called for the EventID and DeviceID for which you called RegisterEvent.
ms.assetid: 0f234e87-34e5-4767-9fb4-8176fce48f27
keywords:
- UnregisterEvent method WIA Automation
- UnregisterEvent method WIA Automation , DeviceManager object
- DeviceManager object WIA Automation , UnregisterEvent method
topic_type:
- apiref
api_name:
- DeviceManager.UnregisterEvent
api_location:
- Wiaaut.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DeviceManager.UnregisterEvent method

Unregisters the specified *EventID* for the specified *DeviceID*. **UnregisterEvent** should only be called for the *EventID* and *DeviceID* for which you called [**RegisterEvent**](-wiaaut-idevicemanager-registerevent.md).

## Syntax


```VB
DeviceManager.UnregisterEvent( _
  ByVal EventID As BSTR, _
  [ ByVal DeviceID As BSTR ] _
) As HRESULT
```



## Parameters

<dl> <dt>

*EventID* \[in\]
</dt> <dd>

Type: **BSTR**

Required. **String** value.

</dd> <dt>

*DeviceID* \[in, optional\]
</dt> <dd>

Type: **BSTR**

**String** value.



| Value                                                                                                                               | Meaning              |
|-------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| <dl> <dt></dt> <dt>\*</dt> </dl> | Default. <br/> |



 

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Unlike [**UnregisterPersistentEvent**](-wiaaut-idevicemanager-unregisterpersistentevent.md), **UnregisterEvent** does not need to be called because all events are unregistered automatically when the application exits.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



## See also

<dl> <dt>

**Reference**
</dt> <dt>

[**DeviceID (Device)**](-wiaaut-idevice-deviceid.md)
</dt> <dt>

[**EventID**](-wiaaut-ideviceevent-eventid.md)
</dt> <dt>

[**DeviceID (DeviceInfo)**](-wiaaut-ideviceinfo-deviceid.md)
</dt> <dt>

[**DeviceManager**](-wiaaut-devicemanager.md)
</dt> <dt>

[**OnEvent**](-wiaaut--idevicemanagerevents-onevent.md)
</dt> <dt>

[**RegisterEvent**](-wiaaut-idevicemanager-registerevent.md)
</dt> <dt>

[**RegisterPersistentEvent**](-wiaaut-idevicemanager-registerpersistentevent.md)
</dt> <dt>

[**UnregisterPersistentEvent**](-wiaaut-idevicemanager-unregisterpersistentevent.md)
</dt> <dt>

[**EventID Constants**](-wiaaut-consts-eventid.md)
</dt> </dl>

 

 





