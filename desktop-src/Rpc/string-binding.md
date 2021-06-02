---
title: String Binding
description: The string binding is an unsigned character string composed of strings that represent the binding object UUID, the RPC protocol sequence, the network address, and the endpoint and endpoint options.
ms.assetid: 5e55ddd0-d71c-42ef-90cc-dd1f0b9ed305
ms.topic: article
ms.date: 05/31/2018
---

# String Binding

The string binding is an unsigned character string composed of strings that represent the binding object UUID, the RPC protocol sequence, the network address, and the endpoint and endpoint options.

*ObjectUUID*@*ProtocolSequence*:*NetworkAddress*\[*Endpoint*,*Option*\]

## Parameters

<dl> <dt>

<span id="ObjectUUID"></span><span id="objectuuid"></span><span id="OBJECTUUID"></span>*ObjectUUID*
</dt> <dd>

[UUID](/windows/desktop/Midl/uuid) of the object operated on by the remote procedure call. At the server, the RPC run-time library maps the object type to a manager entry-point vector (an array of function pointers) to invoke the correct manager routine. For a discussion of how to map object UUIDs to manager entry-point vectors, see [Registering Interfaces](registering-interfaces.md).

</dd> <dt>

<span id="ProtocolSequence"></span><span id="protocolsequence"></span><span id="PROTOCOLSEQUENCE"></span>*ProtocolSequence*
</dt> <dd>

Character string that represents a valid combination of an RPC protocol (such as ncacn), a transport protocol (such as TCP), and a network protocol (such as IP). Microsoft RPC supports the following protocols specified in [Protocol Sequence Constants](protocol-sequence-constants.md).

</dd> <dt>

<span id="NetworkAddress"></span><span id="networkaddress"></span><span id="NETWORKADDRESS"></span>*NetworkAddress*
</dt> <dd>

Network address of the system to receive remote procedure calls.

> [!Note]  
> The following protocol sequences are not supported as of Windows XP:

 

-   [ncacn\_nb\_tcp](/windows/desktop/Midl/ncacn-nb-tcp)
-   [ncacn\_nb\_nb](/windows/desktop/Midl/ncacn-nb-nb)
-   [ncacn\_nb\_ipx](/windows/desktop/Midl/ncacn-nb-ipx)
-   [ncacn\_dnet\_nsp](/windows/desktop/Midl/ncacn-dnet-nsp)
-   [ncacn\_vns\_spp](/windows/desktop/Midl/ncacn-vns-spp)
-   [ncadg\_mq](/windows/desktop/Midl/ncadg-mq)
-   [ncadg\_ipx](/windows/desktop/Midl/ncadg-ipx)

The format and content of the network address depend on the specified protocol sequence as follows.



| Protocol sequence                       | Network address                                                                                                                                  | Examples                                               |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| [ncacn\_nb\_tcp](/windows/desktop/Midl/ncacn-nb-tcp)     | Computer name                                                                                                                                    | myserver                                               |
| [ncacn\_nb\_ipx](/windows/desktop/Midl/ncacn-nb-ipx)     | Computer name                                                                                                                                    | myserver                                               |
| [ncacn\_nb\_nb](/windows/desktop/Midl/ncacn-nb-nb)       | Computer name                                                                                                                                    | myserver                                               |
| [ncacn\_ip\_tcp](/windows/desktop/Midl/ncacn-ip-tcp)     | Four-octet Internet address, or host name. If the IPv6 network stack is installed, IPv6 is fully supported and an IPv6 address is also accepted. | 128.10.2.30 anynode.microsoft.com                      |
| [ncacn\_np](/windows/desktop/Midl/ncacn-np)              | Server name (leading double backslashes are optional)                                                                                            | myserver \\\\myotherserver                             |
| [ncacn\_spx](/windows/desktop/Midl/ncacn-spx)            | IPX Internet address, or server name                                                                                                             | ~0000000108002B30612C myserver                         |
| [ncacn\_dnet\_nsp](/windows/desktop/Midl/ncacn-dnet-nsp) | Area and node syntax                                                                                                                             | 4.120                                                  |
| [ncacn\_at\_dsp](/windows/desktop/Midl/ncacn-at-dsp)     | Computer name, optionally followed by @ and the AppleTalk zone name. Defaults to @\*, the client's zone, if no zone provided                     | servername@zonename servername                         |
| [ncacn\_vns\_spp](/windows/desktop/Midl/ncacn-vns-spp)   | StreetTalk server name of the form item@group@organization                                                                                       | printserver@sdkdocs@microsoft                          |
| [ncadg\_mq](/windows/desktop/Midl/ncadg-mq)              | Server name                                                                                                                                      | myserver                                               |
| [ncacn\_http](/windows/desktop/Midl/ncacn-http)          | Internet address (either four-octet or friendly name, or local server name                                                                       | 128.10.2.30 somesvr@anywhere.com mylocalsvr<br/> |
| [ncadg\_ip\_udp](/windows/desktop/Midl/ncadg-ip-udp)     | Four-octet Internet address, or host name                                                                                                        | 128.10.2.30 anynode.microsoft.com                      |
| [ncadg\_ipx](/windows/desktop/Midl/ncadg-ipx)            | IPX Internet address, or server name                                                                                                             | ~0000000108002B30612C myserver                         |
| [ncalrpc](/windows/desktop/Midl/ncalrpc)                 | Machine name                                                                                                                                     | thismachine                                            |



 

The network-address field is optional. When you do not specify a network address, the string binding refers to your local host. It is possible to specify the name of the local computer when you use the **ncalrpc** protocol sequence, however doing so is completely unnecessary.

</dd> <dt>

<span id="Endpoint"></span><span id="endpoint"></span><span id="ENDPOINT"></span>*Endpoint*
</dt> <dd>

Endpoint, or address, of the process to receive remote procedure calls. An endpoint can be preceded by the keyword **endpoint=**. Specifying the endpoint is optional if the server has registered its bindings with the endpoint mapper. See [**RpcEpRegister**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcepregister).

The format and content of an endpoint depend on the specified protocol sequence as shown in the following Endpoint/Option Table.

</dd> <dt>

<span id="Option"></span><span id="option"></span><span id="OPTION"></span>*Option*
</dt> <dd>

Protocol-specific options. The option field is not required. Each option is specified by a {name, value} pair that uses the syntax *option name*=*option value*. Options are defined for each protocol sequence as shown in the following Endpoint/Option table.



| Protocol sequence                       | Endpoint                                                                                           | Examples             | Option name                                            |
|-----------------------------------------|----------------------------------------------------------------------------------------------------|----------------------|--------------------------------------------------------|
| [ncacn\_nb\_tcp](/windows/desktop/Midl/ncacn-nb-tcp)     | Integer between 1 and 254. Many values between 0 and 32 are reserved by Microsoft.                 | 100                  | None                                                   |
| [ncacn\_nb\_ipx](/windows/desktop/Midl/ncacn-nb-ipx)     | (as above)                                                                                         | (as above)           | None                                                   |
| [ncacn\_nb\_nb](/windows/desktop/Midl/ncacn-nb-nb)       | (as above)                                                                                         | (as above)           | None                                                   |
| [ncacn\_ip\_tcp](/windows/desktop/Midl/ncacn-ip-tcp)     | Internet port number.                                                                              | 1025                 | None                                                   |
| [ncacn\_np](/windows/desktop/Midl/ncacn-np)              | Named pipe. Name must start with "\\\\pipe".                                                       | \\\\pipe\\\\pipename | Security                                               |
| [ncacn\_spx](/windows/desktop/Midl/ncacn-spx)            | Integer between 1 and 65535.                                                                       | 5000                 | None                                                   |
| [ncacn\_dnet\_nsp](/windows/desktop/Midl/ncacn-dnet-nsp) | DECnet phase IV object number (must be preceded by the \# character), or object name.              | mailserver \#17      | None                                                   |
| [ncacn\_at\_dsp](/windows/desktop/Midl/ncacn-at-dsp)     | A character string, up to 22 bytes long.                                                           | myservicesendpoint   | None                                                   |
| [ncacn\_vns\_spp](/windows/desktop/Midl/ncacn-vns-spp)   | Vines SPP port number between 250 and 511.                                                         | 500                  | None                                                   |
| [ncadg\_mq](/windows/desktop/Midl/ncadg-mq)              | Integer between 1 and 65535.                                                                       | 5000                 | None                                                   |
| [ncacn\_http](/windows/desktop/Midl/ncacn-http)          | Internet port number.                                                                              | 2215                 | HTTP and RPC proxy server names, HttpConnection option |
| [ncadg\_ip\_udp](/windows/desktop/Midl/ncadg-ip-udp)     | Internet port number.                                                                              | 1025                 | None                                                   |
| [ncadg\_ipx](/windows/desktop/Midl/ncadg-ipx)            | Integer between 1 and 65535.                                                                       | 5000                 | None                                                   |
| [ncalrpc](/windows/desktop/Midl/ncalrpc)                 | String specifying application or service name. The string cannot include any backslash characters. | my\_printer          | Security                                               |



 

The **HttpConnectionOption** option name, supported for the ncacn\_http protocol sequence, takes the following value.



| Option name       | Value            |
|-------------------|------------------|
| HttpConnectOption | **UseHttpProxy** |



 

The **HttpConnectionOption** allows you to direct RPC s behavior when making HTTP connections. The **UseHttpProxy** value instructs RPC to route its traffic through the Http proxy at all times, including when the client has the Internet Options set in Internet Explorer to  Bypass proxy server for local addresses.  This option directs the client to forcefully connect to the RPC proxy through the Http proxy. This speeds up the time to establish a connection since it bypasses any delay searching for the RPC server directly prior to using the HTTP proxy.

If this **HttpConnectionOption** option is used and Internet Explorer on the client is not configured to use that Http proxy, connections may fail with **RPC\_S\_INVALID\_NETWORK\_OPTIONS**.

``` syntax
HttpConnectOption=UseHttpProxy
```

For more information about the **HttpConnectionOption**, see [Using HTTP as an RPC Transport](using-http-as-an-rpc-transport.md).

The **Security** option name, supported for the ncalrpc, ncacn\_np, ncadg\_ip\_udp, and ncadg\_ipx protocol sequences, takes the following option values.



| Option name  | Option value                                                                               |
|--------------|--------------------------------------------------------------------------------------------|
| **Security** | {identification \| anonymous \| impersonation} {dynamic \| static} {**true** \| **false**} |



 

If the security option name is specified, one entry from each of the sets of security option values must also be supplied. The option values must be separated by a single-space character. For example, the following *Option* fields are valid:

``` syntax
Security=identification dynamic true
Security=impersonation static true
```

The security option values have the following meanings.



| Security option value | Description                                                                                                                                                                                                                                                                                                                                              |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Anonymous             | The client is anonymous to the server.                                                                                                                                                                                                                                                                                                                   |
| Dynamic               | Changes in the client security identity are seen by the server when the server uses transport security. This is the default mode for LRPC (ncalrpc) transport level security, and for local named pipe (ncacn\_np) transport level security.                                                                                                             |
| **False**             | Effective = **FALSE**; all token privileges settings, including those set to OFF, are included in the token on the server and can be enabled by the server. Privileges are relevant for same-machine RPC calls only.                                                                                                                                     |
| **Identification**    | The server has information about the client but cannot impersonate.                                                                                                                                                                                                                                                                                      |
| **Impersonation**     | The server can act on behalf of the client within the local system (transport-level security does not support delegation).                                                                                                                                                                                                                               |
| **Static**            | Changes in the client security identity are not seen by the server when the server uses transport security. This is the only mode available to remote named pipe (ncacn\_np) transport level security. The identity of the caller is saved during the first remote procedure call on that binding handle, not at the time the binding handle is created. |
| **True**              | Effective = **TRUE**; only token privileges settings set to ON are included in the token on the server. Privileges set to OFF cannot be turned on by the server if this option is used. Privileges are relevant for same-machine RPC calls only.                                                                                                         |



 

For more information about security options, [Security](security.md).

</dd> </dl>

## Remarks

White space is not allowed in string bindings except where required by the *Option* syntax. Default settings for the *NetworkAddress*, *Endpoint*, and *Option* fields vary according to the value of the *ProtocolSequence* member.

For all string-binding fields, a single backslash character (\\) is interpreted as an escape character. To specify a single literal backslash character, you must supply two backslash characters (\\\\).

A string binding contains the character representation of a binding handle and occasionally portions of a binding handle. String bindings are convenient for representing portions of a binding handle, but they can't be used for making remote procedure calls. They must first be converted to a binding handle by calling [**RpcBindingFromStringBinding**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingfromstringbinding).

Additionally, a string binding does not contain all of the information from a binding handle. For example, the authentication information, if any, associated with a binding handle is not translated into the string binding returned by calling the [**RpcBindingToStringBinding**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingtostringbinding).

During the development of a distributed application, servers can communicate their binding information to clients using string bindings to establish a client-server relationship without using the endpoint-map database or name-service database. To establish such a relationship, use the function [**RpcBindingToStringBinding**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingtostringbinding) to convert one or more binding handles from a binding-handle vector to a string binding, and provide the string binding to the client.

## Examples

The following are examples of valid string bindings. In these examples, *obj-uuid* is used for convenience to represent a valid UUID in string form. Instead of showing the UUID 308FB580-1EB2-11CA-923B-08002B1075A7, the examples show *obj-uuid*.

``` syntax
obj-uuid@ncadg_mq:mymqserver
obj-uuid@ncacn_http:major7.microsoft.com[2225]
obj_uuid@ncacn_http:major7.microsoft.com[,HttpProxy=proxysvr:80,
    RpcProxy=websvr1.microsoft.com:80]
obj_uuid@ncacn_http:major7.microsoft.com[,HttpProxy=proxysvr:80,
    RpcProxy=websvr1.microsoft.com:80,HttpConnectOption=UseHttpProxy]
obj-uuid@ncacn_ip_tcp:16.20.16.27[2001]
obj-uuid@ncacn_ip_tcp:16.20.16.27[endpoint=2001]
obj-uuid@ncacn_nb_nb:
obj-uuid@ncacn_nb_nb:[100]
obj-uuid@ncacn_np:
obj-uuid@ncacn_np:[\\pipe\\p3,Security=impersonation static true]
obj-uuid@ncacn_np:\\\\marketing[\\pipe\\p2\\p3\\p4]
obj-uuid@ncacn_np:\\\\marketing[endpoint=\\pipe\\p2\\p3\\p4]
obj-uuid@ncacn_np:\\\\sales
obj-uuid@ncacn_np:\\\\sales[\\pipe\\p1,Security=identification dynamic true]
obj-uuid@ncalrpc:
obj-uuid@ncalrpc:[object1_name_demonstrating_that_these_can_be_lengthy]
obj-uuid@ncalrpc:[object2_name,Security=anonymous static true]
obj-uuid@ncacn_vns_spp:server@group@org[500]
obj-uuid@ncacn_dnet_nsp:took[elf_server]
obj-uuid@ncacn_dnet_nsp:took[endpoint=elf_server]
obj-uuid@ncadg_ip_udp:128.10.2.30
obj-uuid@ncadg_ip_udp:maryos.microsoft.com[1025]
obj-uuid@ncadg_ipx: ~0000000108002B30612C[5000]
obj-uuid@ncadg_ipx:printserver
obj-uuid@ncacn_spx:annaw[4390]
obj-uuid@ncacn_spx:~0000000108002B30612C
```

## Related topics

<dl> <dt>

[**RpcBindingFromStringBinding**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingfromstringbinding)
</dt> <dt>

[**RpcBindingToStringBinding**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingtostringbinding)
</dt> <dt>

[**RpcEpRegister**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcepregister)
</dt> <dt>

[Using HTTP as an RPC Transport](using-http-as-an-rpc-transport.md)
</dt> </dl>

 

