---
title: IMsRdpClientNonScriptable2 UIParentWindowHandle property
description: Sets or retrieves the window handle to be the parent window for any dialog boxes displayed by the control. This allows any windows displayed by the control to be properly modal with respect to any windows displayed by the parent application.
ms.assetid: 5ecf1fc3-492e-4faf-89c5-7f7abb3778a0
ms.tgt_platform: multiple
keywords:
- UIParentWindowHandle property Remote Desktop Services
- UIParentWindowHandle property Remote Desktop Services , IMsRdpClientNonScriptable2 interface
- IMsRdpClientNonScriptable2 interface Remote Desktop Services , UIParentWindowHandle property
- UIParentWindowHandle property Remote Desktop Services , IMsRdpClientNonScriptable3 interface
- IMsRdpClientNonScriptable3 interface Remote Desktop Services , UIParentWindowHandle property
- UIParentWindowHandle property Remote Desktop Services , IMsRdpClientNonScriptable4 interface
- IMsRdpClientNonScriptable4 interface Remote Desktop Services , UIParentWindowHandle property
- UIParentWindowHandle property Remote Desktop Services , IMsRdpClientNonScriptable5 interface
- IMsRdpClientNonScriptable5 interface Remote Desktop Services , UIParentWindowHandle property
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable2.UIParentWindowHandle
- IMsRdpClientNonScriptable2.get_UIParentWindowHandle
- IMsRdpClientNonScriptable2.put_UIParentWindowHandle
- IMsRdpClientNonScriptable3.UIParentWindowHandle
- IMsRdpClientNonScriptable3.get_UIParentWindowHandle
- IMsRdpClientNonScriptable3.put_UIParentWindowHandle
- IMsRdpClientNonScriptable4.UIParentWindowHandle
- IMsRdpClientNonScriptable4.get_UIParentWindowHandle
- IMsRdpClientNonScriptable4.put_UIParentWindowHandle
- IMsRdpClientNonScriptable5.UIParentWindowHandle
- IMsRdpClientNonScriptable5.get_UIParentWindowHandle
- IMsRdpClientNonScriptable5.put_UIParentWindowHandle
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientNonScriptable2::UIParentWindowHandle property

Sets or retrieves the window handle to be the parent window for any dialog boxes displayed by the control. This allows any windows displayed by the control to be properly modal with respect to any windows displayed by the parent application.

This property is read/write.

## Syntax


```C++
HRESULT put_UIParentWindowHandle(
  [in]  HWND hwndUIParentWindowHandle
);

HRESULT get_UIParentWindowHandle(
  [out] HWND *phwndUIParentWindowHandle
);
```



## Property value

The new window handle.

## Error codes

Returns **S\_OK** if successful.

## Remarks

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008, Windows Server 2008 with SP1<br/>                                  |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>        |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>        |
| IID<br/>                      | IID\_IMsRdpClientNonScriptable2 is defined as 17a5e535-4072-4fa4-af32-c8d0d47345e9<br/> |



## See also

<dl> <dt>

[**IMsRdpClientNonScriptable3**](imsrdpclientnonscriptable3.md)
</dt> <dt>

[**IMsRdpClientNonScriptable4**](imsrdpclientnonscriptable4.md)
</dt> <dt>

[**IMsRdpClientNonScriptable5**](imsrdpclientnonscriptable5.md)
</dt> <dt>

[**OnAuthenticationWarningDisplayed**](imstscaxevents-onauthenticationwarningdisplayed.md)
</dt> <dt>

[**OnAuthenticationWarningDismissed**](imstscaxevents-onauthenticationwarningdismissed.md)
</dt> <dt>

[**IMsRdpClientNonScriptable2**](imsrdpclientnonscriptable2.md)
</dt> </dl>

 

 





