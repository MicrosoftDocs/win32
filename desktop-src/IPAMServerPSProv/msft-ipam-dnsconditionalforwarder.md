---
Description: 'DNS conditional forwarder object in IPAM.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'fddb1924-682c-410e-8fb9-793af1242a86'
ms.prod: 'windows-server-dev'
ms.technology:
- 'internet-protocol-address-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'MSFT\_IPAM\_DnsConditionalForwarder class'
---

# MSFT\_IPAM\_DnsConditionalForwarder class

DNS conditional forwarder object in IPAM.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("IPAMServerPSProvider"), AMENDMENT]
class MSFT_IPAM_DnsConditionalForwarder
{
  string  InstanceID;
  string  ConditionalForwarderName;
  string  ServerFqdn;
  string  MasterServers[];
  uint64  ForwarderTimeout;
  string  DirectoryPartitionName;
  string  ReplicationScope;
  boolean IsADIntegrated;
  string  AccessScopePath;
  boolean IsInheritedAccessScope;
};
```

## Members

The **MSFT\_IPAM\_DnsConditionalForwarder** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_IPAM\_DnsConditionalForwarder** class has these properties.

<dl> <dt>

**AccessScopePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Access scope path for this DNS conditional forwarder.

</dd> <dt>

**ConditionalForwarderName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the DNS conditional forwarder.

</dd> <dt>

**DirectoryPartitionName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Directory partition name for this DNS conditional forwarder.

</dd> <dt>

**ForwarderTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Forwarder timeout for this DNS conditional forwarder.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Opaquely and uniquely identifies an instance of this class within the scope of the instantiating Namespace.

</dd> <dt>

**IsADIntegrated**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether this DNS conditional forwarder is active directory integrated or not.

</dd> <dt>

**IsInheritedAccessScope**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the access scope for this DNS conditional forwarder is inherited from parent.

</dd> <dt>

**MasterServers**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Master servers for this DNS conditional forwarder.

</dd> <dt>

**ReplicationScope**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Replication scope for this DNS conditional forwarder.

</dd> <dt>

**ServerFqdn**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

DNS server fully qualified domain name to which this DNS conditional forwarder belongs.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\IPAM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>IPAMServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IPAMServerPSProvider.dll</dt> </dl> |



 

 




