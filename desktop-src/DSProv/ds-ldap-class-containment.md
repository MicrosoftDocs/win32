---
title: DS\_LDAP\_Class\_Containment class
description: The DS\_LDAP\_Class\_Containment class models the hierarchical object store of the Active Directory.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '73bcec4e-0578-43c4-a42e-c9e88dbd752a'
ms.prod: 'windows-server-dev'
ms.technology:
- 'active-directory-domain-services'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DS_LDAP_Class_Containment class", "DS_LDAP_Class_Containment class, described"]
topic_type:
- apiref
api_name:
- DS_LDAP_Class_Containment
- DS_LDAP_Class_Containment.ChildClass
- DS_LDAP_Class_Containment.ParentClass
api_location:
- Dsprov.dll
api_type:
- DllExport
---

# DS\_LDAP\_Class\_Containment class

The **DS\_LDAP\_Class\_Containment** class models the hierarchical object store of the Active Directory.

## Syntax

``` syntax
[Association, dynamic, HasClassRefs, provider("Microsoft|DSLDAPClassAssociationsProvider|V1.0"), AMENDMENT]
class DS_LDAP_Class_Containment
{
  object REF ChildClass;
  object REF ParentClass;
};
```

## Members

The **DS\_LDAP\_Class\_Containment** class has these types of members:

-   [Properties](#properties)

### Properties

The **DS\_LDAP\_Class\_Containment** class has these properties.

<dl> <dt>

**ChildClass**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), **classref** ("DS\_LDAP\_Root\_Class")
</dt> </dl>

Reference to the child Directory Services (DS) class.

</dd> <dt>

**ParentClass**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), **classref** ("DS\_LDAP\_Root\_Class")
</dt> </dl>

Reference to the parent DS class.

</dd> </dl>

## Remarks

The DS is essentially a hierarchical store of objects. Those objects that can appear at a nonleaf level in the hierarchy are called "containers". The structure of this hierarchy is further controlled by the Poss-Superiors and System-Poss-Superiors properties of a class in the schema. These, taken together, specify the set of classes whose instances can be contained within an instance of a container class. This specification can be modeled as a CIM association in the following way as instances of the static association class **DS\_LDAP\_Class\_Containment**.

The association class provider supports the [**GetObjectAsync**](https://msdn.microsoft.com/library/aa392110) and [**CreateClassEnumAsync**](https://msdn.microsoft.com/library/aa392096) methods.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Namespace<br/>                | Root\\directory\\ldap<br/>                                                      |
| MOF<br/>                      | <dl> <dt>Dsprov.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Dsprov.dll</dt> </dl> |



 

 





