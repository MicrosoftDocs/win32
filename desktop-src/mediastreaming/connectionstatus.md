---
title: ConnectionStatus enumeration
description: Represents the state of the device in the network as last seen.
ms.assetid: 'e1893a59-ce7d-4e9c-a013-02ac916d4ee8'
keywords:
- ConnectionStatus enumeration Media Streaming API
topic_type:
- apiref
api_name:
- ConnectionStatus
api_location:
- Windows.Media.Streaming.idl
api_type:
- IDLDef
ms.topic: reference
ms.date: 05/31/2018
---

# ConnectionStatus enumeration

Represents the state of the device in the network as last seen.

## Syntax


```C++
typedef enum ConnectionStatus { 
  Online    = 0,
  Offline   = 1,
  Sleeping  = 2
} ConnectionStatus;
```



## Constants

<dl> <dt>

<span id="Online"></span><span id="online"></span><span id="ONLINE"></span>**Online**
</dt> <dd>

Device is online and active on the network.

</dd> <dt>

<span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span>**Offline**
</dt> <dd>

Device is offline.

</dd> <dt>

<span id="Sleeping"></span><span id="sleeping"></span><span id="SLEEPING"></span>**Sleeping**
</dt> <dd>

Device is currently offline but might automatically wake up when an attempt is made to communicate with it.

</dd> </dl>

## Requirements



| Requirement | Value |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| IDL<br/> | <dl> <dt>Windows.Media.Streaming.idl (reference Windows.Media.Streaming.idl)</dt> </dl> |



 

 





