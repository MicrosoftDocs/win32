---
title: ISystemMediaTransportControls put\_PlaybackStatus method
description: Sets the media playback status.
ms.assetid: FA69B2EF-F5CF-41D3-B766-F1C5BD4D1231
keywords:
- put_PlaybackStatus method
- put_PlaybackStatus method, ISystemMediaTransportControls interface
- ISystemMediaTransportControls interface, put_PlaybackStatus method
topic_type:
- apiref
api_name:
- ISystemMediaTransportControls.put_PlaybackStatus
api_location:
- Windows.Media.SystemMediaTransportControls.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ISystemMediaTransportControls::put\_PlaybackStatus method

Sets the media playback status.

## Syntax


```C++
HRESULT put_PlaybackStatus(
   MediaPlaybackStatus value
);
```



## Parameters

<dl> <dt>

*value* 
</dt> <dd>

Type: **[**MediaPlaybackStatus**](https://msdn.microsoft.com/library/windows/apps/dn278665)**

The media playback status.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                           |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                                                      |
| Header<br/>                   | <dl> <dt>Windows.Media.SystemMediaTransportControls.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Windows.Media.SystemMediaTransportControls.idl</dt> </dl> |



## See also

<dl> <dt>

[**ISystemMediaTransportControls**](isystemmediatransportcontrols.md)
</dt> </dl>

 

 





