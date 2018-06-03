---
title: CIM\_SettingAssociatedToCapabilities class
description: This association defines settings that can be used to create or modify elements. Unlike ElementSettingData, these settings are not used to express the characteristics of existing managed elements.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d0c4679b-2418-4514-810d-ae7d6e597519
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_SettingAssociatedToCapabilities class iSCSI Software Target API
- CIM_SettingAssociatedToCapabilities class iSCSI Software Target API , described
topic_type:
- apiref
api_name:
- CIM_SettingAssociatedToCapabilities
- CIM_SettingAssociatedToCapabilities.Antecedent
- CIM_SettingAssociatedToCapabilities.Dependent
- CIM_SettingAssociatedToCapabilities.DefaultSetting
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CIM\_SettingAssociatedToCapabilities class

This association defines settings that can be used to create or modify elements. Unlike ElementSettingData, these settings are not used to express the characteristics of existing managed elements.

Typically, the capabilities associated with this class define the characteristics of a service in creating or modifying elements that are dependent on the service directly or indirectly. A CIM Client may use this association to find SettingData instances that can be used to create or modify these dependent elements.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Version("2.11.0"), UMLPackagePath("CIM::System::FilesystemServices")]
class CIM_SettingAssociatedToCapabilities : CIM_Dependency
{
  CIM_Capabilities REF Antecedent;
  CIM_SettingData  REF Dependent;
  boolean              DefaultSetting = FALSE;
};
```

## Members

The **CIM\_SettingAssociatedToCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_SettingAssociatedToCapabilities** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Capabilities**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

The Capabilities.

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

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_SettingData**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The Setting.

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

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

 





