---
title: CIM\_SystemSpecificCollection class
description: Represents the a generic collection that is contained by a system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'b69877dd-de70-4201-a57a-00d36647a875'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_SystemSpecificCollection class", "CIM_SystemSpecificCollection class, described"]
topic_type:
- apiref
api_name:
- CIM_SystemSpecificCollection
- CIM_SystemSpecificCollection.Caption
- CIM_SystemSpecificCollection.Description
- CIM_SystemSpecificCollection.ElementName
- CIM_SystemSpecificCollection.InstanceID
api_location:
- VMMS.exe
api_type:
- DllExport
---

# CIM\_SystemSpecificCollection class

Represents the a generic collection that is contained by a system.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Abstract, Version("2.19.0"), UMLPackagePath("CIM::Core::Collection"), AMENDMENT]
class CIM_SystemSpecificCollection : CIM_Collection
{
  string Caption;
  string Description;
  string ElementName;
  string InstanceID;
};
```

## Members

The **CIM\_SystemSpecificCollection** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_SystemSpecificCollection** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("InstanceID")
</dt> </dl>

Uniquely identifies an instance of this class within the scope of the containing namespace.

In order to ensure uniqueness within the namespace, the value of the **InstanceID** property should be constructed in the following format: *OrgID*:*LocalID*

-   *OrgID* must include a copyrighted, trademarked or a unique name that is owned by the business entity that defines the **InstanceID**, or be a registered ID that is assigned by a recognized global authority. This pattern is similar to the structure of schema class names.
-   The first colon in **InstanceID** must be between the *OrgID* and*LocalID*. Therefore the *OrgID* must not contain a colon (':').
-   *LocalID* is chosen by the business entity and should not be re-used to identify different underlying real-world elements.
-   If this format is not used, the defining entity must assure that the resultant **InstanceID** value is not re-used across any **InstanceID** properties that are produced by this provider or other providers for this namespace.
-   For Distributed Management Task Force (DMTF) defined instances, the pattern must be used with the *OrgID* set to CIM.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                         |
| Namespace<br/>                | Root\\HyperVCluster\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsHyperVCluster.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>VMMS.exe</dt> </dl>                    |



## See also

<dl> <dt>

[**CIM\_Collection**](cim-collection.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





