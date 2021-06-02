---
title: IMsTscNonScriptable ClearTextPassword property
description: Sets the Remote Desktop ActiveX control password in plaintext format.
ms.assetid: 93d35b10-5c92-4ab7-a32a-328ba6fcf16b
ms.tgt_platform: multiple
keywords:
- ClearTextPassword property Remote Desktop Services
- ClearTextPassword property Remote Desktop Services , IMsTscNonScriptable interface
- IMsTscNonScriptable interface Remote Desktop Services , ClearTextPassword property
- ClearTextPassword property Remote Desktop Services , IMsRdpClientNonScriptable interface
- IMsRdpClientNonScriptable interface Remote Desktop Services , ClearTextPassword property
- ClearTextPassword property Remote Desktop Services , IMsRdpClientNonScriptable2 interface
- IMsRdpClientNonScriptable2 interface Remote Desktop Services , ClearTextPassword property
- ClearTextPassword property Remote Desktop Services , IMsRdpClientNonScriptable3 interface
- IMsRdpClientNonScriptable3 interface Remote Desktop Services , ClearTextPassword property
- ClearTextPassword property Remote Desktop Services , IMsRdpClientNonScriptable4 interface
- IMsRdpClientNonScriptable4 interface Remote Desktop Services , ClearTextPassword property
- ClearTextPassword property Remote Desktop Services , IMsRdpClientNonScriptable5 interface
- IMsRdpClientNonScriptable5 interface Remote Desktop Services , ClearTextPassword property
- ClearTextPassword property Remote Desktop Services , MsRdpClient6 object
- MsRdpClient6 object Remote Desktop Services , ClearTextPassword property
- ClearTextPassword property Remote Desktop Services , MsRdpClient7 object
- MsRdpClient7 object Remote Desktop Services , ClearTextPassword property
- ClearTextPassword property Remote Desktop Services , MsRdpClient8 object
- MsRdpClient8 object Remote Desktop Services , ClearTextPassword property
- ClearTextPassword property Remote Desktop Services , MsRdpClient9 object
- MsRdpClient9 object Remote Desktop Services , ClearTextPassword property
topic_type:
- apiref
api_name:
- IMsTscNonScriptable.ClearTextPassword
- IMsTscNonScriptable.put_ClearTextPassword
- IMsRdpClientNonScriptable.ClearTextPassword
- IMsRdpClientNonScriptable.put_ClearTextPassword
- IMsRdpClientNonScriptable2.ClearTextPassword
- IMsRdpClientNonScriptable2.put_ClearTextPassword
- IMsRdpClientNonScriptable3.ClearTextPassword
- IMsRdpClientNonScriptable3.put_ClearTextPassword
- IMsRdpClientNonScriptable4.ClearTextPassword
- IMsRdpClientNonScriptable4.put_ClearTextPassword
- IMsRdpClientNonScriptable5.ClearTextPassword
- IMsRdpClientNonScriptable5.put_ClearTextPassword
- MsRdpClient6.ClearTextPassword
- MsRdpClient7.ClearTextPassword
- MsRdpClient8.ClearTextPassword
- MsRdpClient9.ClearTextPassword
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscNonScriptable::ClearTextPassword property

Sets the Remote Desktop ActiveX control password in plaintext format.

This property is write-only.

## Syntax


```C++
HRESULT put_ClearTextPassword(
  [in] BSTR newClearTextPass
);
```



## Property value

The password to be used to connect, specified in plaintext format.

## Error codes

Return **S\_OK** if successful.

## Remarks

The password is passed to the server in the safely encrypted RDP communications channel. After a plaintext password is set, it cannot be retrieved in plaintext format.

The **ClearTextPassword** property can only be set when the Remote Desktop ActiveX control is not in the connected state. Setting this property fails if the control is connected. To check for the connected state, retrieve the [**IMsTscAx::Connected**](imstscax-connected.md) property.

You can also call this method to set a plaintext password before converting it to either a portable encoded password or to a binary (nonportable) encoded password. Note however that encoded passwords should not be considered securely encrypted.

If you first call this method to set a password in plaintext format, you can then convert the password to encoded format.

**To convert a plaintext password to encoded format**

1.  Set the password in plaintext format in the **ClearTextPassword** property.
2.  To retrieve the password in binary (nonportable) encoded format, retrieve the [**BinaryPassword**](imstscnonscriptable-binarypassword.md) property and the [**BinarySalt**](imstscnonscriptable-binarysalt.md) properties. Both the encoded password part and the salt part are required to set a password in binary encoded format.
3.  To retrieve the password in portable encoded format, retrieve the [**PortablePassword**](imstscnonscriptable-portablepassword.md) method and the [**PortableSalt**](imstscnonscriptable-portablesalt.md) properties. Both parts are required to set a password in portable encoded format.

After following the preceding three steps, you can set the password in encoded format by setting the [**BinaryPassword**](imstscnonscriptable-binarypassword.md) and [**BinarySalt**](imstscnonscriptable-binarysalt.md) properties, or [**PortablePassword**](imstscnonscriptable-portablepassword.md) and [**PortableSalt**](imstscnonscriptable-portablesalt.md) properties. Both parts are required.

To enable automatic logon, you must also set the [**UserName**](imstscax-username.md) and [**Domain**](imstscax-domain.md) properties. If the password fails to authenticate the user, the Windows Logon dialog box is displayed at the server to prompt the user for the password.

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsTscNonScriptable is defined as c1e6743a-41c1-4a74-832a-0dd06c1c7a0e<br/> |



## See also

<dl> <dt>

[**IMsRdpClientNonScriptable**](imsrdpclientnonscriptable-interface.md)
</dt> <dt>

[**IMsRdpClientNonScriptable2**](imsrdpclientnonscriptable2.md)
</dt> <dt>

[**IMsRdpClientNonScriptable3**](imsrdpclientnonscriptable3.md)
</dt> <dt>

[**IMsRdpClientNonScriptable4**](imsrdpclientnonscriptable4.md)
</dt> <dt>

[**IMsRdpClientNonScriptable5**](imsrdpclientnonscriptable5.md)
</dt> <dt>

[**IMsTscNonScriptable**](imstscnonscriptable-interface.md)
</dt> </dl>

 

 





