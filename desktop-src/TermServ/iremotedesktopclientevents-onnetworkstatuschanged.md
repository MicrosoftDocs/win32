---
title: IRemoteDesktopClientEvents OnNetworkStatusChanged method
description: Called when the network status has changed. | IRemoteDesktopClientEvents OnNetworkStatusChanged method
ms.assetid: B68D1AA0-6403-40CA-95C5-BBBF39CEFFD8
ms.tgt_platform: multiple
keywords:
- OnNetworkStatusChanged method Remote Desktop Services
- OnNetworkStatusChanged method Remote Desktop Services , IRemoteDesktopClientEvents interface
- IRemoteDesktopClientEvents interface Remote Desktop Services , OnNetworkStatusChanged method
topic_type:
- apiref
api_name:
- IRemoteDesktopClientEvents.OnNetworkStatusChanged
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IRemoteDesktopClientEvents::OnNetworkStatusChanged method

Called when the network status has changed.

## Syntax


```C++
void OnNetworkStatusChanged(
  [in] unsigned long qualityLevel,
  [in] long          bandwidth,
  [in] long          rtt
);
```



## Parameters

<dl> <dt>

*qualityLevel* \[in\]
</dt> <dd>

The new quality level of the connection. The quality level is determined from the bandwidth and round-trip time (rtt) values.

One of the following values.



| Value                                                                        | Meaning                                                     |
|------------------------------------------------------------------------------|-------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | The quality level could not be determined.<br/>       |
| <dl> <dt>1</dt> </dl> | The connection quality is poor (one bar).<br/>        |
| <dl> <dt>2</dt> </dl> | The connection quality is fair (two bars).<br/>       |
| <dl> <dt>3</dt> </dl> | The connection quality is good (three bars).<br/>     |
| <dl> <dt>4</dt> </dl> | The connection quality is excellent (four bars).<br/> |



 

</dd> <dt>

*bandwidth* \[in\]
</dt> <dd>

Specifies the new connection bandwidth, in kilobits per second (Kbps).

</dd> <dt>

*rtt* \[in\]
</dt> <dd>

Specifies the new connection roundtrip time (latency), in milliseconds.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                 |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>         |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>         |
| IID<br/>                      | DIID\_IRemoteDesktopClientEvents is defined as 079863B7-6D47-4105-8BFE-0CDCB360E67D<br/> |



## See also

<dl> <dt>

[**IRemoteDesktopClientEvents**](iremotedesktopclientevents.md)
</dt> </dl>

 

 





