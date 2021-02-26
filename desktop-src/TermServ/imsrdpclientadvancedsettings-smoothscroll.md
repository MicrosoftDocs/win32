---
title: IMsRdpClientAdvancedSettings SmoothScroll property
description: This property is not supported. | IMsRdpClientAdvancedSettings SmoothScroll property
ms.assetid: 7f1ce439-0b6e-4426-8dd6-3748509130e1
ms.tgt_platform: multiple
keywords:
- SmoothScroll property Remote Desktop Services
- SmoothScroll property Remote Desktop Services , IMsRdpClientAdvancedSettings interface
- IMsRdpClientAdvancedSettings interface Remote Desktop Services , SmoothScroll property
- SmoothScroll property Remote Desktop Services , IMsRdpClientAdvancedSettings2 interface
- IMsRdpClientAdvancedSettings2 interface Remote Desktop Services , SmoothScroll property
- SmoothScroll property Remote Desktop Services , IMsRdpClientAdvancedSettings3 interface
- IMsRdpClientAdvancedSettings3 interface Remote Desktop Services , SmoothScroll property
- SmoothScroll property Remote Desktop Services , IMsRdpClientAdvancedSettings4 interface
- IMsRdpClientAdvancedSettings4 interface Remote Desktop Services , SmoothScroll property
- SmoothScroll property Remote Desktop Services , IMsRdpClientAdvancedSettings5 interface
- IMsRdpClientAdvancedSettings5 interface Remote Desktop Services , SmoothScroll property
- SmoothScroll property Remote Desktop Services , IMsRdpClientAdvancedSettings6 interface
- IMsRdpClientAdvancedSettings6 interface Remote Desktop Services , SmoothScroll property
- SmoothScroll property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , SmoothScroll property
- SmoothScroll property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , SmoothScroll property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings.SmoothScroll
- IMsRdpClientAdvancedSettings.get_SmoothScroll
- IMsRdpClientAdvancedSettings.put_SmoothScroll
- IMsRdpClientAdvancedSettings2.SmoothScroll
- IMsRdpClientAdvancedSettings2.get_SmoothScroll
- IMsRdpClientAdvancedSettings2.put_SmoothScroll
- IMsRdpClientAdvancedSettings3.SmoothScroll
- IMsRdpClientAdvancedSettings3.get_SmoothScroll
- IMsRdpClientAdvancedSettings3.put_SmoothScroll
- IMsRdpClientAdvancedSettings4.SmoothScroll
- IMsRdpClientAdvancedSettings4.get_SmoothScroll
- IMsRdpClientAdvancedSettings4.put_SmoothScroll
- IMsRdpClientAdvancedSettings5.SmoothScroll
- IMsRdpClientAdvancedSettings5.get_SmoothScroll
- IMsRdpClientAdvancedSettings5.put_SmoothScroll
- IMsRdpClientAdvancedSettings6.SmoothScroll
- IMsRdpClientAdvancedSettings6.get_SmoothScroll
- IMsRdpClientAdvancedSettings6.put_SmoothScroll
- IMsRdpClientAdvancedSettings7.SmoothScroll
- IMsRdpClientAdvancedSettings7.get_SmoothScroll
- IMsRdpClientAdvancedSettings7.put_SmoothScroll
- IMsRdpClientAdvancedSettings8.SmoothScroll
- IMsRdpClientAdvancedSettings8.get_SmoothScroll
- IMsRdpClientAdvancedSettings8.put_SmoothScroll
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings::SmoothScroll property

This property is not supported.

This property is read/write.

## Syntax


```C++
HRESULT put_SmoothScroll(
  [in]  LONG smoothScroll
);

HRESULT get_SmoothScroll(
  [out] LONG *psmoothScroll
);
```



## Property value

Set this parameter to 0 to disable smooth scrolling or a nonzero value to enable smooth scrolling.

## Error codes

Returns **S\_FALSE**.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                       |
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

 

 





