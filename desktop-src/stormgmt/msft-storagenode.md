---
title: MSFT\_StorageNode class
description: Represents a storage node in a cluster.
ms.assetid: EAEDDC82-F170-48C4-BA93-A414C96C00D1
keywords:
- MSFT_StorageNode class Windows Storage Management API
- MSFT_StorageNode class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageNode
- MSFT_StorageNode.Name
- MSFT_StorageNode.NameFormat
- MSFT_StorageNode.OtherIdentifyingInfo
- MSFT_StorageNode.OtherIdentifyingInfoDescription
- MSFT_StorageNode.OperationalStatus
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFT\_StorageNode class

Represents a storage node in a cluster.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_StorageNode : MSFT_StorageObject
{
  String Name;
  UInt16 NameFormat;
  String OtherIdentifyingInfo[];
  String OtherIdentifyingInfoDescription[];
  UInt16 OperationalStatus;
};
```

## Members

The **MSFT\_StorageNode** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageNode** class has these properties.

<dl> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Human-readable identifier of a storage node.

</dd> <dt>

**NameFormat**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The format of **Name**.



| Value                                                                                                  | Meaning            |
|--------------------------------------------------------------------------------------------------------|--------------------|
| <span id="1"></span><dl> <dt>**1**</dt> </dl>   | Other<br/>   |
| <span id="2"></span><dl> <dt>**2**</dt> </dl>   | IP<br/>      |
| <span id="3"></span><dl> <dt>**3**</dt> </dl>   | Dial<br/>    |
| <span id="4"></span><dl> <dt>**4**</dt> </dl>   | HID<br/>     |
| <span id="5"></span><dl> <dt>**5**</dt> </dl>   | NWA<br/>     |
| <span id="6"></span><dl> <dt>**6**</dt> </dl>   | HWA<br/>     |
| <span id="7"></span><dl> <dt>**7**</dt> </dl>   | X25<br/>     |
| <span id="8"></span><dl> <dt>**8**</dt> </dl>   | ISDN<br/>    |
| <span id="9"></span><dl> <dt>**9**</dt> </dl>   | IPX<br/>     |
| <span id="10"></span><dl> <dt>**10**</dt> </dl> | DCC<br/>     |
| <span id="11"></span><dl> <dt>**11**</dt> </dl> | ICD<br/>     |
| <span id="12"></span><dl> <dt>**12**</dt> </dl> | E.164<br/>   |
| <span id="13"></span><dl> <dt>**13**</dt> </dl> | SNA<br/>     |
| <span id="14"></span><dl> <dt>**14**</dt> </dl> | OID/OSI<br/> |
| <span id="15"></span><dl> <dt>**15**</dt> </dl> | WWN<br/>     |
| <span id="16"></span><dl> <dt>**16**</dt> </dl> | NAA<br/>     |



 

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The current status of the node.



| Value                                                                                                  | Meaning            |
|--------------------------------------------------------------------------------------------------------|--------------------|
| <span id="0"></span><dl> <dt>**0**</dt> </dl>   | Unknown<br/> |
| <span id="2"></span><dl> <dt>**2**</dt> </dl>   | Up<br/>      |
| <span id="6"></span><dl> <dt>**6**</dt> </dl>   | Down<br/>    |
| <span id="8"></span><dl> <dt>**8**</dt> </dl>   | Joining<br/> |
| <span id="10"></span><dl> <dt>**10**</dt> </dl> | Paused<br/>  |



 

</dd> <dt>

**OtherIdentifyingInfo**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Custom identifiers for the node. If this field is set, **OtherIdentifyingInfoDescription** must also be set.

</dd> <dt>

**OtherIdentifyingInfoDescription**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptions of the format used in the custom identifiers in **OtherIdentifyingInfo**. There must be a 1:1 mapping between this array and **OtherIdentifyingInfo**.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageObject**](msft-storageobject.md)
</dt> </dl>

 

 





