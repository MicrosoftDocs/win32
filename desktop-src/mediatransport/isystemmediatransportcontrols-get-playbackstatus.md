---
title: ISystemMediaTransportControls get\_PlaybackStatus method
description: Gets the media playback status.
ms.assetid: '61D27DB6-B3DD-4FD2-B5E9-9BD8DA26A165'
keywords: ["get_PlaybackStatus method", "get_PlaybackStatus method, ISystemMediaTransportControls interface", "ISystemMediaTransportControls interface, get_PlaybackStatus method"]
topic_type:
- apiref
api_name:
- ISystemMediaTransportControls.get_PlaybackStatus
api_location:
- Windows.Media.SystemMediaTransportControls.h
api_type:
- COM
---

# ISystemMediaTransportControls::get\_PlaybackStatus method

Gets the media playback status.

## Syntax


```C++
HRESULT get_PlaybackStatus(
  [out] MediaPlaybackStatus *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Type: **[**MediaPlaybackStatus**](https://msdn.microsoft.com/library/windows/apps/dn278665)\***

The media playback status.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                           |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                                                      |
| Header<br/>                   | <dl> <dt>Windows.Media.SystemMediaTransportControls.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Windows.Media.SystemMediaTransportControls.idl</dt> </dl> |



## See also

<dl> <dt>

[**ISystemMediaTransportControls**](isystemmediatransportcontrols.md)
</dt> </dl>

 

 





