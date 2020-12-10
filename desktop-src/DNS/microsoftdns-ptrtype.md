---
title: MicrosoftDNS_PTRType class
description: The subclass of MicrosoftDNS\_ResourceRecord that represents a Pointer (PTR) record.
ms.assetid: 2cb0f13b-e683-473b-9cdd-bc5d805b919d
keywords:
- MicrosoftDNS_PTRType class DNS
- MicrosoftDNS_PTRType class DNS , described
topic_type:
- apiref
api_name:
- MicrosoftDNS_PTRType
- MicrosoftDNS_PTRType.CreateInstanceFromPropertyData
- MicrosoftDNS_PTRType.Modify
- MicrosoftDNS_PTRType.PTRDomainName
api_location:
- Root\MicrosoftDNS
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# MicrosoftDNS\_PTRType class

The subclass of [**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md) that represents a Pointer (PTR) record.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
class MicrosoftDNS_PTRType : MicrosoftDNS_ResourceRecord
{
  string PTRDomainName;
};
```

## Members

The **MicrosoftDNS\_PTRType** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MicrosoftDNS\_PTRType** class has these methods.



| Method                             | Description                                                                                                                                                                                                                                                                                                                                           |
|:-----------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CreateInstanceFromPropertyData** | Instantiates a DNS PTR Resource Record based on the data in the method's input parameters: the record's DNS Server Name, Container Name, Owner Name, class (default = IN), time-to-live value and the FQDN of the PTR record. It returns a reference to the new object as an output parameter. <br/> Qualifiers: Implemented, static<br/> |
| **Modify**                         | Updates the TTL and PTR Domain Name to the values specified as the input parameters of this method. If a new value for a parameter is not specified, the current value for the parameter is not changed. The method returns a reference to the modified object as an output parameter. <br/> Qualifiers: Implemented<br/>                 |



 

### Properties

The **MicrosoftDNS\_PTRType** class has these properties.

<dl> <dt>

**PTRDomainName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

FQDN of the PTR record data.

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

[**CreateInstanceFromPropertyData Method of the MicrosoftDNS\_PTRType Class**](microsoftdns-ptrtype-createinstancefrompropertydata.md)
</dt> <dt>

[**Modify Method of the MicrosoftDNS\_PTRType Class**](microsoftdns-ptrtype-modify.md)
</dt> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> </dl>

 

 





