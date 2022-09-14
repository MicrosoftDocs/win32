---
title: MicrosoftDNS_MGType class
description: The subclass of MicrosoftDNS\_ResourceRecord that represents a Mail Group (MG) record.
ms.assetid: ce5795d1-e575-46ef-ad82-62b329e261d6
keywords:
- MicrosoftDNS_MGType class DNS
- MicrosoftDNS_MGType class DNS , described
topic_type:
- apiref
api_name:
- MicrosoftDNS_MGType
- MicrosoftDNS_MGType.CreateInstanceFromPropertyData
- MicrosoftDNS_MGType.Modify
- MicrosoftDNS_MGType.MGMailbox
api_location:
- Root\MicrosoftDNS
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
---

# MicrosoftDNS\_MGType class

The subclass of [**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md) that represents a Mail Group (MG) record.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
class MicrosoftDNS_MGType : MicrosoftDNS_ResourceRecord
{
  string MGMailbox;
};
```

## Members

The **MicrosoftDNS\_MGType** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MicrosoftDNS\_MGType** class has these methods.



| Method                             | Description                                                                                                                                                                                                                                                                                                                                                      |
|:-----------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CreateInstanceFromPropertyData** | This method instantiates an MG Type of RR based on the data in the method's input parameters: the record's DNS Server Name, Container Name, Owner Name of the mail group, class (default = IN), time-to-live value and the mailbox name. It returns a reference to the new object as an output parameter. <br/> Qualifiers: Implemented, static<br/> |
| **Modify**                         | This method updates the TTL and MG Mailbox to the values specified as the input parameters of this method. If a new value for a parameter is not specified, then the current value for the parameter is not changed. The method returns a reference to the modified object as an output parameter. <br/> Qualifiers: Implemented<br/>                |



 

### Properties

The **MicrosoftDNS\_MGType** class has these properties.

<dl> <dt>

**MGMailbox**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

FQDN specifying a mailbox that is a member of the mail group specified by the record's owner name.

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

[**CreateInstanceFromPropertyData Method of the MicrosoftDNS\_MGType Class**](microsoftdns-mgtype-createinstancefrompropertydata.md)
</dt> <dt>

[**Modify Method of the MicrosoftDNS\_MGType Class**](microsoftdns-mgtype-modify.md)
</dt> <dt>

[**MicrosoftDNS\_ResourceRecord**](microsoftdns-resourcerecord.md)
</dt> </dl>

 

 





