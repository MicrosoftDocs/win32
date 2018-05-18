---
title: DnsDomain class
description: Represents a DNS domain.
audience: developer
ms.assetid: '42e43817-1206-4bff-9bca-853453c345f8'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DnsDomain class", "DnsDomain class, described"]
topic_type:
- apiref
api_name:
- DnsDomain
- DnsDomain.DistinguishedName
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# DnsDomain class

Represents a DNS domain.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsDomain
{
  string DistinguishedName;
};
```

## Members

The **DnsDomain** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsDomain** class has these properties.

<dl> <dt>

**DistinguishedName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Lightweight Directory Access Protocol (LDAP) name of the domain.

</dd> </dl>

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

 

 





