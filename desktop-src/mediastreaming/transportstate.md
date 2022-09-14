---
title: TransportState enumeration
description: Defines the available transport states as defined by the UPnP Guidelines.
ms.assetid: 2F942EAC-514B-4E65-A12F-85558E9A96A0
keywords:
- TransportState enumeration Media Streaming API
topic_type:
- apiref
api_name:
- TransportState
api_location:
- Windows.Media.Streaming.idl
api_type:
- IDLDef
ms.topic: reference
ms.date: 05/31/2018
---

# TransportState enumeration

Defines the available transport states as defined by the UPnP Guidelines.

## Syntax


```C++
typedef enum _TransportState { 
  Unknown         = 0,
  Stopped         = 1,
  Playing         = 2,
  Transitioning   = 3,
  Paused          = 4,
  Recording       = 5,
  NoMediaPresent  = 6,
  Last            = 7
} TransportState;
```



## Constants

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown**
</dt> <dd>

Erroneous device state.

</dd> <dt>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>**Stopped**
</dt> <dd>

The device s transport is in a stopped state.

</dd> <dt>

<span id="Playing"></span><span id="playing"></span><span id="PLAYING"></span>**Playing**
</dt> <dd>

The device s transport is in a playing state.

</dd> <dt>

<span id="Transitioning"></span><span id="transitioning"></span><span id="TRANSITIONING"></span>**Transitioning**
</dt> <dd>

The device s transport is in a transitioning state which will result in another state value.

</dd> <dt>

<span id="Paused"></span><span id="paused"></span><span id="PAUSED"></span>**Paused**
</dt> <dd>

The device s transport is in a paused state.

</dd> <dt>

<span id="Recording"></span><span id="recording"></span><span id="RECORDING"></span>**Recording**
</dt> <dd>

The device s transport is in a recording state.

</dd> <dt>

<span id="NoMediaPresent"></span><span id="nomediapresent"></span><span id="NOMEDIAPRESENT"></span>**NoMediaPresent**
</dt> <dd>

The device s transport does not have an URI set for playback.

</dd> <dt>

<span id="Last"></span><span id="last"></span><span id="LAST"></span>**Last**
</dt> <dd>

The device s previous state to the current transport state.

</dd> </dl>

## Requirements



| Requirement | Value |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| IDL<br/> | <dl> <dt>Windows.Media.Streaming.idl (reference Windows.Media.Streaming.idl)</dt> </dl> |



 

 





