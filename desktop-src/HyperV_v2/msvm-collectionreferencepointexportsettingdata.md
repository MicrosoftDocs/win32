---
description: Export setting data to be passed in to the ExportReferencePoint method of the Msvm\_CollectionReferencePointService class.
ms.assetid: 38299050-a53a-496c-8792-9199c394591d
title: Msvm_CollectionReferencePointExportSettingData class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_CollectionReferencePointExportSettingData
- Msvm_CollectionReferencePointExportSettingData.BaseReferencePointCollection
- Msvm_CollectionReferencePointExportSettingData.VirtualMachinesToDisksToExport
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_CollectionReferencePointExportSettingData class

Export setting data to be passed in to the [**ExportReferencePoint**](msvm-collectionreferencepointservice-exportreferencepoint.md) method of the [**Msvm\_CollectionReferencePointService**](msvm-collectionreferencepointservice.md) class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[AMENDMENT]
class Msvm_CollectionReferencePointExportSettingData : CIM_SettingData
{
  string BaseReferencePointCollection;
  string VirtualMachinesToDisksToExport[];
};
```

## Members

The **Msvm\_CollectionReferencePointExportSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_CollectionReferencePointExportSettingData** class has these properties.

<dl> <dt>

**BaseReferencePointCollection**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Path to a [**Msvm\_ReferencePointCollection**](msvm-referencepointcollection.md) instance that represents the base reference point collection to be used for differential export.

</dd> <dt>

**VirtualMachinesToDisksToExport**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: **HyperVEmbeddedInstance** ("Msvm\_VirtualMachineToDisks")
</dt> </dl>

List of "VirtualMachines To DisksToExport" map information for which data needs to be exported.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_SettingData**](cim-settingdata.md)
</dt> </dl>

 

 




