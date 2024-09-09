---
title: TransportStatus enumeration
description: Defines the available transport status as defined by the UPnP Guidelines.
ms.assetid: 6fde82f0-9bc4-4abb-9d10-0000501c2b24
keywords:
- TransportStatus enumeration Media Streaming API
topic_type:
- apiref
api_name:
- TransportStatus
api_location:
- Windows.Media.Streaming.idl
api_type:
- IDLDef
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# TransportStatus enumeration

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Defines the available transport status as defined by the UPnP Guidelines.

## Syntax


```C++
typedef enum TransportStatus { 
  Unknown        = 0,
  Ok             = 1,
  ErrorOccurred  = 2,
  Last           = 3
} TransportStatus;
```



## Constants

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown**
</dt> <dd>

Erroneous device status.

</dd> <dt>

<span id="Ok"></span><span id="ok"></span><span id="OK"></span>**Ok**
</dt> <dd>

The device is in a good status.

</dd> <dt>

<span id="ErrorOccurred"></span><span id="erroroccurred"></span><span id="ERROROCCURRED"></span>**ErrorOccurred**
</dt> <dd>

An error occurred on the device.

</dd> <dt>

<span id="Last"></span><span id="last"></span><span id="LAST"></span>**Last**
</dt> <dd>

The device s previous status to the current transport status.

</dd> </dl>

## Requirements



| Requirement | Value |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| IDL<br/> | <dl> <dt>Windows.Media.Streaming.idl (reference Windows.Media.Streaming.idl)</dt> </dl> |



 

 





