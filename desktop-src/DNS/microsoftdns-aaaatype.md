---
title: MicrosoftDNS_AAAAType class
description: Subclass of MicrosoftDNS\_ResourceRecord that represents an IPv6 Address (AAAA) record. The AAAA record is commonly pronounced \ 0034;quad-a record \ 0034;.
ms.assetid: e16a7a69-18df-43dc-add9-700a702724ce
keywords:
- MicrosoftDNS_AAAAType class DNS
- MicrosoftDNS_AAAAType class DNS , described
topic_type:
- apiref
api_name:
- MicrosoftDNS_AAAAType
- MicrosoftDNS_AAAAType.CreateInstanceFromPropertyData
- MicrosoftDNS_AAAAType.Modify
- MicrosoftDNS_AAAAType.IPv6Address
api_location:
- Root\MicrosoftDNS
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# MicrosoftDNS\_AAAAType class

Subclass of [**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md) that represents an IPv6 Address (AAAA) record. The AAAA record is commonly pronounced "quad-a record".

The following syntax is simplified from MOF code.

## Syntax

``` syntax
class MicrosoftDNS_AAAAType : MicrosoftDNS_ResourceRecord
{
  string IPv6Address;
};
```

## Members

The **MicrosoftDNS\_AAAAType** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MicrosoftDNS\_AAAAType** class has these methods.



| Method                             | Description                                                                                                                                                                                                                                                                                                                                  |
|:-----------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CreateInstanceFromPropertyData** | Instantiates an 'AAAA' type of RR based on the data in the method's input parameters: the record's DNS Server Name, Container Name, Owner/Host Name, class (default = IN), time-to-live value, and the IPv6 address. It returns a reference to the new object as an output parameter. <br/> Qualifiers: Implemented, static<br/> |
| **Modify**                         | Updates the TTL and IPv6 address to the values specified as the input parameters of this method. If a new value for a parameter is not specified, then the current value for the parameter is not changed. The method returns a reference to the modified object as an output parameter. <br/> Qualifiers: Implemented<br/>      |



 

### Properties

The **MicrosoftDNS\_AAAAType** class has these properties.

<dl> <dt>

**IPv6Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

IPv6 address for the host.

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

[**CreateInstanceFromPropertyData Method of the MicrosoftDNS\_AAAAType Class**](microsoftdns-aaaatype-createinstancefrompropertydata.md)
</dt> <dt>

[**Modify Method of the MicrosoftDNS\_AAAAType Class**](microsoftdns-aaaatype-modify.md)
</dt> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> </dl>

 

 





