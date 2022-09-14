---
title: MicrosoftDNS_MBType class
description: The subclass of MicrosoftDNS\_ResourceRecord that represents a Mailbox (MB) resource record.
ms.assetid: b8f3b106-58f4-44b8-b2db-b00f1a495641
keywords:
- MicrosoftDNS_MBType class DNS
- MicrosoftDNS_MBType class DNS , described
topic_type:
- apiref
api_name:
- MicrosoftDNS_MBType
- MicrosoftDNS_MBType.CreateInstanceFromPropertyData
- MicrosoftDNS_MBType.Modify
- MicrosoftDNS_MBType.MBHost
api_location:
- Root\MicrosoftDNS
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# MicrosoftDNS\_MBType class

The subclass of [**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md) that represents a Mailbox (MB) resource record.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
class MicrosoftDNS_MBType : MicrosoftDNS_ResourceRecord
{
  string MBHost;
};
```

## Members

The **MicrosoftDNS\_MBType** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MicrosoftDNS\_MBType** class has these methods.



| Method                             | Description                                                                                                                                                                                                                                                                                                                               |
|:-----------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CreateInstanceFromPropertyData** | Instantiates an MB RR based on the data in the method's input parameters: the record's DNS Server Name, Container Name, Owner Name of the mailbox, class (default = IN), time-to-live value and the mailbox host. It returns a reference to the new object as an output parameter. <br/> Qualifiers: Implemented, static<br/> |
| **Modify**                         | Updates the TTL and MB host to the values specified as the input parameters of this method. If a new value for a parameter is not specified, then the current value for the parameter is not changed. The method returns a reference to the modified object as an output parameter. <br/> Qualifiers: Implemented<br/>        |



 

### Properties

The **MicrosoftDNS\_MBType** class has these properties.

<dl> <dt>

**MBHost**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

FQDN that specifies a host of the mailbox specified in the record's Owner Name.

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

[**CreateInstanceFromPropertyData Method of the MicrosoftDNS\_MBType Class**](microsoftdns-mbtype-createinstancefrompropertydata.md)
</dt> <dt>

[**Modify Method of the MicrosoftDNS\_MBType Class**](microsoftdns-mbtype-modify.md)
</dt> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> </dl>

 

 





