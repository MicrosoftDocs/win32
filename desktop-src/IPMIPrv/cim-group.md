---
title: CIM\_Group class
description: Collects ManagedElements into groups.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c4100e8d-fa76-41eb-9b64-480c2113d453'
ms.prod: 'windows-server-dev'
ms.technology:
- 'intelligent-platform-management-interface'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_Group class", "CIM_Group class, described"]
topic_type:
- apiref
api_name:
- CIM_Group
- CIM_Group.Caption
- CIM_Group.Description
- CIM_Group.ElementName
- CIM_Group.CreationClassName
- CIM_Group.Name
- CIM_Group.BusinessCategory
- CIM_Group.CommonName
api_location:
- IpmiPrv.dll
api_type:
- DllExport
---

# CIM\_Group class

Collects ManagedElements into groups.

This class is defined so as to incorporate commonly-used LDAP attributes to permit implementations to easily derive this information from LDAP-accessible directories.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Version("2.6.0"), AMENDMENT]
class CIM_Group : CIM_Collection
{
  string Caption;
  string Description;
  string ElementName;
  string CreationClassName;
  string Name;
  string BusinessCategory;
  string CommonName;
};
```

## Members

The **CIM\_Group** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_Group** class has these properties.

<dl> <dt>

**BusinessCategory**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (128)
</dt> </dl>

Describes the kind of business activity performed by the members of the group.

</dd> <dt>

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

**CommonName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A name by which the group is commonly known in some limited scope, such as an organization, and conforms to the naming conventions of the country or culture with which it is associated.

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

The name of the class used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

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

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties/identity data, and description information.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (1024)
</dt> </dl>

The label by which the object is known. In the case of an LDAP-derived instance, the **Name** property value may be set to the distinguished name of the LDAP-accessed object.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\Hardware<br/>                                                              |
| MOF<br/>                      | <dl> <dt>IpmiPrv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IpmiPrv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Collection**](cim-collection.md)
</dt> </dl>

 

 





