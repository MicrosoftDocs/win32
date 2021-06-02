---
title: IMsTscAxEvents OnNetworkStatusChanged method
description: Called when the network status has changed. | IMsTscAxEvents OnNetworkStatusChanged method
ms.assetid: 177A410E-2449-4FC7-8DE5-21F83A6DD028
ms.tgt_platform: multiple
keywords:
- OnNetworkStatusChanged method Remote Desktop Services
- OnNetworkStatusChanged method Remote Desktop Services , IMsTscAxEvents interface
- IMsTscAxEvents interface Remote Desktop Services , OnNetworkStatusChanged method
topic_type:
- apiref
api_name:
- IMsTscAxEvents.OnNetworkStatusChanged
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAxEvents::OnNetworkStatusChanged method

Called when the network status has changed.

## Syntax


```C++
void OnNetworkStatusChanged(
  [in] ULONG qualityLevel,
  [in] LONG  bandwidth,
  [in] LONG  rtt
);
```



## Parameters

<dl> <dt>

*qualityLevel* \[in\]
</dt> <dd>

Specifies the new connection speed. This will be one of the following values.

<dt>

1
</dt> <dd>

Less than 512 kilobytes per second (KBps).

</dd> <dt>

2
</dt> <dd>

512 to 1,999 KBps.

</dd> <dt>

3
</dt> <dd>

2,000 to 9,999 KBps.

</dd> <dt>

4
</dt> <dd>

Greater than or equal to 10,000 KBps.

</dd> </dl> </dd> <dt>

*bandwidth* \[in\]
</dt> <dd>

Specifies the connection bandwidth.

</dd> <dt>

*rtt* \[in\]
</dt> <dd>

Specifies the connection latency.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IMsTscAxEvents is defined as 336d5562-efa8-482e-8cb3-c5c0fc7a7db6<br/>           |



## See also

<dl> <dt>

[**IMsTscAxEvents**](imstscaxevents-interface.md)
</dt> </dl>

 

 





