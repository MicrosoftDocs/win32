---
description: Disables the TCPIP checksum offload properties on the network adapter.
ms.assetid: 5b766937-6c37-4873-9de8-0fc29d969f67
title: Disable method of the MSFT\_NetAdapterChecksumOffloadSettingData class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- kbSyntax
api_name: 
api_type: 
api_location: 
---

# Disable method of the MSFT\_NetAdapterChecksumOffloadSettingData class

Disables the TCPIP checksum offload properties on the network adapter.

## Syntax


```mof
uint32 Disable(
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

**true** to disable IP checksum offload for IPv4 packets.

</dd> <dt>

*TcpIPv4* \[in\]
</dt> <dd>

**true** to disable TCP checksum offload for IPv4 packets.

</dd> <dt>

*TcpIPv6* \[in\]
</dt> <dd>

**true** to disable TCP checksum offload for IPv6 packets.

</dd> <dt>

*UdpIPv4* \[in\]
</dt> <dd>

**true** to disable UDP checksum offload for IPv4 packets.

</dd> <dt>

*UdpIPv6* \[in\]
</dt> <dd>

**true** to disable UDP checksum offload for IPv6 packets.

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

 

 




