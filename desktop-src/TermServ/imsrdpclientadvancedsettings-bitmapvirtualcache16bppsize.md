---
title: IMsRdpClientAdvancedSettings BitmapVirtualCache16BppSize property
description: Specifies the size, in megabytes, of the persistent bitmap cache file to use for the 15 and 16 bits-per-pixel high-color settings.
ms.assetid: f2558c88-d60f-4be3-9941-8e0e18bbb778
ms.tgt_platform: multiple
keywords:
- BitmapVirtualCache16BppSize property Remote Desktop Services
- BitmapVirtualCache16BppSize property Remote Desktop Services , IMsRdpClientAdvancedSettings interface
- IMsRdpClientAdvancedSettings interface Remote Desktop Services , BitmapVirtualCache16BppSize property
- BitmapVirtualCache16BppSize property Remote Desktop Services , IMsRdpClientAdvancedSettings2 interface
- IMsRdpClientAdvancedSettings2 interface Remote Desktop Services , BitmapVirtualCache16BppSize property
- BitmapVirtualCache16BppSize property Remote Desktop Services , IMsRdpClientAdvancedSettings3 interface
- IMsRdpClientAdvancedSettings3 interface Remote Desktop Services , BitmapVirtualCache16BppSize property
- BitmapVirtualCache16BppSize property Remote Desktop Services , IMsRdpClientAdvancedSettings4 interface
- IMsRdpClientAdvancedSettings4 interface Remote Desktop Services , BitmapVirtualCache16BppSize property
- BitmapVirtualCache16BppSize property Remote Desktop Services , IMsRdpClientAdvancedSettings5 interface
- IMsRdpClientAdvancedSettings5 interface Remote Desktop Services , BitmapVirtualCache16BppSize property
- BitmapVirtualCache16BppSize property Remote Desktop Services , IMsRdpClientAdvancedSettings6 interface
- IMsRdpClientAdvancedSettings6 interface Remote Desktop Services , BitmapVirtualCache16BppSize property
- BitmapVirtualCache16BppSize property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , BitmapVirtualCache16BppSize property
- BitmapVirtualCache16BppSize property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , BitmapVirtualCache16BppSize property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings.BitmapVirtualCache16BppSize
- IMsRdpClientAdvancedSettings.get_BitmapVirtualCache16BppSize
- IMsRdpClientAdvancedSettings.put_BitmapVirtualCache16BppSize
- IMsRdpClientAdvancedSettings2.BitmapVirtualCache16BppSize
- IMsRdpClientAdvancedSettings2.get_BitmapVirtualCache16BppSize
- IMsRdpClientAdvancedSettings2.put_BitmapVirtualCache16BppSize
- IMsRdpClientAdvancedSettings3.BitmapVirtualCache16BppSize
- IMsRdpClientAdvancedSettings3.get_BitmapVirtualCache16BppSize
- IMsRdpClientAdvancedSettings3.put_BitmapVirtualCache16BppSize
- IMsRdpClientAdvancedSettings4.BitmapVirtualCache16BppSize
- IMsRdpClientAdvancedSettings4.get_BitmapVirtualCache16BppSize
- IMsRdpClientAdvancedSettings4.put_BitmapVirtualCache16BppSize
- IMsRdpClientAdvancedSettings5.BitmapVirtualCache16BppSize
- IMsRdpClientAdvancedSettings5.get_BitmapVirtualCache16BppSize
- IMsRdpClientAdvancedSettings5.put_BitmapVirtualCache16BppSize
- IMsRdpClientAdvancedSettings6.BitmapVirtualCache16BppSize
- IMsRdpClientAdvancedSettings6.get_BitmapVirtualCache16BppSize
- IMsRdpClientAdvancedSettings6.put_BitmapVirtualCache16BppSize
- IMsRdpClientAdvancedSettings7.BitmapVirtualCache16BppSize
- IMsRdpClientAdvancedSettings7.get_BitmapVirtualCache16BppSize
- IMsRdpClientAdvancedSettings7.put_BitmapVirtualCache16BppSize
- IMsRdpClientAdvancedSettings8.BitmapVirtualCache16BppSize
- IMsRdpClientAdvancedSettings8.get_BitmapVirtualCache16BppSize
- IMsRdpClientAdvancedSettings8.put_BitmapVirtualCache16BppSize
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings::BitmapVirtualCache16BppSize property

Specifies the size, in megabytes, of the persistent bitmap cache file to use for the 15 and 16 bits-per-pixel high-color settings.

This property is read/write.

## Syntax


```C++
HRESULT put_BitmapVirtualCache16BppSize(
  [in]  LONG bitmapVirtualCache16BppSize
);

HRESULT get_BitmapVirtualCache16BppSize(
  [out] LONG *pbitmapVirtualCache16BppSize
);
```



## Property value

The new cache size. The valid values are 1 to 32 inclusive, and the default value is 20. Note that the maximum size for all virtual cache files is 128 MB.

## Error codes

Returns **S\_OK** if successful.

## Remarks

Related properties include the **BitmapVirtualCacheSize** and **BitmapVirtualCache24BppSize** properties.

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

 

 





