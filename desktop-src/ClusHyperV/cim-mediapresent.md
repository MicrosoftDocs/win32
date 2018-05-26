---
title: CIM\_MediaPresent class
description: Represents a relationship in which a storage extent must be accessed through a media access device.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cff32285-48ac-4d66-a801-bbbd25e8ad8f
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_MediaPresent class
- CIM_MediaPresent class, described
topic_type:
- apiref
api_name:
- CIM_MediaPresent
- CIM_MediaPresent.Antecedent
- CIM_MediaPresent.Dependent
- CIM_MediaPresent.FixedMedia
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_MediaPresent class

Represents a relationship in which a storage extent must be accessed through a media access device.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Abstract, Version("2.6.0"), UMLPackagePath("CIM::Device::StorageExtents"), MappingStrings("MIF.DMTF|Storage Devices|001.8")]
class CIM_MediaPresent : CIM_Dependency
{
  CIM_MediaAccessDevice REF Antecedent;
  CIM_StorageExtent     REF Dependent;
  boolean                   FixedMedia;
};
```

## Members

The **CIM\_MediaPresent** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_MediaPresent** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_MediaAccessDevice**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

The media access device.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_StorageExtent**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The storage extent that is accessed when using the media access device.

</dd> <dt>

**FixedMedia**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if the storage extent is fixed in the media access device and can not be ejected; otherwise, **false**.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





