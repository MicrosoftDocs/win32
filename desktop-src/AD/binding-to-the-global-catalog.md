---
title: Binding to the Global Catalog
description: The Global Catalog is a namespace that contains directory data for all domains in a forest.
ms.assetid: c3c131c7-d9dd-4dbd-a909-abd0ffd9f375
ms.tgt_platform: multiple
keywords:
- Binding to the Global Catalog AD
- global catalog AD , binding to
ms.topic: article
ms.date: 05/31/2018
---

# Binding to the Global Catalog

The Global Catalog is a namespace that contains directory data for all domains in a forest. The Global Catalog contains a partial replica of every domain directory. It contains an entry for every object in the enterprise forest, but does not contain all the properties of each object. Instead, it contains only the properties specified for inclusion in the Global Catalog.

The Global Catalog is stored on specific servers throughout the enterprise. Only domain controllers can serve as Global Catalog servers. Administrators indicate whether a given domain controller holds a Global Catalog by using the Active Directory Sites and Services Manager.

To bind to the Global Catalog with ADSI, use the "GC:" moniker.

There are two ways to bind to the Global Catalog to perform a search in a forest:

-   Bind to the enterprise root object to search across all domains in the forest.
-   Bind to a specific object to search that object and its children. For example, if you bind to a domain that has two domains beneath it in a domain tree in the forest, you can search across those three domains. Be aware that the distinguished name for the object to bind to is exactly the same as the distinguished name used to bind to the "LDAP:" namespace. Recall that "LDAP:" is a full replica of a single domain and that "GC:" is a partial replica of all domains in the forest.

As with the "LDAP:" moniker, you can use serverless binding or bind to a specific Global Catalog server. If searching in the current forest, use serverless binding. However, if searching in another forest, specify either a domain name or a Global Catalog server to bind to, such as shown in the following examples.

Bind using the domain name:

``` syntax
GC://fabrikam.com
```

Bind using the server name:

``` syntax
GC://servername
```

You can also bind to a specific object within the Global Catalog. To bind to the sales object in the fabrikam domain, use the following format.

``` syntax
GC://fabrikam.com/DC=sales,DC=fabrikam,DC=com
```

Or, to bind to the sales object on the server, use the following format.

``` syntax
GC://servername.fabrikam.com/DC=sales,DC=fabrikam,DC=com
```

**To search the entire forest**

1.  Bind to the root of the Global Catalog namespace.
2.  Enumerate the Global Catalog container. The Global Catalog container contains a single object that you can use to search the entire forest.
3.  Use the object in the container to perform the search. In C/C++, call [**QueryInterface**](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) to get an [**IDirectorySearch**](/windows/desktop/api/iads/nn-iads-idirectorysearch) pointer on the object so that you can use the **IDirectorySearch** interface to perform the search. In Visual Basic, use the object returned from the enumeration in your ADO query.

To enumerate the Global Catalog servers in a site, perform an LDAP subtree search of "cn=&lt;yoursite&gt;,cn=sites,\<DN of the configurationNamingContext\>", using the following filter string.

``` syntax
(&(objectCategory=nTDSDSA)(options:1.2.840.113556.1.4.803:=1))
```

This filter uses the **LDAP\_MATCHING\_RULE\_BIT\_AND** matching rule operator (1.2.840.113556.1.4.803) to find **nTDSDSA** objects that have the low-order bit set in the bitmask of the **options** attribute. The low-order bit, which corresponds to the **NTDSDSA\_OPT\_IS\_GC** constant defined in Ntdsapi.h, identifies the **nTDSDSA** object of a Global Catalog server. For more information about matching rules, see [Search Filter Syntax](/windows/desktop/ADSI/search-filter-syntax).

The parent of the **nTDSDSA** object is the server object, and the **dNSHostName** property of the server object is the DNS name of the Global Catalog server.

You cannot use \#define constants such as **NTDSDSA\_OPT\_IS\_GC** and **LDAP\_MATCHING\_RULE\_BIT\_AND** directly in a search filter string. However, you could use these constants as arguments to a function such as [**swprintf\_s**](/windows/win32/api/winuser/nf-winuser-wsprintfa) to insert the constant values into a filter string.

The global catalog does not represent the entire forest tree structure. For example, you might expect that the following code example would enumerate all of the domains in the forest and all child objects of each domain. In reality, what it actually does is enumerate all of the domains in the forest, but none of the enumerated domain objects contain any children. This is a limitation of the global catalog.


```VB
Dim oGC As IADs
Dim oDomain As IADs
Dim oChild As IADs

Set oGC = GetObject("GC:")
For Each oDomain In oGC
    ' Print the name of the domain.
    Debug.Print oDomain.Name
    
    ' Enumerate the child objects of the domain.
    For Each oChild In oDomain
        Debug.Print oChild.Name
    Next
Next
```



To correct this, it is necessary to bind to each domain object and then enumerate the child objects of each domain. The proper technique is shown in the following code example.


```VB
Dim oGC As IADs
Dim oDomainEnum As IADs
Dim oDomainBind As IADs
Dim oChild As IADs

Set oGC = GetObject("GC:")
For Each oDomainEnum In oGC
    ' Print the name of the domain.
    Debug.Print oDomainEnum.Name
    
    ' Bind to the domain.
    Set oDomainBind = GetObject("LDAP://" + oDomainEnum.Name)
    
    ' Enumerate the child objects of the domain.
    For Each oChild In oDomainBind
        Debug.Print oChild.Name
    Next
Next
```



For more information and code examples that show how to search an entire forest, see [Example Code for Searching a Forest](example-code-for-searching-a-forest.md).

 

 
