---
title: Enumerating Users
description: Unlike Windows NT 4.0 domains, Windows 2000 users can be placed in any container or organizational unit (OU) in a domain as well as the root of the domain.
ms.assetid: 4a35af7a-f43b-4cf9-a030-77f6c2518ae7
ms.tgt_platform: multiple
keywords:
- Enumerating Users AD
- users AD , enumerating a user
- Active Directory, using,users, enumerating a user
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Users

Unlike Windows NT 4.0 domains, Windows 2000 users can be placed in any container or organizational unit (OU) in a domain as well as the root of the domain. This means that users can be in numerous locations in the directory hierarchy. Therefore, you have two choices for enumerating users:

-   Enumerate the users directly contained in a container, OU, or at the root of the domain:

    Explicitly bind to the container object that contains the users you are interested in enumerating, set a filter containing "user" as the class using the [**IADsContainer.Filter**](/windows/desktop/ADSI/iadscontainer-property-methods) property, and use the [**IADsContainer::get\_\_NewEnum**](/windows/desktop/api/iads/nf-iads-iadscontainer-get__newenum) method to enumerate the user objects.

    This technique can be used to enumerate users that are directly contained in a container or OU object. If the container contains other containers that can potentially contain other users, you must bind to those containers and recursively enumerate the users on those containers. If it is not required that you manipulate the user objects, and only need to read specific properties, use the deep search described in Option 2.

    Because enumeration returns pointers to ADSI COM objects representing each user object, you can call [**QueryInterface**](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) to get [**IADs**](/windows/desktop/api/iads/nn-iads-iads), [**IADsUser**](/windows/desktop/api/iads/nn-iads-iadsuser), and [**IADsPropertyList**](/windows/desktop/api/iads/nn-iads-iadspropertylist) interface pointers to the user object. This means you can get interface pointers to each enumerated user object in a container without having to explicitly bind to each user object. To perform operations on all the users directly within a container, enumeration avoids having to bind to each user in order to call **IADs** or **IADsUser** methods. To retrieve specific properties from users, use [**IDirectorySearch**](/windows/desktop/api/iads/nn-iads-idirectorysearch) as described in option 2.

-   Perform a deep search for (&(objectClass=user)(objectCategory=person)) to find all users in a tree:

    First, bind to the container object where to begin the search. For example, to find all users in a domain, bind to root of the domain; to find all users in the forest, bind to the global catalog and search from the root of the GC.

    Then use [**IDirectorySearch**](/windows/desktop/api/iads/nn-iads-idirectorysearch) to query using a search filter containing (&(objectClass=user)(objectCategory=person)) and search preference of ADS\_SCOPE\_SUBTREE.

    You can perform a search with a search preference of ADS\_SCOPE\_ONELEVEL to limit the search to the direct contents of the container object that you bound to.

    [**IDirectorySearch**](/windows/desktop/api/iads/nn-iads-idirectorysearch) retrieves only the values of specific properties from users. To retrieve values, use **IDirectorySearch**. To manipulate the user objects returned from a search, that is, you want to use [**IADs**](/windows/desktop/api/iads/nn-iads-iads) or [**IADsUser**](/windows/desktop/api/iads/nn-iads-iadsuser) methods, you must explicitly bind to them. To do this, specify **distinguishedName** as one of the properties to return from the search and use the returned distinguished names to bind to each user returned in the search.

    Only specific properties are retrieved. You cannot retrieve all attributes without explicitly specifying every possible attribute of the user class.

 

 