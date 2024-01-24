---
title: ClientSpec enumeration
description: Used with the ClientProtocolSpec property to specify the remote desktop protocol used between the client and the server.
ms.assetid: BFB2CD3C-04BF-4CB3-B156-8B08AE697327
ms.tgt_platform: multiple
keywords:
- ClientSpec enumeration Remote Desktop Services
topic_type:
- apiref
api_name:
- ClientSpec
api_location:
- MsTscAx.dll
api_type:
- LibDef
ms.topic: reference
ms.date: 05/31/2018
---

# ClientSpec enumeration

Used with the [**ClientProtocolSpec**](imsrdpclientadvancedsettings8-clientprotocolspec.md) property to specify the remote desktop protocol used between the client and the server.

## Syntax


```C++
typedef enum  { 
  FullMode        = 0,
  ThinClientMode,
  SmallCacheMode
} ClientSpec;
```



## Constants

<dl> <dt>

<span id="FullMode"></span><span id="fullmode"></span><span id="FULLMODE"></span>**FullMode**
</dt> <dd>

The protocol is full Windows 8 Remote Desktop protocol.

</dd> <dt>

<span id="ThinClientMode"></span><span id="thinclientmode"></span><span id="THINCLIENTMODE"></span>**ThinClientMode**
</dt> <dd>

The protocol is limited to using the Windows 7 with SP1 RemoteFX codec and a smaller cache. All other codecs are disabled. This protocol has the smallest memory footprint.

</dd> <dt>

<span id="SmallCacheMode"></span><span id="smallcachemode"></span><span id="SMALLCACHEMODE"></span>**SmallCacheMode**
</dt> <dd>

The protocol is the same as **FullMode**, except it uses a smaller cache.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |



## See also

<dl> <dt>

[**IMsRdpClientAdvancedSettings8::ClientProtocolSpec**](imsrdpclientadvancedsettings8-clientprotocolspec.md)
</dt> </dl>

 

 





