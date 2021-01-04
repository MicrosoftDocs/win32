---
title: IRemoteDesktopClient Settings property
description: Retrieves the settings object for the Remote Desktop Protocol (RDP) app container client.
ms.assetid: 59999489-9ad0-4b85-9643-3b8355b817c2
ms.tgt_platform: multiple
keywords:
- Settings property Remote Desktop Services
- Settings property Remote Desktop Services , IRemoteDesktopClient interface
- IRemoteDesktopClient interface Remote Desktop Services , Settings property
topic_type:
- apiref
api_name:
- IRemoteDesktopClient.Settings
- IRemoteDesktopClient.get_Settings
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IRemoteDesktopClient::Settings property

Retrieves the settings object for the Remote Desktop Protocol (RDP) app container client.

This property is read-only.

## Syntax


```C++
HRESULT get_Settings(
  [out, retval] IRemoteDesktopClientSettings **Settings
);
```



## Property value

The settings object for the RDP client.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>  |
| IID<br/>                      | IID\_IRemoteDesktopClient is defined as 57D25668-625A-4905-BE4E-304CAA13F89C<br/> |



## See also

<dl> <dt>

[**IRemoteDesktopClient**](/windows/win32/api/rdpappcontainerclient/nn-rdpappcontainerclient-iremotedesktopclient)
</dt> </dl>

 

