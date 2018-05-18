---
Description: 'Set access scope on an array of DNS conditional forwarders from IPAM.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'de6e2b34-1a07-4153-af15-a4d6a40f657d'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'SetDnsConditionalForwarderAccessScope method of the MSFT\_IPAM\_AccessScope class'
---

# SetDnsConditionalForwarderAccessScope method of the MSFT\_IPAM\_AccessScope class

Set access scope on an array of DNS conditional forwarders from IPAM.

## Syntax


```mof
uint32 SetDnsConditionalForwarderAccessScope(
  [in]  boolean                           IpamDnsConditionalForwarder,
  [in]  string                            AccessScopePath,
  [in]  boolean                           IsInheritedAccessScope,
  [in]  MSFT_IPAM_DnsConditionalForwarder InputObject[],
  [out] MSFT_IPAM_DnsConditionalForwarder Output[]
);
```



## Parameters

<dl> <dt>

*IpamDnsConditionalForwarder* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*AccessScopePath* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*IsInheritedAccessScope* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*InputObject* \[in\]
</dt> <dd>

An array of [**MSFT\_IPAM\_DnsConditionalForwarder**](msft-ipam-dnsconditionalforwarder.md) embedded instances.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

Returns the scope as an array of [**MSFT\_IPAM\_DnsConditionalForwarder**](msft-ipam-dnsconditionalforwarder.md) embedded instances.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_IPAM\_AccessScope**](msft-ipam-accessscope.md)
</dt> </dl>

 

 




