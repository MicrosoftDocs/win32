---
title: Whats New in MIB
description: On the Microsoft Windows Software Development Kit (SDK) released for Windows Vista and later, the organization of header files has changed and some of the older MIB structures are defined in the Ipmib.h header file not in the Iprtrmib.h header file.
ms.assetid: 213b88b6-56b0-4d70-9765-c61094f6f9ff
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# What's New in MIB

On the Microsoft Windows Software Development Kit (SDK) released for Windows Vista and later, the organization of header files has changed and some of the older MIB structures are defined in the *Ipmib.h* header file not in the *Iprtrmib.h* header file. Note that the *Ipmib.h* header file is automatically included in *Iprtrmib.h* which is automatically included in the *Iphlpapi.h* header file. The new MIB structures introduced with Windows Vista and later are defined in the *Netioapi.h* which is automatically included in the *Iphlpapi.h* header file. The *Ipmib.h*, *Iprtrmib.h*, and *Netioapi.h* header files should never be used directly.

## Windows 8 and Windows Server 2012

The following structure has been added to the Management Information Base for Windows 8 and Windows Server 2012:

-   [**MIB\_IP\_NETWORK\_CONNECTION\_BANDWIDTH\_ESTIMATES**](/windows/win32/Netioapi/ns-netioapi-_mib_ip_network_connection_bandwidth_estimates?branch=master)

## Windows Vista

The following structures and enumerations have been added to the Management Information Base for Windows Vista:

-   [**MIB\_ANYCASTIPADDRESS\_ROW**](/windows/win32/Netioapi/ns-netioapi-_mib_anycastipaddress_row?branch=master)
-   [**MIB\_ANYCASTIPADDRESS\_TABLE**](/windows/win32/Netioapi/ns-netioapi-_mib_anycastipaddress_table?branch=master)
-   [**MIB\_IFSTACK\_ROW**](/windows/win32/Netioapi/ns-netioapi-_mib_ifstack_row?branch=master)
-   [**MIB\_IFSTACK\_TABLE**](/windows/win32/Netioapi/ns-netioapi-_mib_ifstack_table?branch=master)
-   [**MIB\_IF\_ROW2**](/windows/win32/Netioapi/ns-netioapi-_mib_if_row2?branch=master)
-   [**MIB\_IF\_TABLE2**](/windows/win32/Netioapi/ns-netioapi-_mib_if_table2?branch=master)
-   [**MIB\_INVERTEDIFSTACK\_ROW**](/windows/win32/Netioapi/ns-netioapi-_mib_invertedifstack_row?branch=master)
-   [**MIB\_INVERTEDIFSTACK\_TABLE**](/windows/win32/Netioapi/ns-netioapi-_mib_invertedifstack_table?branch=master)
-   [**MIB\_IPFORWARD\_ROW2**](/windows/win32/Netioapi/ns-netioapi-_mib_ipforward_row2?branch=master)
-   [**MIB\_IPFORWARD\_TABLE2**](/windows/win32/Netioapi/ns-netioapi-_mib_ipforward_table2?branch=master)
-   [**MIB\_IPINTERFACE\_ROW**](/windows/win32/Netioapi/ns-netioapi-_mib_ipinterface_row?branch=master)
-   [**MIB\_IPINTERFACE\_TABLE**](/windows/win32/Netioapi/ns-netioapi-_mib_ipinterface_table?branch=master)
-   [**MIB\_IPNET\_ROW2**](/windows/win32/Netioapi/ns-netioapi-_mib_ipnet_row2?branch=master)
-   [**MIB\_IPNET\_TABLE2**](/windows/win32/Netioapi/ns-netioapi-_mib_ipnet_table2?branch=master)
-   [**MIB\_IPPATH\_ROW**](/windows/win32/Netioapi/ns-netioapi-_mib_ippath_row?branch=master)
-   [**MIB\_IPPATH\_TABLE**](/windows/win32/Netioapi/ns-netioapi-_mib_ippath_table?branch=master)
-   [**MIB\_MULTICASTIPADDRESS\_ROW**](/windows/win32/Netioapi/ns-netioapi-_mib_multicastipaddress_row?branch=master)
-   [**MIB\_MULTICASTIPADDRESS\_TABLE**](/windows/win32/Netioapi/ns-netioapi-_mib_multicastipaddress_table?branch=master)
-   [**MIB\_NOTIFICATION\_TYPE**](/windows/win32/Netioapi/ne-netioapi-_mib_notification_type?branch=master)
-   [**MIB\_TCP6ROW**](/windows/previous-versions/Tcpmib/ns-tcpmib-_mib_tcp6row?branch=master)
-   [**MIB\_TCP6ROW2**](/windows/previous-versions/Tcpmib/ns-tcpmib-_mib_tcp6row2?branch=master)
-   [**MIB\_TCP6TABLE**](/windows/previous-versions/Tcpmib/ns-tcpmib-_mib_tcp6table?branch=master)
-   [**MIB\_TCP6TABLE2**](/windows/previous-versions/Tcpmib/ns-tcpmib-_mib_tcp6table2?branch=master)
-   [**MIB\_TCPROW2**](/windows/previous-versions/Tcpmib/ns-tcpmib-_mib_tcprow2?branch=master)
-   [**MIB\_TCPTABLE2**](/windows/previous-versions/Tcpmib/ns-tcpmib-_mib_tcptable2?branch=master)
-   [**MIB\_UDP6ROW**](/windows/previous-versions/Udpmib/ns-udpmib-_mib_udp6row?branch=master)
-   [**MIB\_UDP6TABLE**](/windows/previous-versions/Udpmib/ns-udpmib-_mib_udp6table?branch=master)
-   [**MIB\_UNICASTIPADDRESS\_TABLE**](/windows/win32/Netioapi/ns-netioapi-_mib_unicastipaddress_table?branch=master)
-   [**NL\_INTERFACE\_OFFLOAD\_ROD**](/windows/win32/Nldef/ns-nldef-_nl_interface_offload_rod?branch=master)
-   [**TCP\_CONNECTION\_OFFLOAD\_STATE**](/windows/previous-versions/Tcpmib/ne-tcpmib-tcp_connection_offload_state?branch=master)

## Windows Server 2003 Service Pack 1

The following structures have been added to the Management Information Base for Windows Server 2003 with Service Pack 1 (SP1):

-   [**MIB\_BOUNDARYROW**](/windows/win32/Iprtrmib/ns-iprtrmib-mib_boundaryrow?branch=master)
-   [**MIB\_IPMCAST\_BOUNDARY**](/windows/win32/Iprtrmib/ns-iprtrmib-_mib_ipmcast_boundary?branch=master)
-   [**MIB\_IPMCAST\_BOUNDARY\_TABLE**](/windows/win32/Iprtrmib/ns-iprtrmib-_mib_ipmcast_boundary_table?branch=master)
-   [**MIB\_IPMCAST\_MFE\_STATS\_EX**](/windows/previous-versions/Ipmib/ns-ipmib-_mib_ipmcast_mfe_stats_ex_xp?branch=master)
-   [**MIB\_IPMCAST\_SCOPE**](/windows/win32/Iprtrmib/ns-iprtrmib-_mib_ipmcast_scope?branch=master)
-   [**MIB\_MCAST\_LIMIT\_ROW**](/windows/win32/Iprtrmib/ns-iprtrmib-mib_mcast_limit_row?branch=master)
-   [**MIB\_MFE\_STATS\_TABLE\_EX**](/windows/previous-versions/Ipmib/ns-ipmib-_mib_mfe_stats_table_ex_xp?branch=master)

 

 




