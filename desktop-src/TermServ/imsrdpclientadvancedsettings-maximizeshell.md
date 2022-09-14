---
title: IMsRdpClientAdvancedSettings MaximizeShell property
description: Specifies if programs launched with the StartProgram property should be maximized.
ms.assetid: d8c194b6-04ef-495f-a763-7e18064230e6
ms.tgt_platform: multiple
keywords:
- MaximizeShell property Remote Desktop Services
- MaximizeShell property Remote Desktop Services , IMsRdpClientAdvancedSettings interface
- IMsRdpClientAdvancedSettings interface Remote Desktop Services , MaximizeShell property
- MaximizeShell property Remote Desktop Services , IMsRdpClientAdvancedSettings2 interface
- IMsRdpClientAdvancedSettings2 interface Remote Desktop Services , MaximizeShell property
- MaximizeShell property Remote Desktop Services , IMsRdpClientAdvancedSettings3 interface
- IMsRdpClientAdvancedSettings3 interface Remote Desktop Services , MaximizeShell property
- MaximizeShell property Remote Desktop Services , IMsRdpClientAdvancedSettings4 interface
- IMsRdpClientAdvancedSettings4 interface Remote Desktop Services , MaximizeShell property
- MaximizeShell property Remote Desktop Services , IMsRdpClientAdvancedSettings5 interface
- IMsRdpClientAdvancedSettings5 interface Remote Desktop Services , MaximizeShell property
- MaximizeShell property Remote Desktop Services , IMsRdpClientAdvancedSettings6 interface
- IMsRdpClientAdvancedSettings6 interface Remote Desktop Services , MaximizeShell property
- MaximizeShell property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , MaximizeShell property
- MaximizeShell property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , MaximizeShell property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings.MaximizeShell
- IMsRdpClientAdvancedSettings.get_MaximizeShell
- IMsRdpClientAdvancedSettings.put_MaximizeShell
- IMsRdpClientAdvancedSettings2.MaximizeShell
- IMsRdpClientAdvancedSettings2.get_MaximizeShell
- IMsRdpClientAdvancedSettings2.put_MaximizeShell
- IMsRdpClientAdvancedSettings3.MaximizeShell
- IMsRdpClientAdvancedSettings3.get_MaximizeShell
- IMsRdpClientAdvancedSettings3.put_MaximizeShell
- IMsRdpClientAdvancedSettings4.MaximizeShell
- IMsRdpClientAdvancedSettings4.get_MaximizeShell
- IMsRdpClientAdvancedSettings4.put_MaximizeShell
- IMsRdpClientAdvancedSettings5.MaximizeShell
- IMsRdpClientAdvancedSettings5.get_MaximizeShell
- IMsRdpClientAdvancedSettings5.put_MaximizeShell
- IMsRdpClientAdvancedSettings6.MaximizeShell
- IMsRdpClientAdvancedSettings6.get_MaximizeShell
- IMsRdpClientAdvancedSettings6.put_MaximizeShell
- IMsRdpClientAdvancedSettings7.MaximizeShell
- IMsRdpClientAdvancedSettings7.get_MaximizeShell
- IMsRdpClientAdvancedSettings7.put_MaximizeShell
- IMsRdpClientAdvancedSettings8.MaximizeShell
- IMsRdpClientAdvancedSettings8.get_MaximizeShell
- IMsRdpClientAdvancedSettings8.put_MaximizeShell
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings::MaximizeShell property

Specifies if programs launched with the [**StartProgram**](imstscsecuredsettings-startprogram.md) property should be maximized.

This property is read/write.

## Syntax


```C++
HRESULT put_MaximizeShell(
  [in]  LONG maximizeShell
);

HRESULT get_MaximizeShell(
  [out] LONG *pmaximizeShell
);
```



## Property value

Set this parameter to 0 to disable the feature or a nonzero value to enable the feature.

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

 

 





