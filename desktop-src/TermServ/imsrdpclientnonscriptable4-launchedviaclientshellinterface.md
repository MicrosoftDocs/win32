---
title: IMsRdpClientNonScriptable4 LaunchedViaClientShellInterface property
description: Specifies whether the user launched the client control by using the Remote Desktop Web Access (RD Web Access) interface.
ms.assetid: bf72c375-0eec-49c7-9f9a-c7545a95bdce
ms.tgt_platform: multiple
keywords:
- LaunchedViaClientShellInterface property Remote Desktop Services
- LaunchedViaClientShellInterface property Remote Desktop Services , IMsRdpClientNonScriptable4 interface
- IMsRdpClientNonScriptable4 interface Remote Desktop Services , LaunchedViaClientShellInterface property
- LaunchedViaClientShellInterface property Remote Desktop Services , IMsRdpClientNonScriptable5 interface
- IMsRdpClientNonScriptable5 interface Remote Desktop Services , LaunchedViaClientShellInterface property
- LaunchedViaClientShellInterface property Remote Desktop Services , MsRdpClient5 object
- MsRdpClient5 object Remote Desktop Services , LaunchedViaClientShellInterface property
- LaunchedViaClientShellInterface property Remote Desktop Services , MsRdpClient6 object
- MsRdpClient6 object Remote Desktop Services , LaunchedViaClientShellInterface property
- LaunchedViaClientShellInterface property Remote Desktop Services , MsRdpClient7 object
- MsRdpClient7 object Remote Desktop Services , LaunchedViaClientShellInterface property
- LaunchedViaClientShellInterface property Remote Desktop Services , MsRdpClient8 object
- MsRdpClient8 object Remote Desktop Services , LaunchedViaClientShellInterface property
- LaunchedViaClientShellInterface property Remote Desktop Services , MsRdpClient9 object
- MsRdpClient9 object Remote Desktop Services , LaunchedViaClientShellInterface property
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable4.LaunchedViaClientShellInterface
- IMsRdpClientNonScriptable4.get_LaunchedViaClientShellInterface
- IMsRdpClientNonScriptable4.put_LaunchedViaClientShellInterface
- IMsRdpClientNonScriptable5.LaunchedViaClientShellInterface
- IMsRdpClientNonScriptable5.get_LaunchedViaClientShellInterface
- IMsRdpClientNonScriptable5.put_LaunchedViaClientShellInterface
- MsRdpClient5.LaunchedViaClientShellInterface
- MsRdpClient6.LaunchedViaClientShellInterface
- MsRdpClient7.LaunchedViaClientShellInterface
- MsRdpClient8.LaunchedViaClientShellInterface
- MsRdpClient9.LaunchedViaClientShellInterface
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientNonScriptable4::LaunchedViaClientShellInterface property

Specifies whether the user launched the client control by using the Remote Desktop Web Access (RD Web Access) interface.

This property is read/write.

## Syntax


```C++
HRESULT put_LaunchedViaClientShellInterface(
  [in]  VARIANT_BOOL fLaunchedViaClientShellInterface
);

HRESULT get_LaunchedViaClientShellInterface(
  [out]  VARIANT_BOOL *pfLaunchedViaClientShellInterface
);
```



## Property value

Sets the **LaunchedViaClientShellInterface** property.

## Error codes

Returns **S\_OK** if successful.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>   |
| IID<br/>                      | IMsRdpClientNonScriptable4 is defined as f50fa8aa-1c7d-4f59-b15c-a90cacae1fcb<br/> |



## See also

<dl> <dt>

[**IMsRdpClientNonScriptable5**](imsrdpclientnonscriptable5.md)
</dt> <dt>

[**IMsRdpClientNonScriptable4**](imsrdpclientnonscriptable4.md)
</dt> </dl>

 

 





