---
description: Represents a protocol controller that manages a SCSI interface.
ms.assetid: 01ef85fc-2f05-4453-b524-7d63b647f6fb
title: CIM_SCSIProtocolController class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_SCSIProtocolController
- CIM_SCSIProtocolController.NameFormat
- CIM_SCSIProtocolController.OtherNameFormat
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_SCSIProtocolController class

Represents a protocol controller that manages a SCSI interface.

## Syntax

``` syntax
[Abstract, Version("2.8.1000"), UMLPackagePath("CIM::Device::ProtocolController"), AMENDMENT]
class CIM_SCSIProtocolController : CIM_ProtocolController
{
  uint16 NameFormat;
  string OtherNameFormat;
};
```

## Members

The **CIM\_SCSIProtocolController** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_SCSIProtocolController** class has these properties.

<dl> <dt>

**NameFormat**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_SCSIProtocolController**.**Name**", "**CIM\_SCSIProtocolController**.**OtherNameFormat**")
</dt> </dl>

The format of the **Name** property of the **CIM\_SCSIProtocolController**.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="FC_Port_WWN"></span><span id="fc_port_wwn"></span><span id="FC_PORT_WWN"></span>

**FC Port WWN** (2)


</dt> <dd></dd> <dt>

<span id="iSCSI_Name"></span><span id="iscsi_name"></span><span id="ISCSI_NAME"></span>

**iSCSI Name** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**OtherNameFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("**CIM\_SCSIProtocolController**.**Name**", "**CIM\_SCSIProtocolController**.**NameFormat**")
</dt> </dl>

A description of the **NameFormat** property when **NameFormat** is set to "1" (other).

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_ProtocolController**](cim-protocolcontroller.md)
</dt> </dl>

 

