---
title: Querying for Users
description: To query for a user, the query must contain the search expression \ 0034;( (objectClass user)(objectCategory person)) \ 0034;.
ms.assetid: a9f12de4-e1e2-41bb-b2cc-ff9c9fa1c39a
ms.tgt_platform: multiple
keywords:
- users AD , querying for users
- Active Directory, using, users, querying for users
ms.topic: article
ms.date: 05/31/2018
---

# Querying for Users

To query for a user, the query must contain the search expression "(&(objectClass=user)(objectCategory=person))".

Because the computer class is a subclass of user, a query containing only (objectClass=user) would return user objects and computer objects. Also, the object category of the user object is person (not user); therefore, the expression (objectCategory=user) does not return any users. If you use the expression (objectCategory=person), the query returns user objects and contact objects.

Users can be placed in any container or organizational unit in a domain as well as the root of the domain. This means that users can be in numerous locations in the directory hierarchy. You can perform a deep search for "(objectCategory=user)" to find all users in a container, organizational unit, domain, domain tree, or forest—depending on the object that the [**IDirectorySearch**](/windows/desktop/api/iads/nn-iads-idirectorysearch) pointer you are using is bound to.

 

 