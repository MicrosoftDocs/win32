---
title: MicrosoftDNS_X25Type class
description: The subclass of MicrosoftDNS\_ResourceRecord that represents an X.25 (X25) record.
ms.assetid: 1213dfd7-30b3-413e-b723-f4284fa0b416
keywords:
- MicrosoftDNS_X25Type class DNS
- MicrosoftDNS_X25Type class DNS , described
topic_type:
- apiref
api_name:
- MicrosoftDNS_X25Type
- MicrosoftDNS_X25Type.CreateInstanceFromPropertyData
- MicrosoftDNS_X25Type.Modify
- MicrosoftDNS_X25Type.PSDNAddress
api_location:
- Root\MicrosoftDNS
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# MicrosoftDNS\_X25Type class

The subclass of [**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md) that represents an X.25 (X25) record.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
class MicrosoftDNS_X25Type : MicrosoftDNS_ResourceRecord
{
  string PSDNAddress;
};
```

## Members

The **MicrosoftDNS\_X25Type** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MicrosoftDNS\_X25Type** class has these methods.



| Method                             | Description                                                                                                                                                                                                                                                                                                                                         |
|:-----------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CreateInstanceFromPropertyData** | Instantiates an 'X25' Type of RR based on the data in the method's input parameters: the record's DNS Server Name, Container Name, Owner Name, class (default = IN), time-to-live value, and the PSDN address. It returns a reference to the new object as an output parameter. <br/> Qualifiers: Implemented, static<br/>              |
| **Modify**                         | This method updates the TTL and PSDN Address to the values specified as the input parameters of this method. If a new value for a parameter is not specified, then the current value for the parameter is not changed. The method returns a reference to the modified object as an output parameter. <br/> Qualifiers: Implemented<br/> |



 

### Properties

The **MicrosoftDNS\_X25Type** class has these properties.

<dl> <dt>

**PSDNAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

PSDN address of the owner of the RR.

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

[**CreateInstanceFromPropertyData Method of the MicrosoftDNS\_X25Type Class**](microsoftdns-x25type-createinstancefrompropertydata.md)
</dt> <dt>

[**Modify Method of the MicrosoftDNS\_X25Type Class**](microsoftdns-x25type-modify.md)
</dt> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> </dl>

 

 





