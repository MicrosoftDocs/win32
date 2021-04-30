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
ms.date: 05/31/2018
---

# TransportStatus enumeration

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



 

 





