---
title: DS\_LDAP\_Root\_Class class
description: The base class of all the classes provided by the DS Provider.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 59648ddd-92ff-4536-8c3f-42012aabef3a
ms.prod: windows-server-dev
ms.technology:
- active-directory-domain-services
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DS_LDAP_Root_Class class
- DS_LDAP_Root_Class class, described
topic_type:
- apiref
api_name:
- DS_LDAP_Root_Class
- DS_LDAP_Root_Class.ADSIPath
api_location:
- Dsprov.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DS\_LDAP\_Root\_Class class

The base class of all the classes provided by the DS Provider.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, AMENDMENT]
class DS_LDAP_Root_Class
{
  string ADSIPath;
};
```

## Members

The **DS\_LDAP\_Root\_Class** class has these types of members:

-   [Properties](#properties)

### Properties

The **DS\_LDAP\_Root\_Class** class has these properties.

<dl> <dt>

**ADSIPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**KEY**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The key for any DS Object.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Namespace<br/>                | Root\\directory\\LDAP<br/>                                                      |
| MOF<br/>                      | <dl> <dt>DsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Dsprov.dll</dt> </dl> |



 

 





