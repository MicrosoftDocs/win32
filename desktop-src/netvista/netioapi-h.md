---
Description: This section contains kernel mode network driver reference topics for the Netioapi.h header.
ms.assetid: D344B5F4-3094-4DAB-8CBB-5A9FFEE93018
title: Netioapi.h
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Netioapi.h

This section contains kernel mode network driver reference topics for the Netioapi.h header. This header is included in the Windows SDK as it is also shared with user mode networking applications.

The Netioapi.h header contains definitions for version agnostic IP helper APIs.

## In this section



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>CancelMibChangeNotify2</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>CancelMibChangeNotify2</strong> function deregisters a driver change notification for IP interface changes, IP address changes, IP route changes, and requests to retrieve the stable Unicast IP address table.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ConvertInterfaceAliasToLuid</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>ConvertInterfaceAliasToLuid</strong> function converts an interface alias name for a network interface to the locally unique identifier (LUID) for the interface.<br/>
<blockquote>
[!Note]<br />
The ConvertInterface<em>Xxx</em> API family enumerates identifiers over all interfaces bound to TCP/IP, which may include virtual miniports, lightweight filters, tunnel adapters, and physical interfaces.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ConvertInterfaceGuidToLuid</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>ConvertInterfaceGuidToLuid</strong> function converts a globally unique identifier (GUID) for a network interface to the locally unique identifier (LUID) for the interface.<br/>
<blockquote>
[!Note]<br />
The ConvertInterface<em>Xxx</em> API family enumerates identifiers over all interfaces bound to TCP/IP, which may include virtual miniports, lightweight filters, tunnel adapters, and physical interfaces.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>ConvertInterfaceIndexToLuid</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>ConvertInterfaceIndexToLuid</strong> function converts a local index for a network interface to the locally unique identifier (LUID) for the interface.<br/>
<blockquote>
[!Note]<br />
The ConvertInterface<em>Xxx</em> API family enumerates identifiers over all interfaces bound to TCP/IP, which may include virtual miniports, lightweight filters, tunnel adapters, and physical interfaces.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ConvertInterfaceLuidToAlias</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>ConvertInterfaceLuidToAlias</strong> function converts a locally unique identifier (LUID) for a network interface to an interface alias.<br/>
<blockquote>
[!Note]<br />
The ConvertInterface<em>Xxx</em> API family enumerates identifiers over all interfaces bound to TCP/IP, which may include virtual miniports, lightweight filters, tunnel adapters, and physical interfaces.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>ConvertInterfaceLuidToGuid</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>ConvertInterfaceLuidToGuid</strong> function converts a locally unique identifier (LUID) for a network interface to a globally unique identifier (GUID) for the interface.<br/>
<blockquote>
[!Note]<br />
The ConvertInterface<em>Xxx</em> API family enumerates identifiers over all interfaces bound to TCP/IP, which may include virtual miniports, lightweight filters, tunnel adapters, and physical interfaces.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ConvertInterfaceLuidToIndex</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>ConvertInterfaceLuidToIndex</strong> function converts a locally unique identifier (LUID) for a network interface to the local index for the interface.<br/>
<blockquote>
[!Note]<br />
The ConvertInterface<em>Xxx</em> API family enumerates identifiers over all interfaces bound to TCP/IP, which may include virtual miniports, lightweight filters, tunnel adapters, and physical interfaces.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>ConvertInterfaceLuidToNameA</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>ConvertInterfaceLuidToNameA</strong> function converts a locally unique identifier (LUID) for a network interface to the ANSI interface name.<br/>
<blockquote>
[!Note]<br />
The ConvertInterface<em>Xxx</em> API family enumerates identifiers over all interfaces bound to TCP/IP, which may include virtual miniports, lightweight filters, tunnel adapters, and physical interfaces.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ConvertInterfaceLuidToNameW</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>ConvertInterfaceLuidToNameW</strong> function converts a locally unique identifier (LUID) for a network interface to the Unicode interface name.<br/>
<blockquote>
[!Note]<br />
The ConvertInterface<em>Xxx</em> API family enumerates identifiers over all interfaces bound to TCP/IP, which may include virtual miniports, lightweight filters, tunnel adapters, and physical interfaces.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>ConvertInterfaceNameToLuidA</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>ConvertInterfaceNameToLuidA</strong> function converts an ANSI network interface name to the locally unique identifier (LUID) for the interface.<br/>
<blockquote>
[!Note]<br />
The ConvertInterface<em>Xxx</em> API family enumerates identifiers over all interfaces bound to TCP/IP, which may include virtual miniports, lightweight filters, tunnel adapters, and physical interfaces.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ConvertInterfaceNameToLuidW</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>ConvertInterfaceNameToLuidW</strong> function converts a Unicode network interface name to the locally unique identifier (LUID) for the interface.<br/>
<blockquote>
[!Note]<br />
The ConvertInterface<em>Xxx</em> API family enumerates identifiers over all interfaces bound to TCP/IP, which may include virtual miniports, lightweight filters, tunnel adapters, and physical interfaces.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>CreateAnycastIpAddressEntry</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>CreateAnycastIpAddressEntry</strong> function adds a new anycast IP address entry on a local computer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CreateIpForwardEntry2</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>CreateIpForwardEntry2</strong> function creates a new IP route entry on a local computer.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CreateIpNetEntry2</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>CreateIpNetEntry2</strong> function creates a new neighbor IP address entry on the local computer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>CreateSortedAddressPairs</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>From a supplied list of potential IP destination addresses, the <strong>CreateSortedAddressPairs</strong> function pairs the destination addresses together with the host machine's local IP addresses and sorts the pairs according to the preferred order of communication.<br/></td>
</tr>
<tr class="even">
<td>[<strong>CreateUnicastIpAddressEntry</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>CreateUnicastIpAddressEntry</strong> function adds a new unicast IP address entry on the local computer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DeleteAnycastIpAddressEntry</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>DeleteAnycastIpAddressEntry</strong> function deletes an existing anycast IP address entry on a local computer.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DeleteIpForwardEntry2</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>DeleteIpForwardEntry2</strong> function deletes an IP route entry on a local computer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DeleteIpNetEntry2</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>DeleteIpNetEntry2</strong> function deletes a neighbor IP address entry on a local computer.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DeleteUnicastIpAddressEntry</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>DeleteUnicastIpAddressEntry</strong> function deletes an existing unicast IP address entry on a local computer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FlushIpNetTable2</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>FlushIpNetTable2</strong> function flushes the IP neighbor table on a local computer.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FlushIpPathTable</strong>](/windows/win32/Netioapi/?branch=master)<br/></td>
<td>The <strong>FlushIpPathTable</strong> function flushes the IP path table on a local computer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>FreeMibTable</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>FreeMibTable</strong> function frees the buffer that is allocated by the functions that return tables of network interfaces, addresses, and routes (for example, [<strong>GetIfTable2</strong>](/windows/win32/netioapi/?branch=master) and [<strong>GetAnycastIpAddressTable</strong>](/windows/win32/netioapi/?branch=master)).<br/></td>
</tr>
<tr class="even">
<td>[<strong>GetAnycastIpAddressEntry</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>GetAnycastIpAddressEntry</strong> function retrieves information for an existing anycast IP address entry on a local computer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>GetAnycastIpAddressTable</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>GetAnycastIpAddressTable</strong> function retrieves the anycast IP address table on a local computer.<br/></td>
</tr>
<tr class="even">
<td>[<strong>GetBestRoute2</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>GetBestRoute2</strong> function retrieves the IP route entry on a local computer for the best route to the specified destination IP address.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>GetIfEntry2</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>GetIfEntry2</strong> function retrieves information for the specified interface on a local computer.<br/></td>
</tr>
<tr class="even">
<td>[<strong>GetIfStackTable</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>GetIfStackTable</strong> function retrieves a table of network interface stack row entries that specify the relationship of the network interfaces on an interface stack.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>GetIfTable2</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>GetIfTable2</strong> function retrieves the MIB-II interface table.<br/></td>
</tr>
<tr class="even">
<td>[<strong>GetIfTable2Ex</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>GetIfTable2Ex</strong> function retrieves the MIB-II interface table, given a level of interface information to retrieve.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>GetInvertedIfStackTable</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>GetInvertedIfStackTable</strong> function retrieves a table of inverted network interface stack row entries that specify the relationship of the network interfaces on an interface stack.<br/></td>
</tr>
<tr class="even">
<td>[<strong>GetIpForwardEntry2</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>GetIpForwardEntry2</strong> function retrieves information for an IP route entry on a local computer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>GetIpForwardTable2</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>GetIpForwardTable2</strong> function retrieves the IP route entries on a local computer.<br/></td>
</tr>
<tr class="even">
<td>[<strong>GetIpInterfaceEntry</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>GetIpInterfaceEntry</strong> function retrieves IP information for the specified interface on a local computer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>GetIpInterfaceTable</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>GetIpInterfaceTable</strong> function retrieves the IP interface entries on a local computer.<br/></td>
</tr>
<tr class="even">
<td>[<strong>GetIpNetEntry2</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>GetIpNetEntry2</strong> function retrieves information for a neighbor IP address entry on the local computer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>GetIpNetTable2</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>GetIpNetTable2</strong> function retrieves the IP neighbor table on a local computer.<br/></td>
</tr>
<tr class="even">
<td>[<strong>GetIpPathEntry</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>GetIpPathEntry</strong> function retrieves information for an IP path entry on a local computer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>GetIpPathTable</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>GetIpPathEntry</strong> function retrieves information for an IP path entry on a local computer.<br/></td>
</tr>
<tr class="even">
<td>[<strong>GetMulticastIpAddressEntry</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>GetMulticastIpAddressEntry</strong> function retrieves information for an existing multicast IP address entry on a local computer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>GetMulticastIpAddressTable</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>GetMulticastIpAddressTable</strong> function retrieves the multicast IP address table on a local computer.<br/></td>
</tr>
<tr class="even">
<td>[<strong>GetTeredoPort</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>GetTeredoPort</strong> function retrieves the dynamic UDP port number that the Teredo client uses on a local computer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>GetUnicastIpAddressEntry</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>GetUnicastIpAddressEntry</strong> function retrieves information for an existing unicast IP address entry on a local computer.<br/></td>
</tr>
<tr class="even">
<td>[<strong>GetUnicastIpAddressTable</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>GetUnicastIpAddressTable</strong> function retrieves the unicast IP address table on a local computer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>if_indextoname</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>if_indextoname</strong> function converts the local index for a network interface to the ANSI interface name.<br/></td>
</tr>
<tr class="even">
<td>[<strong>if_nametoindex</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>if_nametoindex</strong> function converts the ANSI interface name for a network interface to the local index for the interface.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>InitializeIpForwardEntry</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>InitializeIpForwardEntry</strong> function initializes a [<strong>MIB_IPFORWARD_ROW2</strong>](/windows/win32/netioapi/?branch=master) structure with default values for an IP route entry on a local computer.<br/></td>
</tr>
<tr class="even">
<td>[<strong>InitializeIpInterfaceEntry</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>InitializeIpInterfaceEntry</strong> function initializes the members of an [<strong>MIB_IPINTERFACE_ROW</strong>](/windows/win32/netioapi/?branch=master) structure entry with default values.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>InitializeUnicastIpAddressEntry</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>InitializeUnicastIpAddressEntry</strong> function initializes a [<strong>MIB_UNICASTIPADDRESS_ROW</strong>](/windows/win32/netioapi/?branch=master) structure with default values for a unicast IP address entry on a local computer.<br/></td>
</tr>
<tr class="even">
<td>[<strong>NotifyIpInterfaceChange</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>NotifyIpInterfaceChange</strong> function registers the driver to be notified for changes to all IP interfaces, IPv4 interfaces, or IPv6 interfaces on a local computer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>NotifyRouteChange2</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>NotifyRouteChange2</strong> function registers the driver to be notified for changes to IP route entries on a local computer.<br/></td>
</tr>
<tr class="even">
<td>[<strong>NotifyStableUnicastIpAddressTable</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>NotifyStableUnicastIpAddressTable</strong> function retrieves the stable unicast IP address table on a local computer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>NotifyTeredoPortChange</strong>](/windows/win32/Netioapi/?branch=master)<br/></td>
<td>The <strong>NotifyTeredoPortChange</strong> function registers the driver to be notified for changes to the UDP port number that the Teredo client uses for the Teredo service port on a local computer.<br/></td>
</tr>
<tr class="even">
<td>[<strong>NotifyUnicastIpAddressChange</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>NotifyUnicastIpAddressChange</strong> function registers the driver to be notified for changes to all unicast IP interfaces, unicast IPv4 addresses, or unicast IPv6 addresses on a local computer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ResolveIpNetEntry2</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>ResolveIpNetEntry2</strong> function resolves the physical address for a neighbor IP address entry on a local computer.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SetIpForwardEntry2</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>SetIpForwardEntry2</strong> function sets the properties of an IP route entry on a local computer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SetIpInterfaceEntry</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>SetIpInterfaceEntry</strong> function sets the properties of an IP interface on a local computer.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SetIpNetEntry2</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>SetIpNetEntry2</strong> function sets the physical address of an existing neighbor IP address entry on a local computer.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SetUnicastIpAddressEntry</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The <strong>SetUnicastIpAddressEntry</strong> function sets the properties of an existing unicast IP address entry on a local computer.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IP_ADDRESS_PREFIX</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The IP_ADDRESS_PREFIX structure stores an IP address prefix.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MIB_ANYCASTIPADDRESS_ROW</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The MIB_ANYCASTIPADDRESS_ROW structure stores information about an anycast IP address.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MIB_ANYCASTIPADDRESS_TABLE</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The MIB_ANYCASTIPADDRESS_TABLE structure contains a table of anycast IP address entries.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MIB_IFSTACK_ROW</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The MIB_IFSTACK_ROW structure represents the relationship between two network interfaces.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MIB_IFSTACK_TABLE</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The MIB_IFSTACK_TABLE structure contains a table of network interface stack row entries. This table specifies the relationship of the network interfaces on an interface stack.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MIB_IF_ROW2</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The MIB_IF_ROW2 structure stores information about a particular interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MIB_IF_TABLE2</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The MIB_IF_TABLE2 structure contains a table of logical and physical interface entries.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MIB_INVERTEDIFSTACK_ROW</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The MIB_INVERTEDIFSTACK_ROW structure represents the relationship between two network interfaces.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MIB_INVERTEDIFSTACK_TABLE</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The MIB_INVERTEDIFSTACK_TABLE structure contains a table of inverted network interface stack row entries. This table specifies the relationship of the network interfaces on an interface stack in reverse order.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MIB_IPFORWARD_ROW2</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The MIB_IPFORWARD_ROW2 structure stores information about an IP route entry.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MIB_IPFORWARD_TABLE2</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The MIB_IPFORWARD_TABLE2 structure contains a table of IP route entries.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MIB_IPINTERFACE_ROW</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The MIB_IPINTERFACE_ROW structure stores interface management information for a particular IP address family on a network interface.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MIB_IPINTERFACE_TABLE</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The MIB_IPINTERFACE_TABLE structure contains a table of IP interface entries.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MIB_IPNET_ROW2</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The MIB_IPNET_ROW2 structure stores information about a neighbor IP address.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MIB_IPNET_TABLE2</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The MIB_IPNET_TABLE2 structure contains a table of neighbor IP address entries.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MIB_IPPATH_ROW</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The MIB_IPPATH_ROW structure stores information about an IP path entry.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MIB_IPPATH_TABLE</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The MIB_IPPATH_TABLE structure contains a table of IP path entries.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MIB_MULTICASTIPADDRESS_ROW</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The MIB_MULTICASTIPADDRESS_ROW structure stores information about a multicast IP address.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MIB_MULTICASTIPADDRESS_TABLE</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The MIB_MULTICASTIPADDRESS_TABLE structure contains a table of multicast IP address entries.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MIB_UNICASTIPADDRESS_ROW</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The MIB_UNICASTIPADDRESS_ROW structure stores information about a unicast IP address.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MIB_UNICASTIPADDRESS_TABLE</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The MIB_UNICASTIPADDRESS_TABLE structure contains a table of unicast IP address entries.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MIB_IF_TABLE_LEVEL</strong>](/windows/win32/netioapi/ne-netioapi-_mib_if_table_level?branch=master)<br/></td>
<td>The MIB_IF_TABLE_LEVEL enumeration type defines the level of interface information to retrieve.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MIB_NOTIFICATION_TYPE</strong>](/windows/win32/netioapi/?branch=master)<br/></td>
<td>The MIB_NOTIFICATION_TYPE enumeration type defines the notification type that is passed to a callback function when a notification occurs.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ConvertIpv4MaskToLength</strong>](/windows/win32/Netioapi/?branch=master)<br/></td>
<td>Reserved for future use. Do not use this function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>ConvertLengthtoIpv4Mask</strong>](/windows/win32/Netioapi/?branch=master)<br/></td>
<td>Reserved for future use. Do not use this function.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>GetCurrentThreadCompartmentId</strong>](/windows/win32/Netioapi/nf-netioapi-getcurrentthreadcompartmentid?branch=master)<br/></td>
<td>Reserved for future use. Do not use this function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>GetNetworkInformation</strong>](/windows/win32/Netioapi/nf-netioapi-getnetworkinformation?branch=master)<br/></td>
<td>Reserved for future use. Do not use this function.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>GetSessionCompartmentId</strong>](/windows/win32/Netioapi/nf-netioapi-getsessioncompartmentid?branch=master)<br/></td>
<td>Reserved for future use. Do not use this function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SetCurrentThreadCompartmentId</strong>](/windows/win32/Netioapi/nf-netioapi-setcurrentthreadcompartmentid?branch=master)<br/></td>
<td>Reserved for future use. Do not use this function.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SetNetworkInformation</strong>](/windows/win32/Netioapi/nf-netioapi-setnetworkinformation?branch=master)<br/></td>
<td>Reserved for future use. Do not use this function.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SetSessionCompartmentId</strong>](/windows/win32/Netioapi/nf-netioapi-setsessioncompartmentid?branch=master)<br/></td>
<td>Reserved for future use. Do not use this function.<br/></td>
</tr>
</tbody>
</table>



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20Netioapi.h%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




