---
title: MicrosoftDNS_ATMAType class
description: The subclass of MicrosoftDNS\_ResourceRecord that represents an ATM Address to Name (ATMA) record.
ms.assetid: 3e9e4032-08a0-4a2e-bcff-f461b69a44d4
keywords:
- MicrosoftDNS_ATMAType class DNS
- MicrosoftDNS_ATMAType class DNS , described
topic_type:
- apiref
api_name:
- MicrosoftDNS_ATMAType
- MicrosoftDNS_ATMAType.CreateInstanceFromPropertyData
- MicrosoftDNS_ATMAType.Modify
- MicrosoftDNS_ATMAType.Format
- MicrosoftDNS_ATMAType.ATMAddress
api_location:
- Root\MicrosoftDNS
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# MicrosoftDNS\_ATMAType class

The subclass of [**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md) that represents an ATM Address to Name (ATMA) record.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
class MicrosoftDNS_ATMAType : MicrosoftDNS_ResourceRecord
{
  uint16 Format;
  string ATMAddress;
};
```

## Members

The **MicrosoftDNS\_ATMAType** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MicrosoftDNS\_ATMAType** class has these methods.



| Method                             | Description                                                                                                                                                                                                                                                                                                                                        |
|:-----------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CreateInstanceFromPropertyData** | Instantiates an ATMA Resource Record based on the data in the method's input parameters: the record's DNS Server Name, Container Name, Owner/Node Name, class (default = IN), time-to-live value, and ATM format and address. Returns a reference to the new object as an output parameter. <br/> Qualifiers: Implemented, static<br/> |
| **Modify**                         | Updates the TTL, Format and ATMA Address to the values specified as the input parameters of this method. If a new value for a parameter is not specified, the current value for the parameter is not changed. The method returns a reference to the modified object as an output parameter. <br/> Qualifiers: Implemented<br/>         |



 

### Properties

The **MicrosoftDNS\_ATMAType** class has these properties.

<dl> <dt>

**ATMAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Variable length string of octets containing the ATM address of the node/owner to which this RR pertains. The first 4 bytes of the array are used to store the size of the octet string. The most significant byte is stored in byte 0.

</dd> <dt>

**Format**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

ATM address format. Valid values are: 0 indicating ATM End System Address (AESA) format and 1 indicating E.164 format.

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

[**CreateInstanceFromPropertyData Method of the MicrosoftDNS\_ATMAType Class**](microsoftdns-atmatype-createinstancefrompropertydata.md)
</dt> <dt>

[**Modify Method of the MicrosoftDNS\_ATMAType Class**](microsoftdns-atmatype-modify.md)
</dt> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> </dl>

 

 





