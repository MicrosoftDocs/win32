---
title: IMsTscSecuredSettings Fullscreen property
description: Specifies the full-screen state of the client control.
ms.assetid: f65c2fa3-b2d0-4e64-bf1e-08394c91eda8
ms.tgt_platform: multiple
keywords:
- Fullscreen property Remote Desktop Services
- Fullscreen property Remote Desktop Services , IMsTscSecuredSettings interface
- IMsTscSecuredSettings interface Remote Desktop Services , Fullscreen property
- Fullscreen property Remote Desktop Services , IMsRdpClientSecuredSettings interface
- IMsRdpClientSecuredSettings interface Remote Desktop Services , Fullscreen property
topic_type:
- apiref
api_name:
- IMsTscSecuredSettings.Fullscreen
- IMsTscSecuredSettings.get_Fullscreen
- IMsTscSecuredSettings.put_Fullscreen
- IMsRdpClientSecuredSettings.Fullscreen
- IMsRdpClientSecuredSettings.get_Fullscreen
- IMsRdpClientSecuredSettings.put_Fullscreen
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscSecuredSettings::Fullscreen property

Specifies the full-screen state of the client control.

This property is read/write.

## Syntax


```C++
HRESULT put_Fullscreen(
  [in]  BOOL fFullScreen
);

HRESULT get_Fullscreen(
  [out] BOOL *pfFullScreen
);
```



## Property value

Set this parameter to **TRUE** if the control should use full-screen mode and **FALSE** otherwise.

## Error codes

Returns **S\_OK** if successful.

## Remarks

For more information about this method, see [Providing for RDP Client Security](providing-for-rdp-client-security.md).

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

Note that although the use of this property is restricted to the allowed Internet Explorer URL security zones, a user can always change to full-screen mode after the connection has been established by pressing the full-screen mode [shortcut key](terminal-services-shortcut-keys.md) combination (CTRL+ALT+BREAK).

This method can be called while the client connection is established.

You must call the [**IMsRdpClientNonScriptable3::put\_ConnectionBarText**](imsrdpclientnonscriptable3-connectionbartext.md) method before you call the **IMsTscSecuredSettings::put\_Fullscreen** method or the [**IMsRdpClient::put\_Fullscreen**](imsrdpclient-fullscreen.md) method.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>   |
| IID<br/>                      | IID\_IMsTscSecuredSettings is defined as c9d65442-a0f9-45b2-8f73-d61d2db8cbb6<br/> |



## See also

<dl> <dt>

[**IMsRdpClientSecuredSettings**](imsrdpclientsecuredsettings-interface.md)
</dt> <dt>

[**IMsTscSecuredSettings**](imstscsecuredsettings-interface.md)
</dt> </dl>

 

 





