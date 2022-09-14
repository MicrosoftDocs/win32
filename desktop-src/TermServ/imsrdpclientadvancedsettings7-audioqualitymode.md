---
title: IMsRdpClientAdvancedSettings7 AudioQualityMode property
description: Specifies or retrieves a value that indicates the audio quality mode setting for redirected audio. By default this is set to 0.
ms.assetid: 9945c524-ca50-41ae-a7cf-1386cd758c0f
ms.tgt_platform: multiple
keywords:
- AudioQualityMode property Remote Desktop Services
- AudioQualityMode property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , AudioQualityMode property
- AudioQualityMode property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , AudioQualityMode property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings7.AudioQualityMode
- IMsRdpClientAdvancedSettings7.get_AudioQualityMode
- IMsRdpClientAdvancedSettings7.put_AudioQualityMode
- IMsRdpClientAdvancedSettings8.AudioQualityMode
- IMsRdpClientAdvancedSettings8.get_AudioQualityMode
- IMsRdpClientAdvancedSettings8.put_AudioQualityMode
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings7::AudioQualityMode property

Specifies or retrieves a value that indicates the audio quality mode setting for redirected audio. By default this is set to 0.

This property is read/write.

## Syntax


```C++
HRESULT put_AudioQualityMode(
  [in]          UINT audioQualityMode
);

HRESULT get_AudioQualityMode(
  [out, retval] UINT *pAudioQualityMode
);
```



## Property value

A value that specifies the audio quality mode.

The possible values are:

<dt>

0
</dt> <dd>

Dynamic audio quality. This is the default audio quality setting. The server dynamically adjusts audio output quality in response to network conditions and the client and server capabilities.

</dd> <dt>

1
</dt> <dd>

Medium audio quality. The server uses a fixed but compressed format for audio output.

</dd> <dt>

2
</dt> <dd>

High audio quality. The server provides audio output in uncompressed PCM format with lower processing overhead for latency.

</dd> </dl>

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

 

 





