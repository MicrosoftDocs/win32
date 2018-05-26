---
title: MSFT\_MTRegistryObject class
description: Abstract base class for registry objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fe7341c5-d1e0-4e87-9b8b-fcc7dc27583f
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_MTRegistryObject class
- MSFT_MTRegistryObject class, described
topic_type:
- apiref
api_name:
- MSFT_MTRegistryObject
- MSFT_MTRegistryObject.InstanceID
- MSFT_MTRegistryObject.Caption
- MSFT_MTRegistryObject.Description
- MSFT_MTRegistryObject.ElementName
- MSFT_MTRegistryObject.Name
api_location:
- RegProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_MTRegistryObject class

Abstract base class for registry objects.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Core::CoreElements"), Abstract, AMENDMENT]
class MSFT_MTRegistryObject : CIM_ManagedElement
{
  string InstanceID;
  string Caption;
  string Description;
  string ElementName;
  string Name;
};
```

## Members

The **MSFT\_MTRegistryObject** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_MTRegistryObject** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

The Caption property is a short textual description (one- line string) of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Description property provides a textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property enables each instance to define a display name in addition to its key properties, identity data, and description information. Be aware that the **Name** property of [**CIM\_ManagedSystemElement**](https://msdn.microsoft.com/library/aa387898) is also defined as a display name. However, it is often subclassed to be a Key. The same property can convey both identity and a user-friendly name, without inconsistencies. Where **Name** exists and is not a Key (such as for instances of [**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884)), the same information can be present in both the **Name** and **ElementName** properties.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Within the scope of the instantiating Namespace, **InstanceId** opaquely and uniquely identifies an instance of this class. To ensure uniqueness within the NameSpace, the value of **InstanceId** should be constructed using the following "preferred" algorithm: *OrgID*:*LocalID* Where *OrgID* and *LocalID* are separated by a colon (:), and where *OrgID* must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the **InstanceId** or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the *SchemaName*\_*ClassName* structure of Schema class names.) In addition, to ensure uniqueness, *OrgID* must not contain a colon (:). When using this algorithm, the first colon to appear in **InstanceId** must appear between *OrgID* and *LocalID*. *LocalID* is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If the above preferred algorithm is not used, the defining entity must assure that the resulting **InstanceId** is not reused across any **InstanceId**s produced by this or other providers for the NameSpace of this instance. For DMTF-defined instances, the "preferred" algorithm must be used with the *OrgID* set to CIM.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The unique name of the registry object.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                         |
| Namespace<br/>                | Root\\Microsoft\\Windows\\ManagementTools<br/>                                   |
| MOF<br/>                      | <dl> <dt>RegProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RegProv.dll</dt> </dl> |



 

 





