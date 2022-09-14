---
title: IMsRdpClientAdvancedSettings GrabFocusOnConnect property
description: Specifies if the client control should have the focus while connecting.
ms.assetid: c67fc284-6e07-4749-84bf-70c0ae4d1b2b
ms.tgt_platform: multiple
keywords:
- GrabFocusOnConnect property Remote Desktop Services
- GrabFocusOnConnect property Remote Desktop Services , IMsRdpClientAdvancedSettings interface
- IMsRdpClientAdvancedSettings interface Remote Desktop Services , GrabFocusOnConnect property
- GrabFocusOnConnect property Remote Desktop Services , IMsRdpClientAdvancedSettings2 interface
- IMsRdpClientAdvancedSettings2 interface Remote Desktop Services , GrabFocusOnConnect property
- GrabFocusOnConnect property Remote Desktop Services , IMsRdpClientAdvancedSettings3 interface
- IMsRdpClientAdvancedSettings3 interface Remote Desktop Services , GrabFocusOnConnect property
- GrabFocusOnConnect property Remote Desktop Services , IMsRdpClientAdvancedSettings4 interface
- IMsRdpClientAdvancedSettings4 interface Remote Desktop Services , GrabFocusOnConnect property
- GrabFocusOnConnect property Remote Desktop Services , IMsRdpClientAdvancedSettings5 interface
- IMsRdpClientAdvancedSettings5 interface Remote Desktop Services , GrabFocusOnConnect property
- GrabFocusOnConnect property Remote Desktop Services , IMsRdpClientAdvancedSettings6 interface
- IMsRdpClientAdvancedSettings6 interface Remote Desktop Services , GrabFocusOnConnect property
- GrabFocusOnConnect property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , GrabFocusOnConnect property
- GrabFocusOnConnect property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , GrabFocusOnConnect property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings.GrabFocusOnConnect
- IMsRdpClientAdvancedSettings.get_GrabFocusOnConnect
- IMsRdpClientAdvancedSettings.put_GrabFocusOnConnect
- IMsRdpClientAdvancedSettings2.GrabFocusOnConnect
- IMsRdpClientAdvancedSettings2.get_GrabFocusOnConnect
- IMsRdpClientAdvancedSettings2.put_GrabFocusOnConnect
- IMsRdpClientAdvancedSettings3.GrabFocusOnConnect
- IMsRdpClientAdvancedSettings3.get_GrabFocusOnConnect
- IMsRdpClientAdvancedSettings3.put_GrabFocusOnConnect
- IMsRdpClientAdvancedSettings4.GrabFocusOnConnect
- IMsRdpClientAdvancedSettings4.get_GrabFocusOnConnect
- IMsRdpClientAdvancedSettings4.put_GrabFocusOnConnect
- IMsRdpClientAdvancedSettings5.GrabFocusOnConnect
- IMsRdpClientAdvancedSettings5.get_GrabFocusOnConnect
- IMsRdpClientAdvancedSettings5.put_GrabFocusOnConnect
- IMsRdpClientAdvancedSettings6.GrabFocusOnConnect
- IMsRdpClientAdvancedSettings6.get_GrabFocusOnConnect
- IMsRdpClientAdvancedSettings6.put_GrabFocusOnConnect
- IMsRdpClientAdvancedSettings7.GrabFocusOnConnect
- IMsRdpClientAdvancedSettings7.get_GrabFocusOnConnect
- IMsRdpClientAdvancedSettings7.put_GrabFocusOnConnect
- IMsRdpClientAdvancedSettings8.GrabFocusOnConnect
- IMsRdpClientAdvancedSettings8.get_GrabFocusOnConnect
- IMsRdpClientAdvancedSettings8.put_GrabFocusOnConnect
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings::GrabFocusOnConnect property

Specifies if the client control should have the focus while connecting. The control will not attempt to grab focus from a window running in a different process.

This property is read/write.

## Syntax


```C++
HRESULT put_GrabFocusOnConnect(
  [in]  VARIANT_BOOL fGrabFocusOnConnect
);

HRESULT get_GrabFocusOnConnect(
  [out] VARIANT_BOOL pfGrabFocusOnConnect
);
```



## Property value

Set this parameter to **VARIANT\_FALSE** to disable the feature or **VARIANT\_TRUE** to enable the feature. Setting this property to **VARIANT\_FALSE** prevents the control from grabbing focus when connecting.

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

 

 





