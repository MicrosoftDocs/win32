---
title: IMsRdpClientSecuredSettings AudioRedirectionMode property
description: Specifies the audio redirection settings, which specify whether to redirect sounds or play sounds at the Remote Desktop Session Host (RD Session Host) server.
ms.assetid: 6aa63a50-a714-4a9b-a4ec-c0551920467a
ms.tgt_platform: multiple
keywords:
- AudioRedirectionMode property Remote Desktop Services
- AudioRedirectionMode property Remote Desktop Services , IMsRdpClientSecuredSettings interface
- IMsRdpClientSecuredSettings interface Remote Desktop Services , AudioRedirectionMode property
topic_type:
- apiref
api_name:
- IMsRdpClientSecuredSettings.AudioRedirectionMode
- IMsRdpClientSecuredSettings.get_AudioRedirectionMode
- IMsRdpClientSecuredSettings.put_AudioRedirectionMode
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientSecuredSettings::AudioRedirectionMode property

Specifies the audio redirection settings, which specify whether to redirect sounds or play sounds at the Remote Desktop Session Host (RD Session Host) server.

This property is read/write.

## Syntax


```C++
HRESULT put_AudioRedirectionMode(
  [in]  LONG audioRedirectionMode
);

HRESULT get_AudioRedirectionMode(
  [out] LONG *paudioRedirectionMode
);
```



## Property value

The new settings. This parameter can be one of the following values.

<dt>

0
</dt> <dd>

Redirect sounds to the client. This is the default value.

</dd> <dt>

1
</dt> <dd>

Play sounds at the remote computer.

</dd> <dt>

2
</dt> <dd>

Disable sound redirection; do not play sounds at the server.

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

 

 





