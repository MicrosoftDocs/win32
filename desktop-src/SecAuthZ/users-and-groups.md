---
description: Explains the definition of users and groups in the Authorization Manager API.
ms.assetid: 783be0b2-7894-4780-900d-98918f824a04
title: Users and Groups
ms.topic: article
ms.date: 05/31/2018
---

# Users and Groups

In Authorization Manager, recipients of authorization policy are represented by the following groups:

-   Windows Users and Groups

    These groups include users, computers, and built-in groups for security principals.

-   LDAP Query Groups

    Membership in these groups is dynamically calculated as needed from Lightweight Directory Access Protocol (LDAP) queries. An LDAP query group is a type of application group.

-   Basic Application Groups

    These groups consist of LDAP query groups, Windows users and groups, and other basic application groups.

## Windows Users and Groups

These are the same as the users and groups used throughout the Windows operating system.

## LDAP Query Groups

In Authorization Manager, you can use LDAP queries to match the user's attributes with those of the user's object in Active Directory.

For example, the following query finds everyone except Andy.


```C++
(&(objectCategory=person)(objectClass=user)(!cn=andy))
```



The following query finds all members of the someone alias at `www.fabrikam.com`.


```C++
(memberOf=CN=someone,OU=litwareinc,DC=Fabrikam,DC=com)
```



## Basic Application Groups

In the Authorization Manager API, an application group is represented by an [**IAzApplicationGroup**](/windows/desktop/api/Azroles/nn-azroles-iazapplicationgroup) object. A basic application group is a type of application group.

To define basic application group membership, define who is a member and define who is not a member. Both of these steps are carried out in the same way. Specify zero or more Windows users and groups, previously defined basic application groups, or LDAP query groups. The membership of the basic application group is calculated by removing any nonmembers from the group. Authorization Manager does this automatically at run time.

Nonmembership in a basic application group takes precedence over membership.

Circular membership definitions are not allowed; they result in the following error message: "Cannot add GroupName. The following problem occurred: A loop has been detected."

## Related topics

<dl> <dt>

[Defining Groups of Users in C++](defining-groups-of-users-in-c--.md)
</dt> </dl>

 

 



