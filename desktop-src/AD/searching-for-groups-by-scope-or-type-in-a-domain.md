---
title: Searching for Groups by Scope or Type in a Domain
description: In Windows 2000 domains, there is single class called group for all group scopes (Domain Local, Global, Universal) and types (security, distribution).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'e32629d9-aa62-4953-aa49-43af726b7deb'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["Searching for Groups by Scope or Type in a Domain AD"]
---

# Searching for Groups by Scope or Type in a Domain

In Windows 2000 domains, there is single class called [**group**](https://msdn.microsoft.com/library/ms682251) for all group scopes (Domain Local, Global, Universal) and types (security, distribution). The [**groupType**](https://msdn.microsoft.com/library/ms675935) attribute of the group object specifies the group type and scope.

To use type or scope to search for groups on Windows 2000 domains, use a filter that contains a matching rule for the [**groupType**](https://msdn.microsoft.com/library/ms675935) attribute. For more information about matching rules, see [Search Filter Syntax](https://msdn.microsoft.com/library/aa746475).

For more information and a code example that shows how to search for groups in a domain, see [Example Code for Searching for Groups in a Domain](example-code-for-performing-a-query-in-a-domain.md).

## Example LDAP Query Strings

The following query string examples show how to construct an LDAP query string used to search for or filter specific group types.

The following query string will search for security groups. This example uses "-2147483648" as the decimal equivalent of the **ADS\_GROUP\_TYPE\_SECURITY\_ENABLED** flag.


```C++
(&amp;(objectCategory=group)(groupType:1.2.840.113556.1.4.803:=-2147483648))
```



The following query string will search for universal distribution groups; that is, groups that contain the **ADS\_GROUP\_TYPE\_UNIVERSAL\_GROUP** flag and do not contain the **ADS\_GROUP\_TYPE\_SECURITY\_ENABLED** flag. This example uses "8" as the decimal equivalent of **ADS\_GROUP\_TYPE\_UNIVERSAL\_GROUP** and "-2147483648" as the decimal equivalent of the **ADS\_GROUP\_TYPE\_SECURITY\_ENABLED** flag.


```C++
(&amp;(objectCategory=group)((&amp;(groupType:1.2.840.113556.1.4.803:=8)(!(groupType:1.2.840.113556.1.4.803:=-2147483648)))))
```



 

 




