---
Description: Set access scope on an array of DHCP superscopes from IPAM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 44d66163-95f0-493b-b3e8-02b98a49a95e
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: SetDhcpSuperscopeAccessScope method of the MSFT\_IPAM\_AccessScope class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetDhcpSuperscopeAccessScope method of the MSFT\_IPAM\_AccessScope class

Set access scope on an array of DHCP superscopes from IPAM.

## Syntax


```mof
uint32 SetDhcpSuperscopeAccessScope(
  [in]  boolean                  IpamDhcpSuperscope,
  [in]  string                   AccessScopePath,
  [in]  boolean                  IsInheritedAccessScope,
  [in]  MSFT_IPAM_DhcpSuperscope InputObject[],
  [out] MSFT_IPAM_DhcpSuperscope Output[]
);
```



## Parameters

<dl> <dt>

*IpamDhcpSuperscope* \[in\]
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

An array of [**MSFT\_IPAM\_DhcpSuperscope**](msft-ipam-dhcpsuperscope.md) embedded instances.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

Returns the scope as an array of [**MSFT\_IPAM\_DhcpSuperscope**](msft-ipam-dhcpsuperscope.md) embedded instances.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_IPAM\_AccessScope**](msft-ipam-accessscope.md)
</dt> </dl>

 

 




