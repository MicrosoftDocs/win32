---
title: IMsRdpClientAdvancedSettings3 ConnectionBarShowRestoreButton property
description: Specifies whether to display the Restore button on the connection bar.
ms.assetid: a56c3c05-d253-404a-bf49-9c1d804802e0
ms.tgt_platform: multiple
keywords:
- ConnectionBarShowRestoreButton property Remote Desktop Services
- ConnectionBarShowRestoreButton property Remote Desktop Services , IMsRdpClientAdvancedSettings3 interface
- IMsRdpClientAdvancedSettings3 interface Remote Desktop Services , ConnectionBarShowRestoreButton property
- ConnectionBarShowRestoreButton property Remote Desktop Services , IMsRdpClientAdvancedSettings4 interface
- IMsRdpClientAdvancedSettings4 interface Remote Desktop Services , ConnectionBarShowRestoreButton property
- ConnectionBarShowRestoreButton property Remote Desktop Services , IMsRdpClientAdvancedSettings5 interface
- IMsRdpClientAdvancedSettings5 interface Remote Desktop Services , ConnectionBarShowRestoreButton property
- ConnectionBarShowRestoreButton property Remote Desktop Services , IMsRdpClientAdvancedSettings6 interface
- IMsRdpClientAdvancedSettings6 interface Remote Desktop Services , ConnectionBarShowRestoreButton property
- ConnectionBarShowRestoreButton property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , ConnectionBarShowRestoreButton property
- ConnectionBarShowRestoreButton property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , ConnectionBarShowRestoreButton property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings3.ConnectionBarShowRestoreButton
- IMsRdpClientAdvancedSettings3.get_ConnectionBarShowRestoreButton
- IMsRdpClientAdvancedSettings3.put_ConnectionBarShowRestoreButton
- IMsRdpClientAdvancedSettings4.ConnectionBarShowRestoreButton
- IMsRdpClientAdvancedSettings4.get_ConnectionBarShowRestoreButton
- IMsRdpClientAdvancedSettings4.put_ConnectionBarShowRestoreButton
- IMsRdpClientAdvancedSettings5.ConnectionBarShowRestoreButton
- IMsRdpClientAdvancedSettings5.get_ConnectionBarShowRestoreButton
- IMsRdpClientAdvancedSettings5.put_ConnectionBarShowRestoreButton
- IMsRdpClientAdvancedSettings6.ConnectionBarShowRestoreButton
- IMsRdpClientAdvancedSettings6.get_ConnectionBarShowRestoreButton
- IMsRdpClientAdvancedSettings6.put_ConnectionBarShowRestoreButton
- IMsRdpClientAdvancedSettings7.ConnectionBarShowRestoreButton
- IMsRdpClientAdvancedSettings7.get_ConnectionBarShowRestoreButton
- IMsRdpClientAdvancedSettings7.put_ConnectionBarShowRestoreButton
- IMsRdpClientAdvancedSettings8.ConnectionBarShowRestoreButton
- IMsRdpClientAdvancedSettings8.get_ConnectionBarShowRestoreButton
- IMsRdpClientAdvancedSettings8.put_ConnectionBarShowRestoreButton
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings3::ConnectionBarShowRestoreButton property

Specifies whether to display the **Restore** button on the connection bar.

This property is read/write.

## Syntax


```C++
HRESULT put_ConnectionBarShowRestoreButton(
  [in]  VARIANT_BOOL fShowRestore
);

HRESULT get_ConnectionBarShowRestoreButton(
  [out] VARIANT_BOOL *pfShowRestore
);
```



## Property value

Set to **VARIANT\_TRUE** to display the **Restore** button, and to **VARIANT\_FALSE** to disable the display of the **Restore** button.

## Error codes

Returns **S\_OK** if successful.

## Remarks

This property cannot be set while the control is connected.

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                   |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>           |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>           |
| IID<br/>                      | IID\_IMsRdpClientAdvancedSettings3 is defined as 19cd856b-c542-4c53-acee-f127e3be1a59<br/> |



## See also

<dl> <dt>

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

[**IMsRdpClientAdvancedSettings3**](imsrdpclientadvancedsettings3.md)
</dt> </dl>

 

 





