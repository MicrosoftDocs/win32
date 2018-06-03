---
Description: This MSIscsiInitiator\_LUNList structure defines a mapping between the LUN number that is used by the operating system and the LUN number that is configured in the iSCSI target.
ms.assetid: 582202d0-fcfc-43f2-a28d-8e4b6e9d07e4
title: MSIscsiInitiator\_LUNList class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSIscsiInitiator\_LUNList class

This **MSIscsiInitiator\_LUNList** structure defines a mapping between the LUN number that is used by the operating system and the LUN number that is configured in the iSCSI target.

## Syntax

``` syntax
class MSIscsiInitiator_LUNList
{
  uint32 OSLunNumber;
  uint64 TargetLun;
};
```

## Members

The **MSIscsiInitiator\_LUNList** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSIscsiInitiator\_LUNList** class has these properties.

<dl> <dt>

**OSLunNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The SCSI LUN (which is valid in the local operating system) that the remote LUN is mapped to.

</dd> <dt>

**TargetLun**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A LUN that is globally valid anywhere in the network.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Namespace<br/>                | Root\\WMI<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>Iscsidsc.mof</dt> </dl> |



 

 




