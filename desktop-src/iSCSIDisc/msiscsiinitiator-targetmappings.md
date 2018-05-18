---
Description: 'This MSIscsiInitiator\_LUNList structure describes the characteristics of the logical unit number (LUN) mapping.'
ms.assetid: '846849a1-8447-4c8c-9f2f-4f08eaedea59'
title: 'MSIscsiInitiator\_TargetMappings class'
---

# MSIscsiInitiator\_TargetMappings class

This [**MSIscsiInitiator\_LUNList**](msiscsiinitiator-lunlist.md) structure describes the characteristics of the logical unit number (LUN) mapping.

## Syntax

``` syntax
class MSIscsiInitiator_TargetMappings
{
  string                   InitiatorName;
  string                   TargetName;
  string                   OSDeviceName;
  uint32                   OSBusNumber;
  uint32                   OSTargetNumber;
  MSIscsiInitiator_LUNList LUNList[];
};
```

## Members

The **MSIscsiInitiator\_TargetMappings** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSIscsiInitiator\_TargetMappings** class has these properties.

<dl> <dt>

**InitiatorName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The iSCSI initiator instance name.

</dd> <dt>

**LUNList**
</dt> <dd> <dl> <dt>

Data type: **MSIscsiInitiator\_LUNList** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An [**MSIscsiInitiator\_LUNList**](msiscsiinitiator-lunlist.md) structure that contains a list of LUNs associated with the target device.

</dd> <dt>

**OSBusNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The SCSI bus number (which is valid in the local operating system) that the remote target is mapped to. A value of 0xffffffff indicates that the miniport driver can associate any SCSI bus number with the target.

</dd> <dt>

**OSDeviceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The device name assigned to the target by the local operating system.

</dd> <dt>

**OSTargetNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The SCSI target number (which is valid in the local operating system) that the remote target is mapped to. A value of 0xffffffff indicates that the miniport driver can pick any number to identify the remote target device.

</dd> <dt>

**TargetName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A wide character string that indicates the target name.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Namespace<br/>                | Root\\WMI<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>Iscsidsc.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSIscsiInitiator\_LUNList**](msiscsiinitiator-lunlist.md)
</dt> </dl>

 

 




