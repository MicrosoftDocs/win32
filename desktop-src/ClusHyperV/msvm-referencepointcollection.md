---
title: Msvm\_ReferencePointCollection class
description: Represents a collection of virtual machine reference points.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ff30a757-0422-4927-9fde-24bf74fdde9a
ms.prod: windows-server-dev
ms.technology:
- failover-cluster-hyperv
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Msvm_ReferencePointCollection class
- Msvm_ReferencePointCollection class, described
topic_type:
- apiref
api_name:
- Msvm_ReferencePointCollection
- Msvm_ReferencePointCollection.InstanceID
- Msvm_ReferencePointCollection.Caption
- Msvm_ReferencePointCollection.Description
- Msvm_ReferencePointCollection.CollectionID
- Msvm_ReferencePointCollection.ElementName
- Msvm_ReferencePointCollection.ReferencePointType
- Msvm_ReferencePointCollection.ConsistencyLevel
- Msvm_ReferencePointCollection.VirtualSystemCollectionId
- Msvm_ReferencePointCollection.HasAssociatedLog
api_location:
- VMMS.exe
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Msvm\_ReferencePointCollection class

Represents a collection of virtual machine reference points.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ReferencePointCollection : CIM_Collection
{
  string  InstanceID;
  string  Caption;
  string  Description;
  string  CollectionID;
  string  ElementName;
  uint16  ReferencePointType;
  uint16  ConsistencyLevel;
  string  VirtualSystemCollectionId;
  boolean HasAssociatedLog;
};
```

## Members

The **Msvm\_ReferencePointCollection** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ReferencePointCollection** class has these properties.

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

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("CollectionID"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The unique identifier of the collection object.

</dd> <dt>

**ConsistencyLevel**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The consistency level of the reference points.

The possible values are:

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Crash_Consistent"></span><span id="crash_consistent"></span><span id="CRASH_CONSISTENT"></span>

**Crash Consistent** (1)


</dt> <dd></dd> <dt>

<span id="Application_Consistent"></span><span id="application_consistent"></span><span id="APPLICATION_CONSISTENT"></span>

**Application Consistent** (2)


</dt> <dd></dd> </dl>

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
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("ElementName")
</dt> </dl>

A user-defined name for the collection.

</dd> <dt>

**HasAssociatedLog**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**true** if all of the reference points log based and have logs.; otherwise, **false**.

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

</dd> <dt>

**ReferencePointType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**In**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The type of the reference points.

The possible values are:

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Log_based"></span><span id="log_based"></span><span id="LOG_BASED"></span>

**Log based** (1)


</dt> <dd></dd> <dt>

<span id="RCT_based"></span><span id="rct_based"></span><span id="RCT_BASED"></span>

**RCT based** (2)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>3 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**VirtualSystemCollectionId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**Msvm\_VirtualSystemCollection**](msvm-virtualsystemcollection.md).**CollectionID**")
</dt> </dl>

The identifier of the [**Msvm\_VirtualSystemCollection**](msvm-virtualsystemcollection.md) that contains the reference points.

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

 

 





