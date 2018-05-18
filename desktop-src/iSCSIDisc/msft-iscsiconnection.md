---
Description: 'Represents a connection from an iSCSI initiator to an iSCSI target.'
ms.assetid: 'BBCE76AE-08B5-44F4-A866-C6FBC86BC0A4'
title: 'MSFT\_iSCSIConnection class'
---

# MSFT\_iSCSIConnection class

Represents a connection from an iSCSI initiator to an iSCSI target.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_iSCSIConnection
{
  string ConnectionIdentifier;
  string InitiatorAddress;
  string TargetAddress;
  uint32 InitiatorPortNumber;
  uint32 TargetPortNumber;
};
```

## Members

The **MSFT\_iSCSIConnection** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_iSCSIConnection** class has these properties.

<dl> <dt>

**ConnectionIdentifier**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The connection identifier.

</dd> <dt>

**InitiatorAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string that contains an IP address for each network adapter on the initiator. The default value is "0.0.0.0".

</dd> <dt>

**InitiatorPortNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The TCP port number for the initiator.

</dd> <dt>

**TargetAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The IP address of the target.

</dd> <dt>

**TargetPortNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The TCP port number for the target. The default value is 3260.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Iscsiwmiv2.mof</dt> </dl> |



 

 




