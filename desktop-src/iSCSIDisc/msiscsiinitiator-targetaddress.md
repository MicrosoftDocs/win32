---
Description: This MSIscsiInitiator\_TargetAddress structure describes the characteristics of the SCSI address mapped to a target by the operation system.
ms.assetid: 4a48d73e-ed8d-4c23-a232-0a4060cc01ea
title: MSIscsiInitiator\_TargetAddress class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSIscsiInitiator\_TargetAddress class

This [**MSIscsiInitiator\_TargetAddress**](https://www.bing.com/search?q=**MSIscsiInitiator\_TargetAddress**) structure describes the characteristics of the SCSI address mapped to a target by the operation system.

## Syntax

``` syntax
class MSIscsiInitiator_TargetAddress
{
  string OSDeviceName;
  uint32 OSBusNumber;
  uint32 OSTargetNumber;
  uint32 OSLunNumber;
};
```

## Members

The **MSIscsiInitiator\_TargetAddress** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSIscsiInitiator\_TargetAddress** class has these properties.

<dl> <dt>

**OSBusNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The SCSI bus number mapped to the target by the operating system.

</dd> <dt>

**OSDeviceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The device name assigned to the target by the operating system.

</dd> <dt>

**OSLunNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The logical unit number (LUN) assigned to the target by the operation system.

</dd> <dt>

**OSTargetNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The target device number assigned to the target by the operating system.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Namespace<br/>                | Root\\WMI<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>Iscsidsc.mof</dt> </dl> |



 

 




