---
description: Enables the TCPIP checksum offload properties on the network adapter.
ms.assetid: c9df0070-77ba-4371-ba60-a67d3fc972d9
title: Enable method of the MSFT\_NetAdapterChecksumOffloadSettingData class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- kbSyntax
api_name: 
api_type: 
api_location: 
---

# Enable method of the MSFT\_NetAdapterChecksumOffloadSettingData class

Enables the TCPIP checksum offload properties on the network adapter.

## Syntax


```mof
uint32 Enable(
  [in]  boolean IpIPv4,
  [in]  boolean TcpIPv4,
  [in]  boolean TcpIPv6,
  [in]  boolean UdpIPv4,
  [in]  boolean UdpIPv6,
  [in]  uint32  RxTxControl,
  [out] string  cmdletOutput
);
```



## Parameters

<dl> <dt>

*IpIPv4* \[in\]
</dt> <dd>

**true** to enable IP checksum offload for IPv4 packets.

</dd> <dt>

*TcpIPv4* \[in\]
</dt> <dd>

**true** to enable TCP checksum offload for IPv4 packets.

</dd> <dt>

*TcpIPv6* \[in\]
</dt> <dd>

**true** to enable TCP checksum offload for IPv6 packets.

</dd> <dt>

*UdpIPv4* \[in\]
</dt> <dd>

**true** to enable UDP checksum offload for IPv4 packets.

</dd> <dt>

*UdpIPv6* \[in\]
</dt> <dd>

**true** to enable UDP checksum offload for IPv6 packets.

</dd> <dt>

*RxTxControl* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**MSFT\_NetAdapterChecksumOffloadSettingData**](msft-netadapterchecksumoffloadsettingdata.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_NetAdapterChecksumOffloadSettingData**](msft-netadapterchecksumoffloadsettingdata.md)
</dt> </dl>

 

 




