---
title: CIM\_ElementSoftwareIdentity class
description: ElementSoftwareIdentity allows a Managed Element to report its software related asset information (firmware, drivers, configuration software, and etc.).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 77d6c2a4-aebe-4e1e-9647-06175c000114
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_ElementSoftwareIdentity class iSCSI Software Target API
- CIM_ElementSoftwareIdentity class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- CIM_ElementSoftwareIdentity
- CIM_ElementSoftwareIdentity.Antecedent
- CIM_ElementSoftwareIdentity.Dependent
- CIM_ElementSoftwareIdentity.UpgradeCondition
- CIM_ElementSoftwareIdentity.OtherUpgradeCondition
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CIM\_ElementSoftwareIdentity class

ElementSoftwareIdentity allows a Managed Element to report its software related asset information (firmware, drivers, configuration software, and etc.)

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Version("2.8.0"), UMLPackagePath("CIM::Core::Software")]
class CIM_ElementSoftwareIdentity : CIM_Dependency
{
  CIM_SoftwareIdentity REF Antecedent;
  CIM_ManagedElement   REF Dependent;
  uint16                   UpgradeCondition;
  string                   OtherUpgradeCondition;
};
```

## Members

The **CIM\_ElementSoftwareIdentity** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ElementSoftwareIdentity** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_SoftwareIdentity**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

A LogicalElement's Software Asset.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The ManagedElement that requires or uses the software.

</dd> <dt>

**OtherUpgradeCondition**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ElementSoftwareIdentity.UpgradeCondition")
</dt> </dl>

Describes the upgrade condition, when UpgradeCondition is set to 1 ("Other").

</dd> <dt>

**UpgradeCondition**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ElementSoftwareIdentity.OtherUpgradeCondition")
</dt> </dl>

Indicates the element's ability to upgrade this software asset. 'Resides off element' 2, indicates the persistence of the software is outside of the element. Typically for a element this software is part of the OperatingSystem is typically upgradeable. 'Owner Upgradeable' 3, indicates the persistence of the software is on the element and is upgradeable by the owner. 'FactoryUpgradeable' 4,indicates the persistence of the software is on the element and is upgradeable by the manufacturer. 'Not Upgradeable' 5, indicates the presistence of the software is on the element and is not upgradeable. (i.e. burned into a non replaceable ROM chip.)

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Resides_off_device"></span><span id="resides_off_device"></span><span id="RESIDES_OFF_DEVICE"></span>

**Resides off device** (2)


</dt> <dd></dd> <dt>

<span id="Owner_Upgradeable"></span><span id="owner_upgradeable"></span><span id="OWNER_UPGRADEABLE"></span>

**Owner Upgradeable** (3)


</dt> <dd></dd> <dt>

<span id="Factory_Upgradeable"></span><span id="factory_upgradeable"></span><span id="FACTORY_UPGRADEABLE"></span>

**Factory Upgradeable** (4)


</dt> <dd></dd> <dt>

<span id="Not_Upgradeable"></span><span id="not_upgradeable"></span><span id="NOT_UPGRADEABLE"></span>

**Not Upgradeable** (5)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>6 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



 

 





