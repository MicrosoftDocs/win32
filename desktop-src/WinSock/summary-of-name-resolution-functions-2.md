---
Description: 'The name resolution functions can be grouped into three categories: Service installation, client queries, and helper (with macros).'
ms.assetid: 'c16a7163-11f5-4ad6-9df1-9bad2a964e48'
title: Summary of Name Resolution Functions
---

# Summary of Name Resolution Functions

The name resolution functions can be grouped into three categories: Service installation, client queries, and helper (with macros). The sections that follow identify the functions in each category and briefly describe their intended use. Key data structures are also described.

## Service Installation

-   [**WSAInstallServiceClass**](wsainstallserviceclass-2.md)
-   [**WSARemoveServiceClass**](wsaremoveserviceclass-2.md)
-   [**WSASetService**](wsasetservice-2.md)

When the required service class does not already exist, an application uses [**WSAInstallServiceClass**](wsainstallserviceclass-2.md) to install a new service class by supplying a service class name, a GUID for the service class identifier, and a series of [**WSANSCLASSINFO**](wsansclassinfo.md) structures. These structures are each specific to a particular namespace, and supply common values such as recommended TCP port numbers or NetWare SAP Identifiers. A service class can be removed by calling [**WSARemoveServiceClass**](wsaremoveserviceclass-2.md) and supplying the GUID corresponding to the class identifier.

Once a service class exists, specific instances of a service can be installed or removed through [**WSASetService**](wsasetservice-2.md). This function takes a [**WSAQUERYSET**](wsaqueryset-2.md) structure as an input parameter along with an operation code and operation flags. The operation code indicates whether the service is being installed or removed. The **WSAQUERYSET** structure provides all of the relevant information about the service including service class identifier, service name (for this instance), applicable namespace identifier and protocol information, and a set of transport addresses at which the service listens. Services should invoke **WSASetService** when they initialize to advertise their presence in dynamic namespaces.

## Client Query

-   [**WSAEnumNameSpaceProviders**](wsaenumnamespaceproviders-2.md)
-   [**WSALookupServiceBegin**](wsalookupservicebegin-2.md)
-   [**WSALookupServiceNext**](wsalookupservicenext-2.md)
-   [**WSALookupServiceEnd**](wsalookupserviceend-2.md)

The [**WSAEnumNameSpaceProviders**](wsaenumnamespaceproviders-2.md) function allows an application to discover which namespaces are accessible through Winsock name resolution facilities. It also allows an application to determine whether a given namespace is supported by more than one namespace provider, and to discover the provider identifier for any particular namespace provider. Using a provider identifier, the application can restrict a query operation to a specified namespace provider.

Winsock namespace–query operations involve a series of calls: [**WSALookupServiceBegin**](wsalookupservicebegin-2.md), followed by one or more calls to [**WSALookupServiceNext**](wsalookupservicenext-2.md) and ending with a call to [**WSALookupServiceEnd**](wsalookupserviceend-2.md). **WSALookupServiceBegin** takes a [**WSAQUERYSET**](wsaqueryset-2.md) structure as input to define the query parameters along with a set of flags to provide additional control over the search operation. It returns a query handle which is used in the subsequent calls to **WSALookupServiceNext** and **WSALookupServiceEnd**.

The application invokes [**WSALookupServiceNext**](wsalookupservicenext-2.md) to obtain query results, with results supplied in an application-supplied [**WSAQUERYSET**](wsaqueryset-2.md) buffer. The application continues to call **WSALookupServiceNext** until the error code WSA\_E\_NO\_MORE is returned indicating that all results have been retrieved. The search is then terminated by a call to [**WSALookupServiceEnd**](wsalookupserviceend-2.md). The **WSALookupServiceEnd** function can also be used to cancel a currently pending **WSALookupServiceNext** when called from another thread.

In Windows Sockets 2, conflicting error codes are defined for WSAENOMORE (10102) and WSA\_E\_NO\_MORE (10110). The error code WSAENOMORE will be removed in a future version and only WSA\_E\_NO\_MORE will remain. For Windows Sockets 2, however, applications should check for both WSAENOMORE and WSA\_E\_NO\_MORE for the widest possible compatibility with namespace providers that use either one.

## Helper Functions

-   [**WSAGetServiceClassNameByClassId**](wsagetserviceclassnamebyclassid-2.md)
-   [**WSAAddressToString**](wsaaddresstostring-2.md)
-   [**WSAStringToAddress**](wsastringtoaddress-2.md)
-   [**WSAGetServiceClassInfo**](wsagetserviceclassinfo-2.md)

The name resolution helper functions include a function to retrieve a service class name given a service class identifier, a pair of functions used to translate a transport address between a [**SOCKADDR**](sockaddr-2.md) structure and an ASCII string representation, a function to retrieve the service class schema information for a given service class, and a set of macros for mapping well known services to preallocated GUIDs.

The following macros from Winsock2.h aid in mapping between well known service classes and these namespaces:

| Macro                                                                                                            | Description                                                                                                                |
|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| SVCID\_TCP(Port) SVCID\_UDP(Port)<br/> SVCID\_NETWARE(Object Type)<br/>                              | Given a port for TCP/IP or UDP/IP or the object type in the case of NetWare, returns the GUID (port number in host order). |
| IS\_SVCID\_TCP(GUID)IS\_SVCID\_UDP(GUID)<br/> IS\_SVCID\_NETWARE(GUID)<br/>                          | Returns **TRUE** if the GUID is within the allowable range.                                                                |
| SET\_TCP\_SVCID(GUID, port)SET\_UDP\_SVCID(GUID, port)<br/>                                                | Initializes a GUID structure with the GUID equivalent for a TCP or UDP port number (port number must be in host order).    |
| PORT\_FROM\_SVCID\_TCP(GUID)PORT\_FROM\_SVCID\_UDP(GUID)<br/> SAPID\_FROM\_SVCID\_NETWARE(GUID)<br/> | Returns the port or object type associated with the GUID (port number in host order).                                      |



 

## Related topics

<dl> <dt>

[**getaddrinfo**](getaddrinfo-2.md)
</dt> <dt>

[**GetAddrInfoEx**](getaddrinfoex.md)
</dt> <dt>

[**GetAddrInfoW**](getaddrinfow.md)
</dt> <dt>

[**getnameinfo**](getnameinfo-2.md)
</dt> <dt>

[**GetNameInfoW**](getnameinfow.md)
</dt> <dt>

[Name Resolution Data Structures](name-resolution-data-structures-2.md)
</dt> <dt>

[Name Resolution Model](name-resolution-model-2.md)
</dt> <dt>

[Protocol-Independent Name Resolution](protocol-independent-name-resolution-2.md)
</dt> <dt>

[Registration and Name Resolution](registration-and-name-resolution-2.md)
</dt> <dt>

[**SOCKADDR**](sockaddr-2.md)
</dt> <dt>

[**WSAEnumNameSpaceProviders**](wsaenumnamespaceproviders-2.md)
</dt> <dt>

[**WSAGetServiceClassNameByClassId**](wsagetserviceclassnamebyclassid-2.md)
</dt> <dt>

[**WSAInstallServiceClass**](wsainstallserviceclass-2.md)
</dt> <dt>

[**WSALookupServiceBegin**](wsalookupservicebegin-2.md)
</dt> <dt>

[**WSALookupServiceEnd**](wsalookupserviceend-2.md)
</dt> <dt>

[**WSALookupServiceNext**](wsalookupservicenext-2.md)
</dt> <dt>

[**WSARemoveServiceClass**](wsaremoveserviceclass-2.md)
</dt> <dt>

[**WSASetService**](wsasetservice-2.md)
</dt> <dt>

[**WSAQUERYSET**](wsaqueryset-2.md)
</dt> <dt>

[**WSANSCLASSINFO**](wsansclassinfo.md)
</dt> </dl>

 

 




