---
title: IMsTscAdvancedSettings DisableRdpdr property
description: Specifies whether printer and clipboard redirection is enabled.
ms.assetid: 63e0e024-4792-4efe-a6c5-d122f8adcb0a
ms.tgt_platform: multiple
keywords:
- DisableRdpdr property Remote Desktop Services
- DisableRdpdr property Remote Desktop Services , IMsTscAdvancedSettings interface
- IMsTscAdvancedSettings interface Remote Desktop Services , DisableRdpdr property
- DisableRdpdr property Remote Desktop Services , IMsRdpClientAdvancedSettings interface
- IMsRdpClientAdvancedSettings interface Remote Desktop Services , DisableRdpdr property
- DisableRdpdr property Remote Desktop Services , IMsRdpClientAdvancedSettings2 interface
- IMsRdpClientAdvancedSettings2 interface Remote Desktop Services , DisableRdpdr property
- DisableRdpdr property Remote Desktop Services , IMsRdpClientAdvancedSettings3 interface
- IMsRdpClientAdvancedSettings3 interface Remote Desktop Services , DisableRdpdr property
- DisableRdpdr property Remote Desktop Services , IMsRdpClientAdvancedSettings4 interface
- IMsRdpClientAdvancedSettings4 interface Remote Desktop Services , DisableRdpdr property
- DisableRdpdr property Remote Desktop Services , IMsRdpClientAdvancedSettings5 interface
- IMsRdpClientAdvancedSettings5 interface Remote Desktop Services , DisableRdpdr property
- DisableRdpdr property Remote Desktop Services , IMsRdpClientAdvancedSettings6 interface
- IMsRdpClientAdvancedSettings6 interface Remote Desktop Services , DisableRdpdr property
- DisableRdpdr property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , DisableRdpdr property
- DisableRdpdr property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , DisableRdpdr property
topic_type:
- apiref
api_name:
- IMsTscAdvancedSettings.DisableRdpdr
- IMsTscAdvancedSettings.get_DisableRdpdr
- IMsTscAdvancedSettings.put_DisableRdpdr
- IMsRdpClientAdvancedSettings.DisableRdpdr
- IMsRdpClientAdvancedSettings.get_DisableRdpdr
- IMsRdpClientAdvancedSettings.put_DisableRdpdr
- IMsRdpClientAdvancedSettings2.DisableRdpdr
- IMsRdpClientAdvancedSettings2.get_DisableRdpdr
- IMsRdpClientAdvancedSettings2.put_DisableRdpdr
- IMsRdpClientAdvancedSettings3.DisableRdpdr
- IMsRdpClientAdvancedSettings3.get_DisableRdpdr
- IMsRdpClientAdvancedSettings3.put_DisableRdpdr
- IMsRdpClientAdvancedSettings4.DisableRdpdr
- IMsRdpClientAdvancedSettings4.get_DisableRdpdr
- IMsRdpClientAdvancedSettings4.put_DisableRdpdr
- IMsRdpClientAdvancedSettings5.DisableRdpdr
- IMsRdpClientAdvancedSettings5.get_DisableRdpdr
- IMsRdpClientAdvancedSettings5.put_DisableRdpdr
- IMsRdpClientAdvancedSettings6.DisableRdpdr
- IMsRdpClientAdvancedSettings6.get_DisableRdpdr
- IMsRdpClientAdvancedSettings6.put_DisableRdpdr
- IMsRdpClientAdvancedSettings7.DisableRdpdr
- IMsRdpClientAdvancedSettings7.get_DisableRdpdr
- IMsRdpClientAdvancedSettings7.put_DisableRdpdr
- IMsRdpClientAdvancedSettings8.DisableRdpdr
- IMsRdpClientAdvancedSettings8.get_DisableRdpdr
- IMsRdpClientAdvancedSettings8.put_DisableRdpdr
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAdvancedSettings::DisableRdpdr property

Specifies whether printer and clipboard redirection is enabled.

This property is read/write.

## Syntax


```C++
HRESULT put_DisableRdpdr(
  [in]  BOOL DisableRdpdr
);

HRESULT get_DisableRdpdr(
  [out] BOOL *pDisableRdpdr
);
```



## Property value

Set this parameter to **TRUE** to disable redirection or **FALSE** to enable redirection.

## Error codes

Returns **S\_OK** if successful.

## Remarks

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                            |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>    |
| IID<br/>                      | IID\_IMsTscAdvancedSettings is defined as 809945cc-4b3b-4a92-a6b0-dbf9b5f2ef2d<br/> |



## See also

<dl> <dt>

[**IMsRdpClientAdvancedSettings**](imsrdpclientadvancedsettings-interface.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings2**](imsrdpclientadvancedsettings2.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings3**](imsrdpclientadvancedsettings3.md)
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

[**IMsTscAdvancedSettings**](imstscadvancedsettings-interface.md)
</dt> </dl>

 

 





