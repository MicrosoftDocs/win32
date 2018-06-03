---
title: CIM\_StorageSettingsAssociatedToCapabilities class
description: This association define StorageSettings that reflect the capabilities of the associated StorageCapabilities.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b62e42e5-5457-466c-a740-5a7c2f7f3a52
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_StorageSettingsAssociatedToCapabilities class iSCSI Software Target API
- CIM_StorageSettingsAssociatedToCapabilities class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- CIM_StorageSettingsAssociatedToCapabilities
- CIM_StorageSettingsAssociatedToCapabilities.DefaultSetting
- CIM_StorageSettingsAssociatedToCapabilities.Antecedent
- CIM_StorageSettingsAssociatedToCapabilities.Dependent
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CIM\_StorageSettingsAssociatedToCapabilities class

This association define StorageSettings that reflect the capabilities of the associated StorageCapabilities. The associated StorageSetting may not define the operational characteristics (through settings properties) of any storage element. Certain StorageSetting instances can be defined as "Fixed = Not Changeable" by using the "ChangeableType" attribute. "Fixed" settings have this special association. This association should be defined between "Fixed - Not Changeable" instances of StorageSetting with the StorageCapabilities instances that are associated with the StoragePools which support the storage characteristics described by the StorageSetting instance.

Fixed settings may be associated to many StorageCapabilities.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Version("2.11.0"), UMLPackagePath("CIM::Device::StorageServices")]
class CIM_StorageSettingsAssociatedToCapabilities : CIM_SettingAssociatedToCapabilities
{
  boolean                     DefaultSetting = FALSE;
  CIM_StorageCapabilities REF Antecedent;
  CIM_StorageSetting      REF Dependent;
};
```

## Members

The **CIM\_StorageSettingsAssociatedToCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_StorageSettingsAssociatedToCapabilities** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_StorageCapabilities**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

The StorageCapabilities.

</dd> <dt>

**DefaultSetting**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

If an element whose characteristics are described by the associated Capabilities instance has a dependent element created or modified without specifying an associated SettingData instance, then the default SettingData will be used in that operation.

This property is inherited from [**CIM\_SettingAssociatedToCapabilities**](cim-settingassociatedtocapabilities.md).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_StorageSetting**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The fixed and predefined StorageSetting.

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_SettingAssociatedToCapabilities**](cim-settingassociatedtocapabilities.md)
</dt> </dl>

 

 





