---
title: PrivilegeGroup class
description: Represents a group of AuthorizedPrivilege objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'D0C4587C-2F3D-41D2-BD25-13E814F2C4BA'
ms.prod: 'windows-server-dev'
ms.technology:
- 'intelligent-platform-management-interface'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PrivilegeGroup class", "PrivilegeGroup class, described"]
topic_type:
- apiref
api_name:
- PrivilegeGroup
- PrivilegeGroup.Caption
- PrivilegeGroup.Description
- PrivilegeGroup.ElementName
- PrivilegeGroup.CreationClassName
- PrivilegeGroup.Name
- PrivilegeGroup.BusinessCategory
- PrivilegeGroup.CommonName
api_location:
- IpmiPrv.dll
api_type:
- DllExport
---

# PrivilegeGroup class

Represents a group of [**AuthorizedPrivilege**](authorizedprivilege.md) objects.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("IPMIPrv"), AMENDMENT]
class PrivilegeGroup : CIM_Group
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

The **PrivilegeGroup** class has these types of members:

-   [Properties](#properties)

### Properties

The **PrivilegeGroup** class has these properties.

<dl> <dt>

**BusinessCategory**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (128)
</dt> </dl>

May be used to describe the kind of business activity performed by the members of the group.

This property is inherited from [**CIM\_Group**](cim-group.md).

</dd> <dt>

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

**CommonName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A (possibly ambiguous) name by which the group is commonly known in some limited scope (such as an organization) and conforms to the naming conventions of the country or culture with which it is associated.

This property is inherited from [**CIM\_Group**](cim-group.md).

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

Indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

This property is inherited from [**CIM\_Group**](cim-group.md).

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

A user-friendly name for the object. This property allows each instance to define a user-friendly name IN ADDITION TO its key properties/identity data, and description information.

Note that ManagedSystemElement's Name property is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information MAY be present in both the Name and ElementName properties.

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

Defines the label by which the object is known. In the case of an LDAP-derived instance, the Name property value may be set to the distinguished name of the LDAP-accessed object instance.

This property is inherited from [**CIM\_Group**](cim-group.md).

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\hardware<br/>                                                              |
| MOF<br/>                      | <dl> <dt>IpmiPrv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IpmiPrv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Group**](cim-group.md)
</dt> <dt>

[IPMI Provider](ipmi-provider.md)
</dt> </dl>

 

 





