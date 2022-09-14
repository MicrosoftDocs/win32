---
title: DevicePair Server property (Asptlb.h)
description: Gets the server for the active basic device pair.
ms.assetid: 25FD523F-36C7-4165-BBB2-6A3410D896EF
keywords:
- Server property Media Streaming API
- Server property Media Streaming API , DevicePair interface
- DevicePair interface Media Streaming API , Server property
topic_type:
- apiref
api_name:
- DevicePair.Server
- DevicePair.get_Server
api_location:
- asptlb.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# DevicePair::Server property

Gets the server for the active basic device pair.

This property is read-only.

## Syntax


```C++
HRESULT get_Server(
  [out] ActiveBasicDevice **value
);
```



## Property value

Receives a [**ActiveBasicDevice**](/previous-versions/windows/desktop/legacy/dn385755(v=vs.85)) object that represents the server device.

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Asptlb.h</dt> </dl> |



## See also

<dl> <dt>

[**DevicePair**](/previous-versions/windows/desktop/legacy/dn385771(v=vs.85))
</dt> </dl>

 

