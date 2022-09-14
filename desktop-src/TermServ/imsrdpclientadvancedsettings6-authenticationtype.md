---
title: IMsRdpClientAdvancedSettings6 AuthenticationType property
description: Specifies the type of authentication used for this connection.
ms.assetid: A6DAAE0A-5045-4C2C-B065-AB5BFB39F955
ms.tgt_platform: multiple
keywords:
- AuthenticationType property Remote Desktop Services
- AuthenticationType property Remote Desktop Services , IMsRdpClientAdvancedSettings6 interface
- IMsRdpClientAdvancedSettings6 interface Remote Desktop Services , AuthenticationType property
- AuthenticationType property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , AuthenticationType property
- AuthenticationType property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , AuthenticationType property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings6.AuthenticationType
- IMsRdpClientAdvancedSettings6.get_AuthenticationType
- IMsRdpClientAdvancedSettings7.AuthenticationType
- IMsRdpClientAdvancedSettings7.get_AuthenticationType
- IMsRdpClientAdvancedSettings8.AuthenticationType
- IMsRdpClientAdvancedSettings8.get_AuthenticationType
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings6::AuthenticationType property

Specifies the type of authentication used for this connection.

This property is read-only.

## Syntax


```C++
HRESULT get_AuthenticationType(
  [out] UINT *puiAuthType
);
```



## Property value

Receives a value that specifies the type of authentication used for this connection. This can be one of the following values.

<dt>

0
</dt> <dd>

No authentication is used.

</dd> <dt>

1
</dt> <dd>

Certificate authentication is used.

</dd> <dt>

2
</dt> <dd>

Kerberos authentication is used.

</dd> <dt>

3
</dt> <dd>

Both certificate and Kerberos authentication are used.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                   |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>           |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>           |
| IID<br/>                      | IID\_IMsRdpClientAdvancedSettings6 is defined as 222c4b5d-45d9-4df0-a7c6-60cf9089d285<br/> |



## See also

<dl> <dt>

[**IMsRdpClientAdvancedSettings7**](imsrdpclientadvancedsettings7.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings8**](imsrdpclientadvancedsettings8.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings6**](imsrdpclientadvancedsettings6.md)
</dt> </dl>

 

 





