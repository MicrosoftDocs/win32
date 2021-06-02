---
description: A namespace provider implements an interface mapping between the Winsock namespace SPI and the native programmatic interface of an existing name service such as DNS, X.500, or NetWare Directory Services (NDS).
ms.assetid: 9b35aa58-9011-4e0d-8c93-02714952b4a5
title: Namespace Service Providers
ms.topic: article
ms.date: 05/31/2018
---

# Namespace Service Providers

A namespace provider implements an interface mapping between the Winsock namespace SPI and the native programmatic interface of an existing name service such as DNS, X.500, or NetWare Directory Services (NDS). While a namespace provider supports exactly one namespace, it is possible for multiple providers for a given namespace to be installed. It is also possible for a single DLL to create an instance of multiple namespace providers. As namespace providers are installed, a catalog of [**WSANAMESPACE\_INFO**](/windows/desktop/api/Winsock2/ns-winsock2-wsanamespace_infow) structures is maintained. An application may use [**WSAEnumNameSpaceProviders**](/windows/desktop/api/Winsock2/nf-winsock2-wsaenumnamespaceprovidersa) to discover which namespaces are supported on a computer.

On Windows Vista and later, an enhanced [**WSANAMESPACE\_INFOEX**](/windows/desktop/api/Winsock2/ns-winsock2-wsanamespace_infoexw) structure and [**WSAEnumNameSpaceProvidersEx**](/windows/desktop/api/Winsock2/nf-winsock2-wsaenumnamespaceprovidersexa) function are provided.

On 64-bit platforms, similar [**WSCEnumNameSpaceProviders32**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscenumnamespaceproviders32) and [**WSCEnumNameSpaceProvidersEx32**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscenumnamespaceprovidersex32) functions are provided to enumerate the 32-bit catalog.

Refer to [Winsock Namespace Service Provider Requirements](winsock-namespace-service-provider-requirements.md) for detailed information.

## Legacy GetXbyY Service Providers

Windows Sockets 2 fully supports the TCP/IP-specific name resolution facilities found in Windows Sockets version 1.1. It does this by including the set of **GetXbyY** functions in the SPI. However, the treatment of this set of functions is somewhat different from the rest of the SPI functions. The **GetXbyY** functions appearing in the SPI are prefaced with GETXBYYSP\_, and are summarized in the following table.

Berkeley Style Functions



| SPI function name           | Description                                                                              |
|-----------------------------|------------------------------------------------------------------------------------------|
| GETXBYYSP\_gethostbyaddr    | Supplies a [**hostent**](/windows/desktop/api/winsock/ns-winsock-hostent) structure for the specified host address.        |
| GETXBYYSP\_gethostbyname    | Supplies a [**hostent**](/windows/desktop/api/winsock/ns-winsock-hostent) structure for the specified host name.           |
| GETXBYYSP\_getprotobyname   | Supplies a [**protoent**](/windows/desktop/api/winsock/ns-winsock-protoent) structure for the specified protocol name.     |
| GETXBYYSP\_getprotobynumber | Supplies a [**protoent**](/windows/desktop/api/winsock/ns-winsock-protoent) structure for the specified protocol number.   |
| GETXBYYSP\_getservbyname    | Supplies a [**servent**](/windows/desktop/api/winsock/ns-winsock-servent) structure for the specified service nam.e        |
| GETXBYYSP\_getservbyport    | Supplies a [**servent**](/windows/desktop/api/winsock/ns-winsock-servent) structure for the service at the specified port. |
| GETXBYYSP\_gethostname      | Returns the standard host name for the local computer.                                   |



 

Async Style Functions



| SPI function name                   | Description                                                                              |
|-------------------------------------|------------------------------------------------------------------------------------------|
| GETXBYYSP\_WSAAsyncGetHostByAddr    | Supplies a [**hostent**](/windows/desktop/api/winsock/ns-winsock-hostent) structure for the specified host address.        |
| GETXBYYSP\_WSAAsyncGetHostByName    | Supplies a [**hostent**](/windows/desktop/api/winsock/ns-winsock-hostent) structure for the specified host name.           |
| GETXBYYSP\_WSAAsyncGetProtoByName   | Supplies a [**protoent**](/windows/desktop/api/winsock/ns-winsock-protoent) structure for the specified protocol name.     |
| GETXBYYSP\_WSAAsyncGetProtoByNumber | Supplies a [**protoent**](/windows/desktop/api/winsock/ns-winsock-protoent) structure for the specified protocol number.   |
| GETXBYYSP\_WSAAsyncGetServByName    | Supplies a [**servent**](/windows/desktop/api/winsock/ns-winsock-servent) structure for the specified service name.        |
| GETXBYYSP\_WSAAsyncGetServByPort    | Supplies a [**servent**](/windows/desktop/api/winsock/ns-winsock-servent) structure for the service at the specified port. |
| GETXBYYSP\_WSACancelAsyncRequest    | Cancels an asynchronous **GetXbyY** operation.                                           |



 

The syntax and semantics of these **GetXbyY** functions in the SPI are exactly the same as those documented in the API Specification and are, therefore, not repeated here.

The Windows Sockets 2 DLL allows exactly one service provider to offer these services. Therefore, there is no need to include pointers to these functions in the procedure table received from service providers at startup. In Windows environments the path to the DLL that implements these functions is retrieved from the value found in the following registry path. This registry entry does not exist by default:

**HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Services**\\**WinSock2**\\**Parameters**\\**GetXByYLibraryPath**

## Built-In Default GetXbyY Service Provider

A default **GetXbyY** service provider is integrated into the standard Windows Sockets 2 run-time components. This default provider implements all of the above functions, thus it is not required for these functions to be implemented by any namespace provider. However, a namespace provider is free to provide any or all of these functions (and thus override the defaults) by simply storing the string which is the path to the DLL that implements these functions in the indicated registry key. Any of the **GetXbyY** functions not exported by the named provider DLL will be supplied through the built-in defaults. Note, however, that if a provider elects to supply any of the async version of the **GetXbyY** functions, he should supply all of the async functions so that the cancel operation will work appropriately.

The current implementation of the default **GetXbyY** service provider resides within the Wsock32.dll. Depending on how the TCP/IP settings have been established through Control Panel, name resolution will occur using either DNS or local host files. When DNS is used, the default **GetXbyY** service provider uses standard Windows Sockets 1.1 API calls to communicate with the DNS server. These transactions will occur using whatever TCP/IP stack is configured as the default TCP/IP stack. Two special cases however, deserve special mention.

The default implementation of GETXBYYSP\_gethostname obtains the local host name from the registry. This will correspond to the name assigned to "My Computer". The default implementation of GETXBYYSP\_gethostbyname and GETXBYYSP\_WSAAsyncGetHostByName always compares the supplied host name with the local host name. If they match, the default implementation uses a private interface to probe the Microsoft TCP/IP stack in order to discover its local IP address. Thus, in order to be completely independent of the Microsoft TCP/IP stack, a namespace provider must implement both GETXBYYSP\_gethostbyname and GETXBYYSP\_WSAAsyncGetHostByName.

 

 



