---
description: Represents a record in a DNS client cache.
ms.assetid: 86422d6e-c0ab-46a0-aacf-f3fe017eef80
title: MSFT\_DNSClientCache class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_DNSClientCache
- MSFT_DNSClientCache.InstanceId
- MSFT_DNSClientCache.Caption
- MSFT_DNSClientCache.Description
- MSFT_DNSClientCache.ElementName
- MSFT_DNSClientCache.Entry
- MSFT_DNSClientCache.Name
- MSFT_DNSClientCache.Type
- MSFT_DNSClientCache.TimeToLive
- MSFT_DNSClientCache.DataLength
- MSFT_DNSClientCache.Section
- MSFT_DNSClientCache.Data
- MSFT_DNSClientCache.Status
api_type: 
- DllExport
api_location: 
- DnsClientCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_DNSClientCache class

Represents a record in a DNS client cache.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_DNSClientCache : CIM_ManagedElement
{
  string InstanceId;
  string Caption;
  string Description;
  string ElementName;
  string Entry;
  string Name;
  uint16 Type;
  uint32 TimeToLive;
  uint16 DataLength;
  uint8  Section;
  string Data;
  uint32 Status;
};
```

## Members

The **MSFT\_DNSClientCache** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_DNSClientCache** class has these methods.



| Method                                     | Description                                                    |
|:-------------------------------------------|:---------------------------------------------------------------|
| [**Clear**](clear-msft-dnsclientcache.md) | Deletes the cache record from the DNS client cache.<br/> |



 

### Properties

The **MSFT\_DNSClientCache** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/win32/wmisdk/standard-qualifiers) (64), [**Dynamic**](/windows/win32/wmisdk/standard-wmi-qualifiers)
</dt> </dl>

Gets the short description of the cache record.

This property is inherited from **CIM\_ManagedElement**.

</dd> <dt>

**Data**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the DNS record data from the cache record.

</dd> <dt>

**DataLength**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the length of the cache record, in bytes.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the description of the cache record.

This property is inherited from **CIM\_ManagedElement**.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the user-friendly name of the cache record.

This property is inherited from **CIM\_ManagedElement**.

</dd> <dt>

**Entry**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Gets the resource name of the cache record.

</dd> <dt>

**InstanceId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the unique identifier of this object. The ID must be unique within the scope of the instantiating namespace.

This property is inherited from **CIM\_ManagedElement**.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Gets the DNS record name of the cache record.

</dd> <dt>

**Section**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the section of the DNS record from which the cache record originates.

This property contains one of the following values:



| Value                                                                        | Meaning               |
|------------------------------------------------------------------------------|-----------------------|
| <dl> <dt>1</dt> </dl> | Answer<br/>     |
| <dl> <dt>2</dt> </dl> | Authority<br/>  |
| <dl> <dt>3</dt> </dl> | Additional<br/> |



 

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the status of the cache record.

This property contains one of the following values:



| Value                                                                           | Meaning              |
|---------------------------------------------------------------------------------|----------------------|
| <dl> <dt>0</dt> </dl>    | Success<br/>   |
| <dl> <dt>9003</dt> </dl> | NotExist<br/>  |
| <dl> <dt>9701</dt> </dl> | NoRecords<br/> |



 

</dd> <dt>

**TimeToLive**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the time to live (TTL) for the cache record, in seconds, which indicates when the record will expire.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the DNS record type of the cache record.

This property contains one of the following values:



| Value                                                                         | Meaning          |
|-------------------------------------------------------------------------------|------------------|
| <dl> <dt>1</dt> </dl>  | A<br/>     |
| <dl> <dt>2</dt> </dl>  | NS<br/>    |
| <dl> <dt>5</dt> </dl>  | CNAME<br/> |
| <dl> <dt>6</dt> </dl>  | SOA<br/>   |
| <dl> <dt>12</dt> </dl> | PTR<br/>   |
| <dl> <dt>15</dt> </dl> | MX<br/>    |
| <dl> <dt>28</dt> </dl> | AAAA<br/>  |
| <dl> <dt>33</dt> </dl> | SRV<br/>   |



 

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                              |
| MOF<br/>                      | <dl> <dt>DnsClientCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsClientCim.dll</dt> </dl> |



## See also

<dl> <dt>

[Dnsclientcim Provider Classes](dns-client-classes.md)
</dt> </dl>

 

