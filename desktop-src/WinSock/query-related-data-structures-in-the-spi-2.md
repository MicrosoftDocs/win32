---
Description: 'The WSAQUERYSET structure is used to form queries for the NSPLookupServiceBegin function, and used to deliver query results for the NSPLookupServiceNext function.'
ms.assetid: '017b5828-bc6e-42b7-aba7-21648b2dd707'
title: 'Query-Related Data Structures in the SPI'
---

# Query-Related Data Structures in the SPI

The [**WSAQUERYSET**](wsaqueryset-2.md) structure is used to form queries for [**NSPLookupServiceBegin**](nsplookupservicebegin-2.md), and used to deliver query results for [**NSPLookupServiceNext**](nsplookupservicenext-2.md). It is a complex structure because it contains pointers to several other structures, some of which reference still other structures. The relationship between **WSAQUERYSET** and the structures it references is illustrated as follows:

![wsaqueryset structures](images/ovrvw3-2.png)

Within the [**WSAQUERYSET**](wsaqueryset-2.md) structure, most of the members are self explanatory, but some deserve additional explanation. The **dwSize** will be filled in with sizeof( **WSAQUERYSET**), and can be used by namespace providers to detect and adapt to different versions of the **WSAQUERYSET** structure that may appear.

The **dwOutputFlags** member is used by a namespace provider to provide additional data about query results. For more information, see [**NSPLookupServiceNext**](nsplookupservicenext-2.md).

The [**WSAECOMPARATOR**](wsaecomparator-2.md) structure referenced by **lpversion** is used for both query constraint and results. For queries, the **dwVersion** member indicates the desired version of the service. The **ecHow** member is an enumerated type which specifies how the comparison will be made. The choices are COMP\_EQUALS which requires that an exact match in version occurs, or COMP\_NOTLESS which specifies that the service's version number be no less than the value of **dwVersion**.

The interpretation of **dwNameSpace** and **lpNSProviderId** depends upon how the structure is being used and is described further in the individual function descriptions that utilize this structure.

The **lpszContext** member applies to hierarchical namespaces, and specifies the starting point of a query or the location within the hierarchy where the service resides. The general rules are:

-   A value of **NULL**, blank ("") will start the search at the default context.
-   A value of "\\" starts the search at the top of the namespace.
-   Any other value starts the search at the designated point.

Providers that do not support containment may return an error if anything other than "" or "\\" is specified. Providers that support limited containment, such as groups, should accept "", '\\", or a designated point. Contexts are namespace specific. If **dwNameSpace** is NS\_ALL, then only "" or "\\" should be passed as the context because these are recognized by all namespaces.

The **lpszQueryString** member is used to supply additional, namespace-specific query information such as a string describing a well-known service and transport protocol name, as in "ftp/tcp".

The [**AFPROTOCOLS**](afprotocols-2.md) structure referenced by **lpafpProtocols** is used for query purposes only, and supplies a list of protocols to constrain the query. These protocols are represented as (address family, protocol) pairs, because protocol values only have meaning within the context of an address family.

The array of [**CSADDR\_INFO**](csaddr-info-2.md) structure referenced by **lpcsaBuffer** contains all of the information required for either a service to use in establishing a listen, or a client to use in establishing a connection to the service. The **LocalAddr** and **RemoteAddr** members both directly contain a [**SOCKET\_ADDRESS**](socket-address-2.md) structure. A service would create a socket using the tuple (LocalAddr.lpSockaddr-&gt;sa\_family, iSocketType, iProtocol). It would bind the socket to a local address using LocalAddr.lpSockaddr, and LocalAddr.lpSockaddrLength. The client creates its socket with the tuple (RemoteAddr.lpSockaddr-&gt;sa\_family, iSocketType, iProtocol), and uses the combination of RemoteAddr.lpSockaddr, and RemoteAddr.lpSockaddrLength when making a remote connection.

 

 



