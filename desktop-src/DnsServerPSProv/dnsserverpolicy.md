---
title: DnsServerPolicy class
description: Contains the DNS server policy.
audience: developer
ms.assetid: f7441c92-0645-4f96-8c9a-7b60c8e2374f
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerPolicy class
- DnsServerPolicy class, described
topic_type:
- apiref
api_name:
- DnsServerPolicy
- DnsServerPolicy.Name
- DnsServerPolicy.Level
- DnsServerPolicy.AppliesOn
- DnsServerPolicy.Action
- DnsServerPolicy.Condition
- DnsServerPolicy.IsEnabled
- DnsServerPolicy.ProcessingOrder
- DnsServerPolicy.ZoneName
- DnsServerPolicy.Criteria
- DnsServerPolicy.Content
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerPolicy class

Contains the DNS server policy.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerPolicy
{
  string                  Name;
  string                  Level;
  string                  AppliesOn;
  string                  Action;
  string                  Condition;
  boolean                 IsEnabled;
  uint32                  ProcessingOrder;
  string                  ZoneName;
  DnsServerPolicyCriteria Criteria[];
  DnsServerPolicyContent  Content[];
};
```

## Members

The **DnsServerPolicy** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerPolicy** class has these properties.

<dl> <dt>

**Action**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The action of the policy.

The possible values are.

<dt>

<span id="Deny"></span><span id="deny"></span><span id="DENY"></span>

**Deny** ("Deny")


</dt> <dd></dd> <dt>

<span id="Allow"></span><span id="allow"></span><span id="ALLOW"></span>

**Allow** ("Allow")


</dt> <dd></dd> <dt>

<span id="Ignore"></span><span id="ignore"></span><span id="IGNORE"></span>

**Ignore** ("Ignore")


</dt> <dd></dd> </dl>

</dd> <dt>

**AppliesOn**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Applies on.

The possible values are.

<dt>

<span id="QueryProcessing"></span><span id="queryprocessing"></span><span id="QUERYPROCESSING"></span>

<span id="QueryProcessing"></span><span id="queryprocessing"></span><span id="QUERYPROCESSING"></span>**QueryProcessing** ("QueryProcessing")


</dt> <dd>

Query processing.

</dd> <dt>

<span id="ZoneTransfer"></span><span id="zonetransfer"></span><span id="ZONETRANSFER"></span>

<span id="ZoneTransfer"></span><span id="zonetransfer"></span><span id="ZONETRANSFER"></span>**ZoneTransfer** ("ZoneTransfer")


</dt> <dd>

Zone transfer.

</dd> <dt>

<span id="DynamicUpdate"></span><span id="dynamicupdate"></span><span id="DYNAMICUPDATE"></span>

<span id="DynamicUpdate"></span><span id="dynamicupdate"></span><span id="DYNAMICUPDATE"></span>**DynamicUpdate** ("DynamicUpdate")


</dt> <dd>

Dynamic update.

</dd> <dt>

<span id="Recursion"></span><span id="recursion"></span><span id="RECURSION"></span>

<span id="Recursion"></span><span id="recursion"></span><span id="RECURSION"></span>**Recursion** ("Recursion")


</dt> <dd>

Recursion.

</dd> </dl>

</dd> <dt>

**Condition**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The condition of the policy.

The possible values are.

<dt>

<span id="And"></span><span id="and"></span><span id="AND"></span>

**And** ("And")


</dt> <dd></dd> <dt>

<span id="Or"></span><span id="or"></span><span id="OR"></span>

**Or** ("Or")


</dt> <dd></dd> </dl>

</dd> <dt>

**Content**
</dt> <dd> <dl> <dt>

Data type: **DnsServerPolicyContent** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerPolicyContent**](dnsserverpolicycontent.md)")
</dt> </dl>

An array of [**DnsServerPolicyContent**](dnsserverpolicycontent.md) containing DNS server policy content.

</dd> <dt>

**Criteria**
</dt> <dd> <dl> <dt>

Data type: **DnsServerPolicyCriteria** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**DnsServerPolicyCriteria**](dnsserverpolicycriteria.md)")
</dt> </dl>

An array of [**DnsServerPolicyCriteria**](dnsserverpolicycriteria.md) containing the DNS server policy criteria.

</dd> <dt>

**IsEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Is enabled.

</dd> <dt>

**Level**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The level of the policy.

The possible values are.

<dt>

<span id="Server"></span><span id="server"></span><span id="SERVER"></span>

<span id="Server"></span><span id="server"></span><span id="SERVER"></span>**Server** ("Server")


</dt> <dd>

The policy applies to a single server.

</dd> <dt>

<span id="Zone"></span><span id="zone"></span><span id="ZONE"></span>

<span id="Zone"></span><span id="zone"></span><span id="ZONE"></span>**Zone** ("Zone")


</dt> <dd>

The policy applies to a zone.

</dd> </dl>

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the policy.

</dd> <dt>

**ProcessingOrder**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The processing order.

</dd> <dt>

**ZoneName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the zone.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





