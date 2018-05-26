---
title: DeviceManager.UnregisterPersistentEvent method
description: Unregisters the specified Command for the specified EventID for the specified DeviceID. UnregisterPersistentEvent should only be called for the Command, Name, Description, Icon, EventID, and DeviceID for which you called RegisterPersistentEvent.
ms.assetid: 6e4842c2-f3fc-4883-9b5a-63b852693993
keywords:
- UnregisterPersistentEvent method WIA Automation
- UnregisterPersistentEvent method WIA Automation , DeviceManager object
- DeviceManager object WIA Automation , UnregisterPersistentEvent method
topic_type:
- apiref
api_name:
- DeviceManager.UnregisterPersistentEvent
api_location:
- Wiaaut.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DeviceManager.UnregisterPersistentEvent method

Unregisters the specified *Command* for the specified *EventID* for the specified *DeviceID*. **UnregisterPersistentEvent** should only be called for the *Command*, *Name*, *Description*, *Icon*, *EventID*, and *DeviceID* for which you called [**RegisterPersistentEvent**](-wiaaut-idevicemanager-registerpersistentevent.md).

## Syntax


```VB
DeviceManager.UnregisterPersistentEvent( _
  ByVal Command As BSTR, _
  ByVal Name As BSTR, _
  ByVal Description As BSTR, _
  ByVal Icon As BSTR, _
  ByVal EventID As BSTR, _
  [ ByVal DeviceID As BSTR ] _
) As HRESULT
```



## Parameters

<dl> <dt>

*Command* \[in\]
</dt> <dd>

Type: **BSTR**

Required. **String** value.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

Type: **BSTR**

Required. **String** value.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

Type: **BSTR**

Required. **String** value.

</dd> <dt>

*Icon* \[in\]
</dt> <dd>

Type: **BSTR**

Required. **String** value.

</dd> <dt>

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

For example code, see [Implement a Windows Script Host Script that Runs Automatically](-wiaaut-shared-samples.md#implement-a-windows-script-host-script-that-runs-automatically) in Shared Samples.

The **UnregisterPersistentEvent** method requires Administrator permission to function successfully.

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

[**Description (DeviceCommand)**](-wiaaut-idevicecommand-description.md)
</dt> <dt>

[**Name (DeviceCommand)**](-wiaaut-idevicecommand-name.md)
</dt> <dt>

[**Description (DeviceEvent)**](-wiaaut-ideviceevent-description.md)
</dt> <dt>

[**EventID**](-wiaaut-ideviceevent-eventid.md)
</dt> <dt>

[**Name (DeviceEvent)**](-wiaaut-ideviceevent-name.md)
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

[**UnregisterEvent**](-wiaaut-idevicemanager-unregisterevent.md)
</dt> <dt>

[**EventID Constants**](-wiaaut-consts-eventid.md)
</dt> <dt>

[**Description (Filter)**](-wiaaut-ifilter-description.md)
</dt> <dt>

[**Name (Filter)**](-wiaaut-ifilter-name.md)
</dt> <dt>

[**Description (FilterInfo)**](-wiaaut-ifilterinfo-description.md)
</dt> <dt>

[**Name (FilterInfo)**](-wiaaut-ifilterinfo-name.md)
</dt> <dt>

[**Add (Items)**](-wiaaut-iitems-add.md)
</dt> <dt>

[**Name (Property)**](-wiaaut-iproperty-name.md)
</dt> </dl>

 

 





