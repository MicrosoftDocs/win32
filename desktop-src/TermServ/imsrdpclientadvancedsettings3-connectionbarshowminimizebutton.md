---
title: IMsRdpClientAdvancedSettings3 ConnectionBarShowMinimizeButton property
description: Specifies whether to display the Minimize button on the connection bar.
ms.assetid: 3ad89f25-f1ff-4bfc-ae86-09603058c9b5
ms.tgt_platform: multiple
keywords:
- ConnectionBarShowMinimizeButton property Remote Desktop Services
- ConnectionBarShowMinimizeButton property Remote Desktop Services , IMsRdpClientAdvancedSettings3 interface
- IMsRdpClientAdvancedSettings3 interface Remote Desktop Services , ConnectionBarShowMinimizeButton property
- ConnectionBarShowMinimizeButton property Remote Desktop Services , IMsRdpClientAdvancedSettings4 interface
- IMsRdpClientAdvancedSettings4 interface Remote Desktop Services , ConnectionBarShowMinimizeButton property
- ConnectionBarShowMinimizeButton property Remote Desktop Services , IMsRdpClientAdvancedSettings5 interface
- IMsRdpClientAdvancedSettings5 interface Remote Desktop Services , ConnectionBarShowMinimizeButton property
- ConnectionBarShowMinimizeButton property Remote Desktop Services , IMsRdpClientAdvancedSettings6 interface
- IMsRdpClientAdvancedSettings6 interface Remote Desktop Services , ConnectionBarShowMinimizeButton property
- ConnectionBarShowMinimizeButton property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , ConnectionBarShowMinimizeButton property
- ConnectionBarShowMinimizeButton property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , ConnectionBarShowMinimizeButton property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings3.ConnectionBarShowMinimizeButton
- IMsRdpClientAdvancedSettings3.get_ConnectionBarShowMinimizeButton
- IMsRdpClientAdvancedSettings3.put_ConnectionBarShowMinimizeButton
- IMsRdpClientAdvancedSettings4.ConnectionBarShowMinimizeButton
- IMsRdpClientAdvancedSettings4.get_ConnectionBarShowMinimizeButton
- IMsRdpClientAdvancedSettings4.put_ConnectionBarShowMinimizeButton
- IMsRdpClientAdvancedSettings5.ConnectionBarShowMinimizeButton
- IMsRdpClientAdvancedSettings5.get_ConnectionBarShowMinimizeButton
- IMsRdpClientAdvancedSettings5.put_ConnectionBarShowMinimizeButton
- IMsRdpClientAdvancedSettings6.ConnectionBarShowMinimizeButton
- IMsRdpClientAdvancedSettings6.get_ConnectionBarShowMinimizeButton
- IMsRdpClientAdvancedSettings6.put_ConnectionBarShowMinimizeButton
- IMsRdpClientAdvancedSettings7.ConnectionBarShowMinimizeButton
- IMsRdpClientAdvancedSettings7.get_ConnectionBarShowMinimizeButton
- IMsRdpClientAdvancedSettings7.put_ConnectionBarShowMinimizeButton
- IMsRdpClientAdvancedSettings8.ConnectionBarShowMinimizeButton
- IMsRdpClientAdvancedSettings8.get_ConnectionBarShowMinimizeButton
- IMsRdpClientAdvancedSettings8.put_ConnectionBarShowMinimizeButton
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings3::ConnectionBarShowMinimizeButton property

Specifies whether to display the **Minimize** button on the connection bar.

This property is read/write.

## Syntax


```C++
HRESULT put_ConnectionBarShowMinimizeButton(
  [in]  VARIANT_BOOL fShowMinimize
);

HRESULT get_ConnectionBarShowMinimizeButton(
  [out] VARIANT_BOOL *pfShowMinimize
);
```



## Property value

Set this parameter to **VARIANT\_TRUE** to display the **Minimize** button, and to **VARIANT\_FALSE** to disable the display of the **Minimize** button.

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

 

 





