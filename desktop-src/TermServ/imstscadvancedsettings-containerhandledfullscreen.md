---
title: IMsTscAdvancedSettings ContainerHandledFullScreen property
description: Specifies whether the container-handled full-screen mode is enabled.
ms.assetid: 67679323-4a74-4d91-abd0-607415295f3d
ms.tgt_platform: multiple
keywords:
- ContainerHandledFullScreen property Remote Desktop Services
- ContainerHandledFullScreen property Remote Desktop Services , IMsTscAdvancedSettings interface
- IMsTscAdvancedSettings interface Remote Desktop Services , ContainerHandledFullScreen property
- ContainerHandledFullScreen property Remote Desktop Services , IMsRdpClientAdvancedSettings interface
- IMsRdpClientAdvancedSettings interface Remote Desktop Services , ContainerHandledFullScreen property
- ContainerHandledFullScreen property Remote Desktop Services , IMsRdpClientAdvancedSettings2 interface
- IMsRdpClientAdvancedSettings2 interface Remote Desktop Services , ContainerHandledFullScreen property
- ContainerHandledFullScreen property Remote Desktop Services , IMsRdpClientAdvancedSettings3 interface
- IMsRdpClientAdvancedSettings3 interface Remote Desktop Services , ContainerHandledFullScreen property
- ContainerHandledFullScreen property Remote Desktop Services , IMsRdpClientAdvancedSettings4 interface
- IMsRdpClientAdvancedSettings4 interface Remote Desktop Services , ContainerHandledFullScreen property
- ContainerHandledFullScreen property Remote Desktop Services , IMsRdpClientAdvancedSettings5 interface
- IMsRdpClientAdvancedSettings5 interface Remote Desktop Services , ContainerHandledFullScreen property
- ContainerHandledFullScreen property Remote Desktop Services , IMsRdpClientAdvancedSettings6 interface
- IMsRdpClientAdvancedSettings6 interface Remote Desktop Services , ContainerHandledFullScreen property
- ContainerHandledFullScreen property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , ContainerHandledFullScreen property
- ContainerHandledFullScreen property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , ContainerHandledFullScreen property
topic_type:
- apiref
api_name:
- IMsTscAdvancedSettings.ContainerHandledFullScreen
- IMsTscAdvancedSettings.get_ContainerHandledFullScreen
- IMsTscAdvancedSettings.put_ContainerHandledFullScreen
- IMsRdpClientAdvancedSettings.ContainerHandledFullScreen
- IMsRdpClientAdvancedSettings.get_ContainerHandledFullScreen
- IMsRdpClientAdvancedSettings.put_ContainerHandledFullScreen
- IMsRdpClientAdvancedSettings2.ContainerHandledFullScreen
- IMsRdpClientAdvancedSettings2.get_ContainerHandledFullScreen
- IMsRdpClientAdvancedSettings2.put_ContainerHandledFullScreen
- IMsRdpClientAdvancedSettings3.ContainerHandledFullScreen
- IMsRdpClientAdvancedSettings3.get_ContainerHandledFullScreen
- IMsRdpClientAdvancedSettings3.put_ContainerHandledFullScreen
- IMsRdpClientAdvancedSettings4.ContainerHandledFullScreen
- IMsRdpClientAdvancedSettings4.get_ContainerHandledFullScreen
- IMsRdpClientAdvancedSettings4.put_ContainerHandledFullScreen
- IMsRdpClientAdvancedSettings5.ContainerHandledFullScreen
- IMsRdpClientAdvancedSettings5.get_ContainerHandledFullScreen
- IMsRdpClientAdvancedSettings5.put_ContainerHandledFullScreen
- IMsRdpClientAdvancedSettings6.ContainerHandledFullScreen
- IMsRdpClientAdvancedSettings6.get_ContainerHandledFullScreen
- IMsRdpClientAdvancedSettings6.put_ContainerHandledFullScreen
- IMsRdpClientAdvancedSettings7.ContainerHandledFullScreen
- IMsRdpClientAdvancedSettings7.get_ContainerHandledFullScreen
- IMsRdpClientAdvancedSettings7.put_ContainerHandledFullScreen
- IMsRdpClientAdvancedSettings8.ContainerHandledFullScreen
- IMsRdpClientAdvancedSettings8.get_ContainerHandledFullScreen
- IMsRdpClientAdvancedSettings8.put_ContainerHandledFullScreen
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAdvancedSettings::ContainerHandledFullScreen property

Specifies whether the container-handled full-screen mode is enabled.

> [!Note]  
> The value of the **ContainerHandledFullScreen** property has no effect when the Remote Desktop ActiveX control is safe for scripting, and returns **S\_FALSE** when an attempt is made to change the value.

 

This property is read/write.

## Syntax


```C++
HRESULT put_ContainerHandledFullScreen(
  [in]  BOOL ContainerHandledFullScreen
);

HRESULT get_ContainerHandledFullScreen(
  [out] BOOL *pContainerHandledFullScreen
);
```



## Property value

Set this parameter to **TRUE** to enable the mode or another value to disable the mode.

## Error codes

Returns **S\_OK** if successful. Returns **S\_FALSE** if not supported.

## Remarks

When this mode is enabled, the current container processes the switch into and out of full-screen mode. This method should be used only if the current container needs extensive control over full-screen mode behavior. When this property is set, the control does not enter or leave full-screen mode in response to the full-screen mode shortcut key combination (CTRL+ALT+BREAK); instead, the [**IMsTscAxEvents::OnRequestGoFullScreen**](imstscaxevents-onrequestgofullscreen.md) and [**IMsTscAxEvents::OnRequestLeaveFullScreen**](imstscaxevents-onrequestleavefullscreen.md) events are called. See [**IMsTscAxEvents**](imstscaxevents-interface.md) for more information about these events.

Most container applications will not need to use container-handled full-screen mode.

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

 

 





