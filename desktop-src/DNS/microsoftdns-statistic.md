---
title: MicrosoftDNS_Statistic class
description: The MicrosoftDNS\_Statistic class represents a single DNS Server statistic.
ms.assetid: 49ee79d6-b93f-4a9b-8054-1ad290d092d6
keywords:
- MicrosoftDNS_Statistic class DNS
- MicrosoftDNS_Statistic class DNS , described
topic_type:
- apiref
api_name:
- MicrosoftDNS_Statistic
- MicrosoftDNS_Statistic.DnsServerName
- MicrosoftDNS_Statistic.CollectionName
- MicrosoftDNS_Statistic.CollectionId
- MicrosoftDNS_Statistic.Name
- MicrosoftDNS_Statistic.Value
- MicrosoftDNS_Statistic.StringValue
api_location:
- Root\MicrosoftDNS
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# MicrosoftDNS\_Statistic class

The **MicrosoftDNS\_Statistic** class represents a single DNS Server statistic.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
class MicrosoftDNS_Statistic
{
  string DnsServerName;
  string CollectionName;
  uint32 CollectionId;
  string Name;
  uint32 Value;
  string StringValue;
};
```

## Members

The **MicrosoftDNS\_Statistic** class has these types of members:

-   [Properties](#properties)

### Properties

The **MicrosoftDNS\_Statistic** class has these properties.

<dl> <dt>

**CollectionId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Numeric representation of **CollectionName**.

</dd> <dt>

**CollectionName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the collection to which the statistic belongs.

</dd> <dt>

**DnsServerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the FQDN or IP address of the DNS Server that contains the statistic.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the statistic.

</dd> <dt>

**StringValue**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

String value of the statistic, used only when the statistic value is not represented as a DWORD.

</dd> <dt>

**Value**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Numeric value of the statistic, represented as a DWORD.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\MicrosoftDNS<br/>                                                          |
| MOF<br/>                      | <dl> <dt>Dnsprov.mof</dt> </dl> |



## See also

<dl> <dt>

[MicrosoftDNS\_StatisticCollection](microsoftdns-statisticcollection.md)
</dt> </dl>

 

 





