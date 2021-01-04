---
title: ControlReconnectStatus enumeration
description: Specifies the result of the IMsRdpClient8 Reconnect method.
ms.assetid: FB0AC4CF-18F5-4CDD-A75C-59A7CF716688
ms.tgt_platform: multiple
keywords:
- ControlReconnectStatus enumeration Remote Desktop Services
topic_type:
- apiref
api_name:
- ControlReconnectStatus
api_location:
- MsTscAx.dll
api_type:
- LibDef
ms.topic: reference
ms.date: 05/31/2018
---

# ControlReconnectStatus enumeration

Specifies the result of the [**IMsRdpClient8::Reconnect**](imsrdpclient8-reconnect.md) method.

## Syntax


```C++
typedef enum  { 
  controlReconnectStarted  = 0x0000,
  controlReconnectBlocked  = 0x0001
} ControlReconnectStatus;
```



## Constants

<dl> <dt>

<span id="controlReconnectStarted"></span><span id="controlreconnectstarted"></span><span id="CONTROLRECONNECTSTARTED"></span>**controlReconnectStarted**
</dt> <dd>

The reconnect operation was started.

</dd> <dt>

<span id="controlReconnectBlocked"></span><span id="controlreconnectblocked"></span><span id="CONTROLRECONNECTBLOCKED"></span>**controlReconnectBlocked**
</dt> <dd>

The reconnect operation could not be started.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |



## See also

<dl> <dt>

[**IMsRdpClient8::Reconnect**](imsrdpclient8-reconnect.md)
</dt> </dl>

 

 





