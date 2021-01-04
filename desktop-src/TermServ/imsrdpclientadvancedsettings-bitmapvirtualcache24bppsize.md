---
title: IMsRdpClientAdvancedSettings BitmapVirtualCache24BppSize property
description: Specifies the size, in megabytes, of the persistent bitmap cache file to use for the 24 bits-per-pixel high-color setting.
ms.assetid: 5891c90d-f463-4f27-b212-351ebf21ae00
ms.tgt_platform: multiple
keywords:
- BitmapVirtualCache24BppSize property Remote Desktop Services
- BitmapVirtualCache24BppSize property Remote Desktop Services , IMsRdpClientAdvancedSettings interface
- IMsRdpClientAdvancedSettings interface Remote Desktop Services , BitmapVirtualCache24BppSize property
- BitmapVirtualCache24BppSize property Remote Desktop Services , IMsRdpClientAdvancedSettings2 interface
- IMsRdpClientAdvancedSettings2 interface Remote Desktop Services , BitmapVirtualCache24BppSize property
- BitmapVirtualCache24BppSize property Remote Desktop Services , IMsRdpClientAdvancedSettings3 interface
- IMsRdpClientAdvancedSettings3 interface Remote Desktop Services , BitmapVirtualCache24BppSize property
- BitmapVirtualCache24BppSize property Remote Desktop Services , IMsRdpClientAdvancedSettings4 interface
- IMsRdpClientAdvancedSettings4 interface Remote Desktop Services , BitmapVirtualCache24BppSize property
- BitmapVirtualCache24BppSize property Remote Desktop Services , IMsRdpClientAdvancedSettings5 interface
- IMsRdpClientAdvancedSettings5 interface Remote Desktop Services , BitmapVirtualCache24BppSize property
- BitmapVirtualCache24BppSize property Remote Desktop Services , IMsRdpClientAdvancedSettings6 interface
- IMsRdpClientAdvancedSettings6 interface Remote Desktop Services , BitmapVirtualCache24BppSize property
- BitmapVirtualCache24BppSize property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , BitmapVirtualCache24BppSize property
- BitmapVirtualCache24BppSize property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , BitmapVirtualCache24BppSize property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings.BitmapVirtualCache24BppSize
- IMsRdpClientAdvancedSettings.get_BitmapVirtualCache24BppSize
- IMsRdpClientAdvancedSettings.put_BitmapVirtualCache24BppSize
- IMsRdpClientAdvancedSettings2.BitmapVirtualCache24BppSize
- IMsRdpClientAdvancedSettings2.get_BitmapVirtualCache24BppSize
- IMsRdpClientAdvancedSettings2.put_BitmapVirtualCache24BppSize
- IMsRdpClientAdvancedSettings3.BitmapVirtualCache24BppSize
- IMsRdpClientAdvancedSettings3.get_BitmapVirtualCache24BppSize
- IMsRdpClientAdvancedSettings3.put_BitmapVirtualCache24BppSize
- IMsRdpClientAdvancedSettings4.BitmapVirtualCache24BppSize
- IMsRdpClientAdvancedSettings4.get_BitmapVirtualCache24BppSize
- IMsRdpClientAdvancedSettings4.put_BitmapVirtualCache24BppSize
- IMsRdpClientAdvancedSettings5.BitmapVirtualCache24BppSize
- IMsRdpClientAdvancedSettings5.get_BitmapVirtualCache24BppSize
- IMsRdpClientAdvancedSettings5.put_BitmapVirtualCache24BppSize
- IMsRdpClientAdvancedSettings6.BitmapVirtualCache24BppSize
- IMsRdpClientAdvancedSettings6.get_BitmapVirtualCache24BppSize
- IMsRdpClientAdvancedSettings6.put_BitmapVirtualCache24BppSize
- IMsRdpClientAdvancedSettings7.BitmapVirtualCache24BppSize
- IMsRdpClientAdvancedSettings7.get_BitmapVirtualCache24BppSize
- IMsRdpClientAdvancedSettings7.put_BitmapVirtualCache24BppSize
- IMsRdpClientAdvancedSettings8.BitmapVirtualCache24BppSize
- IMsRdpClientAdvancedSettings8.get_BitmapVirtualCache24BppSize
- IMsRdpClientAdvancedSettings8.put_BitmapVirtualCache24BppSize
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings::BitmapVirtualCache24BppSize property

Specifies the size, in megabytes, of the persistent bitmap cache file to use for the 24 bits-per-pixel high-color setting.

This property is read/write.

## Syntax


```C++
HRESULT put_BitmapVirtualCache24BppSize(
  [in]  LONG bitmapVirtualCache24BppSize
);

HRESULT get_BitmapVirtualCache24BppSize(
  [out] LONG *pbitmapVirtualCache24BppSize
);
```



## Property value

The new cache size. The valid values are 1 to 32 inclusive, and the default value is 30. Note that the maximum size for all virtual cache files is 128 MB.

## Error codes

Returns **S\_OK** if successful.

## Remarks

Related properties include the **BitmapVirtualCacheSize** and **BitmapVirtualCache16BppSize** properties.

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

 

 





