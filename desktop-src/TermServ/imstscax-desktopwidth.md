---
title: IMsTscAx DesktopWidth property
description: Specifies the current control's width, in pixels, on the initial remote desktop.
ms.assetid: 3b349f6c-d068-4047-b8b5-29d022894729
ms.tgt_platform: multiple
keywords:
- DesktopWidth property Remote Desktop Services
- DesktopWidth property Remote Desktop Services , IMsTscAx interface
- IMsTscAx interface Remote Desktop Services , DesktopWidth property
- DesktopWidth property Remote Desktop Services , IMsRdpClient interface
- IMsRdpClient interface Remote Desktop Services , DesktopWidth property
- DesktopWidth property Remote Desktop Services , IMsRdpClient2 interface
- IMsRdpClient2 interface Remote Desktop Services , DesktopWidth property
- DesktopWidth property Remote Desktop Services , IMsRdpClient3 interface
- IMsRdpClient3 interface Remote Desktop Services , DesktopWidth property
- DesktopWidth property Remote Desktop Services , IMsRdpClient4 interface
- IMsRdpClient4 interface Remote Desktop Services , DesktopWidth property
- DesktopWidth property Remote Desktop Services , IMsRdpClient5 interface
- IMsRdpClient5 interface Remote Desktop Services , DesktopWidth property
- DesktopWidth property Remote Desktop Services , IMsRdpClient6 interface
- IMsRdpClient6 interface Remote Desktop Services , DesktopWidth property
- DesktopWidth property Remote Desktop Services , IMsRdpClient7 interface
- IMsRdpClient7 interface Remote Desktop Services , DesktopWidth property
- DesktopWidth property Remote Desktop Services , IMsRdpClient8 interface
- IMsRdpClient8 interface Remote Desktop Services , DesktopWidth property
- DesktopWidth property Remote Desktop Services , IMsRdpClient9 interface
- IMsRdpClient9 interface Remote Desktop Services , DesktopWidth property
topic_type:
- apiref
api_name:
- IMsTscAx.DesktopWidth
- IMsTscAx.get_DesktopWidth
- IMsTscAx.put_DesktopWidth
- IMsRdpClient.DesktopWidth
- IMsRdpClient.get_DesktopWidth
- IMsRdpClient.put_DesktopWidth
- IMsRdpClient2.DesktopWidth
- IMsRdpClient2.get_DesktopWidth
- IMsRdpClient2.put_DesktopWidth
- IMsRdpClient3.DesktopWidth
- IMsRdpClient3.get_DesktopWidth
- IMsRdpClient3.put_DesktopWidth
- IMsRdpClient4.DesktopWidth
- IMsRdpClient4.get_DesktopWidth
- IMsRdpClient4.put_DesktopWidth
- IMsRdpClient5.DesktopWidth
- IMsRdpClient5.get_DesktopWidth
- IMsRdpClient5.put_DesktopWidth
- IMsRdpClient6.DesktopWidth
- IMsRdpClient6.get_DesktopWidth
- IMsRdpClient6.put_DesktopWidth
- IMsRdpClient7.DesktopWidth
- IMsRdpClient7.get_DesktopWidth
- IMsRdpClient7.put_DesktopWidth
- IMsRdpClient8.DesktopWidth
- IMsRdpClient8.get_DesktopWidth
- IMsRdpClient8.put_DesktopWidth
- IMsRdpClient9.DesktopWidth
- IMsRdpClient9.get_DesktopWidth
- IMsRdpClient9.put_DesktopWidth
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAx::DesktopWidth property

Specifies the current control's width, in pixels, on the initial remote desktop.

This property is read/write.

## Syntax


```C++
HRESULT put_DesktopWidth(
  [in]  LONG newVal
);

HRESULT get_DesktopWidth(
  [out] LONG *pVal
);
```



## Property value

The new width, in pixels.

## Error codes

Return **S\_OK** if successful.

## Remarks

Setting the **DesktopWidth** property is optional, but it must be set before calling the [**Connect**](imstscax-connect.md) method. If a desktop width is not specified, or is set to zero, the desktop width is set to the width of the control. The minimum and maximum values are dependent upon the operating system version of the Remote Desktop client.

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

After a connection is established, any changes to the control's width do not change the width of the remote desktop. Instead, the control brings up scroll bars or centers the remote desktop, as appropriate. To change the desktop size of an active connection, use the [**IMsRdpClient8::Reconnect**](imsrdpclient8-reconnect.md) method.

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

 

 





