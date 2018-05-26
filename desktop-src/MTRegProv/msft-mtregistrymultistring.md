---
title: MSFT\_MTRegistryMultiString class
description: Represent the multi string registry data.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5fe53e16-2e2e-4e85-9421-1aa154a7408c
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_MTRegistryMultiString class
- MSFT_MTRegistryMultiString class, described
topic_type:
- apiref
api_name:
- MSFT_MTRegistryMultiString
- MSFT_MTRegistryMultiString.InstanceID
- MSFT_MTRegistryMultiString.Caption
- MSFT_MTRegistryMultiString.Description
- MSFT_MTRegistryMultiString.ElementName
- MSFT_MTRegistryMultiString.Name
- MSFT_MTRegistryMultiString.Type
- MSFT_MTRegistryMultiString.Status
- MSFT_MTRegistryMultiString.Data
api_location:
- RegProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_MTRegistryMultiString class

Represent the multi string registry data.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Core::CoreElements"), dynamic, provider("regprov"), AMENDMENT]
class MSFT_MTRegistryMultiString : MSFT_MTRegistryValue
{
  string InstanceID;
  string Caption;
  string Description;
  string ElementName;
  string Name;
  uint32 Type;
  uint16 Status;
  string Data[];
};
```

## Members

The **MSFT\_MTRegistryMultiString** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_MTRegistryMultiString** class has these methods.



| Method                                                  | Description                                                                                                                                          |
|:--------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetValue**](msft-mtregistrymultistring-getvalue.md) | Gets the registry value object.<br/> This method is inherited from the [**MSFT\_MTRegistryValue**](msft-mtregistryvalue.md) class.<br/> |
| [**Rename**](msft-mtregistrymultistring-rename.md)     | Renames the registry object.<br/> This method is inherited from the [**MSFT\_MTRegistryValue**](msft-mtregistryvalue.md) class.<br/>    |



 

### Properties

The **MSFT\_MTRegistryMultiString** class has these properties.

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

**Data**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Multi string data of the registry value.

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

This property is inherited from [**MSFT\_MTRegistryObject**](msft-mtregistryobject.md).

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: 
</dt> </dl>

The status of data contained in the registry value.

This property is inherited from [**MSFT\_MTRegistryValue**](msft-mtregistryvalue.md).

The possible values are.

<dt>

<span id="OK"></span><span id="ok"></span>

**OK** (1)


</dt> <dd></dd> <dt>

<span id="RawBinary"></span><span id="rawbinary"></span><span id="RAWBINARY"></span>

**RawBinary** (2)


</dt> <dd></dd> <dt>

<span id="Invalid"></span><span id="invalid"></span><span id="INVALID"></span>

**Invalid** (3)


</dt> <dd></dd> <dt>

<span id="LargeExceeded"></span><span id="largeexceeded"></span><span id="LARGEEXCEEDED"></span>

**LargeExceeded** (4)


</dt> <dd></dd> </dl>

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: 
</dt> </dl>

The type of data contained in the registry value.

This property is inherited from [**MSFT\_MTRegistryValue**](msft-mtregistryvalue.md).

The possible values are.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (0)


</dt> <dd></dd> <dt>

<span id="String"></span><span id="string"></span><span id="STRING"></span>

**String** (1)


</dt> <dd></dd> <dt>

<span id="ExpandString"></span><span id="expandstring"></span><span id="EXPANDSTRING"></span>

**ExpandString** (2)


</dt> <dd></dd> <dt>

<span id="Binary"></span><span id="binary"></span><span id="BINARY"></span>

**Binary** (3)


</dt> <dd></dd> <dt>

<span id="DwordLittleEndian"></span><span id="dwordlittleendian"></span><span id="DWORDLITTLEENDIAN"></span>

**DwordLittleEndian** (4)


</dt> <dd></dd> <dt>

<span id="DwordBigEndian"></span><span id="dwordbigendian"></span><span id="DWORDBIGENDIAN"></span>

**DwordBigEndian** (5)


</dt> <dd></dd> <dt>

<span id="Link"></span><span id="link"></span><span id="LINK"></span>

**Link** (6)


</dt> <dd></dd> <dt>

<span id="MultiString"></span><span id="multistring"></span><span id="MULTISTRING"></span>

**MultiString** (7)


</dt> <dd></dd> <dt>

<span id="ResourceList"></span><span id="resourcelist"></span><span id="RESOURCELIST"></span>

**ResourceList** (8)


</dt> <dd></dd> <dt>

<span id="ResourceDescriptor"></span><span id="resourcedescriptor"></span><span id="RESOURCEDESCRIPTOR"></span>

**ResourceDescriptor** (9)


</dt> <dd></dd> <dt>

<span id="ResourceRequirementsList"></span><span id="resourcerequirementslist"></span><span id="RESOURCEREQUIREMENTSLIST"></span>

**ResourceRequirementsList** (10)


</dt> <dd></dd> <dt>

<span id="QwordLittleEndian"></span><span id="qwordlittleendian"></span><span id="QWORDLITTLEENDIAN"></span>

**QwordLittleEndian** (11)


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                         |
| Namespace<br/>                | Root\\Microsoft\\Windows\\ManagementTools<br/>                                   |
| MOF<br/>                      | <dl> <dt>RegProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RegProv.dll</dt> </dl> |



 

 





