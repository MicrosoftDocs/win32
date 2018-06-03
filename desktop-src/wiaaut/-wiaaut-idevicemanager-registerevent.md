---
title: DeviceManager.RegisterEvent method
description: Registers the specified EventID Constants for the specified DeviceID. If DeviceID is \ 0034;\ \ 0034; then OnEvent is called whenever the event specified occurs for any device. Otherwise, OnEvent is only called if the event specified occurs on the device specified.
ms.assetid: 7186244e-0387-4206-8a9e-f379e566827e
keywords:
- RegisterEvent method WIA Automation
- RegisterEvent method WIA Automation , DeviceManager object
- DeviceManager object WIA Automation , RegisterEvent method
topic_type:
- apiref
api_name:
- DeviceManager.RegisterEvent
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

# DeviceManager.RegisterEvent method

Registers the specified [**EventID Constants**](-wiaaut-consts-eventid.md) for the specified *DeviceID*. If *DeviceID* is "\*" then [**OnEvent**](-wiaaut--idevicemanagerevents-onevent.md) is called whenever the event specified occurs for any device. Otherwise, **OnEvent** is only called if the event specified occurs on the device specified.

## Syntax


```VB
DeviceManager.RegisterEvent( _
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

> \[!Warning\]  
> Using the [**IWiaDevMgr::RegisterEventCallbackInterface**](https://msdn.microsoft.com/library/windows/desktop/ms630146), [**IWiaDevMgr2::RegisterEventCallbackInterface**](https://msdn.microsoft.com/library/windows/desktop/ms630135), and **DeviceManager.RegisterEvent** methods from the same process after the Still Image Service is restarted may cause an access violation, if the functions were used before the service was stopped.

 

For example code, see [Download New Items as They are Created](https://www.bing.com/search?q=Download New Items as They are Created) in Shared Samples.

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

[**RegisterPersistentEvent**](-wiaaut-idevicemanager-registerpersistentevent.md)
</dt> <dt>

[**UnregisterEvent**](-wiaaut-idevicemanager-unregisterevent.md)
</dt> <dt>

[**UnregisterPersistentEvent**](-wiaaut-idevicemanager-unregisterpersistentevent.md)
</dt> <dt>

[**EventID Constants**](-wiaaut-consts-eventid.md)
</dt> </dl>

 

 





