---
description: All IPv6 configuration is done with the Ipv6.exe tool.
ms.assetid: cb701070-cb7f-472a-97c7-1de9c0ddec0f
title: Ipv6.exe
ms.topic: article
ms.date: 05/31/2018
---

# Ipv6.exe

All IPv6 configuration is done with the Ipv6.exe tool. This tool is primarily used for the querying and configuring of IPv6 interfaces, addresses, caches, and routes. The following are IPv6 subcommands:

<dl> <dt>

<span id="ipv6_if__if__"></span><span id="IPV6_IF__IF__"></span>**ipv6 if** \[if\#\]
</dt> <dd>

Displays information about interfaces. If an interface number is specified, only information about that interface is displayed. Otherwise, information about all interfaces is displayed. The output includes the interface's link-layer address and the list of IPv6 addresses assigned to the interface, including the interface's current MTU and the maximum (true) MTU that the interface can support.

Interface \#1 is a pseudo-interface used for loopback. Interface \#2 is a pseudo-interface used for configured tunneling, automatic tunneling, and 6to4 tunneling. Other interfaces are numbered sequentially in the order in which they are created. This order varies from one computer to another.

Link-layer addresses in *aa*-*bb*-*cc*-*dd*-*ee*-*ff* format are Ethernet addresses. Link-layer address in *a*.*b*.*c*.*d* form are 6-over-4 interfaces. For more information on 6-over-4, see RFC 2529.

The two pseudo-interfaces do not use IPv6 Neighbor Discovery.

</dd> <dt>

<span id="ipv6_ifc_if___forwards___advertises___-forwards___-advertises___mtu__bytes___site_site-identifier_"></span><span id="IPV6_IFC_IF___FORWARDS___ADVERTISES___-FORWARDS___-ADVERTISES___MTU__BYTES___SITE_SITE-IDENTIFIER_"></span>**ipv6 ifc** if\# \[forwards\] \[advertises\] \[-forwards\] \[-advertises\] \[mtu \#bytes\] \[site site-identifier\]
</dt> <dd>

Controls interface attributes. Interfaces can be forwarding, in which case they forward packets with destination addresses not assigned to the interface. Interfaces can be advertising, in which case they send router advertisements. These attributes can be independently controlled. An interface either sends router solicitations and receives router advertisements, or receives router solicitations and sends router advertisements.

Because the two pseudo-interfaces do not use Neighbor Discovery, they cannot be configured to send router advertisements.

Forwards can be abbreviated as forw, and advertised as adv.

The MTU for the interface can also be set. The new MTU must be less than or equal to the link's maximum (true) MTU (as reported by ipv6 if) and greater than or equal to the minimum IPv6 MTU (1280 bytes).

The site-identifier for an interface can also be changed. Site identifiers are used in the sin6\_scope\_id field with site-local addresses.

</dd> <dt>

<span id="ipv6_ifd_if_"></span><span id="IPV6_IFD_IF_"></span>**ipv6 ifd** if\#
</dt> <dd>

Deletes an interface. The loopback and tunnel pseudo-interfaces cannot be deleted.

</dd> <dt>

<span id="ipv6_nc__if___address__"></span><span id="IPV6_NC__IF___ADDRESS__"></span>**ipv6 nc** \[if\# \[address\]\]
</dt> <dd>

Displays the contents of the neighbor cache. If an interface number is specified, only the contents of that interface's neighbor cache are displayed. Otherwise, the contents of all the interface's neighbor caches are displayed. If an interface is specified, an IPv6 address can be specified to display only that neighbor cache entry.

For each neighbor cache entry, the interface, IPv6 address, link-layer address, and reach state are displayed.

</dd> <dt>

<span id="ipv6_ncf__if___address__"></span><span id="IPV6_NCF__IF___ADDRESS__"></span>**ipv6 ncf** \[if\# \[address\]\]
</dt> <dd>

Flushes the specified neighbor cache entries. Only neighbor cache entries without references are purged. Because route cache entries hold references to neighbor cache entries, the route cache should be flushed first. Routing table entries can also hold references to neighbor cache entries.

</dd> <dt>

<span id="ipv6_rc__if__address_"></span><span id="IPV6_RC__IF__ADDRESS_"></span>**ipv6 rc** \[if\# address\]
</dt> <dd>

Displays the contents of the route cache. The route cache is the Microsoft IPv6 implementation name for the destination cache. If an interface and address are specified, the route cache entry for reaching the address through the interface is displayed. Otherwise, all route cache entries are displayed.

For each route cache entry, the IPv6 address and the current next-hop interface and neighbor address are displayed. The preferred source address for use with this destination, the current path MTU for reaching this destination through the interface, and the determination of whether this is an interface specific–route cache entry are also displayed. Any care-of address (for mobility) for the destination address is displayed as well.

A destination address can have multiple route cache entries—as many as one for each outgoing interface. However, a destination address can have a maximum of one route cache entry that is not interface-specific. An interface specific–route cache entry is only used if the application explicitly specifies that outgoing interface.

</dd> <dt>

<span id="ipv6_rcf__if___address__"></span><span id="IPV6_RCF__IF___ADDRESS__"></span>**ipv6 rcf** \[if\# \[address\]\]
</dt> <dd>

Flushes the specified route cache entries.

</dd> <dt>

<span id="ipv6_bc"></span><span id="IPV6_BC"></span>**ipv6 bc**
</dt> <dd>

Displays the contents of the binding cache, which holds bindings between home addresses and care-of addresses for mobile IPv6.

For each binding, the home address, care-of address, binding sequence number, and lifetime are displayed.

</dd> <dt>

<span id="ipv6_adu_if__address__lifetime_VL__PL____anycast___unicast_"></span><span id="ipv6_adu_if__address__lifetime_vl__pl____anycast___unicast_"></span><span id="IPV6_ADU_IF__ADDRESS__LIFETIME_VL__PL____ANYCAST___UNICAST_"></span>**ipv6 adu** if\#/address \[lifetime VL\[/PL\]\] \[anycast\] \[unicast\]
</dt> <dd>

Adds or removes a unicast or anycast address assignment on an interface. The unicast address is acted upon unless anycast is specified.

Lifetime is infinite if unspecified. If only a valid lifetime is specified, the preferred lifetime is equal to the valid lifetime. An infinite lifetime may be specified, or a finite value in seconds. The preferred lifetime must be less than or equal to the valid lifetime. Specifying a lifetime of zero causes the address to be removed.

You can abbreviate lifetime as life.

For anycast addresses, the only valid lifetime values are zero and infinite.

</dd> <dt>

<span id="ipv6_spt"></span><span id="IPV6_SPT"></span>**ipv6 spt**
</dt> <dd>

Displays the current contents of the site prefix table.

For each site prefix, the command displays the prefix, the interface to which the site prefix applies, and the prefix lifetime in seconds.

Site prefixes are normally auto-configured from router advertisements. They are used in the [**getaddrinfo**](/windows/desktop/api/Ws2tcpip/nf-ws2tcpip-getaddrinfo) function to filter inappropriate site-local addresses.

</dd> <dt>

<span id="ipv6_spu_prefix_if___lifetime_L_"></span><span id="ipv6_spu_prefix_if___lifetime_l_"></span><span id="IPV6_SPU_PREFIX_IF___LIFETIME_L_"></span>**ipv6 spu** prefix if\# \[lifetime L\]
</dt> <dd>

Adds, removes, or updates a prefix in the site prefix table.

The prefix and interface number are required. The site prefix lifetime, specified in seconds, defaults to infinite if not specified. Specifying a lifetime of zero deletes the site prefix.

This command is unnecessary for the normal configuration of hosts or routers.

</dd> <dt>

<span id="ipv6_rt"></span><span id="IPV6_RT"></span>**ipv6 rt**
</dt> <dd>

Displays the current contents of the routing table.

For each routing table entry, the command displays the route prefix, an on-link interface or a next-hop neighbor on an interface, a preference value (smaller is preferred), and a lifetime in seconds.

Routing table entries may also have **publish** and **aging** attributes. By default, they age (the lifetime counts down, rather than remaining constant) and are not published (not used in constructing router advertisements).

On hosts, routing table entries are normally auto-configured from router advertisements.

</dd> <dt>

<span id="ipv6_rtu_prefix_if___nexthop___lifetime_L___preference_P___publish___age___spl_site-prefix-length_"></span><span id="ipv6_rtu_prefix_if___nexthop___lifetime_l___preference_p___publish___age___spl_site-prefix-length_"></span><span id="IPV6_RTU_PREFIX_IF___NEXTHOP___LIFETIME_L___PREFERENCE_P___PUBLISH___AGE___SPL_SITE-PREFIX-LENGTH_"></span>**ipv6 rtu** prefix if\#\[/nexthop\] \[lifetime L\] \[preference P\] \[publish\] \[age\] \[spl site-prefix-length\]
</dt> <dd>

Adds or removes a route in the routing table. The route prefix is required. The prefix can be on-link to a specified interface, or next-hop, specified with a neighbor address on an interface. The route can have a lifetime in seconds, with the default infinite, and a preference, with the default of zero, or most preferred. Specifying a lifetime of zero deletes the route.

If the route is specified as published, indicating it will be used in constructing router advertisements, it does not age. The route's lifetime does not count down and therefore is effectively infinite, but the value is used in router advertisements. Optionally, a route can be specified as a published route that also ages. A nonpublished route by default always ages.

The optional spl suboption can be used to specify a site prefix length associated with the route. The site prefix length is used only when sending router advertisements.

Lifetime can be abbreviated as life, preference as pref, and publish as pub.

</dd> </dl>

 

 



