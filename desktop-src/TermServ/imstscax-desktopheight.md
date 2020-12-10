---
title: IMsTscAx DesktopHeight property
description: Specifies the current control's height, in pixels, on the initial remote desktop.
ms.assetid: 7071053b-bdd1-408b-ab69-965c504fafb0
ms.tgt_platform: multiple
keywords:
- DesktopHeight property Remote Desktop Services
- DesktopHeight property Remote Desktop Services , IMsTscAx interface
- IMsTscAx interface Remote Desktop Services , DesktopHeight property
- DesktopHeight property Remote Desktop Services , IMsRdpClient interface
- IMsRdpClient interface Remote Desktop Services , DesktopHeight property
- DesktopHeight property Remote Desktop Services , IMsRdpClient2 interface
- IMsRdpClient2 interface Remote Desktop Services , DesktopHeight property
- DesktopHeight property Remote Desktop Services , IMsRdpClient3 interface
- IMsRdpClient3 interface Remote Desktop Services , DesktopHeight property
- DesktopHeight property Remote Desktop Services , IMsRdpClient4 interface
- IMsRdpClient4 interface Remote Desktop Services , DesktopHeight property
- DesktopHeight property Remote Desktop Services , IMsRdpClient5 interface
- IMsRdpClient5 interface Remote Desktop Services , DesktopHeight property
- DesktopHeight property Remote Desktop Services , IMsRdpClient6 interface
- IMsRdpClient6 interface Remote Desktop Services , DesktopHeight property
- DesktopHeight property Remote Desktop Services , IMsRdpClient7 interface
- IMsRdpClient7 interface Remote Desktop Services , DesktopHeight property
- DesktopHeight property Remote Desktop Services , IMsRdpClient8 interface
- IMsRdpClient8 interface Remote Desktop Services , DesktopHeight property
- DesktopHeight property Remote Desktop Services , IMsRdpClient9 interface
- IMsRdpClient9 interface Remote Desktop Services , DesktopHeight property
topic_type:
- apiref
api_name:
- IMsTscAx.DesktopHeight
- IMsTscAx.get_DesktopHeight
- IMsTscAx.put_DesktopHeight
- IMsRdpClient.DesktopHeight
- IMsRdpClient.get_DesktopHeight
- IMsRdpClient.put_DesktopHeight
- IMsRdpClient2.DesktopHeight
- IMsRdpClient2.get_DesktopHeight
- IMsRdpClient2.put_DesktopHeight
- IMsRdpClient3.DesktopHeight
- IMsRdpClient3.get_DesktopHeight
- IMsRdpClient3.put_DesktopHeight
- IMsRdpClient4.DesktopHeight
- IMsRdpClient4.get_DesktopHeight
- IMsRdpClient4.put_DesktopHeight
- IMsRdpClient5.DesktopHeight
- IMsRdpClient5.get_DesktopHeight
- IMsRdpClient5.put_DesktopHeight
- IMsRdpClient6.DesktopHeight
- IMsRdpClient6.get_DesktopHeight
- IMsRdpClient6.put_DesktopHeight
- IMsRdpClient7.DesktopHeight
- IMsRdpClient7.get_DesktopHeight
- IMsRdpClient7.put_DesktopHeight
- IMsRdpClient8.DesktopHeight
- IMsRdpClient8.get_DesktopHeight
- IMsRdpClient8.put_DesktopHeight
- IMsRdpClient9.DesktopHeight
- IMsRdpClient9.get_DesktopHeight
- IMsRdpClient9.put_DesktopHeight
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAx::DesktopHeight property

Specifies the current control's height, in pixels, on the initial remote desktop.

This property is read/write.

## Syntax


```C++
HRESULT put_DesktopHeight(
  [in]  LONG newVal
);

HRESULT get_DesktopHeight(
  [out] LONG *pVal
);
```



## Property value

The new height, in pixels.

## Error codes

Return **S\_OK** if successful.

## Remarks

Setting the **DesktopHeight** property is optional, but it must be set before calling the [**Connect**](imstscax-connect.md) method. If a desktop height is not specified, or is set to zero, the desktop height is set to the height of the control. The minimum and maximum values are dependent upon the operating system version of the Remote Desktop client.

<dl> <dt>

<span id="_"></span>Windows 8/Windows Server 2012
</dt> <dd>

200 minimum, 8192 maximum

</dd> <dt>

<span id="_"></span>Windows 7/Windows Server 2008
</dt> <dd>

200 minimum, 2048 maximum

</dd> <dt>

Windows Vista
</dt> <dd>

200 minimum, 1200 maximum

</dd> </dl>

After a connection is established, any changes to the control's height do not change the height of the remote desktop. Instead, the control brings up scroll bars or centers the remote desktop, as appropriate. To change the desktop size of an active connection, use the [**IMsRdpClient8::Reconnect**](imsrdpclient8-reconnect.md) method.

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsTscAx is defined as 8C11EFAE-92C3-11D1-BC1E-00C04FA31489<br/>            |



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

[**IMsTscAx**](imstscax-interface.md)
</dt> </dl>

 

 





