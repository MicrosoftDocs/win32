---
title: CIM\_CollectionOfMSEs class
description: An abstract class for subclasses that represent a collection of CIM\_ManagedSystemElement objects. These collections allow managed system elements to be grouped for identification purposes and to simplify the association of settings and configurations.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3ddb8e3f-5296-48ff-80d3-c1bb92600d32
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CIM_CollectionOfMSEs class
- CIM_CollectionOfMSEs class, described
topic_type:
- apiref
api_name:
- CIM_CollectionOfMSEs
- CIM_CollectionOfMSEs.InstanceID
- CIM_CollectionOfMSEs.Caption
- CIM_CollectionOfMSEs.Description
- CIM_CollectionOfMSEs.ElementName
- CIM_CollectionOfMSEs.CollectionID
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_CollectionOfMSEs class

An abstract class for subclasses that represent a collection of [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md) objects. These collections allow managed system elements to be grouped for identification purposes and to simplify the association of settings and configurations.

> [!Note]  
> These collections are for grouping purposes and must not define state or status information.

 

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Abstract, Version("2.10.0"), UMLPackagePath("CIM::Core::Collection"), AMENDMENT]
class CIM_CollectionOfMSEs : CIM_Collection
{
  string InstanceID;
  string Caption;
  string Description;
  string ElementName;
  string CollectionID;
};
```

## Members

The **CIM\_CollectionOfMSEs** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_CollectionOfMSEs** class has these properties.

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

**CollectionID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The identification of the collection object. When subclassed, the **CollectionID** property can be overridden as a key property.

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

[**CIM\_Collection**](cim-collection.md)
</dt> <dt>

[Failover Clustering Hyper-V WMI Provider](failover-clustering-hyper-v-wmi-provider-portal.md)
</dt> </dl>

 

 





