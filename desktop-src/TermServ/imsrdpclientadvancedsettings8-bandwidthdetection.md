---
title: IMsRdpClientAdvancedSettings8 BandwidthDetection property
description: Specifies if bandwidth changes are automatically detected.
ms.assetid: 30b2b7b3-9050-4a11-9929-2ad1dbf5ed2d
ms.tgt_platform: multiple
keywords:
- BandwidthDetection property Remote Desktop Services
- BandwidthDetection property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , BandwidthDetection property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- kbSyntax
api_name: 
api_type: 
api_location: 
---

# IMsRdpClientAdvancedSettings8::BandwidthDetection property

Specifies if bandwidth changes are automatically detected.

This property is read/write.

## Syntax


```C++
HRESULT put_BandwidthDetection(
  [in]          VARIANT_BOOL fAutodetect
);

HRESULT get_BandwidthDetection(
  [out, retval] VARIANT_BOOL *pfAutodetect
);
```



## Property value

**VARIANT\_TRUE** if bandwidth changes are automatically detected or **VARIANT\_FALSE** otherwise.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |



## See also

<dl> <dt>

[**IMsRdpClientAdvancedSettings8**](imsrdpclientadvancedsettings8.md)
</dt> </dl>

 

 





