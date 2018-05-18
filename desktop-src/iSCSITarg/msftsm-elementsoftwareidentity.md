---
title: MSFTSM\_ElementSoftwareIdentity class
description: Associates a managed element with a software asset.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '88264e0b-4b3a-42a9-9833-f416658fc518'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFTSM_ElementSoftwareIdentity class iSCSI Software Target API", "MSFTSM_ElementSoftwareIdentity class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- MSFTSM_ElementSoftwareIdentity
- MSFTSM_ElementSoftwareIdentity.UpgradeCondition
- MSFTSM_ElementSoftwareIdentity.OtherUpgradeCondition
- MSFTSM_ElementSoftwareIdentity.Antecedent
- MSFTSM_ElementSoftwareIdentity.Dependent
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# MSFTSM\_ElementSoftwareIdentity class

Associates a managed element with a software asset.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Version("1.0.0"), Provider("MSiSCSITargetProv")]
class MSFTSM_ElementSoftwareIdentity : CIM_ElementSoftwareIdentity
{
  uint16                   UpgradeCondition;
  string                   OtherUpgradeCondition;
  CIM_SoftwareIdentity REF Antecedent;
  CIM_ManagedElement   REF Dependent;
};
```

## Members

The **MSFTSM\_ElementSoftwareIdentity** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFTSM\_ElementSoftwareIdentity** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_SoftwareIdentity**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Antecedent), **MSFT\_TargetNamespace** ("root\\\\cimv2\\\\storage\\\\iscsitarget")
</dt> </dl>

Indicates the [**MSFTSM\_SoftwareIdentity**](msftsm-softwareidentity.md) instance that describes the software asset.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ManagedElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Dependent)
</dt> </dl>

Indicates the managed element that requires or uses the software.

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

This property is inherited from [**CIM\_ElementSoftwareIdentity**](cim-elementsoftwareidentity.md).

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

This property is inherited from [**CIM\_ElementSoftwareIdentity**](cim-elementsoftwareidentity.md).

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


</dt> <dd>6–32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768–65535</dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ElementSoftwareIdentity**](cim-elementsoftwareidentity.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> </dl>

 

 





