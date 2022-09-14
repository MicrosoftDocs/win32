---
title: IMsRdpClient FullScreen property
description: Determines whether the client control is in full-screen mode.
ms.assetid: 64fe2835-c00e-4d21-812d-dcf160147d93
ms.tgt_platform: multiple
keywords:
- FullScreen property Remote Desktop Services
- FullScreen property Remote Desktop Services , IMsRdpClient interface
- IMsRdpClient interface Remote Desktop Services , FullScreen property
- FullScreen property Remote Desktop Services , IMsRdpClient2 interface
- IMsRdpClient2 interface Remote Desktop Services , FullScreen property
- FullScreen property Remote Desktop Services , IMsRdpClient3 interface
- IMsRdpClient3 interface Remote Desktop Services , FullScreen property
- FullScreen property Remote Desktop Services , IMsRdpClient4 interface
- IMsRdpClient4 interface Remote Desktop Services , FullScreen property
- FullScreen property Remote Desktop Services , IMsRdpClient5 interface
- IMsRdpClient5 interface Remote Desktop Services , FullScreen property
- FullScreen property Remote Desktop Services , IMsRdpClient6 interface
- IMsRdpClient6 interface Remote Desktop Services , FullScreen property
- FullScreen property Remote Desktop Services , IMsRdpClient7 interface
- IMsRdpClient7 interface Remote Desktop Services , FullScreen property
- FullScreen property Remote Desktop Services , IMsRdpClient8 interface
- IMsRdpClient8 interface Remote Desktop Services , FullScreen property
- FullScreen property Remote Desktop Services , IMsRdpClient9 interface
- IMsRdpClient9 interface Remote Desktop Services , FullScreen property
- FullScreen property Remote Desktop Services , IMsRdpClient10 interface
- IMsRdpClient10 interface Remote Desktop Services , FullScreen property
topic_type:
- apiref
api_name:
- IMsRdpClient.FullScreen
- IMsRdpClient.get_FullScreen
- IMsRdpClient.put_FullScreen
- IMsRdpClient2.FullScreen
- IMsRdpClient2.get_FullScreen
- IMsRdpClient2.put_FullScreen
- IMsRdpClient3.FullScreen
- IMsRdpClient3.get_FullScreen
- IMsRdpClient3.put_FullScreen
- IMsRdpClient4.FullScreen
- IMsRdpClient4.get_FullScreen
- IMsRdpClient4.put_FullScreen
- IMsRdpClient5.FullScreen
- IMsRdpClient5.get_FullScreen
- IMsRdpClient5.put_FullScreen
- IMsRdpClient6.FullScreen
- IMsRdpClient6.get_FullScreen
- IMsRdpClient6.put_FullScreen
- IMsRdpClient7.FullScreen
- IMsRdpClient7.get_FullScreen
- IMsRdpClient7.put_FullScreen
- IMsRdpClient8.FullScreen
- IMsRdpClient8.get_FullScreen
- IMsRdpClient8.put_FullScreen
- IMsRdpClient9.FullScreen
- IMsRdpClient9.get_FullScreen
- IMsRdpClient9.put_FullScreen
- IMsRdpClient10.FullScreen
- IMsRdpClient10.get_FullScreen
- IMsRdpClient10.put_FullScreen
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClient::FullScreen property

Determines whether the client control is in full-screen mode.

This property is read/write.

## Syntax


```C++
HRESULT put_FullScreen(
  [in]  VARIANT_BOOL fFullScreen
);

HRESULT get_FullScreen(
  [out] VARIANT_BOOL *pfFullScreen
);
```



## Property value

**True** to enter full-screen mode, **False** to leave full-screen mode and return to window mode.

## Error codes

If the methods succeed, **S\_OK** is returned. Any other **HRESULT** value indicates that the call failed.

## Remarks

You can set this property when the control is connected.

You must call the [**IMsRdpClientNonScriptable3::put\_ConnectionBarText**](imsrdpclientnonscriptable3-connectionbartext.md) method before you call the [**IMsTscSecuredSettings::put\_Fullscreen**](imstscsecuredsettings-fullscreen.md) method or the **IMsRdpClient::put\_Fullscreen** method.

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsRdpClient is defined as 92b4a539-7115-4b7c-a5a9-e5d9efc2780a<br/>        |



## See also

<dl> <dt>

[**IMsRdpClient**](imsrdpclient-interface.md)
</dt> <dt>

[**IMsRdpClient2**](imsrdpclient2.md)
</dt> <dt>

[**IMsRdpClient3**](imsrdpclient3.md)
</dt> <dt>

[**IMsRdpClient4**](imsrdpclient4.md)
</dt> <dt>

[**IMsRdpClient5**](imsrdpclient5.md)
</dt> <dt>

[**IMsRdpClient6**](imsrdpclient6.md)
</dt> <dt>

[**IMsRdpClient7**](imsrdpclient7.md)
</dt> <dt>

[**IMsRdpClient8**](imsrdpclient8.md)
</dt> <dt>

[**IMsRdpClient9**](imsrdpclient9.md)
</dt> <dt>

[**IMsRdpClient10**](imsrdpclient10.md)
</dt> </dl>

 

 





