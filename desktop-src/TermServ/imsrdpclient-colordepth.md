---
title: IMsRdpClient ColorDepth property
description: The color depth (in bits per pixel) for the control's connection.
ms.assetid: 9ba4d8fe-20cd-40e9-a71a-0dce0ddd29fc
ms.tgt_platform: multiple
keywords:
- ColorDepth property Remote Desktop Services
- ColorDepth property Remote Desktop Services , IMsRdpClient interface
- IMsRdpClient interface Remote Desktop Services , ColorDepth property
- ColorDepth property Remote Desktop Services , IMsRdpClient2 interface
- IMsRdpClient2 interface Remote Desktop Services , ColorDepth property
- ColorDepth property Remote Desktop Services , IMsRdpClient3 interface
- IMsRdpClient3 interface Remote Desktop Services , ColorDepth property
- ColorDepth property Remote Desktop Services , IMsRdpClient4 interface
- IMsRdpClient4 interface Remote Desktop Services , ColorDepth property
- ColorDepth property Remote Desktop Services , IMsRdpClient5 interface
- IMsRdpClient5 interface Remote Desktop Services , ColorDepth property
- ColorDepth property Remote Desktop Services , IMsRdpClient6 interface
- IMsRdpClient6 interface Remote Desktop Services , ColorDepth property
- ColorDepth property Remote Desktop Services , IMsRdpClient7 interface
- IMsRdpClient7 interface Remote Desktop Services , ColorDepth property
- ColorDepth property Remote Desktop Services , IMsRdpClient8 interface
- IMsRdpClient8 interface Remote Desktop Services , ColorDepth property
- ColorDepth property Remote Desktop Services , IMsRdpClient9 interface
- IMsRdpClient9 interface Remote Desktop Services , ColorDepth property
- ColorDepth property Remote Desktop Services , IMsRdpClient10 interface
- IMsRdpClient10 interface Remote Desktop Services , ColorDepth property
topic_type:
- apiref
api_name:
- IMsRdpClient.ColorDepth
- IMsRdpClient.get_ColorDepth
- IMsRdpClient.put_ColorDepth
- IMsRdpClient2.ColorDepth
- IMsRdpClient2.get_ColorDepth
- IMsRdpClient2.put_ColorDepth
- IMsRdpClient3.ColorDepth
- IMsRdpClient3.get_ColorDepth
- IMsRdpClient3.put_ColorDepth
- IMsRdpClient4.ColorDepth
- IMsRdpClient4.get_ColorDepth
- IMsRdpClient4.put_ColorDepth
- IMsRdpClient5.ColorDepth
- IMsRdpClient5.get_ColorDepth
- IMsRdpClient5.put_ColorDepth
- IMsRdpClient6.ColorDepth
- IMsRdpClient6.get_ColorDepth
- IMsRdpClient6.put_ColorDepth
- IMsRdpClient7.ColorDepth
- IMsRdpClient7.get_ColorDepth
- IMsRdpClient7.put_ColorDepth
- IMsRdpClient8.ColorDepth
- IMsRdpClient8.get_ColorDepth
- IMsRdpClient8.put_ColorDepth
- IMsRdpClient9.ColorDepth
- IMsRdpClient9.get_ColorDepth
- IMsRdpClient9.put_ColorDepth
- IMsRdpClient10.ColorDepth
- IMsRdpClient10.get_ColorDepth
- IMsRdpClient10.put_ColorDepth
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClient::ColorDepth property

The color depth (in bits per pixel) for the control's connection.

This property is read/write.

## Syntax


```C++
HRESULT put_ColorDepth(
  [in]  LONG colorDepth
);

HRESULT get_ColorDepth(
  [out] LONG pcolorDepth
);
```



## Property value

The color depth. Values include 8, 15, 16, 24, and 32 bits per pixel.

## Error codes

If the methods succeed, **S\_OK** is returned. Any other **HRESULT** value indicates that the call failed.

## Remarks

This property cannot be set when the control is connected.

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

 

 





