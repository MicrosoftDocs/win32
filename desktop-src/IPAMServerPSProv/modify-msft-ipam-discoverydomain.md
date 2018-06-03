---
Description: Updates the IPAM discovery settings for a domain.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ddd41e9b-ca5d-4ae9-89b3-88819fb1aa26
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Modify method of the MSFT\_IPAM\_DiscoveryDomain class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Modify method of the MSFT\_IPAM\_DiscoveryDomain class

Updates the IPAM discovery settings for a domain.

## Syntax


```mof
uint32 Modify(
  [in]  string                    Name,
  [in]  boolean                   DiscoverDc,
  [in]  boolean                   DiscoverDns,
  [in]  boolean                   DiscoverDhcp,
  [out] MSFT_IPAM_DiscoveryDomain DiscoveryDomain
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the domain.

</dd> <dt>

*DiscoverDc* \[in\]
</dt> <dd>

**True** to enable IPAM to discover domain controllers on the domain; otherwise, **false**.

</dd> <dt>

*DiscoverDns* \[in\]
</dt> <dd>

**True** to enable IPAM to discover DNS servers on the domain; otherwise, **false**.

</dd> <dt>

*DiscoverDhcp* \[in\]
</dt> <dd>

**True** to enable IPAM to discover DHCP servers on the domain; otherwise, **false**.

</dd> <dt>

*DiscoveryDomain* \[out\]
</dt> <dd>

When this method returns, this parameter receives the updated domain.

</dd> </dl>

## Return value

Returns "0" if the operation completes successfully; otherwise, returns a WMI error code.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_IPAM\_DiscoveryDomain**](msft-ipam-discoverydomain.md)
</dt> </dl>

 

 




