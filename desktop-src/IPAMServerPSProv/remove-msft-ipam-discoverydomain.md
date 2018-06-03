---
Description: Deletes an Active Directory domain from the IPAM database that is used to discover IP infrastructure servers.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 89a16c64-8326-40a1-aa1c-22a190f3d74a
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Remove method of the MSFT\_IPAM\_DiscoveryDomain class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Remove method of the MSFT\_IPAM\_DiscoveryDomain class

Deletes an Active Directory domain from the IPAM database that is used to discover IP infrastructure servers.

## Syntax


```mof
uint32 Remove(
  [in]  string                    Name,
  [out] MSFT_IPAM_DiscoveryDomain DiscoveryDomain
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the domain to delete.

</dd> <dt>

*DiscoveryDomain* \[out\]
</dt> <dd>

When this method returns, this parameter receives the deleted domain.

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

 

 




