---
title: IMsTscAdvancedSettings BitmapPeristence property
description: Specifies whether bitmap caching is enabled.
ms.assetid: 8cabeae8-26bc-4d33-82cc-47bb201d79b6
ms.tgt_platform: multiple
keywords:
- BitmapPeristence property Remote Desktop Services
- BitmapPeristence property Remote Desktop Services , IMsTscAdvancedSettings interface
- IMsTscAdvancedSettings interface Remote Desktop Services , BitmapPeristence property
- BitmapPeristence property Remote Desktop Services , IMsRdpClientAdvancedSettings interface
- IMsRdpClientAdvancedSettings interface Remote Desktop Services , BitmapPeristence property
- BitmapPeristence property Remote Desktop Services , IMsRdpClientAdvancedSettings2 interface
- IMsRdpClientAdvancedSettings2 interface Remote Desktop Services , BitmapPeristence property
- BitmapPeristence property Remote Desktop Services , IMsRdpClientAdvancedSettings3 interface
- IMsRdpClientAdvancedSettings3 interface Remote Desktop Services , BitmapPeristence property
- BitmapPeristence property Remote Desktop Services , IMsRdpClientAdvancedSettings4 interface
- IMsRdpClientAdvancedSettings4 interface Remote Desktop Services , BitmapPeristence property
- BitmapPeristence property Remote Desktop Services , IMsRdpClientAdvancedSettings5 interface
- IMsRdpClientAdvancedSettings5 interface Remote Desktop Services , BitmapPeristence property
- BitmapPeristence property Remote Desktop Services , IMsRdpClientAdvancedSettings6 interface
- IMsRdpClientAdvancedSettings6 interface Remote Desktop Services , BitmapPeristence property
- BitmapPeristence property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , BitmapPeristence property
- BitmapPeristence property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , BitmapPeristence property
topic_type:
- apiref
api_name:
- IMsTscAdvancedSettings.BitmapPeristence
- IMsTscAdvancedSettings.get_BitmapPeristence
- IMsTscAdvancedSettings.put_BitmapPeristence
- IMsRdpClientAdvancedSettings.BitmapPeristence
- IMsRdpClientAdvancedSettings.get_BitmapPeristence
- IMsRdpClientAdvancedSettings.put_BitmapPeristence
- IMsRdpClientAdvancedSettings2.BitmapPeristence
- IMsRdpClientAdvancedSettings2.get_BitmapPeristence
- IMsRdpClientAdvancedSettings2.put_BitmapPeristence
- IMsRdpClientAdvancedSettings3.BitmapPeristence
- IMsRdpClientAdvancedSettings3.get_BitmapPeristence
- IMsRdpClientAdvancedSettings3.put_BitmapPeristence
- IMsRdpClientAdvancedSettings4.BitmapPeristence
- IMsRdpClientAdvancedSettings4.get_BitmapPeristence
- IMsRdpClientAdvancedSettings4.put_BitmapPeristence
- IMsRdpClientAdvancedSettings5.BitmapPeristence
- IMsRdpClientAdvancedSettings5.get_BitmapPeristence
- IMsRdpClientAdvancedSettings5.put_BitmapPeristence
- IMsRdpClientAdvancedSettings6.BitmapPeristence
- IMsRdpClientAdvancedSettings6.get_BitmapPeristence
- IMsRdpClientAdvancedSettings6.put_BitmapPeristence
- IMsRdpClientAdvancedSettings7.BitmapPeristence
- IMsRdpClientAdvancedSettings7.get_BitmapPeristence
- IMsRdpClientAdvancedSettings7.put_BitmapPeristence
- IMsRdpClientAdvancedSettings8.BitmapPeristence
- IMsRdpClientAdvancedSettings8.get_BitmapPeristence
- IMsRdpClientAdvancedSettings8.put_BitmapPeristence
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAdvancedSettings::BitmapPeristence property

Specifies whether bitmap caching is enabled. Persistent caching can improve performance but requires additional disk space.

> [!Note]  
> The spelling error in the name of the property and its parameter is in the released version of the control.

 

This property is read/write.

## Syntax


```C++
HRESULT put_BitmapPeristence(
  [in]  LONG bitmapPeristence
);

HRESULT get_BitmapPeristence(
  [out] LONG *pbitmapPeristence
);
```



## Property value

Set this parameter to 0 to disable caching or a nonzero value to enable caching.

## Error codes

Returns **S\_OK** if successful.

## Remarks

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

 

 





