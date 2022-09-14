---
title: IMsRdpClientAdvancedSettings EnableWindowsKey property
description: Specifies if the Windows key can be used in the remote session.
ms.assetid: fcf0460d-3cd1-4da4-8009-0b1256adf312
ms.tgt_platform: multiple
keywords:
- EnableWindowsKey property Remote Desktop Services
- EnableWindowsKey property Remote Desktop Services , IMsRdpClientAdvancedSettings interface
- IMsRdpClientAdvancedSettings interface Remote Desktop Services , EnableWindowsKey property
- EnableWindowsKey property Remote Desktop Services , IMsRdpClientAdvancedSettings2 interface
- IMsRdpClientAdvancedSettings2 interface Remote Desktop Services , EnableWindowsKey property
- EnableWindowsKey property Remote Desktop Services , IMsRdpClientAdvancedSettings3 interface
- IMsRdpClientAdvancedSettings3 interface Remote Desktop Services , EnableWindowsKey property
- EnableWindowsKey property Remote Desktop Services , IMsRdpClientAdvancedSettings4 interface
- IMsRdpClientAdvancedSettings4 interface Remote Desktop Services , EnableWindowsKey property
- EnableWindowsKey property Remote Desktop Services , IMsRdpClientAdvancedSettings5 interface
- IMsRdpClientAdvancedSettings5 interface Remote Desktop Services , EnableWindowsKey property
- EnableWindowsKey property Remote Desktop Services , IMsRdpClientAdvancedSettings6 interface
- IMsRdpClientAdvancedSettings6 interface Remote Desktop Services , EnableWindowsKey property
- EnableWindowsKey property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , EnableWindowsKey property
- EnableWindowsKey property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , EnableWindowsKey property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings.EnableWindowsKey
- IMsRdpClientAdvancedSettings.get_EnableWindowsKey
- IMsRdpClientAdvancedSettings.put_EnableWindowsKey
- IMsRdpClientAdvancedSettings2.EnableWindowsKey
- IMsRdpClientAdvancedSettings2.get_EnableWindowsKey
- IMsRdpClientAdvancedSettings2.put_EnableWindowsKey
- IMsRdpClientAdvancedSettings3.EnableWindowsKey
- IMsRdpClientAdvancedSettings3.get_EnableWindowsKey
- IMsRdpClientAdvancedSettings3.put_EnableWindowsKey
- IMsRdpClientAdvancedSettings4.EnableWindowsKey
- IMsRdpClientAdvancedSettings4.get_EnableWindowsKey
- IMsRdpClientAdvancedSettings4.put_EnableWindowsKey
- IMsRdpClientAdvancedSettings5.EnableWindowsKey
- IMsRdpClientAdvancedSettings5.get_EnableWindowsKey
- IMsRdpClientAdvancedSettings5.put_EnableWindowsKey
- IMsRdpClientAdvancedSettings6.EnableWindowsKey
- IMsRdpClientAdvancedSettings6.get_EnableWindowsKey
- IMsRdpClientAdvancedSettings6.put_EnableWindowsKey
- IMsRdpClientAdvancedSettings7.EnableWindowsKey
- IMsRdpClientAdvancedSettings7.get_EnableWindowsKey
- IMsRdpClientAdvancedSettings7.put_EnableWindowsKey
- IMsRdpClientAdvancedSettings8.EnableWindowsKey
- IMsRdpClientAdvancedSettings8.get_EnableWindowsKey
- IMsRdpClientAdvancedSettings8.put_EnableWindowsKey
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings::EnableWindowsKey property

Specifies if the Windows key can be used in the remote session.

This property is read/write.

## Syntax


```C++
HRESULT put_EnableWindowsKey(
  [in]  LONG enableWindowsKey
);

HRESULT get_EnableWindowsKey(
  [out] LONG *penableWindowsKey
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

 

 





