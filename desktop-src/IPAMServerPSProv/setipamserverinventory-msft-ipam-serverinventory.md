---
Description: 'Updates an infrastructure server in the IPAM server inventory.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '99f2aa17-8030-4a06-b548-773b7d9241ca'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'SetIpamServerInventory method of the MSFT\_IPAM\_ServerInventory class'
---

# SetIpamServerInventory method of the MSFT\_IPAM\_ServerInventory class

Updates an infrastructure server in the IPAM server inventory.

## Syntax


```mof
uint32 SetIpamServerInventory(
  [in]  string                    Name,
  [in]  string                    NewName,
  [in]  uint16                    ServerType[],
  [in]  uint16                    ManageabilityStatus,
  [in]  string                    Description,
  [in]  string                    AddCustomConfiguration,
  [in]  string                    RemoveCustomConfiguration,
  [in]  string                    Owner,
  [out] MSFT_IPAM_ServerInventory Output
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the server.

</dd> <dt>

*NewName* \[in\]
</dt> <dd>

The new name of the server.

</dd> <dt>

*ServerType* \[in\]
</dt> <dd>

An array that contains the server roles that are running on the server.

The possible values are:

<dt>

0
</dt> <dd>

None

</dd> <dt>

1
</dt> <dd>

Domain Controller

</dd> <dt>

2
</dt> <dd>

Domain Name System (DNS)

</dd> <dt>

3
</dt> <dd>

Dynamic Host Configuration Protocol (DHCP)

</dd> <dt>

3
</dt> <dd>

Network Policy Server (NPS)

</dd> </dl> </dd> <dt>

*ManageabilityStatus* \[in\]
</dt> <dd>

Indicates whether IPAM is managing the server.

The possible values are:

<dt>

1
</dt> <dd>

IPAM is managing the server.

</dd> <dt>

2
</dt> <dd>

IPAM is not managing the server.

</dd> </dl> </dd> <dt>

*Description* \[in\]
</dt> <dd>

A description of the server.

</dd> <dt>

*AddCustomConfiguration* \[in\]
</dt> <dd>

The custom metadata assigned to add to the server.

</dd> <dt>

*RemoveCustomConfiguration* \[in\]
</dt> <dd>

The custom metadata assigned to remove from the server.

</dd> <dt>

*Owner* \[in\]
</dt> <dd>

The owner of the server.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

When this method returns, this parameter contains the updated server object.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                   |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_IPAM\_ServerInventory**](msft-ipam-serverinventory.md)
</dt> </dl>

 

 




