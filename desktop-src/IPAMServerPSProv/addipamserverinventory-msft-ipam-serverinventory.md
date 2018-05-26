---
Description: Adds an infrastructure server to the IPAM server inventory.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1b233b59-9381-4d23-a31f-ea8d8635e7f7
ms.prod: windows-server-dev
ms.technology:
- internet-protocol-address-management
- windows-management-instrumentation
ms.tgt_platform: multiple
title: AddIpamServerInventory method of the MSFT\_IPAM\_ServerInventory class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AddIpamServerInventory method of the MSFT\_IPAM\_ServerInventory class

Adds an infrastructure server to the IPAM server inventory.

## Syntax


```mof
uint32 AddIpamServerInventory(
  [in]  string                    Name,
  [in]  uint16                    ServerType[],
  [in]  uint16                    ManageabilityStatus,
  [in]  string                    Description,
  [in]  string                    CustomConfiguration,
  [in]  string                    Owner,
  [in]  string                    ForestName,
  [out] MSFT_IPAM_ServerInventory Output
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the server.

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

*CustomConfiguration* \[in\]
</dt> <dd>

The custom metadata assigned to the server.

</dd> <dt>

*Owner* \[in\]
</dt> <dd>

The owner of the server.

</dd> <dt>

*ForestName* \[in\]
</dt> <dd>

The forest name for this server.

**Windows Server 2012 R2:** This property is unavailable prior to Windows Server 2016.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

When this method returns, this parameter contains the added server object.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

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

[**MSFT\_IPAM\_ServerInventory**](msft-ipam-serverinventory.md)
</dt> </dl>

 

 




