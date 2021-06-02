---
title: IMsTscSecuredSettings WorkDir property
description: Specifies the working directory of the start program.
ms.assetid: e67f7274-be47-42c4-9267-a05bb93e6725
ms.tgt_platform: multiple
keywords:
- WorkDir property Remote Desktop Services
- WorkDir property Remote Desktop Services , IMsTscSecuredSettings interface
- IMsTscSecuredSettings interface Remote Desktop Services , WorkDir property
- WorkDir property Remote Desktop Services , IMsRdpClientSecuredSettings interface
- IMsRdpClientSecuredSettings interface Remote Desktop Services , WorkDir property
topic_type:
- apiref
api_name:
- IMsTscSecuredSettings.WorkDir
- IMsTscSecuredSettings.get_WorkDir
- IMsTscSecuredSettings.put_WorkDir
- IMsRdpClientSecuredSettings.WorkDir
- IMsRdpClientSecuredSettings.get_WorkDir
- IMsRdpClientSecuredSettings.put_WorkDir
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscSecuredSettings::WorkDir property

Specifies the working directory of the start program.

This property is read/write.

## Syntax


```C++
HRESULT put_WorkDir(
  [in]  BSTR newVal
);

HRESULT get_WorkDir(
  [out] BSTR *pWorkDir
);
```



## Property value

The new working directory. The maximum length of this string is **MAX\_PATH**-1 characters.

## Error codes

Returns **S\_OK** if successful.

## Remarks

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

 

 





