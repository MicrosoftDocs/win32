---
title: IMsRdpClientAdvancedSettings ClearTextPassword property
description: Specifies the password with which to connect. For more information, see the IMsTscNonScriptable interface.
ms.assetid: 9bb12dd6-f74c-488d-b6e5-4f96346610a1
ms.tgt_platform: multiple
keywords:
- ClearTextPassword property Remote Desktop Services
- ClearTextPassword property Remote Desktop Services , IMsRdpClientAdvancedSettings interface
- IMsRdpClientAdvancedSettings interface Remote Desktop Services , ClearTextPassword property
- ClearTextPassword property Remote Desktop Services , IMsRdpClientAdvancedSettings2 interface
- IMsRdpClientAdvancedSettings2 interface Remote Desktop Services , ClearTextPassword property
- ClearTextPassword property Remote Desktop Services , IMsRdpClientAdvancedSettings3 interface
- IMsRdpClientAdvancedSettings3 interface Remote Desktop Services , ClearTextPassword property
- ClearTextPassword property Remote Desktop Services , IMsRdpClientAdvancedSettings4 interface
- IMsRdpClientAdvancedSettings4 interface Remote Desktop Services , ClearTextPassword property
- ClearTextPassword property Remote Desktop Services , IMsRdpClientAdvancedSettings5 interface
- IMsRdpClientAdvancedSettings5 interface Remote Desktop Services , ClearTextPassword property
- ClearTextPassword property Remote Desktop Services , IMsRdpClientAdvancedSettings6 interface
- IMsRdpClientAdvancedSettings6 interface Remote Desktop Services , ClearTextPassword property
- ClearTextPassword property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , ClearTextPassword property
- ClearTextPassword property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , ClearTextPassword property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings.ClearTextPassword
- IMsRdpClientAdvancedSettings.put_ClearTextPassword
- IMsRdpClientAdvancedSettings2.ClearTextPassword
- IMsRdpClientAdvancedSettings2.put_ClearTextPassword
- IMsRdpClientAdvancedSettings3.ClearTextPassword
- IMsRdpClientAdvancedSettings3.put_ClearTextPassword
- IMsRdpClientAdvancedSettings4.ClearTextPassword
- IMsRdpClientAdvancedSettings4.put_ClearTextPassword
- IMsRdpClientAdvancedSettings5.ClearTextPassword
- IMsRdpClientAdvancedSettings5.put_ClearTextPassword
- IMsRdpClientAdvancedSettings6.ClearTextPassword
- IMsRdpClientAdvancedSettings6.put_ClearTextPassword
- IMsRdpClientAdvancedSettings7.ClearTextPassword
- IMsRdpClientAdvancedSettings7.put_ClearTextPassword
- IMsRdpClientAdvancedSettings8.ClearTextPassword
- IMsRdpClientAdvancedSettings8.put_ClearTextPassword
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings::ClearTextPassword property

Specifies the password with which to connect. For more information, see the [**IMsTscNonScriptable**](imstscnonscriptable-interface.md) interface.

> [!Caution]  
> Even though scriptable access to plaintext passwords is available through this property, it is still the responsibility of the developer to exercise every caution and maintain security when passing passwords in their applications.

 

This property is write-only.

## Syntax


```C++
HRESULT put_ClearTextPassword(
  [in] BSTR clearTextPassword
);
```



## Property value

The new password.

## Error codes

Returns **S\_OK** if successful.

## Remarks

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                  |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>          |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>          |
| IID<br/>                      | IID\_IMsRdpClientAdvancedSettings is defined as 3c65b4ab-12b3-465b-acd4-b8dad3bff9e2<br/> |



## See also

<dl> <dt>

[**IMsRdpClientAdvancedSettings2**](imsrdpclientadvancedsettings2.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings3**](imstscadvancedsettings-interface.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings4**](imsrdpclientadvancedsettings4.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings5**](imsrdpclientadvancedsettings5.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings6**](imsrdpclientadvancedsettings6.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings7**](imsrdpclientadvancedsettings7.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings8**](imsrdpclientadvancedsettings8.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings**](imsrdpclientadvancedsettings-interface.md)
</dt> </dl>

 

 





