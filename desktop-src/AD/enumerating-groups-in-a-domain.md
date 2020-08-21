---
title: Enumerating Groups in a Domain
description: Groups can be placed in any container or organizational unit (OU) in a domain as well as the root of the domain.
ms.assetid: 7f9d3c90-b6f4-4bfa-960f-58f380aa487c
ms.tgt_platform: multiple
keywords:
- Enumerating Groups in a Domain AD
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Groups in a Domain

Groups can be placed in any container or organizational unit (OU) in a domain as well as the root of the domain. This means that groups can be in numerous locations in the directory hierarchy. Therefore, you have two choices for enumerating groups:

1.  Enumerate the groups directly contained in a container, OU, or at the root of the domain.

    Explicitly bind to the container object that contains the groups to enumerate, set a filter that contains "groups" as the class using the [**IADsContainer.Filter**](/windows/desktop/api/iads/nn-iads-iadscontainer) property, and use the [**IADsContainer::get\_\_NewEnum**](/windows/desktop/api/iads/nf-iads-iadscontainer-get__newenum) method to enumerate the group objects.

    This technique enumerates groups contained directly in a container or OU object. If the container contains other containers that can potentially contain other groups, you must bind to those containers and recursively enumerate the groups on those containers. To manipulate the group objects and read only specific properties, use the deep search described in Option 2.

    Because enumeration returns pointers to ADSI COM objects representing each group object, you can call [**QueryInterface**](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) to get [**IADs**](/windows/desktop/api/iads/nn-iads-iads), [**IADsGroup**](/windows/desktop/api/iads/nn-iads-iadsgroup), and [**IADsPropertyList**](/windows/desktop/api/iads/nn-iads-iadspropertylist) interface pointers to the group object; that is, you can get interface pointers to each enumerated group object in a container without having to explicitly bind to each group object. To perform operations on all the groups directly within a container, enumeration does not require binding to each group in order to call **IADs** or **IADsGroup** methods. To retrieve specific properties from groups, use [**IDirectorySearch**](/windows/desktop/api/iads/nn-iads-idirectorysearch) as described in the second option.

    An exception to this occurs when you attempt to enumerate a group that contains members that are wellKnown security principals, such as Everyone, Authenticated users, BATCH, and so on. Because you cannot bind to these types of objects, they are not listed when you enumerate groups in the WinNT scope, even though it may appear to bind, because certain IADs methods such as Class, ADsPath, and Name return correct results when invoked on enumerated members.

2.  Perform a deep search for "objectCategory=group" to find all groups in a tree.

    First, bind to the container object where to begin the search. For example, to find all groups in a domain, bind to root of the domain; to find all groups in the forest, bind to global catalog and search from the root of the GC.

    Then use [**IDirectorySearch**](/windows/desktop/api/iads/nn-iads-idirectorysearch) to query using a search filter that contains (objectCategory=group) and search preference of **ADS\_SCOPE\_SUBTREE**.

    > [!Note]  
    > You can perform a search with a search preference of **ADS\_SCOPE\_ONELEVEL** to limit the search to the direct contents of the container object that you bound to.

     

    [**IDirectorySearch**](/windows/desktop/api/iads/nn-iads-idirectorysearch) retrieves only the values of specific properties from groups. To retrieve values, use **IDirectorySearch**. To manipulate the group objects returned from a search, that is, to use [**IADs**](/windows/desktop/api/iads/nn-iads-iads) or [**IADsGroup**](/windows/desktop/api/iads/nn-iads-iadsgroup) methods, explicitly bind to them. To do this, specify **distinguishedName** as one of the properties to return from the search and use the returned distinguished names to bind to each group returned in the search.

    Only specific properties are retrieved. You cannot retrieve all attributes without explicitly specifying every possible attribute of the group class.

 

 