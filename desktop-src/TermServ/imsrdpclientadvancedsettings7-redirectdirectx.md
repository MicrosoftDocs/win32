---
title: IMsRdpClientAdvancedSettings7 RedirectDirectX property
description: This property is not used. | IMsRdpClientAdvancedSettings7 RedirectDirectX property
ms.assetid: a027d8d7-994f-4b24-8c46-18651c8e200b
ms.tgt_platform: multiple
keywords:
- RedirectDirectX property Remote Desktop Services
- RedirectDirectX property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , RedirectDirectX property
- RedirectDirectX property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , RedirectDirectX property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings7.RedirectDirectX
- IMsRdpClientAdvancedSettings7.get_RedirectDirectX
- IMsRdpClientAdvancedSettings7.put_RedirectDirectX
- IMsRdpClientAdvancedSettings8.RedirectDirectX
- IMsRdpClientAdvancedSettings8.get_RedirectDirectX
- IMsRdpClientAdvancedSettings8.put_RedirectDirectX
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings7::RedirectDirectX property

This property is not used.

This property is read/write.

## Syntax


```C++
HRESULT put_RedirectDirectX(
  [in]          VARIANT_BOOL fRedirectDirectX
);

HRESULT get_RedirectDirectX(
  [out, retval] VARIANT_BOOL *pfRedirectDirectX
);
```



## Property value

This property is not used.

## Error codes

This property is not used. The setter method always returns **S\_FALSE** and the getter method always returns **E\_NOTIMPL**.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                             |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                                |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>           |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>           |
| IID<br/>                      | IID\_IMsRdpClientAdvancedSettings7 is defined as 26036036-4010-4578-8091-0db9a1edf9c3<br/> |



## See also

<dl> <dt>

[**IMsRdpClientAdvancedSettings8**](imsrdpclientadvancedsettings8.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings7**](imsrdpclientadvancedsettings7.md)
</dt> </dl>

 

 





