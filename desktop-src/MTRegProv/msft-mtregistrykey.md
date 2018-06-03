---
title: MSFT\_MTRegistryKey class
description: Represent a registry key.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5567ff12-6b28-48a5-852f-4892bcabb9c5
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_MTRegistryKey class
- MSFT_MTRegistryKey class, described
topic_type:
- apiref
api_name:
- MSFT_MTRegistryKey
- MSFT_MTRegistryKey.InstanceID
- MSFT_MTRegistryKey.Caption
- MSFT_MTRegistryKey.Description
- MSFT_MTRegistryKey.ElementName
- MSFT_MTRegistryKey.Name
- MSFT_MTRegistryKey.SubKeyCount
- MSFT_MTRegistryKey.ValueCount
- MSFT_MTRegistryKey.Modified
api_location:
- RegProv.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_MTRegistryKey class

Represent a registry key.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Core::CoreElements"), dynamic, provider("regprov"), AMENDMENT]
class MSFT_MTRegistryKey : MSFT_MTRegistryObject
{
  string   InstanceID;
  string   Caption;
  string   Description;
  string   ElementName;
  string   Name;
  uint32   SubKeyCount;
  uint32   ValueCount;
  datetime Modified;
};
```

## Members

The **MSFT\_MTRegistryKey** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_MTRegistryKey** class has these methods.



| Method                                              | Description                              |
|:----------------------------------------------------|:-----------------------------------------|
| [**GetKey**](msft-mtregistrykey-getkey.md)         | Gets the registry key object.<br/> |
| [**GetSubKeys**](getsubkeys-msft-mtregistrykey.md) | Get child registry keys.<br/>      |
| [**GetValues**](getvalues-msft-mtregistrykey.md)   | Get child registry keys.<br/>      |
| [**Rename**](rename-msft-mtregistrykey.md)         | Renames the registry object.<br/>  |



 

### Properties

The **MSFT\_MTRegistryKey** class has these properties.

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

**Modified**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The timestamp at which this key was last modified.

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

This property is inherited from [**MSFT\_MTRegistryObject**](msft-mtregistryobject.md).

</dd> <dt>

**SubKeyCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of sub keys under this key.

</dd> <dt>

**ValueCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of sub values under this key.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                         |
| Namespace<br/>                | Root\\Microsoft\\Windows\\ManagementTools<br/>                                   |
| MOF<br/>                      | <dl> <dt>RegProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RegProv.dll</dt> </dl> |



 

 





