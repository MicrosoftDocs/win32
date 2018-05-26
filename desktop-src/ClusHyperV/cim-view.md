---
title: CIM\_View class
description: The CIM\_View class is an superclass for classes that provide de-normalized, aggregate representations of managed resources.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c1203217-8b5d-4392-bd3f-3fb9ee4b5af1
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_View class
- CIM_View class, described
topic_type:
- apiref
api_name:
- CIM_View
- CIM_View.InstanceID
- CIM_View.Caption
- CIM_View.Description
- CIM_View.ElementName
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_View class

The **CIM\_View** class is an superclass for classes that provide de-normalized, aggregate representations of managed resources. These subclasses can represents resource classes or associations. A sub-class of must **CIM\_View** include properties propagated from the graph of classes that are used to model the resource in normalized view. These subclasses also require a definition that describes how their properties are propagated. In addition, sub-classes of **CIM\_View** can consist of all read only properties; otherwise, you should carefully consider the data synchronization and consistencies issues that may result.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Abstract, Version("2.26.0"), UMLPackagePath("CIM::Core::CoreElements"), AMENDMENT]
class CIM_View : CIM_ManagedElement
{
  string InstanceID;
  string Caption;
  string Description;
  string ElementName;
};
```

## Members

The **CIM\_View** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_View** class has these properties.

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
</dt> </dl>

Uniquely and opaquely identifies an instance of this class within the scope of the containing namespace.

> \[!Important\]
>
> In order to ensure uniqueness within the namespace, the value of the **InstanceID** property should be constructed in the following pattern: *OrgID*:*LocalID*
>
> *OrgID* must include a copyrighted, trademarked or otherwise unique name that is owned by the business entity that defines the **InstanceID**, or be a registered ID that is assigned by a recognized global authority. This pattern is similar to the structure of schema class names. In addition, to ensure uniqueness, the first colon in **InstanceID** must be between the *OrgID* and*LocalID*. Therefore the *OrgID* must not contain a colon (':').
>
> *LocalID* is chosen by the business entity and should not be re-used to identify different underlying real-world elements.
>
> If the above pattern is not used, the defining entity must assure that the resultant **InstanceID** value is not re-used across any **InstanceID** properties that are produced by this provider or other providers for this namespace.
>
> For Distributed Management Task Force (DMTF) defined instances, the pattern must be used with the *OrgID* set to CIM.

 

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

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

[**CIM\_ManagedElement**](cim-managedelement.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





