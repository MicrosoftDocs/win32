---
description: Developing a secure high-level network infrastructure is a priority for most network application developers. However, socket security is often overlooked despite being very critical when considering a fully secure solution.
ms.assetid: b37a3e33-65ee-43b1-bc8b-3280db7ebee4
title: Using SO_REUSEADDR and SO_EXCLUSIVEADDRUSE
ms.topic: article
ms.date: 05/31/2018
---

# Using SO\_REUSEADDR and SO\_EXCLUSIVEADDRUSE

Developing a secure high-level network infrastructure is a priority for most network application developers. However, socket security is often overlooked despite being very critical when considering a fully secure solution. Socket security, specifically, deals with processes that bind to the same port previously bound by another application process. In the past, it was possible for a network application to "hijack" the port of another application, which could easily lead to a "denial of service" attack or data theft.

In general, socket security applies to server-side processes. More specifically, socket security applies to any network application that accepts connections and receives IP datagram traffic. These applications typically bind to a well-known port and are common targets for malicious network code.

Client applications are less likely to be the targets of such attacks — not because they are less susceptible, but because most clients bind to "ephemeral" local ports rather than static "service" ports. Client network applications should always bind to ephemeral ports (by specifying port 0 in the [**SOCKADDR**](sockaddr-2.md) structure pointed to by the *name* parameter when calling the [**bind**](/windows/win32/api/winsock/nf-winsock-bind) function) unless there is a compelling architectural reason not to. The ephemeral local ports consist of ports greater than port 49151. Most server applications for dedicated services bind to a well-known reserved port that is less than or equal to port 49151. So for most applications, there is not usually a conflict for bind requests between client and server applications.

This section describes the default level of security on various Microsoft Windows platforms and how the specific socket options **SO\_REUSEADDR** and [SO\_EXCLUSIVEADDRUSE](so-exclusiveaddruse.md) impact and affect network application security. An additional feature called enhanced socket security is available on Windows Server 2003 and later. The availability of these socket options and enhanced socket security varies across versions of Microsoft operating systems, as shown in the table below.

| Platform            | SO\_REUSEADDR | SO\_EXCLUSIVEADDRUSE                  | Enhanced socket security |
|---------------------|---------------|---------------------------------------|--------------------------|
| Windows 95          | Available     | Not Available                         | Not Available            |
| Windows 98          | Available     | Not Available                         | Not Available            |
| Windows Me          | Available     | Not Available                         | Not Available            |
| Windows NT 4.0      | Available     | Available in Service Pack 4 and later | Not Available            |
| Windows 2000        | Available     | Available                             | Not Available            |
| Windows XP          | Available     | Available                             | Not Available            |
| Windows Server 2003 | Available     | Available                             | Available                |
| Windows Vista       | Available     | Available                             | Available                |
| Windows Server 2008 | Available     | Available                             | Available                |
| Windows 7and newer  | Available     | Available                             | Available                |

## Using SO\_REUSEADDR

The **SO\_REUSEADDR** socket option allows a socket to forcibly bind to a port in use by another socket. The second socket calls [**setsockopt**](/windows/win32/api/winsock/nf-winsock-setsockopt) with the *optname* parameter set to **SO\_REUSEADDR** and the *optval* parameter set to a boolean value of **TRUE** before calling [**bind**](/windows/win32/api/winsock/nf-winsock-bind) on the same port as the original socket. Once the second socket has successfully bound, the behavior for all sockets bound to that port is indeterminate. For example, if all of the sockets on the same port provide TCP service, any incoming TCP connection requests over the port cannot be guaranteed to be handled by the correct socket — the behavior is non-deterministic. A malicious program can use **SO\_REUSEADDR** to forcibly bind sockets already in use for standard network protocol services in order to deny access to those service. No special privileges are required to use this option.

If a client application binds to a port before a server application is able to bind to the same port, then problems may result. If the server application forcibly binds using the **SO\_REUSEADDR** socket option to the same port, then the behavior for all sockets bound to that port is indeterminate.

The exception to this non-deterministic behavior is multicast sockets. If two sockets are bound to the same interface and port and are members of the same multicast group, data will be delivered to both sockets, rather than an arbitrarily chosen one.

## Using SO\_EXCLUSIVEADDRUSE

Before the **SO\_EXCLUSIVEADDRUSE** socket option was introduced, there was very little a network application developer could do to prevent a malicious program from binding to the port on which the network application had its own sockets bound. In order to address this security issue, Windows Sockets introduced the **SO\_EXCLUSIVEADDRUSE** socket option, which became available on Windows NT 4.0 with Service Pack 4 (SP4) and later.

The **SO\_EXCLUSIVEADDRUSE** socket option can only be used by members of the Administrators security group on Windows XP and earlier. The reasons why this requirement was changed on Windows Server 2003 and later are discussed later in the article.

The **SO\_EXCLUSIVEADDRUSE** option is set by calling the [**setsockopt**](/windows/win32/api/winsock/nf-winsock-setsockopt) function with the *optname* parameter set to **SO\_EXCLUSIVEADDRUSE** and the *optval* parameter set to a boolean value of **TRUE** before the socket is bound. After the option is set, the behavior of subsequent [**bind**](/windows/win32/api/winsock/nf-winsock-bind) calls differs depending on the network address specified in each **bind** call.

The table below describes the behavior that occurs in Windows XP and earlier when a second socket attempts to bind to an address previously bound to by a first socket using specific socket options.

> [!NOTE]  
> In the table below, "wildcard" denotes the wildcard address for the given protocol (such as "0.0.0.0" for IPv4 and "::" for IPv6). "Specific" denotes a specific IP address assigned an interface. The table cells indicate whether or not the bind is successful ("Success") or an error is returned ("INUSE" for the [WSAEADDRINUSE](windows-sockets-error-codes-2.md) error; "ACCESS" for the [WSAEACCES](windows-sockets-error-codes-2.md) error).

<table>
    <tr>
        <td bgcolor="#C0C0C0" colspan="2" rowspan="3">First <a href="/windows/win32/api/winsock/nf-winsock-bind"><strong>bind</strong></a> call</td>
        <td bgcolor="#C0C0C0" colspan="6">Second <a href="/windows/win32/api/winsock/nf-winsock-bind"><strong>bind</strong></a> call</td>
    </tr>
    <tr>
        <td bgcolor="#C0C0C0" colspan="2">Default</td>
        <td bgcolor="#C0C0C0" colspan="2">SO_REUSEADDR</td>
        <td bgcolor="#C0C0C0" colspan="2">SO_EXCLUSIVEADDRUSE</td>
    </tr>
    <tr>
        <td bgcolor="#C0C0C0">Wildcard</td>
        <td bgcolor="#C0C0C0">Specific</td>
        <td bgcolor="#C0C0C0">Wildcard</td>
        <td bgcolor="#C0C0C0">Specific</td>
        <td bgcolor="#C0C0C0">Wildcard</td>
        <td bgcolor="#C0C0C0">Specific</td>
    </tr>
    <tr>
        <td bgcolor="#C0C0C0" rowspan="2">Default</td>
        <td bgcolor="#C0C0C0">Wildcard</td>
        <td>INUSE</td>
        <td>INUSE</td>
        <td>Success</td>
        <td>Success</td>
        <td>INUSE</td>
        <td>INUSE</td>
    </tr>
    <tr>
        <td bgcolor="#C0C0C0">Specific</td>
        <td>INUSE</td>
        <td>INUSE</td>
        <td>Success</td>
        <td>Success</td>
        <td>INUSE</td>
        <td>INUSE</td>
    </tr>
    <tr>
        <td bgcolor="#C0C0C0" rowspan="2">SO_REUSEADDR</td>
        <td bgcolor="#C0C0C0">Wildcard</td>
        <td>INUSE</td>
        <td>INUSE</td>
        <td>Success</td>
        <td>Success</td>
        <td>INUSE</td>
        <td>INUSE</td>
    </tr>
    <tr>
        <td bgcolor="#C0C0C0">Specific</td>
        <td>INUSE</td>
        <td>INUSE</td>
        <td>Success</td>
        <td>Success</td>
        <td>INUSE</td>
        <td>INUSE</td>
    </tr>
    <tr>
        <td bgcolor="#C0C0C0" rowspan="2">SO_EXCLUSIVEADDRUSE</td>
        <td bgcolor="#C0C0C0">Wildcard</td>
        <td>INUSE</td>
        <td>INUSE</td>
        <td>ACCESS</td>
        <td>ACCESS</td>
        <td>INUSE</td>
        <td>INUSE</td>
    </tr>
    <tr>
        <td bgcolor="#C0C0C0">Specific</td>
        <td>INUSE</td>
        <td>INUSE</td>
        <td>ACCESS</td>
        <td>ACCESS</td>
        <td>INUSE</td>
        <td>INUSE</td>
    </tr>
</table>

When two sockets are bound to the same port number but on different explicit interfaces, there is no conflict. For example, in the case where a computer has two IP interfaces, 10.0.0.1 and 10.99.99.99, if the first call to [**bind**](/windows/win32/api/winsock/nf-winsock-bind) is on 10.0.0.1 with the port set to 5150 and **SO\_EXCLUSIVEADDRUSE** specified, then a second call to **bind** on 10.99.99.99 with the port also set to 5150 and no options specified will succeed. However, if the first socket is bound to the wildcard address and port 5150, then any subsequent bind call to port 5150 with **SO\_EXCLUSIVEADDRUSE** set will fail with either [WSAEADDRINUSE](windows-sockets-error-codes-2.md) or [WSAEACCES](windows-sockets-error-codes-2.md) returned by the **bind** operation.

In the case where the first call to [**bind**](/windows/win32/api/winsock/nf-winsock-bind) sets either **SO\_REUSEADDR** or no socket options at all, the second **bind** call will "hijack" the port and the application will be unable to determine which of the two sockets received specific packets sent to the "shared" port.

A typical application that calls the [**bind**](/windows/win32/api/winsock/nf-winsock-bind) function does not allocate the bound socket for exclusive use, unless the **SO\_EXCLUSIVEADDRUSE** socket option is called on the socket before the call to the **bind** function. If a client application binds to an ephemeral port or a specific port before a server application binds to the same port, then problems can result. The server application can forcibly bind to the same port by using the **SO\_REUSEADDR** socket option on the socket before calling the **bind** function, but the behavior for all sockets bound to that port is then indeterminate. If the server application tries to use the **SO\_EXCLUSIVEADDRUSE** socket option for exclusive use of the port, the request will fail.

Conversely, a socket with the **SO\_EXCLUSIVEADDRUSE** set cannot necessarily be reused immediately after socket closure. For example, if a listening socket with **SO\_EXCLUSIVEADDRUSE** set accepts a connection and is then subsequently closed, another socket (also with **SO\_EXCLUSIVEADDRUSE**) cannot bind to the same port as the first socket until the original connection becomes inactive.

This issue can become complicated because the underlying transport protocol may not terminate the connection even though the socket has been closed. Even after the socket has been closed by the application, the system must transmit any buffered data, send a graceful disconnect message to the peer, and wait for a corresponding graceful disconnect message from the peer. It is possible that the underlying transport protocol might never release the connection; for example, the peer participating in the original connection might advertise a zero-size window, or some other form of "attack" configuration. In such a case, the client connection remains in an active state despite the request to close it, since unacknowledged data remains in the buffer.

To avoid this situation, network applications should ensure a graceful shutdown by calling [**shutdown**](/windows/win32/api/winsock/nf-winsock-shutdown) with the SD\_SEND flag set, and then wait in a [**recv**](/windows/win32/api/winsock/nf-winsock-recv) loop until zero bytes are returned over the connection. This guarantees that all data is received by the peer and likewise confirms with the peer that it has received all of the transmitted data, as well as avoiding the aforementioned port reuse issue.

The SO\_LINGER socket option may be set on a socket to prevent the port from transitioning to an "active" wait state; however, this is discouraged as it can lead to desired effects, such as reset connections. For example, if data is received by the peer but remains unacknowledged by it, and the local computer closes the socket with SO\_LINGER set on it, the connection between the two computers is reset and the unacknowledged data discarded by the peer. Picking a suitable time to linger is difficult as a smaller timeout value often results in suddenly aborted connections, whereas larger timeout values leave the system vulnerable to denial-of-service attacks (by establishing many connections and potentially stalling/blocking application threads). Closing a socket that has a nonzero linger timeout value may also cause the [**closesocket**](/windows/win32/api/winsock/nf-winsock-closesocket) call to block.

## Enhanced Socket Security

Enhanced socket security was added with the release of Windows Server 2003. In previous Microsoft server operating system releases, the default socket security easily allowed processes to hijack ports from unsuspecting applications. In Windows Server 2003, sockets are not in a sharable state by default. Therefore, if an application wants to allow other processes to reuse a port on which a socket is already bound, it must specifically enable it. If that is the case, the first socket to call [**bind**](/windows/win32/api/winsock/nf-winsock-bind) on the port must have **SO\_REUSEADDR** set on the socket. The only exception to this case occurs when the second **bind** call is performed by the same user account that made the original call to **bind**. This exception exists solely to provide backward compatibility.

The table below describes the behavior that occurs in Windows Server 2003 and later operating systems when a second socket attempts to bind to an address previously bound to by a first socket using specific socket options.

> [!NOTE]
> In the table below, "wildcard" denotes the wildcard address for the given protocol (such as "0.0.0.0" for IPv4 and "::" for IPv6). "Specific" denotes a specific IP address assigned an interface. The table cells indicate whether or not the bind is successful ("Success") or the error returned ("INUSE" for the [WSAEADDRINUSE](windows-sockets-error-codes-2.md) error; "ACCESS" for the [WSAEACCES](windows-sockets-error-codes-2.md) error).
>
> Also note that in this specific table, both [**bind**](/windows/win32/api/winsock/nf-winsock-bind) calls are made under the same user account.

<table>
    <tr>
        <td bgcolor="#C0C0C0" colspan="2" rowspan="3">First <a href="/windows/win32/api/winsock/nf-winsock-bind"><strong>bind</strong></a> call</td>
        <td bgcolor="#C0C0C0" colspan="6">Second <a href="/windows/win32/api/winsock/nf-winsock-bind"><strong>bind</strong></a> call</td>
    </tr>
    <tr>
        <td bgcolor="#C0C0C0" colspan="2">Default</td>
        <td bgcolor="#C0C0C0" colspan="2">SO_REUSEADDR</td>
        <td bgcolor="#C0C0C0" colspan="2">SO_EXCLUSIVEADDRUSE</td>
    </tr>
    <tr>
        <td bgcolor="#C0C0C0">Wildcard</td>
        <td bgcolor="#C0C0C0">Specific</td>
        <td bgcolor="#C0C0C0">Wildcard</td>
        <td bgcolor="#C0C0C0">Specific</td>
        <td bgcolor="#C0C0C0">Wildcard</td>
        <td bgcolor="#C0C0C0">Specific</td>
    </tr>
    <tr>
        <td bgcolor="#C0C0C0" rowspan="2">Default</td>
        <td bgcolor="#C0C0C0">Wildcard</td>
        <td>INUSE</td>
        <td>Success</td>
        <td>ACCESS</td>
        <td>Success</td>
        <td>INUSE</td>
        <td>Success</td>
    </tr>
    <tr>
        <td bgcolor="#C0C0C0">Specific</td>
        <td>Success</td>
        <td>INUSE</td>
        <td>Success</td>
        <td>ACCESS</td>
        <td>INUSE</td>
        <td>INUSE</td>
    </tr>
    <tr>
        <td bgcolor="#C0C0C0" rowspan="2">SO_REUSEADDR</td>
        <td bgcolor="#C0C0C0">Wildcard</td>
        <td>INUSE</td>
        <td>Success</td>
        <td>Success</td>
        <td>Success</td>
        <td>INUSE</td>
        <td>Success</td>
    </tr>
    <tr>
        <td bgcolor="#C0C0C0">Specific</td>
        <td>Success</td>
        <td>INUSE</td>
        <td>Success</td>
        <td>Success</td>
        <td>INUSE</td>
        <td>INUSE</td>
    </tr>
    <tr>
        <td bgcolor="#C0C0C0" rowspan="2">SO_EXCLUSIVEADDRUSE</td>
        <td bgcolor="#C0C0C0">Wildcard</td>
        <td>INUSE</td>
        <td>ACCESS</td>
        <td>ACCESS</td>
        <td>ACCESS</td>
        <td>INUSE</td>
        <td>ACCESS</td>
    </tr>
    <tr>
        <td bgcolor="#C0C0C0">Specific</td>
        <td>Success</td>
        <td>INUSE</td>
        <td>Success</td>
        <td>ACCESS</td>
        <td>INUSE</td>
        <td>INUSE</td>
    </tr>
</table>

A few entries in the table above merit explanation.

For example, if the first caller sets **SO\_EXCLUSIVEADDRUSE** on a specific address, and second caller attempts to call [**bind**](/windows/win32/api/winsock/nf-winsock-bind) with a wildcard address on the same port, the second **bind** call will succeed. In this particular case, the second caller is bound to all interfaces except the specific address to which the first caller is bound. Note that the reverse of this case is not true: if the first caller sets **SO\_EXCLUSIVEADDRUSE** and calls **bind** with the wildcard flag, the second caller is not able to call **bind** with the same port.

The socket binding behavior changes when the socket bind calls are made under different user accounts. The table below specifies the behavior that occurs in Windows Server 2003 and later operating systems when a second socket attempts to bind to an address previously bound to by a first socket using specific socket options and a different user account.

<table>
    <tr>
        <td bgcolor="#C0C0C0" colspan="2" rowspan="3">First <a href="/windows/win32/api/winsock/nf-winsock-bind"><strong>bind</strong></a> call</td>
        <td bgcolor="#C0C0C0" colspan="6">Second <a href="/windows/win32/api/winsock/nf-winsock-bind"><strong>bind</strong></a> call</td>
    </tr>
    <tr>
        <td bgcolor="#C0C0C0" colspan="2">Default</td>
        <td bgcolor="#C0C0C0" colspan="2">SO_REUSEADDR</td>
        <td bgcolor="#C0C0C0" colspan="2">SO_EXCLUSIVEADDRUSE</td>
    </tr>
    <tr>
        <td bgcolor="#C0C0C0">Wildcard</td>
        <td bgcolor="#C0C0C0">Specific</td>
        <td bgcolor="#C0C0C0">Wildcard</td>
        <td bgcolor="#C0C0C0">Specific</td>
        <td bgcolor="#C0C0C0">Wildcard</td>
        <td bgcolor="#C0C0C0">Specific</td>
    </tr>
    <tr>
        <td bgcolor="#C0C0C0" rowspan="2">Default</td>
        <td bgcolor="#C0C0C0">Wildcard</td>
        <td>INUSE</td>
        <td>ACCESS</td>
        <td>ACCESS</td>
        <td>ACCESS</td>
        <td>INUSE</td>
        <td>ACCESS</td>
    </tr>
    <tr>
        <td bgcolor="#C0C0C0">Specific</td>
        <td>Success</td>
        <td>INUSE</td>
        <td>Success</td>
        <td>ACCESS</td>
        <td>INUSE</td>
        <td>INUSE</td>
    </tr>
    <tr>
        <td bgcolor="#C0C0C0" rowspan="2">SO_REUSEADDR</td>
        <td bgcolor="#C0C0C0">Wildcard</td>
        <td>INUSE</td>
        <td>ACCESS</td>
        <td>Success</td>
        <td>Success</td>
        <td>INUSE</td>
        <td>ACCESS</td>
    </tr>
    <tr>
        <td bgcolor="#C0C0C0">Specific</td>
        <td>Success</td>
        <td>INUSE</td>
        <td>Success</td>
        <td>Success</td>
        <td>INUSE</td>
        <td>INUSE</td>
    </tr>
    <tr>
        <td bgcolor="#C0C0C0" rowspan="2">SO_EXCLUSIVEADDRUSE</td>
        <td bgcolor="#C0C0C0">Wildcard</td>
        <td>INUSE</td>
        <td>ACCESS</td>
        <td>ACCESS</td>
        <td>ACCESS</td>
        <td>INUSE</td>
        <td>ACCESS</td>
    </tr>
    <tr>
        <td bgcolor="#C0C0C0">Specific</td>
        <td>Success</td>
        <td>INUSE</td>
        <td>Success</td>
        <td>ACCESS</td>
        <td>INUSE</td>
        <td>INUSE</td>
    </tr>
</table>

Note that the default behavior is different when the [**bind**](/windows/win32/api/winsock/nf-winsock-bind) calls are made under different user accounts. If the first caller does not set any options on the socket and binds to the wildcard address, then the second caller cannot set the **SO\_REUSEADDR** option and successfully bind to the same port. The default behavior with no options set returns an error, as well.

On Windows Vista and later, a dual stack socket can be created which operates over both IPv6 and IPv4. When a dual stack socket is bound to the wildcard address, the given port is reserved on both the IPv4 and IPv6 networking stacks and the checks associated with **SO\_REUSEADDR** and **SO\_EXCLUSIVEADDRUSE** (if set) are made. These checks must succeed on both networking stacks. For example, if a dual stack TCP socket sets **SO\_EXCLUSIVEADDRUSE** and then tries to bind to port 5000, then no other TCP socket can be previously bound to port 5000 (either wildcard or specific). In this case if an IPv4 TCP socket was previously bound to the loopback address on port 5000, the [**bind**](/windows/win32/api/winsock/nf-winsock-bind) call for the dual stack socket would fail with [WSAEACCES](windows-sockets-error-codes-2.md).

## Application Strategies

When developing network application that operate at the socket layer, it is important to consider the type of socket security necessary. Client applications — applications that connect or send data to a service — rarely require any additional steps since they bind to a random local (ephemeral) port. If the client does require a specific local port binding in order to function correctly, then you must consider socket security.

The **SO\_REUSEADDR** option has very few uses in normal applications aside from multicast sockets where data is delivered to all of the sockets bound on the same port. Otherwise, any application that sets this socket option should be redesigned to remove the dependency since it is eminently vulnerable to "socket hijacking". As long as **SO\_REUSEADDR** socket option can be used to potentially hijack a port in a server application, the application must be considered to be not secure.

All server applications must set **SO\_EXCLUSIVEADDRUSE** for a strong level of socket security. Not only does it prevent malicious software from hijacking the port, but it also indicates whether or not another application is bound to the requested port. For example, a call to [**bind**](/windows/win32/api/winsock/nf-winsock-bind) on the wildcard address by a process with the **SO\_EXCLUSIVEADDRUSE** socket option set will fail if another process is currently bound to the same port on a specific interface.

Lastly, even though socket security has been improved in Windows Server 2003, an application should always set the **SO\_EXCLUSIVEADDRUSE** socket option to ensure that it binds to all the specific interfaces the process has requested. The socket security in Windows Server 2003 adds an increased level of security for legacy applications, but application developers must still design their products with all aspects of security in mind.
