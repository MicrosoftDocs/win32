---
Description: 'The following table describes SOL\_APPLETALK socket options that apply to sockets created for the AppleTalk address family (AF\_APPLETALK).'
ms.assetid: '1a6b18e3-1fea-4ba2-8076-c38e7f679e9e'
title: 'SOL\_APPLETALK Socket Options'
---

# SOL\_APPLETALK Socket Options

The following table describes **SOL\_APPLETALK** socket options that apply to sockets created for the AppleTalk address family (AF\_APPLETALK). See the [**getsockopt**](getsockopt-2.md) and [**setsockopt**](setsockopt-2.md) function reference pages for more information on getting and setting socket options.

To enumerate protocols and discover supported properties for each installed protocol, use the [**WSAEnumProtocols**](wsaenumprotocols-2.md), [**WSCEnumProtocols**](wscenumprotocols-2.md), or [**WSCEnumProtocols32**](wscenumprotocols32.md) function.

<dl> <dt><span id="SOL_APPLETALK_Socket_Options"></span><span id="sol_appletalk_socket_options"></span><span id="SOL_APPLETALK_SOCKET_OPTIONS"></span>**SOL\_APPLETALK Socket Options**</dt> <dd> <dl> <dt> 

| Option                          | Get | Set | Optval type                          | Description                                                                                                                                                                                          |
|---------------------------------|-----|-----|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SO\_CONFIRM\_NAME               | yes |     | **WSH\_NBP\_TUPLE**                  | Confirms that a given AppleTalk name is bound to the given address.                                                                                                                                  |
| SO\_DEREGISTER\_NAME            |     | yes | **WSH\_REGISTER\_NAME**              | Deregisters the name from the network.                                                                                                                                                               |
| SO\_GETLOCALZONES               | yes |     | **WSH\_LOOKUP\_ZONES**               | Returns a list of zone names known to the given adapter name.                                                                                                                                        |
| SO\_GETMYZONE                   | yes |     | char \[\]                            | Returns the default zone on the network.                                                                                                                                                             |
| SO\_GETNETINFO                  | yes |     | **WSH\_LOOKUP\_NETDEF\_ON\_ADAPTER** | Returns the seeded values for the network as well as the default zone. The *optlen* parameter must be at least one byte larger than the size of the **WSH\_LOOKUP\_NETDEF\_ON\_ADAPTER** structure.  |
| SO\_GETZONELIST                 | yes |     | **WSH\_LOOKUP\_ZONES**               | Returns zone names from the Internet zone list. The *optlen* parameter must be at least one byte larger than the size of the **WSH\_LOOKUP\_ZONES** structure.                                       |
| SO\_LOOKUP\_MYZONE              | yes |     |                                      | Same as SO\_GETMYZONE                                                                                                                                                                                |
| SO\_LOOKUP\_NAME                | yes |     | **WSH\_LOOKUP\_NAME**                | Looks up a specified NBP name and returns the matching tuples of name and NBP information. The *optlen* parameter must be at least one byte larger than the size of the WSH\_LOOKUP\_NAME structure. |
| SO\_LOOKUP\_NETDEF\_ON\_ADAPTER | yes |     | **WSH\_LOOKUP\_NETDEF\_ON\_ADAPTER** | Same as SO\_GETNETINFO.                                                                                                                                                                              |
| SO\_LOOKUP\_ZONES               | yes |     | **WSH\_LOOKUP\_ZONES**               | Same as SO\_GETZONELIST.                                                                                                                                                                             |
| SO\_LOOKUP\_ZONES\_ON\_ADAPTER  | yes |     | **WSH\_LOOKUP\_ZONES**               | Same as SO\_GETLOCALZONES.                                                                                                                                                                           |
| SO\_PAP\_GET\_SERVER\_STATUS    | yes |     | **WSH\_PAP\_GET\_SERVER\_STATUS**    | Returns the PAP status from a given server                                                                                                                                                           |
| SO\_PAP\_PRIME\_READ            |     | yes | char \[\]                            | This call primes a read on a PAP connection so the sender can start sending the data                                                                                                                 |
| SO\_PAP\_SET\_SERVER\_STATUS    |     | yes | char \[\]                            | Sets the status to be sent if another client requests the status                                                                                                                                     |
| SO\_REGISTER\_NAME              |     | yes | **WSH\_REGISTER\_NAME**              | Registers the given name on the AppleTalk network                                                                                                                                                    |
| SO\_REMOVE\_NAME                |     | yes | **WSH\_REGISTER\_NAME**              | Same as SO\_DEREGISTER\_NAME                                                                                                                                                                         |



 

</dt> </dl> </dd> <dt><span id="Windows_Support_for_SOL_APPLETALK_options"></span><span id="windows_support_for_sol_appletalk_options"></span><span id="WINDOWS_SUPPORT_FOR_SOL_APPLETALK_OPTIONS"></span>**Windows Support for SOL\_APPLETALK options**</dt> <dd> <dl> <dt> 

| Option                          | Windows Vista and later | Windows Server 2003 | Windows XP | Windows 2000 | Windows NT4 | Windows 9x/Me |
|---------------------------------|-------------------------|---------------------|------------|--------------|-------------|---------------|
| SO\_CONFIRM\_NAME               |                         | x                   | x          | x            | x           |               |
| SO\_DEREGISTER\_NAME            |                         | x                   | x          | x            | x           |               |
| SO\_GETLOCALZONES               |                         | x                   | x          | x            | x           |               |
| SO\_GETMYZONE                   |                         | x                   | x          | x            | x           |               |
| SO\_GETNETINFO                  |                         | x                   | x          | x            | x           |               |
| SO\_GETZONELIST                 |                         | x                   | x          | x            | x           |               |
| SO\_LOOKUP\_MYZONE              |                         | x                   | x          | x            | x           |               |
| SO\_LOOKUP\_NAME                |                         | x                   | x          | x            | x           |               |
| SO\_LOOKUP\_NETDEF\_ON\_ADAPTER |                         | x                   | x          | x            | x           |               |
| SO\_LOOKUP\_ZONES               |                         | x                   | x          | x            | x           |               |
| SO\_LOOKUP\_ZONES\_ON\_ADAPTER  |                         | x                   | x          | x            | x           |               |
| SO\_PAP\_GET\_SERVER\_STATUS    |                         | x                   | x          | x            | x           |               |
| SO\_PAP\_PRIME\_READ            |                         | x                   | x          | x            | x           |               |
| SO\_PAP\_SET\_SERVER\_STATUS    |                         | x                   | x          | x            | x           |               |
| SO\_REGISTER\_NAME              |                         | x                   | x          | x            | x           |               |
| SO\_REMOVE\_NAME                |                         | x                   | x          | x            | x           |               |



 

The **SOL\_APPLETALK** options are only supported on the server versions of Windows 2000 and Windows NT 4.0.


</dt> </dl> </dd> </dl>

## Remarks

The **SOL\_APPLETALK** socket options and the structures used by these socket options are defined in the *Atalkwsh.h* header file.

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Atalkwsh.h</dt> </dl> |



 

 




