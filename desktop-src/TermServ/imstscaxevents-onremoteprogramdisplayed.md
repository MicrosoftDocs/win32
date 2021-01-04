---
title: IMsTscAxEvents OnRemoteProgramDisplayed method
description: Called when a RemoteApp program is displayed.
ms.assetid: 24f5ea52-0c13-4024-9448-5c2c1896ca8b
ms.tgt_platform: multiple
keywords:
- OnRemoteProgramDisplayed method Remote Desktop Services
- OnRemoteProgramDisplayed method Remote Desktop Services , IMsTscAxEvents interface
- IMsTscAxEvents interface Remote Desktop Services , OnRemoteProgramDisplayed method
topic_type:
- apiref
api_name:
- IMsTscAxEvents.OnRemoteProgramDisplayed
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAxEvents::OnRemoteProgramDisplayed method

Called when a RemoteApp program is displayed.

## Syntax


```C++
VOID OnRemoteProgramDisplayed(
  [in] VARIANT_BOOL vbDisplayed,
  [in] ULONG        uDisplayInformation
);
```



## Parameters

<dl> <dt>

*vbDisplayed* \[in\]
</dt> <dd>

Indicates whether the RemoteApp program is displayed or hidden.

</dd> <dt>

*uDisplayInformation* \[in\]
</dt> <dd>

The display information.

<dt>

<span id="RAIL_APPDISPLAY_AUTORECONNECT"></span><span id="rail_appdisplay_autoreconnect"></span>

<span id="RAIL_APPDISPLAY_AUTORECONNECT"></span><span id="rail_appdisplay_autoreconnect"></span>**RAIL\_APPDISPLAY\_AUTORECONNECT**


</dt> <dd>

Automatic reconnect is in progress.

</dd> <dt>

<span id="RAIL_APPDISPLAY_DESKTOPHOOKED"></span><span id="rail_appdisplay_desktophooked"></span>

<span id="RAIL_APPDISPLAY_DESKTOPHOOKED"></span><span id="rail_appdisplay_desktophooked"></span>**RAIL\_APPDISPLAY\_DESKTOPHOOKED**


</dt> <dd>

The RemoteApp count just went to zero.

</dd> </dl> </dd> </dl>

## Return value

This method does not return a value.

## Remarks

Implement this method in your event sink to receive notification that a RemoteApp has been displayed.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IMsTscAxEvents is defined as 336d5562-efa8-482e-8cb3-c5c0fc7a7db6<br/>           |



 

 





