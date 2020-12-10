---
title: IMsRdpClientAdvancedSettings7 EnableSuperPan property
description: Specifies or retrieves a Boolean value that indicates whether SuperPan is enabled or disabled.
ms.assetid: 0d0ef89e-75f5-460a-ad55-01f8d9478df5
ms.tgt_platform: multiple
keywords:
- EnableSuperPan property Remote Desktop Services
- EnableSuperPan property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , EnableSuperPan property
- EnableSuperPan property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , EnableSuperPan property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings7.EnableSuperPan
- IMsRdpClientAdvancedSettings7.get_EnableSuperPan
- IMsRdpClientAdvancedSettings7.put_EnableSuperPan
- IMsRdpClientAdvancedSettings8.EnableSuperPan
- IMsRdpClientAdvancedSettings8.get_EnableSuperPan
- IMsRdpClientAdvancedSettings8.put_EnableSuperPan
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings7::EnableSuperPan property

Specifies or retrieves a Boolean value that indicates whether SuperPan is enabled or disabled. SuperPan is a feature that allows a user to easily navigate a remote desktop in full-screen mode, when the dimensions of the remote desktop are larger than the dimensions of the current client window. Instead of using scroll bars to navigate the desktop, the user can point to the window border, and the remote desktop will scroll automatically in that direction. SuperPan does not support more than one monitor.

This property is read/write.

## Syntax


```C++
HRESULT put_EnableSuperPan(
  [in]          VARIANT_BOOL fEnableSuperPan
);

HRESULT get_EnableSuperPan(
  [out, retval] VARIANT_BOOL *pfEnableSuperPan
);
```



## Property value

A **VARIANT\_BOOL** value that specifies whether SuperPan is enabled. A value of **VARIANT\_TRUE** specifies that SuperPan is enabled.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                             |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                                |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>           |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>           |
| IID<br/>                      | IID\_IMsRdpClientAdvancedSettings7 is defined as 26036036-4010-4578-8091-0db9a1edf9c3<br/> |



## See also

<dl> <dt>

[**IMsRdpClientAdvancedSettings8**](imsrdpclientadvancedsettings8.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings7**](imsrdpclientadvancedsettings7.md)
</dt> </dl>

 

 





