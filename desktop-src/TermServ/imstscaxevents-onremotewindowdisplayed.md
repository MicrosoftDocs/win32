---
title: IMsTscAxEvents OnRemoteWindowDisplayed method
description: Called when a RemoteApp window is displayed.
ms.assetid: B1E83486-50CB-4CA4-BD01-2C72938335AF
ms.tgt_platform: multiple
keywords:
- OnRemoteWindowDisplayed method Remote Desktop Services
- OnRemoteWindowDisplayed method Remote Desktop Services , IMsTscAxEvents interface
- IMsTscAxEvents interface Remote Desktop Services , OnRemoteWindowDisplayed method
topic_type:
- apiref
api_name:
- IMsTscAxEvents.OnRemoteWindowDisplayed
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAxEvents::OnRemoteWindowDisplayed method

Called when a RemoteApp window is displayed.

## Syntax


```C++
void OnRemoteWindowDisplayed(
  [in] VARIANT_BOOL                   vbDisplayed,
  [in] HWND                           hwnd,
  [in] RemoteWindowDisplayedAttribute windowAttribute
);
```



## Parameters

<dl> <dt>

*vbDisplayed* \[in\]
</dt> <dd>

Type: **VARIANT\_BOOL**

Indicates whether the RemoteApp window is displayed or hidden.

</dd> <dt>

*hwnd* \[in\]
</dt> <dd>

Type: **HWND**

The handle of the window displayed.

</dd> <dt>

*windowAttribute* \[in\]
</dt> <dd>

Type: **[**RemoteWindowDisplayedAttribute**](remotewindowdisplayedattribute.md)**

A value of the [**RemoteWindowDisplayedAttribute**](remotewindowdisplayedattribute.md) enumeration that specifies more information about the event.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |



## See also

<dl> <dt>

[**RemoteWindowDisplayedAttribute**](remotewindowdisplayedattribute.md)
</dt> <dt>

[**IMsTscAxEvents**](imstscaxevents-interface.md)
</dt> </dl>

 

 





