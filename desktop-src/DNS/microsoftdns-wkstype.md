---
title: MicrosoftDNS_WKSType class
description: The subclass of MicrosoftDNS\_ResourceRecord that represents a Well-Known Services (WKS) record.
ms.assetid: 7bbfd518-d473-4127-949b-9133a43ac7a7
keywords:
- MicrosoftDNS_WKSType class DNS
- MicrosoftDNS_WKSType class DNS , described
topic_type:
- apiref
api_name:
- MicrosoftDNS_WKSType
- MicrosoftDNS_WKSType.CreateInstanceFromPropertyData
- MicrosoftDNS_WKSType.Modify
- MicrosoftDNS_WKSType.InternetAddress
- MicrosoftDNS_WKSType.IPProtocol
- MicrosoftDNS_WKSType.Services
api_location:
- Root\MicrosoftDNS
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# MicrosoftDNS\_WKSType class

The subclass of [**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md) that represents a Well-Known Services (WKS) record.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
class MicrosoftDNS_WKSType : MicrosoftDNS_ResourceRecord
{
  string InternetAddress;
  string IPProtocol;
  string Services;
};
```

## Members

The **MicrosoftDNS\_WKSType** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MicrosoftDNS\_WKSType** class has these methods.



| Method                             | Description                                                                                                                                                                                                                                                                                                                                                                     |
|:-----------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CreateInstanceFromPropertyData** | Instantiates a WKS Type of RR based on the data in the method's input parameters: the record's DNS Server Name, Container Name, Owner Name, class (default = IN), time-to-live value, and the owner's Internet Address, IP protocol and port bit mask. It returns a reference to the new object as an output parameter. <br/> Qualifiers: Implemented, static<br/>  |
| **Modify**                         | This method updates the TTL, Internet Address, IP Protocol, and Services to the values specified as the input parameters of this method. If a new value for a parameter is not specified, then the current value for the parameter is not changed. The method returns a reference to the modified object as an output parameter. <br/> Qualifiers: Implemented<br/> |



 

### Properties

The **MicrosoftDNS\_WKSType** class has these properties.

<dl> <dt>

**InternetAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Internet IP address for the record's owner.

</dd> <dt>

**IPProtocol**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

String representing the IP protocol for this record. Valid values are UDP or TCP.

</dd> <dt>

**Services**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

String containing all services used by the Well Known Service (WKS) record.

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

[**CreateInstanceFromPropertyData Method of the MicrosoftDNS\_WKSType Class**](microsoftdns-wkstype-createinstancefrompropertydata.md)
</dt> <dt>

[**Modify Method of the MicrosoftDNS\_WKSType Class**](microsoftdns-wkstype-modify.md)
</dt> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> </dl>

 

 





