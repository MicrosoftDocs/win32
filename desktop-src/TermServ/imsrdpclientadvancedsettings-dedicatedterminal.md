---
title: IMsRdpClientAdvancedSettings DedicatedTerminal property
description: This property is not supported. | IMsRdpClientAdvancedSettings DedicatedTerminal property
ms.assetid: 40d54c88-dcac-4e7d-b389-a65caeb6960e
ms.tgt_platform: multiple
keywords:
- DedicatedTerminal property Remote Desktop Services
- DedicatedTerminal property Remote Desktop Services , IMsRdpClientAdvancedSettings interface
- IMsRdpClientAdvancedSettings interface Remote Desktop Services , DedicatedTerminal property
- DedicatedTerminal property Remote Desktop Services , IMsRdpClientAdvancedSettings2 interface
- IMsRdpClientAdvancedSettings2 interface Remote Desktop Services , DedicatedTerminal property
- DedicatedTerminal property Remote Desktop Services , IMsRdpClientAdvancedSettings3 interface
- IMsRdpClientAdvancedSettings3 interface Remote Desktop Services , DedicatedTerminal property
- DedicatedTerminal property Remote Desktop Services , IMsRdpClientAdvancedSettings4 interface
- IMsRdpClientAdvancedSettings4 interface Remote Desktop Services , DedicatedTerminal property
- DedicatedTerminal property Remote Desktop Services , IMsRdpClientAdvancedSettings5 interface
- IMsRdpClientAdvancedSettings5 interface Remote Desktop Services , DedicatedTerminal property
- DedicatedTerminal property Remote Desktop Services , IMsRdpClientAdvancedSettings6 interface
- IMsRdpClientAdvancedSettings6 interface Remote Desktop Services , DedicatedTerminal property
- DedicatedTerminal property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , DedicatedTerminal property
- DedicatedTerminal property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , DedicatedTerminal property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings.DedicatedTerminal
- IMsRdpClientAdvancedSettings.get_DedicatedTerminal
- IMsRdpClientAdvancedSettings.put_DedicatedTerminal
- IMsRdpClientAdvancedSettings2.DedicatedTerminal
- IMsRdpClientAdvancedSettings2.get_DedicatedTerminal
- IMsRdpClientAdvancedSettings2.put_DedicatedTerminal
- IMsRdpClientAdvancedSettings3.DedicatedTerminal
- IMsRdpClientAdvancedSettings3.get_DedicatedTerminal
- IMsRdpClientAdvancedSettings3.put_DedicatedTerminal
- IMsRdpClientAdvancedSettings4.DedicatedTerminal
- IMsRdpClientAdvancedSettings4.get_DedicatedTerminal
- IMsRdpClientAdvancedSettings4.put_DedicatedTerminal
- IMsRdpClientAdvancedSettings5.DedicatedTerminal
- IMsRdpClientAdvancedSettings5.get_DedicatedTerminal
- IMsRdpClientAdvancedSettings5.put_DedicatedTerminal
- IMsRdpClientAdvancedSettings6.DedicatedTerminal
- IMsRdpClientAdvancedSettings6.get_DedicatedTerminal
- IMsRdpClientAdvancedSettings6.put_DedicatedTerminal
- IMsRdpClientAdvancedSettings7.DedicatedTerminal
- IMsRdpClientAdvancedSettings7.get_DedicatedTerminal
- IMsRdpClientAdvancedSettings7.put_DedicatedTerminal
- IMsRdpClientAdvancedSettings8.DedicatedTerminal
- IMsRdpClientAdvancedSettings8.get_DedicatedTerminal
- IMsRdpClientAdvancedSettings8.put_DedicatedTerminal
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings::DedicatedTerminal property

This property is not supported.

This property is read/write.

## Syntax


```C++
HRESULT put_DedicatedTerminal(
  [in]  LONG dedicatedTerminal
);

HRESULT get_DedicatedTerminal(
  [out] LONG *pdedicatedTerminal
);
```



## Property value

Set this parameter to 0 to disable the feature or a nonzero value to enable the feature.

## Error codes

Returns **S\_FALSE**.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                       |
| End of server support<br/>    | None supported<br/>                                                                       |
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

 

 





