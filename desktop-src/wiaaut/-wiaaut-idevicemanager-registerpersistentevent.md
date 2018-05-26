---
title: DeviceManager.RegisterPersistentEvent method
description: Registers the specified Command to launch when the specified EventID for the specified DeviceID occurs. Command can be either a class identifier (CLSID) or the full path name and the appropriate command-line arguments needed to invoke the application.
ms.assetid: 36f03e68-1724-4375-9331-c2749c31db93
keywords:
- RegisterPersistentEvent method WIA Automation
- RegisterPersistentEvent method WIA Automation , DeviceManager object
- DeviceManager object WIA Automation , RegisterPersistentEvent method
topic_type:
- apiref
api_name:
- DeviceManager.RegisterPersistentEvent
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

# DeviceManager.RegisterPersistentEvent method

Registers the specified *Command* to launch when the specified *EventID* for the specified *DeviceID* occurs. *Command* can be either a class identifier (CLSID) or the full path name and the appropriate command-line arguments needed to invoke the application.

## Syntax


```VB
DeviceManager.RegisterPersistentEvent( _
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

The **RegisterPersistentEvent** method requires Administrator permission to function successfully.

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

[**UnregisterEvent**](-wiaaut-idevicemanager-unregisterevent.md)
</dt> <dt>

[**UnregisterPersistentEvent**](-wiaaut-idevicemanager-unregisterpersistentevent.md)
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

 

 





