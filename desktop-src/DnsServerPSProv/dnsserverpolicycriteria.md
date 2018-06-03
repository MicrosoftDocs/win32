---
title: DnsServerPolicyCriteria class
description: Contains the DNS server policy criteria.
audience: developer
ms.assetid: 1ebbe4aa-9197-4801-893a-07ee1c49d466
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerPolicyCriteria class
- DnsServerPolicyCriteria class, described
topic_type:
- apiref
api_name:
- DnsServerPolicyCriteria
- DnsServerPolicyCriteria.CriteriaType
- DnsServerPolicyCriteria.Criteria
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerPolicyCriteria class

Contains the DNS server policy criteria.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerPolicyCriteria
{
  string CriteriaType;
  string Criteria;
};
```

## Members

The **DnsServerPolicyCriteria** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerPolicyCriteria** class has these properties.

<dl> <dt>

**Criteria**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The criteria.

</dd> <dt>

**CriteriaType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The criteria type.

The possible values are.

<dt>

<span id="ClientSubnet"></span><span id="clientsubnet"></span><span id="CLIENTSUBNET"></span>

**ClientSubnet** ("ClientSubnet")


</dt> <dd></dd> <dt>

<span id="TransportProtocol"></span><span id="transportprotocol"></span><span id="TRANSPORTPROTOCOL"></span>

**TransportProtocol** ("TransportProtocol")


</dt> <dd></dd> <dt>

<span id="NetworkProtocol"></span><span id="networkprotocol"></span><span id="NETWORKPROTOCOL"></span>

**NetworkProtocol** ("NetworkProtocol")


</dt> <dd></dd> <dt>

<span id="Interface"></span><span id="interface"></span><span id="INTERFACE"></span>

**Interface** ("Interface")


</dt> <dd></dd> <dt>

<span id="Fqdn"></span><span id="fqdn"></span><span id="FQDN"></span>

**Fqdn** ("Fqdn")


</dt> <dd></dd> <dt>

<span id="Qtype"></span><span id="qtype"></span><span id="QTYPE"></span>

**Qtype** ("Qtype")


</dt> <dd></dd> <dt>

<span id="Time"></span><span id="time"></span><span id="TIME"></span>

**Time** ("Time")


</dt> <dd></dd> </dl>

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

 

 





