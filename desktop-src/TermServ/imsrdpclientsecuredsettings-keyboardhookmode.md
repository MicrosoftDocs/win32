---
title: IMsRdpClientSecuredSettings KeyboardHookMode property
description: Specifies the keyboard redirection settings, which specify how and when to apply Windows keyboard shortcut (for example, ALT+TAB).
ms.assetid: 16734580-9be9-476b-b8e7-1eca3ba24d61
ms.tgt_platform: multiple
keywords:
- KeyboardHookMode property Remote Desktop Services
- KeyboardHookMode property Remote Desktop Services , IMsRdpClientSecuredSettings interface
- IMsRdpClientSecuredSettings interface Remote Desktop Services , KeyboardHookMode property
topic_type:
- apiref
api_name:
- IMsRdpClientSecuredSettings.KeyboardHookMode
- IMsRdpClientSecuredSettings.get_KeyboardHookMode
- IMsRdpClientSecuredSettings.put_KeyboardHookMode
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientSecuredSettings::KeyboardHookMode property

Specifies the keyboard redirection settings, which specify how and when to apply Windows keyboard shortcut (for example, ALT+TAB).

This property is read/write.

## Syntax


```C++
HRESULT put_KeyboardHookMode(
  [in]  LONG keyboardHookMode
);

HRESULT get_KeyboardHookMode(
  [out] LONG *pkeyboardHookMode
);
```



## Property value

The new settings. This parameter can be one of the following values.

<dt>

0
</dt> <dd>

Apply key combinations only locally at the client computer.

</dd> <dt>

1
</dt> <dd>

Apply key combinations at the remote server.

</dd> <dt>

2
</dt> <dd>

Apply key combinations to the remote server only when the client is running in full-screen mode. This is the default value.

</dd> </dl>

## Error codes

Returns **S\_OK** if successful.

## Remarks

These properties cannot be set when the control is connected.

Refer to [Providing for RDP Client Security](providing-for-rdp-client-security.md) for more information.

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                 |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>         |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>         |
| IID<br/>                      | IID\_IMsRdpClientSecuredSettings is defined as 605befcf-39c1-45cc-a811-068fb7be346d<br/> |



## See also

<dl> <dt>

[**IMsRdpClientSecuredSettings**](imsrdpclientsecuredsettings-interface.md)
</dt> </dl>

 

 





