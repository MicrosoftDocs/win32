---
title: WT\_iSCSIStorageSubsystem class
description: This class supports the iSCSIStorageSubsystem noun.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9c89794d-d827-4d62-ad76-bb6a440f3df3
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- WT_iSCSIStorageSubsystem class iSCSI Software Target API
- WT_iSCSIStorageSubsystem class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- WT_iSCSIStorageSubsystem
- WT_iSCSIStorageSubsystem.iSCSITargetServer
api_location:
- StrgPrvdMgmt.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# WT\_iSCSIStorageSubsystem class

This class supports the iSCSIStorageSubsystem noun.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class WT_iSCSIStorageSubsystem
{
  string iSCSITargetServer;
};
```

## Members

The **WT\_iSCSIStorageSubsystem** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **WT\_iSCSIStorageSubsystem** class has these methods.



| Method                                                                            | Description                                                                                           |
|:----------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------|
| [**AddStorageSubsystem**](addstoragesubsystem-wt-iscsistoragesubsystem.md)       | Adds an iSCSI Target Server to the list of subsystems maintained by the VDS provider.<br/>      |
| [**RemoveStorageSubsystem**](removestoragesubsystem-wt-iscsistoragesubsystem.md) | Removes an iSCSI Target Server from the list of subsystems maintained by the VDS provider.<br/> |



 

### Properties

The **WT\_iSCSIStorageSubsystem** class has these properties.

<dl> <dt>

**iSCSITargetServer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

Instance property.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\Wmi<br/>                                                                        |
| MOF<br/>                      | <dl> <dt>StrgPrvdMgmt.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>StrgPrvdMgmt.dll</dt> </dl> |



## See also

<dl> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> </dl>

 

 





