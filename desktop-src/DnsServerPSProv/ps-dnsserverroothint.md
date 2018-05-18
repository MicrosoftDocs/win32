---
title: PS\_DnsServerRootHint class
description: DNS Server Root Hint definition.
audience: developer
ms.assetid: '799266d0-adbf-4a88-9369-31c683db2bdd'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DnsServerRootHint class", "PS_DnsServerRootHint class, described"]
topic_type:
- apiref
api_name:
- PS_DnsServerRootHint
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# PS\_DnsServerRootHint class

DNS Server Root Hint definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerRootHint
{
};
```

## Members

The **PS\_DnsServerRootHint** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerRootHint** class has these methods.



| Method                                                                  | Description                                                                                                                   |
|:------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------|
| [**AddByInputObject**](addbyinputobject-ps-dnsserverroothint.md)       | Adds a DNS root hint to a DNS server based on the specified [**DnsServerRootHint**](dnsserverroothint.md) object.<br/> |
| [**AddByParameters**](addbyparameters-ps-dnsserverroothint.md)         | Adds a DNS root hint to a DNS server based on the specified parameters.<br/>                                            |
| [**Get**](get-ps-dnsserverroothint.md)                                 | Retrieves DNS root hints<br/>                                                                                           |
| [**Import**](import-ps-dnsserverroothint.md)                           | Copies DNS roothints from another server<br/>                                                                           |
| [**RemoveByInputObject**](removebyinputobject-ps-dnsserverroothint.md) | Removes root hints form the list on the server<br/>                                                                     |
| [**RemoveByParameters**](removebyparameters-ps-dnsserverroothint.md)   | Removes root hints form the list on the server<br/>                                                                     |
| [**Set**](set-ps-dnsserverroothint.md)                                 | Updates a DNS root hint.<br/>                                                                                           |



 

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





