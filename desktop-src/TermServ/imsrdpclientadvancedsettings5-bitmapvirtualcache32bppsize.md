---
title: IMsRdpClientAdvancedSettings5 BitmapVirtualCache32BppSize property
description: Sets or retrieves the virtual cache file size for 32 bits per pixel (bpp) bitmaps.
ms.assetid: 7084293a-ae75-4711-a8d8-f813117333e7
ms.tgt_platform: multiple
keywords:
- BitmapVirtualCache32BppSize property Remote Desktop Services
- BitmapVirtualCache32BppSize property Remote Desktop Services , IMsRdpClientAdvancedSettings5 interface
- IMsRdpClientAdvancedSettings5 interface Remote Desktop Services , BitmapVirtualCache32BppSize property
- BitmapVirtualCache32BppSize property Remote Desktop Services , IMsRdpClientAdvancedSettings6 interface
- IMsRdpClientAdvancedSettings6 interface Remote Desktop Services , BitmapVirtualCache32BppSize property
- BitmapVirtualCache32BppSize property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , BitmapVirtualCache32BppSize property
- BitmapVirtualCache32BppSize property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , BitmapVirtualCache32BppSize property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings5.BitmapVirtualCache32BppSize
- IMsRdpClientAdvancedSettings5.get_BitmapVirtualCache32BppSize
- IMsRdpClientAdvancedSettings5.put_BitmapVirtualCache32BppSize
- IMsRdpClientAdvancedSettings6.BitmapVirtualCache32BppSize
- IMsRdpClientAdvancedSettings6.get_BitmapVirtualCache32BppSize
- IMsRdpClientAdvancedSettings6.put_BitmapVirtualCache32BppSize
- IMsRdpClientAdvancedSettings7.BitmapVirtualCache32BppSize
- IMsRdpClientAdvancedSettings7.get_BitmapVirtualCache32BppSize
- IMsRdpClientAdvancedSettings7.put_BitmapVirtualCache32BppSize
- IMsRdpClientAdvancedSettings8.BitmapVirtualCache32BppSize
- IMsRdpClientAdvancedSettings8.get_BitmapVirtualCache32BppSize
- IMsRdpClientAdvancedSettings8.put_BitmapVirtualCache32BppSize
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings5::BitmapVirtualCache32BppSize property

Sets or retrieves the virtual cache file size for 32 bits per pixel (bpp) bitmaps.

This property is read/write.

## Syntax


```C++
HRESULT put_BitmapVirtualCache32BppSize(
  [in]  LONG bitmapVirtualCache32BppSize
);

HRESULT get_BitmapVirtualCache32BppSize(
  [out] LONG *pbitmapVirtualCache32BppSize
);
```



## Property value

Sets the size of the virtual cache file for 32 bpp bitmaps, in megabytes (MB). The maximum value is 48 MB.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                   |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>           |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>           |
| IID<br/>                      | IID\_IMsRdpClientAdvancedSettings5 is defined as FBA7F64E-6783-4405-DA45-FA4A763DABD0<br/> |



## See also

<dl> <dt>

[**IMsRdpClientAdvancedSettings6**](imsrdpclientadvancedsettings6.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings7**](imsrdpclientadvancedsettings7.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings8**](imsrdpclientadvancedsettings8.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings5**](imsrdpclientadvancedsettings5.md)
</dt> </dl>

 

 





