---
title: IMsTscSecuredSettings StartProgram property
description: Specifies the program to be started on the remote server upon connection.
ms.assetid: bd2a5ced-468b-48db-ad51-9940577a0310
ms.tgt_platform: multiple
keywords:
- StartProgram property Remote Desktop Services
- StartProgram property Remote Desktop Services , IMsTscSecuredSettings interface
- IMsTscSecuredSettings interface Remote Desktop Services , StartProgram property
- StartProgram property Remote Desktop Services , IMsRdpClientSecuredSettings interface
- IMsRdpClientSecuredSettings interface Remote Desktop Services , StartProgram property
topic_type:
- apiref
api_name:
- IMsTscSecuredSettings.StartProgram
- IMsTscSecuredSettings.get_StartProgram
- IMsTscSecuredSettings.put_StartProgram
- IMsRdpClientSecuredSettings.StartProgram
- IMsRdpClientSecuredSettings.get_StartProgram
- IMsRdpClientSecuredSettings.put_StartProgram
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscSecuredSettings::StartProgram property

Specifies the program to be started on the remote server upon connection.

This property is read/write.

## Syntax


```C++
HRESULT put_StartProgram(
  [in]  BSTR newVal
);

HRESULT get_StartProgram(
  [out] BSTR *pStartProgram
);
```



## Property value

The name of the new start program. The maximum length of this string is **MAX\_PATH**-1 characters.

## Error codes

Returns **S\_OK** if successful.

## Remarks

If the value of this property is not set, the session user's shell command will be run. The shell command will be read from the following registry value on the server:

**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**Windows NT**\\**CurrentVersion**\\**WinLogon**\\**Shell**

Refer to [Providing for RDP Client Security](providing-for-rdp-client-security.md) for more information.

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

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

 

 





