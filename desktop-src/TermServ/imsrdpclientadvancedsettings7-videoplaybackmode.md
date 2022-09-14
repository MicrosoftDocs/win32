---
title: IMsRdpClientAdvancedSettings7 VideoPlaybackMode property
description: Specifies or retrieves a value that indicates the video playback mode.
ms.assetid: 83f0baa3-3ac2-47ee-b106-5beaf60d73d2
ms.tgt_platform: multiple
keywords:
- VideoPlaybackMode property Remote Desktop Services
- VideoPlaybackMode property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , VideoPlaybackMode property
- VideoPlaybackMode property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , VideoPlaybackMode property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings7.VideoPlaybackMode
- IMsRdpClientAdvancedSettings7.get_VideoPlaybackMode
- IMsRdpClientAdvancedSettings7.put_VideoPlaybackMode
- IMsRdpClientAdvancedSettings8.VideoPlaybackMode
- IMsRdpClientAdvancedSettings8.get_VideoPlaybackMode
- IMsRdpClientAdvancedSettings8.put_VideoPlaybackMode
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings7::VideoPlaybackMode property

Specifies or retrieves a value that indicates the video playback mode.

This property is read/write.

## Syntax


```C++
HRESULT put_VideoPlaybackMode(
  [in]          UINT videoPlaybackMode
);

HRESULT get_VideoPlaybackMode(
  [out, retval] UINT *pVideoPlaybackMode
);
```



## Property value

A value that specifies the video playback mode.

The possible values are:

<dt>

1
</dt> <dd>

The default video playback mode. When the video playback mode is set to this value, video redirection is controlled by the [**AudioRedirectionMode**](imsrdpclientsecuredsettings-autoredirectionmode.md) property. When the **AudioRedirectionMode** property is set to **AUDIO\_MODE\_REDIRECT**, video is decoded and rendered on the client.

</dd> <dt>

0
</dt> <dd>

Video playback redirection is disabled, even when [**AudioRedirectionMode**](imsrdpclientsecuredsettings-autoredirectionmode.md) is set to **AUDIO\_MODE\_REDIRECT**. In this mode, video is decoded and rendered on the RD Session Host server.

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

 

 





