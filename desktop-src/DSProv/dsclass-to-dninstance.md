---
title: DSClass\_To\_DNInstance class
description: Allows the client to give a hint to the DS Instance Provider to scope enumerations and queries to a particular sub-tree or a naming context.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: adef3727-6f35-40d1-9f60-42c5a4573445
ms.prod: windows-server-dev
ms.technology:
- active-directory-domain-services
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DSClass_To_DNInstance class
- DSClass_To_DNInstance class, described
topic_type:
- apiref
api_name:
- DSClass_To_DNInstance
- DSClass_To_DNInstance.DSClass
- DSClass_To_DNInstance.RootDNForSearchAndQuery
api_location:
- Dsprov.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DSClass\_To\_DNInstance class

Allows the client to give a hint to the DS Instance Provider to scope enumerations and queries to a particular sub-tree or a naming context. The client should create instances of this class if it wants the DS Provider to do enumerations and queries of a specific DS class from a specific DS Object as the root

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, AMENDMENT]
class DSClass_To_DNInstance
{
  string       DSClass;
  DN_Class REF RootDNForSearchAndQuery;
};
```

## Members

The **DSClass\_To\_DNInstance** class has these types of members:

-   [Properties](#properties)

### Properties

The **DSClass\_To\_DNInstance** class has these properties.

<dl> <dt>

**DSClass**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**KEY**](https://msdn.microsoft.com/library/aa392157), **classref** ("DS\_LDAP\_Root\_Class")
</dt> </dl>

The Name of the class for which scoping is to be used.

</dd> <dt>

**RootDNForSearchAndQuery**
</dt> <dd> <dl> <dt>

Data type: **DN\_Class**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**KEY**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A reference to an instance of [**DN\_Class**](dn-class.md) that gives the ADSI path of the object below which the search should be scoped.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Namespace<br/>                | Root\\directory\\LDAP<br/>                                                      |
| MOF<br/>                      | <dl> <dt>DsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Dsprov.dll</dt> </dl> |



 

 





