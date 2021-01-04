---
title: IMsRdpClientAdvancedSettings HotKeyAltShiftTab property
description: Specifies the virtual-key code to add to ALT to determine the hotkey replacement for ALT+SHIFT+TAB.
ms.assetid: da52f2fb-15cc-4d55-b26e-cf5465290889
ms.tgt_platform: multiple
keywords:
- HotKeyAltShiftTab property Remote Desktop Services
- HotKeyAltShiftTab property Remote Desktop Services , IMsRdpClientAdvancedSettings interface
- IMsRdpClientAdvancedSettings interface Remote Desktop Services , HotKeyAltShiftTab property
- HotKeyAltShiftTab property Remote Desktop Services , IMsRdpClientAdvancedSettings2 interface
- IMsRdpClientAdvancedSettings2 interface Remote Desktop Services , HotKeyAltShiftTab property
- HotKeyAltShiftTab property Remote Desktop Services , IMsRdpClientAdvancedSettings3 interface
- IMsRdpClientAdvancedSettings3 interface Remote Desktop Services , HotKeyAltShiftTab property
- HotKeyAltShiftTab property Remote Desktop Services , IMsRdpClientAdvancedSettings4 interface
- IMsRdpClientAdvancedSettings4 interface Remote Desktop Services , HotKeyAltShiftTab property
- HotKeyAltShiftTab property Remote Desktop Services , IMsRdpClientAdvancedSettings5 interface
- IMsRdpClientAdvancedSettings5 interface Remote Desktop Services , HotKeyAltShiftTab property
- HotKeyAltShiftTab property Remote Desktop Services , IMsRdpClientAdvancedSettings6 interface
- IMsRdpClientAdvancedSettings6 interface Remote Desktop Services , HotKeyAltShiftTab property
- HotKeyAltShiftTab property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , HotKeyAltShiftTab property
- HotKeyAltShiftTab property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , HotKeyAltShiftTab property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings.HotKeyAltShiftTab
- IMsRdpClientAdvancedSettings.get_HotKeyAltShiftTab
- IMsRdpClientAdvancedSettings.put_HotKeyAltShiftTab
- IMsRdpClientAdvancedSettings2.HotKeyAltShiftTab
- IMsRdpClientAdvancedSettings2.get_HotKeyAltShiftTab
- IMsRdpClientAdvancedSettings2.put_HotKeyAltShiftTab
- IMsRdpClientAdvancedSettings3.HotKeyAltShiftTab
- IMsRdpClientAdvancedSettings3.get_HotKeyAltShiftTab
- IMsRdpClientAdvancedSettings3.put_HotKeyAltShiftTab
- IMsRdpClientAdvancedSettings4.HotKeyAltShiftTab
- IMsRdpClientAdvancedSettings4.get_HotKeyAltShiftTab
- IMsRdpClientAdvancedSettings4.put_HotKeyAltShiftTab
- IMsRdpClientAdvancedSettings5.HotKeyAltShiftTab
- IMsRdpClientAdvancedSettings5.get_HotKeyAltShiftTab
- IMsRdpClientAdvancedSettings5.put_HotKeyAltShiftTab
- IMsRdpClientAdvancedSettings6.HotKeyAltShiftTab
- IMsRdpClientAdvancedSettings6.get_HotKeyAltShiftTab
- IMsRdpClientAdvancedSettings6.put_HotKeyAltShiftTab
- IMsRdpClientAdvancedSettings7.HotKeyAltShiftTab
- IMsRdpClientAdvancedSettings7.get_HotKeyAltShiftTab
- IMsRdpClientAdvancedSettings7.put_HotKeyAltShiftTab
- IMsRdpClientAdvancedSettings8.HotKeyAltShiftTab
- IMsRdpClientAdvancedSettings8.get_HotKeyAltShiftTab
- IMsRdpClientAdvancedSettings8.put_HotKeyAltShiftTab
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings::HotKeyAltShiftTab property

Specifies the virtual-key code to add to ALT to determine the hotkey replacement for ALT+SHIFT+TAB.

This property is valid only when the [**KeyboardHookMode**](imsrdpclientsecuredsettings-keyboardhookmode.md) property is not enabled.

This property is read/write.

## Syntax


```C++
HRESULT put_HotKeyAltShiftTab(
  [in]  LONG hotKeyAltShiftTab
);

HRESULT get_HotKeyAltShiftTab(
  [out] LONG *photKeyAltShiftTab
);
```



## Property value

The new virtual-key code. **VK\_NEXT** is the default value, with ALT+PAGE DOWN as the resulting sequence.

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

 

 





