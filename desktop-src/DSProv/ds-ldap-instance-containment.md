---
title: DS\_LDAP\_Instance\_Containment class
description: DS\_LDAP\_Instance\_Containment is an instance class that models the container relationships in the Active Directory, and is supported by the Active Directory instance provider.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 41b8d033-a987-4b3a-a6e2-1cc620c0a015
ms.prod: windows-server-dev
ms.technology:
- active-directory-domain-services
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DS_LDAP_Instance_Containment class
- DS_LDAP_Instance_Containment class, described
topic_type:
- apiref
api_name:
- DS_LDAP_Instance_Containment
- DS_LDAP_Instance_Containment.ChildInstance
- DS_LDAP_Instance_Containment.ParentInstance
api_location:
- Dsprov.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DS\_LDAP\_Instance\_Containment class

**DS\_LDAP\_Instance\_Containment** is an instance class that models the container relationships in the Active Directory, and is supported by the Active Directory instance provider.

## Syntax

``` syntax
[Association, dynamic, provider("Microsoft|DSLDAPInstanceProvider|V1.0"), AMENDMENT]
class DS_LDAP_Instance_Containment
{
  DS_LDAP_Root_Class REF ChildInstance;
  DS_LDAP_Root_Class REF ParentInstance;
};
```

## Members

The **DS\_LDAP\_Instance\_Containment** class has these types of members:

-   [Properties](#properties)

### Properties

The **DS\_LDAP\_Instance\_Containment** class has these properties.

<dl> <dt>

**ChildInstance**
</dt> <dd> <dl> <dt>

Data type: **DS\_LDAP\_Root\_Class**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**KEY**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Reference to an [**DS\_LDAP\_Root\_Class**](ds-ldap-root-class.md) that represents the child Directory Services instance.

</dd> <dt>

**ParentInstance**
</dt> <dd> <dl> <dt>

Data type: **DS\_LDAP\_Root\_Class**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**KEY**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Reference to an [**DS\_LDAP\_Root\_Class**](ds-ldap-root-class.md) that represents the parent Directory Services instance.

</dd> </dl>

## Remarks

The **DS\_LDAP\_Instance\_Containment** class supports the [**GetObjectAsync**](https://msdn.microsoft.com/library/aa392110) and **ExecuteQueryAsync** methods.

The **DS\_LDAP\_Instance\_Containment** class supports only the following forms of querying that help a client navigate the object hierarchy:

-   A query in which the child instance is specified.

    ```sql
    SELECT * FROM DS_LDAP_Instance_Containment 
    WHERE ChildInstance=<InstancePath>
    ```

    

-   A query in which the parent instance is specified.

    ```sql
    SELECT * FROM DS_LDAP_Instance_Containment 
    WHERE ParentInstance=<InstancePath>
    ```

    

-   A query in which the child instance and parent instance are specified.

    ```sql
    SELECT * FROM DS_LDAP_Instance_Containment 
    WHERE ChildInstance=<InstancePath> 
        AND ParentInstance=<InstancePath>
    ```

    

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Namespace<br/>                | Root\\directory\\ldap<br/>                                                      |
| MOF<br/>                      | <dl> <dt>Dsprov.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Dsprov.dll</dt> </dl> |



 

 





