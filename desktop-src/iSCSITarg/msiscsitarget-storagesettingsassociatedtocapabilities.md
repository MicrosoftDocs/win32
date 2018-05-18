---
title: MSISCSITARGET\_StorageSettingsAssociatedToCapabilities class
description: Associates a MSISCSITARGET\_StorageSetting instance with a MSISCSITARGET\_StorageCapabilities instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e4a263d8-e2fc-4d94-bfc9-0668feb4bb0a'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSISCSITARGET_StorageSettingsAssociatedToCapabilities class iSCSI Software Target API", "MSISCSITARGET_StorageSettingsAssociatedToCapabilities class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageSettingsAssociatedToCapabilities
- MSISCSITARGET_StorageSettingsAssociatedToCapabilities.Antecedent
- MSISCSITARGET_StorageSettingsAssociatedToCapabilities.Dependent
- MSISCSITARGET_StorageSettingsAssociatedToCapabilities.DefaultSetting
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# MSISCSITARGET\_StorageSettingsAssociatedToCapabilities class

Associates a [**MSISCSITARGET\_StorageSetting**](msiscsitarget-storagesetting.md) instance with a [**MSISCSITARGET\_StorageCapabilities**](msiscsitarget-storagecapabilities.md) instance.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MSiSCSITargetProv"), Version("1.0.0")]
class MSISCSITARGET_StorageSettingsAssociatedToCapabilities : CIM_StorageSettingsAssociatedToCapabilities
{
  CIM_StorageCapabilities REF Antecedent;
  CIM_StorageSetting      REF Dependent;
  boolean                     DefaultSetting = TRUE;
};
```

## Members

The **MSISCSITARGET\_StorageSettingsAssociatedToCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSISCSITARGET\_StorageSettingsAssociatedToCapabilities** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_StorageCapabilities**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The StorageCapabilities.

This property is inherited from [**CIM\_StorageSettingsAssociatedToCapabilities**](cim-storagesettingsassociatedtocapabilities.md).

</dd> <dt>

**DefaultSetting**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650), [**Override**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Indicates whether this setting is the default storage setting to use with the **Antecedent** storage capabilities. For Microsoft implementations, each [**MSISCSITARGET\_StoragePool**](msiscsitarget-storagepool.md) is associated with only one [**MSISCSITARGET\_StorageCapabilities**](msiscsitarget-storagecapabilities.md) instance and one [**MSISCSITARGET\_StorageSetting**](msiscsitarget-storagesetting.md) instance. Therefore the one storage setting is the default.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_StorageSetting**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The fixed and predefined StorageSetting.

This property is inherited from [**CIM\_StorageSettingsAssociatedToCapabilities**](cim-storagesettingsassociatedtocapabilities.md).

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

[**CIM\_StorageSettingsAssociatedToCapabilities**](cim-storagesettingsassociatedtocapabilities.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> <dt>

[**MSISCSITARGET\_StorageCapabilities**](msiscsitarget-storagecapabilities.md)
</dt> <dt>

[**MSISCSITARGET\_StorageSetting**](msiscsitarget-storagesetting.md)
</dt> </dl>

 

 





