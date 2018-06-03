---
title: DeviceManager.OnEvent event
description: Fires for any event registered with RegisterEvent.
ms.assetid: fa3a7098-6331-490e-87d8-77351e531855
keywords:
- OnEvent event WIA Automation
- OnEvent event WIA Automation , DeviceManager object
- DeviceManager object WIA Automation , OnEvent event
topic_type:
- apiref
api_name:
- DeviceManager.OnEvent
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

# DeviceManager.OnEvent event

Fires for any event registered with [**RegisterEvent**](-wiaaut-idevicemanager-registerevent.md).

## Syntax


```VB
DeviceManager.OnEvent( _
  ByVal EventID As BSTR, _
  ByVal DeviceID As BSTR, _
  ByVal ItemID As BSTR _
)
```



## Parameters

<dl> <dt>

*EventID* \[in\]
</dt> <dd>

Required. **String** value.

</dd> <dt>

*DeviceID* \[in\]
</dt> <dd>

Required. **String** value.

</dd> <dt>

*ItemID* \[in\]
</dt> <dd>

Required. **String** value.

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

For example code, see [Display all the Properties for the Selected Device](https://www.bing.com/search?q=Display all the Properties for the Selected Device) in Shared Samples.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wiaaut.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wiaaut.idl</dt> </dl> |



 

 





