---
title: DN\_Class class
description: Encapsulates a DN.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'd5bad4db-02e2-4480-904d-0ee2914b2b23'
ms.prod: 'windows-server-dev'
ms.technology:
- 'active-directory-domain-services'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DN_Class class", "DN_Class class, described"]
topic_type:
- apiref
api_name:
- DN_Class
- DN_Class.DN
api_location:
- Dsprov.dll
api_type:
- DllExport
---

# DN\_Class class

Encapsulates a DN.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[AMENDMENT]
class DN_Class
{
  string DN;
};
```

## Members

The **DN\_Class** class has these types of members:

-   [Properties](#properties)

### Properties

The **DN\_Class** class has these properties.

<dl> <dt>

**DN**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**KEY**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The ADSI Path to the object in the DS.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Namespace<br/>                | Root\\directory\\LDAP<br/>                                                      |
| MOF<br/>                      | <dl> <dt>DsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Dsprov.dll</dt> </dl> |



 

 





