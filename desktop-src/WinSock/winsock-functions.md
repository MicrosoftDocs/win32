---
description: The following list provides concise descriptions of each Winsock function. For additional information on any function, click the function name.
ms.assetid: edafb5f9-09fe-4f8e-9651-4002b6f622f4
title: Winsock functions
ms.topic: article
ms.date: 10/01/2019
---

# Winsock functions

The following list provides concise descriptions of each Winsock function. For additional information on any function, click the function name.

| Function | Description |
|-|-|
| [**accept**](/windows/win32/api/Winsock2/nf-winsock2-accept) | Permits an incoming connection attempt on a socket. |
| [**AcceptEx**](/windows/win32/api/mswsock/nf-mswsock-acceptex) | Accepts a new connection, returns the local and remote address, and receives the first block of data sent by the client application. |
| [**bind**](/windows/win32/api/winsock/nf-winsock-bind) | Associates a local address with a socket. |
| [**closesocket**](/windows/win32/api/winsock/nf-winsock-closesocket) | Closes an existing socket. |
| [**connect**](/windows/win32/api/Winsock2/nf-winsock2-connect) | Establishes a connection to a specified socket. |
| [**ConnectEx**](/windows/win32/api/Mswsock/nc-mswsock-lpfn_connectex) | Establishes a connection to a specified socket, and optionally sends data once the connection is established. Only supported on connection-oriented sockets. |
| [**DisconnectEx**](/previous-versions/windows/desktop/legacy/ms737757(v=vs.85)) | Closes a connection on a socket, and allows the socket handle to be reused. |
| [**EnumProtocols**](/windows/win32/api/Nspapi/nf-nspapi-enumprotocolsa) | Retrieves information about a specified set of network protocols that are active on a local host. |
| [**freeaddrinfo**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-freeaddrinfo) | Frees address information that the [**getaddrinfo**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-getaddrinfo) function dynamically allocates in [**addrinfo**](/windows/win32/api/ws2def/ns-ws2def-addrinfoa) structures. |
| [**FreeAddrInfoEx**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-freeaddrinfoex) | Frees address information that the [**GetAddrInfoEx**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-getaddrinfoexa) function dynamically allocates in [**addrinfoex**](/windows/win32/api/Ws2def/ns-ws2def-addrinfoexw) structures. |
| [**FreeAddrInfoW**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-freeaddrinfow) | Frees address information that the [**GetAddrInfoW**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-getaddrinfow) function dynamically allocates in [**addrinfoW**](/windows/win32/api/Ws2def/ns-ws2def-addrinfow) structures. |
| [**gai\_strerror**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-gai_strerrora) | Assists in printing error messages based on the EAI\_\* errors returned by the [**getaddrinfo**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-getaddrinfo) function. |
| [**GetAcceptExSockaddrs**](/windows/win32/api/mswsock/nf-mswsock-getacceptexsockaddrs) | Parses the data obtained from a call to the [**AcceptEx**](/windows/win32/api/mswsock/nf-mswsock-acceptex) function. |
| [**GetAddressByName**](/windows/win32/api/Nspapi/nf-nspapi-getaddressbynamea) | Queries a namespace, or a set of default namespaces, to retrieve network address information for a specified network service. This process is known as service name resolution. A network service can also use the function to obtain local address information that it can use with the [**bind**](/windows/win32/api/winsock/nf-winsock-bind) function. |
| [**getaddrinfo**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-getaddrinfo) | Provides protocol-independent translation from an ANSI host name to an address. |
| [**GetAddrInfoEx**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-getaddrinfoexa) | Provides protocol-independent name resolution with additional parameters to qualify which name space providers should handle the request. |
| [**GetAddrInfoExCancel**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-getaddrinfoexcancel) | Cancels an asynchronous operation by the [**GetAddrInfoEx**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-getaddrinfoexa) function. |
| [**GetAddrInfoExOverlappedResult**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-getaddrinfoexoverlappedresult) | Gets the return code for an **OVERLAPPED** structure used by an asynchronous operation for the [**GetAddrInfoEx**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-getaddrinfoexa) function. |
| [**GetAddrInfoW**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-getaddrinfow) | Provides protocol-independent translation from a Unicode host name to an address. |
| [**gethostbyaddr**](/windows/win32/api/wsipv6ok/nf-wsipv6ok-gethostbyaddr) | Retrieves the host information corresponding to a network address. |
| [**gethostbyname**](/windows/win32/api/wsipv6ok/nf-wsipv6ok-gethostbyname) | Retrieves host information corresponding to a host name from a host database. Deprecated: use [**getaddrinfo**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-getaddrinfo) instead. |
| [**gethostname**](/windows/win32/api/winsock/nf-winsock-gethostname) | Retrieves the standard host name for the local computer. |
| [**GetHostNameW**](/windows/win32/api/Winsock2/nf-winsock2-gethostnamew) | Retrieves the standard host name for the local computer as a Unicode string. |
| [**getipv4sourcefilter**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-getipv4sourcefilter) | Retrieves the multicast filter state for an IPv4 socket. |
| [**GetNameByType**](/windows/win32/api/Nspapi/nf-nspapi-getnamebytypea) | Retrieves the name of a network service for the specified service type. |
| [**getnameinfo**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-getnameinfo) | Provides name resolution from an IPv4 or IPv6 address to an ANSI host name and from a port number to the ANSI service name. |
| [**GetNameInfoW**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-getnameinfow) | Provides name resolution from an IPv4 or IPv6 address to a Unicode host name and from a port number to the Unicode service name. |
| [**getpeername**](/windows/win32/api/winsock/nf-winsock-getpeername) | Retrieves the address of the peer to which a socket is connected. |
| [**getprotobyname**](/windows/win32/api/winsock/nf-winsock-getprotobyname) | Retrieves the protocol information corresponding to a protocol name. |
| [**getprotobynumber**](/windows/win32/api/winsock/nf-winsock-getprotobynumber) | Retrieves protocol information corresponding to a protocol number. |
| [**getservbyname**](/windows/win32/api/winsock/nf-winsock-getservbyname) | Retrieves service information corresponding to a service name and protocol. |
| [**getservbyport**](/windows/win32/api/winsock/nf-winsock-getservbyport) | Retrieves service information corresponding to a port and protocol. |
| [**GetService**](/windows/win32/api/Nspapi/nf-nspapi-getservicea) | Retrieves information about a network service in the context of a set of default namespaces or a specified namespace. |
| [**getsockname**](/windows/win32/api/winsock/nf-winsock-getsockname) | Retrieves the local name for a socket. |
| [**getsockopt**](/windows/win32/api/winsock/nf-winsock-getsockopt) | Retrieves a socket option. |
| [**getsourcefilter**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-getsourcefilter) | Retrieves the multicast filter state for an IPv4 or IPv6 socket. |
| [**GetTypeByName**](/windows/win32/api/Nspapi/nf-nspapi-gettypebynamea) | Retrieves a service type GUID for a network service specified by name. |
| [**htond**](/windows/win32/api/Winsock2/nf-winsock2-htond) | Converts a **double** from host to TCP/IP network byte order (which is big-endian). |
| [**htonf**](/windows/win32/api/Winsock2/nf-winsock2-htonf) | Converts a **float** from host to TCP/IP network byte order (which is big-endian). |
| [**htonl**](/windows/win32/api/winsock/nf-winsock-htonl) | Converts a **u\_long** from host to TCP/IP network byte order (which is big-endian). |
| [**htonll**](/windows/win32/api/Winsock2/nf-winsock2-htonll) | Converts an **unsigned \_\_int64** from host to TCP/IP network byte order (which is big-endian). |
| [**htons**](/windows/win32/api/winsock/nf-winsock-htons) | Converts a **u\_short** from host to TCP/IP network byte order (which is big-endian). |
| [**inet\_addr**](/windows/win32/api/winsock2/nf-winsock2-inet_addr) | Converts a string containing an (Ipv4) Internet Protocol dotted address into a proper address for the [**in\_addr**](/windows/win32/api/winsock2/ns-winsock2-in_addr) structure. |
| [**inet\_ntoa**](/windows/win32/api/winsock2/nf-winsock2-inet_ntoa) | Converts an (IPv4) Internet network address into a string in Internet standard dotted format. |
| [**InetNtop**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-inetntopw) | converts an IPv4 or IPv6 Internet network address into a string in Internet standard format. The ANSI version of this function is [**inet\_ntop**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-inetntopw). |
| [**InetPton**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-inetptonw) | Converts an IPv4 or IPv6 Internet network address in its standard text presentation form into its numeric binary form. The ANSI version of this function is [**inet\_pton**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-inetptonw). |
| [**ioctlsocket**](/windows/win32/api/winsock/nf-winsock-ioctlsocket) | Controls the I/O mode of a socket. |
| [**listen**](/windows/win32/api/Winsock2/nf-winsock2-listen) | Places a socket a state where it is listening for an incoming connection. |
| [**ntohd**](/windows/win32/api/Winsock2/nf-winsock2-ntohd) | Converts an **unsigned \_\_int64** from TCP/IP network order to host byte order (which is little-endian on Intel processors) and returns a **double**. |
| [**ntohf**](/windows/win32/api/Winsock2/nf-winsock2-ntohf) | Converts an **unsigned \_\_int32** from TCP/IP network order to host byte order (which is little-endian on Intel processors) and returns a **float**. |
| [**ntohl**](/windows/win32/api/winsock/nf-winsock-ntohl) | Converts a u\_long from TCP/IP network order to host byte order (which is little-endian on Intel processors). |
| [**ntohll**](/windows/win32/api/Winsock2/nf-winsock2-ntohll) | Converts an **unsigned \_\_int64** from TCP/IP network order to host byte order (which is little-endian on Intel processors). |
| [**ntohs**](/windows/win32/api/winsock/nf-winsock-ntohs) | Converts a u\_short from TCP/IP network byte order to host byte order (which is little-endian on Intel processors). |
| [**recv**](/windows/win32/api/winsock/nf-winsock-recv) | Receives data from a connected or bound socket. |
| [**recvfrom**](/windows/win32/api/winsock/nf-winsock-recvfrom) | Receives a datagram and stores the source address. |
| [**RIOCloseCompletionQueue**](/previous-versions/windows/desktop/legacy/hh448837(v=vs.85)) | Closes an existing completion queue used for I/O completion notification by send and receive requests with the Winsock registered I/O extensions. |
| [**RIOCreateCompletionQueue**](/windows/win32/api/mswsock/nc-mswsock-lpfn_riodequeuecompletion) | Creates an I/O completion queue of a specific size for use with the Winsock registered I/O extensions. |
| [**RIOCreateRequestQueue**](/windows/win32/api/mswsock/nc-mswsock-lpfn_riocreaterequestqueue) | Creates a registered I/O socket descriptor using a specified socket and I/O completion queues for use with the Winsock registered I/O extensions. |
| [**RIODequeueCompletion**](/windows/win32/api/mswsock/nc-mswsock-lpfn_riodequeuecompletion) | Removes entries from an I/O completion queue for use with the Winsock registered I/O extensions. |
| [**RIODeregisterBuffer**](/windows/win32/api/mswsock/nc-mswsock-lpfn_rioderegisterbuffer) | Deregisters a registered buffer used with the Winsock registered I/O extensions. |
| [**RIONotify**](/windows/win32/api/mswsock/nc-mswsock-lpfn_rionotify) | Registers the method to use for notification behavior with an I/O completion queue for use with the Winsock registered I/O extensions. |
| [**RIOReceive**](/windows/win32/api/mswsock/nc-mswsock-lpfn_rioreceive) | Receives network data on a connected registered I/O TCP socket or a bound registered I/O UDP socket for use with the Winsock registered I/O extensions. |
| [**RIOReceiveEx**](/windows/win32/api/mswsock/nc-mswsock-lpfn_rioreceiveex) | Receives network data on a connected registered I/O TCP socket or a bound registered I/O UDP socket with additional options for use with the Winsock registered I/O extensions. |
| [**RIORegisterBuffer**](/previous-versions/windows/desktop/legacy/hh437199(v=vs.85)) | Registers a [**RIO\_BUFFERID**](rio-bufferid.md), a registered buffer descriptor, with a specified buffer for use with the Winsock registered I/O extensions. |
| [**RIOResizeCompletionQueue**](/previous-versions/windows/desktop/legacy/hh437202(v=vs.85)) | Resizes an I/O completion queue to be either larger or smaller for use with the Winsock registered I/O extensions. |
| [**RIOResizeRequestQueue**](/previous-versions/windows/desktop/legacy/hh437204(v=vs.85)) | Resizes a request queue to be either larger or smaller for use with the Winsock registered I/O extensions. |
| [**RIOSend**](/windows/win32/api/mswsock/nc-mswsock-lpfn_riosend) | Sends network data on a connected registered I/O TCP socket or a bound registered I/O UDP socket for use with the Winsock registered I/O extensions. |
| [**RIOSendEx**](/previous-versions/windows/desktop/legacy/hh437216(v=vs.85)) | Sends network data on a connected registered I/O TCP socket or a bound registered I/O UDP socket with additional options for use with the Winsock registered I/O extensions. |
| [**select**](/windows/win32/api/Winsock2/nf-winsock2-select) | Determines the status of one or more sockets, waiting if necessary, to perform synchronous I/O. |
| [**send**](/windows/win32/api/Winsock2/nf-winsock2-send) | Sends data on a connected socket. |
| [**sendto**](/windows/win32/api/winsock/nf-winsock-sendto) | Sends data to a specific destination. |
| [**SetAddrInfoEx**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-setaddrinfoexa) | Registers a host and service name along with associated addresses with a specific namespace provider. |
| [**setipv4sourcefilter**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-setipv4sourcefilter) | Sets the multicast filter state for an IPv4 socket. |
| [**SetService**](/windows/win32/api/Nspapi/nf-nspapi-setservicea) | Registers or removes from the registry a network service within one or more namespaces. Can also add or remove a network service type within one or more namespaces. |
| [**SetSocketMediaStreamingMode**](/windows/win32/api/Socketapi/nf-socketapi-setsocketmediastreamingmode) | Indicates whether the network is to be used for transferring streaming media that requires quality of service. |
| [**setsockopt**](/windows/win32/api/winsock/nf-winsock-setsockopt) | Sets a socket option. |
| [**setsourcefilter**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-setsourcefilter) | Sets the multicast filter state for an IPv4 or IPv6 socket. |
| [**shutdown**](/windows/win32/api/winsock/nf-winsock-shutdown) | Disables sends or receives on a socket. |
| [**socket**](/windows/win32/api/Winsock2/nf-winsock2-socket) | Creates a socket that is bound to a specific service provider. |
| [**TransmitFile**](/windows/win32/api/mswsock/nf-mswsock-transmitfile) | Transmits file data over a connected socket handle. |
| [**TransmitPackets**](/windows/win32/api/Mswsock/nc-mswsock-lpfn_transmitpackets) | Transmits in-memory data or file data over a connected socket. |
| [**WSAAccept**](/windows/win32/api/Winsock2/nf-winsock2-wsaaccept) | Conditionally accepts a connection based on the return value of a condition function, provides quality of service flow specifications, and allows the transfer of connection data. |
| [**WSAAddressToString**](/windows/win32/api/Winsock2/nf-winsock2-wsaaddresstostringa) | Converts all components of a [**sockaddr**](sockaddr-2.md) structure into a human-readable string representation of the address. |
| [**WSAAsyncGetHostByAddr**](/windows/win32/api/winsock/nf-winsock-wsaasyncgethostbyaddr) | Asynchronously retrieves host information that corresponds to an address. |
| [**WSAAsyncGetHostByName**](/windows/win32/api/winsock/nf-winsock-wsaasyncgethostbyname) | Asynchronously retrieves host information that corresponds to a host name. |
| [**WSAAsyncGetProtoByName**](/windows/win32/api/winsock/nf-winsock-wsaasyncgetprotobyname) | Asynchronously retrieves protocol information that corresponds to a protocol name. |
| [**WSAAsyncGetProtoByNumber**](/windows/win32/api/winsock/nf-winsock-wsaasyncgetprotobynumber) | Asynchronously retrieves protocol information that corresponds to a protocol number. |
| [**WSAAsyncGetServByName**](/windows/win32/api/winsock/nf-winsock-wsaasyncgetservbyname) | Asynchronously retrieves service information that corresponds to a service name and port. |
| [**WSAAsyncGetServByPort**](/windows/win32/api/winsock/nf-winsock-wsaasyncgetservbyport) | Asynchronously retrieves service information that corresponds to a port and protocol. |
| [**WSAAsyncSelect**](/windows/win32/api/winsock/nf-winsock-wsaasyncselect) | Requests Windows message-based notification of network events for a socket. |
| [**WSACancelAsyncRequest**](/windows/win32/api/winsock/nf-winsock-wsacancelasyncrequest) | Cancels an incomplete asynchronous operation. |
| [**WSACleanup**](/windows/win32/api/winsock/nf-winsock-wsacleanup) | Terminates use of the Ws2\_32.DLL. |
| [**WSACloseEvent**](/windows/win32/api/Winsock2/nf-winsock2-wsacloseevent) | Closes an open event object handle. |
| [**WSAConnect**](/windows/win32/api/Winsock2/nf-winsock2-wsaconnect) | Establishes a connection to another socket application, exchanges connect data, and specifies needed quality of service based on the specified [**FLOWSPEC**](/windows/win32/api/qos/ns-qos-flowspec) structure. |
| [**WSAConnectByList**](/windows/win32/api/Winsock2/nf-winsock2-wsaconnectbylist) | Establishes a connection to one out of a collection of possible endpoints represented by a set of destination addresses (host names and ports). |
| [**WSAConnectByName**](/windows/win32/api/Winsock2/nf-winsock2-wsaconnectbynamea) | Establishes a connection to another socket application on a specified host and port |
| [**WSACreateEvent**](/windows/win32/api/Winsock2/nf-winsock2-wsacreateevent) | Creates a new event object. |
| [**WSADeleteSocketPeerTargetName**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-wsadeletesocketpeertargetname) | Removes the association between a peer target name and an IP address for a socket. |
| [**WSADuplicateSocket**](/windows/win32/api/Winsock2/nf-winsock2-wsaduplicatesocketa) | Returns a structure that can be used to create a new socket descriptor for a shared socket. |
| [**WSAEnumNameSpaceProviders**](/windows/win32/api/Winsock2/nf-winsock2-wsaenumnamespaceprovidersa) | Retrieves information about available namespaces. |
| [**WSAEnumNameSpaceProvidersEx**](/windows/win32/api/Winsock2/nf-winsock2-wsaenumnamespaceprovidersexa) | Retrieves information about available namespaces. |
| [**WSAEnumNetworkEvents**](/windows/win32/api/Winsock2/nf-winsock2-wsaenumnetworkevents) | Discovers occurrences of network events for the indicated socket, clear internal network event records, and reset event objects (optional). |
| [**WSAEnumProtocols**](/windows/win32/api/Winsock2/nf-winsock2-wsaenumprotocolsa) | Retrieves information about available transport protocols. |
| [**WSAEventSelect**](/windows/win32/api/Winsock2/nf-winsock2-wsaeventselect) | Specifies an event object to be associated with the specified set of FD\_XXX network events. |
| [**\_\_WSAFDIsSet**](/windows/win32/api/winsock/nf-winsock-__wsafdisset) | Specifies whether a socket is included in a set of socket descriptors. |
| [**WSAGetFailConnectOnIcmpError**](/windows/win32/api/ws2tcpip/nf-ws2tcpip-wsagetfailconnectonicmperror) | Queries the state of the [**TCP_FAIL_CONNECT_ON_ICMP_ERROR**](./ipproto-tcp-socket-options.md) socket option. |
| [**WSAGetIcmpErrorInfo**](/windows/win32/api/ws2tcpip/nf-ws2tcpip-wsageticmperrorinfo) | Queries the source address of an ICMP error received on a TCP socket during connection setup. |
| [**WSAGetIPUserMtu**](/windows/win32/api/ws2tcpip/nf-ws2tcpip-wsagetipusermtu) | Retrieves the user-defined IP layer MTU for a socket. |
| [**WSAGetLastError**](/windows/win32/api/winsock/nf-winsock-wsagetlasterror) | Returns the error status for the last operation that failed. |
| [**WSAGetOverlappedResult**](/windows/win32/api/Winsock2/nf-winsock2-wsagetoverlappedresult) | Retrieves the results of an overlapped operation on the specified socket. |
| [**WSAGetQOSByName**](/windows/win32/api/Winsock2/nf-winsock2-wsagetqosbyname) | Initializes a [**QOS**](/windows/win32/api/winsock2/ns-winsock2-qos) structure based on a named template, or it supplies a buffer to retrieve an enumeration of the available template names. |
| [**WSAGetServiceClassInfo**](/windows/win32/api/Winsock2/nf-winsock2-wsagetserviceclassinfoa) | Retrieves the class information (schema) pertaining to a specified service class from a specified namespace provider. |
| [**WSAGetServiceClassNameByClassId**](/windows/win32/api/Winsock2/nf-winsock2-wsagetserviceclassnamebyclassida) | Retrieves the name of the service associated with the specified type. |
| [**WSAGetUdpRecvMaxCoalescedSize**](/windows/win32/api/ws2tcpip/nf-ws2tcpip-wsagetudprecvmaxcoalescedsize) | Retrieves the maximum size of a received, coalesced message for a UDP socket. |
| [**WSAGetUdpSendMessageSize**](/windows/win32/api/ws2tcpip/nf-ws2tcpip-wsagetudpsendmessagesize) | Retrieves the segmentation message size for a UDP socket. |
| [**WSAHtonl**](/windows/win32/api/Winsock2/nf-winsock2-wsahtonl) | Converts a u\_long from host byte order to network byte order. |
| [**WSAHtons**](/windows/win32/api/Winsock2/nf-winsock2-wsahtons) | Converts a u\_short from host byte order to network byte order. |
| [**WSAImpersonateSocketPeer**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-wsaimpersonatesocketpeer) | Used to impersonate the security principal corresponding to a socket peer in order to perform application-level authorization. |
| [**WSAInstallServiceClass**](/windows/win32/api/Winsock2/nf-winsock2-wsainstallserviceclassa) | Registers a service class schema within a namespace. |
| [**WSAIoctl**](/windows/win32/api/Winsock2/nf-winsock2-wsaioctl) | Controls the mode of a socket. |
| [**WSAJoinLeaf**](/windows/win32/api/Winsock2/nf-winsock2-wsajoinleaf) | Joins a leaf node into a multipoint session, exchanges connect data, and specifies needed quality of service based on the specified structures. |
| [**WSALookupServiceBegin**](/windows/win32/api/Winsock2/nf-winsock2-wsalookupservicebegina) | Initiates a client query that is constrained by the information contained within a [**WSAQUERYSET**](/windows/win32/api/Winsock2/ns-winsock2-wsaquerysetw) structure. |
| [**WSALookupServiceEnd**](/windows/win32/api/Winsock2/nf-winsock2-wsalookupserviceend) | Frees the handle used by previous calls to [**WSALookupServiceBegin**](/windows/win32/api/Winsock2/nf-winsock2-wsalookupservicebegina) and [**WSALookupServiceNext**](/windows/win32/api/Winsock2/nf-winsock2-wsalookupservicenexta). |
| [**WSALookupServiceNext**](/windows/win32/api/Winsock2/nf-winsock2-wsalookupservicenexta) | Retrieve the requested service information. |
| [**WSANSPIoctl**](/windows/win32/api/Winsock2/nf-winsock2-wsanspioctl) | Developers to make I/O control calls to a registered namespace. |
| [**WSANtohl**](/windows/win32/api/Winsock2/nf-winsock2-wsantohl) | Converts a u\_long from network byte order to host byte order. |
| [**WSANtohs**](/windows/win32/api/Winsock2/nf-winsock2-wsantohs) | Converts a u\_short from network byte order to host byte order. |
| [**WSAPoll**](/windows/win32/api/winsock2/nf-winsock2-wsapoll) | Determines status of one or more sockets. |
| [**WSAProviderConfigChange**](/windows/win32/api/Winsock2/nf-winsock2-wsaproviderconfigchange) | Notifies the application when the provider configuration is changed. |
| [**WSAQuerySocketSecurity**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-wsaquerysocketsecurity) | Queries information about the security applied to a connection on a socket. |
| [**WSARecv**](/windows/win32/api/Winsock2/nf-winsock2-wsarecv) | Receives data from a connected socket. |
| [**WSARecvDisconnect**](/windows/win32/api/Winsock2/nf-winsock2-wsarecvdisconnect) | Terminates reception on a socket, and retrieves the disconnect data if the socket is connection oriented. |
| [**WSARecvEx**](/windows/win32/api/mswsock/nf-mswsock-wsarecvex) | Receives data from a connected socket. |
| [**WSARecvFrom**](/windows/win32/api/Winsock2/nf-winsock2-wsarecvfrom) | Receives a datagram and stores the source address. |
| [**LPFN_WSARECVMSG (WSARecvMsg)**](/windows/win32/api/mswsock/nc-mswsock-lpfn_wsarecvmsg) | Receives data and optional control information from connected and unconnected sockets. |
| [**WSARemoveServiceClass**](/windows/win32/api/Winsock2/nf-winsock2-wsaremoveserviceclass) | Permanently removes the service class schema from the registry. |
| [**WSAResetEvent**](/windows/win32/api/Winsock2/nf-winsock2-wsaresetevent) | Resets the state of the specified event object to nonsignaled. |
| [**WSARevertImpersonation**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-wsarevertimpersonation) | Terminates the impersonation of a socket peer. |
| [**WSASend**](/windows/win32/api/Winsock2/nf-winsock2-wsasend) | Sends data on a connected socket. |
| [**WSASendDisconnect**](/windows/win32/api/Winsock2/nf-winsock2-wsasenddisconnect) | Initiates termination of the connection for the socket and sends disconnect data. |
| [**WSASendMsg**](/windows/win32/api/winsock2/nf-winsock2-wsasendmsg) | Sends data and optional control information from connected and unconnected sockets. |
| [**WSASendTo**](/windows/win32/api/Winsock2/nf-winsock2-wsasendto) | Sends data to a specific destination, using overlapped I/O where applicable. |
| [**WSASetEvent**](/windows/win32/api/Winsock2/nf-winsock2-wsasetevent) | Sets the state of the specified event object to signaled. |
| [**WSASetFailConnectOnIcmpError**](/windows/win32/api/ws2tcpip/nf-ws2tcpip-wsasetfailconnectonicmperror) | Sets the state of the [**TCP_FAIL_CONNECT_ON_ICMP_ERROR**](./ipproto-tcp-socket-options.md) socket option. |
| [**WSASetIPUserMtu**](/windows/win32/api/ws2tcpip/nf-ws2tcpip-wsasetipusermtu) | Sets the user-defined IP layer MTU on a socket. |
| [**WSASetLastError**](/windows/win32/api/winsock/nf-winsock-wsasetlasterror) | Sets the error code. |
| [**WSASetService**](/windows/win32/api/Winsock2/nf-winsock2-wsasetservicea) | Registers or removes from the registry a service instance within one or more namespaces. |
| [**WSASetSocketPeerTargetName**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-wsasetsocketpeertargetname) | Used to specify the peer target name (SPN) that corresponds to a peer IP address. This target name is meant to be specified by client applications to securely identify the peer that should be authenticated. |
| [**WSASetSocketSecurity**](/windows/win32/api/Ws2tcpip/nf-ws2tcpip-wsasetsocketsecurity) | Enables and applies security for a socket. |
| [**WSASetUdpRecvMaxCoalescedSize**](/windows/win32/api/ws2tcpip/nf-ws2tcpip-wsasetudprecvmaxcoalescedsize) | Sets the maximum size of a coalesced message set on a UDP socket. |
| [**WSASetUdpSendMessageSize**](/windows/win32/api/ws2tcpip/nf-ws2tcpip-wsasetudpsendmessagesize) | Sets the segmentation message size on a UDP socket. |
| [**WSASocket**](/windows/win32/api/Winsock2/nf-winsock2-wsasocketa) | Creates a socket that is bound to a specific transport-service provider. |
| [**WSAStartup**](/windows/win32/api/winsock/nf-winsock-wsastartup) | Initiates use of WS2\_32.DLL by a process. |
| [**WSAStringToAddress**](/windows/win32/api/Winsock2/nf-winsock2-wsastringtoaddressa) | Converts a numeric string to a [**sockaddr**](sockaddr-2.md) structure. |
| [**WSAWaitForMultipleEvents**](/windows/win32/api/Winsock2/nf-winsock2-wsawaitformultipleevents) | Returns either when one or all of the specified event objects are in the signaled state, or when the time-out interval expires. |
