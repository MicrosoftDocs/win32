---
title: What's New in MIB
description: On the Microsoft Windows Software Development Kit (SDK) released for Windows Vista and later, the organization of header files has changed and some of the older MIB structures are defined in the Ipmib.h header file not in the Iprtrmib.h header file.
ms.assetid: 213b88b6-56b0-4d70-9765-c61094f6f9ff
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# What's New in MIB

On the Microsoft Windows Software Development Kit (SDK) released for Windows Vista and later, the organization of header files has changed and some of the older MIB structures are defined in the *Ipmib.h* header file not in the *Iprtrmib.h* header file. Note that the *Ipmib.h* header file is automatically included in *Iprtrmib.h* which is automatically included in the *Iphlpapi.h* header file. The new MIB structures introduced with Windows Vista and later are defined in the *Netioapi.h* which is automatically included in the *Iphlpapi.h* header file. The *Ipmib.h*, *Iprtrmib.h*, and *Netioapi.h* header files should never be used directly.

## Windows 8 and Windows Server 2012

The following structure has been added to the Management Information Base for Windows 8 and Windows Server 2012:

-   [**MIB\_IP\_NETWORK\_CONNECTION\_BANDWIDTH\_ESTIMATES**](/windows/desktop/api/Netioapi/ns-netioapi-_mib_ip_network_connection_bandwidth_estimates)

## Windows Vista

The following structures and enumerations have been added to the Management Information Base for Windows Vista:

-   [**MIB\_ANYCASTIPADDRESS\_ROW**](/windows/desktop/api/Netioapi/ns-netioapi-_mib_anycastipaddress_row)
-   [**MIB\_ANYCASTIPADDRESS\_TABLE**](/windows/desktop/api/Netioapi/ns-netioapi-_mib_anycastipaddress_table)
-   [**MIB\_IFSTACK\_ROW**](/windows/desktop/api/Netioapi/ns-netioapi-_mib_ifstack_row)
-   [**MIB\_IFSTACK\_TABLE**](/windows/desktop/api/Netioapi/ns-netioapi-_mib_ifstack_table)
-   [**MIB\_IF\_ROW2**](/windows/desktop/api/Netioapi/ns-netioapi-_mib_if_row2)
-   [**MIB\_IF\_TABLE2**](/windows/desktop/api/Netioapi/ns-netioapi-_mib_if_table2)
-   [**MIB\_INVERTEDIFSTACK\_ROW**](/windows/desktop/api/Netioapi/ns-netioapi-_mib_invertedifstack_row)
-   [**MIB\_INVERTEDIFSTACK\_TABLE**](/windows/desktop/api/Netioapi/ns-netioapi-_mib_invertedifstack_table)
-   [**MIB\_IPFORWARD\_ROW2**](/windows/desktop/api/Netioapi/ns-netioapi-_mib_ipforward_row2)
-   [**MIB\_IPFORWARD\_TABLE2**](/windows/desktop/api/Netioapi/ns-netioapi-_mib_ipforward_table2)
-   [**MIB\_IPINTERFACE\_ROW**](/windows/desktop/api/Netioapi/ns-netioapi-_mib_ipinterface_row)
-   [**MIB\_IPINTERFACE\_TABLE**](/windows/desktop/api/Netioapi/ns-netioapi-_mib_ipinterface_table)
-   [**MIB\_IPNET\_ROW2**](/windows/desktop/api/Netioapi/ns-netioapi-_mib_ipnet_row2)
-   [**MIB\_IPNET\_TABLE2**](/windows/desktop/api/Netioapi/ns-netioapi-_mib_ipnet_table2)
-   [**MIB\_IPPATH\_ROW**](/windows/desktop/api/Netioapi/ns-netioapi-_mib_ippath_row)
-   [**MIB\_IPPATH\_TABLE**](/windows/desktop/api/Netioapi/ns-netioapi-_mib_ippath_table)
-   [**MIB\_MULTICASTIPADDRESS\_ROW**](/windows/desktop/api/Netioapi/ns-netioapi-_mib_multicastipaddress_row)
-   [**MIB\_MULTICASTIPADDRESS\_TABLE**](/windows/desktop/api/Netioapi/ns-netioapi-_mib_multicastipaddress_table)
-   [**MIB\_NOTIFICATION\_TYPE**](/windows/desktop/api/Netioapi/ne-netioapi-_mib_notification_type)
-   [**MIB\_TCP6ROW**](/previous-versions/windows/desktop/api/Tcpmib/ns-tcpmib-_mib_tcp6row)
-   [**MIB\_TCP6ROW2**](/previous-versions/windows/desktop/api/Tcpmib/ns-tcpmib-_mib_tcp6row2)
-   [**MIB\_TCP6TABLE**](/previous-versions/windows/desktop/api/Tcpmib/ns-tcpmib-_mib_tcp6table)
-   [**MIB\_TCP6TABLE2**](/previous-versions/windows/desktop/api/Tcpmib/ns-tcpmib-_mib_tcp6table2)
-   [**MIB\_TCPROW2**](/previous-versions/windows/desktop/api/Tcpmib/ns-tcpmib-_mib_tcprow2)
-   [**MIB\_TCPTABLE2**](/previous-versions/windows/desktop/api/Tcpmib/ns-tcpmib-_mib_tcptable2)
-   [**MIB\_UDP6ROW**](/previous-versions/windows/desktop/api/Udpmib/ns-udpmib-_mib_udp6row)
-   [**MIB\_UDP6TABLE**](/previous-versions/windows/desktop/api/Udpmib/ns-udpmib-_mib_udp6table)
-   [**MIB\_UNICASTIPADDRESS\_TABLE**](/windows/desktop/api/Netioapi/ns-netioapi-_mib_unicastipaddress_table)
-   [**NL\_INTERFACE\_OFFLOAD\_ROD**](/windows/desktop/api/Nldef/ns-nldef-_nl_interface_offload_rod)
-   [**TCP\_CONNECTION\_OFFLOAD\_STATE**](/previous-versions/windows/desktop/api/Tcpmib/ne-tcpmib-tcp_connection_offload_state)

## Windows Server 2003 Service Pack 1

The following structures have been added to the Management Information Base for Windows Server 2003 with Service Pack 1 (SP1):

-   [**MIB\_BOUNDARYROW**](/windows/desktop/api/Iprtrmib/ns-iprtrmib-mib_boundaryrow)
-   [**MIB\_IPMCAST\_BOUNDARY**](/windows/desktop/api/Iprtrmib/ns-iprtrmib-_mib_ipmcast_boundary)
-   [**MIB\_IPMCAST\_BOUNDARY\_TABLE**](/windows/desktop/api/Iprtrmib/ns-iprtrmib-_mib_ipmcast_boundary_table)
-   [**MIB\_IPMCAST\_MFE\_STATS\_EX**](/previous-versions/windows/desktop/api/Ipmib/ns-ipmib-_mib_ipmcast_mfe_stats_ex_xp)
-   [**MIB\_IPMCAST\_SCOPE**](/windows/desktop/api/Iprtrmib/ns-iprtrmib-_mib_ipmcast_scope)
-   [**MIB\_MCAST\_LIMIT\_ROW**](/windows/desktop/api/Iprtrmib/ns-iprtrmib-mib_mcast_limit_row)
-   [**MIB\_MFE\_STATS\_TABLE\_EX**](/previous-versions/windows/desktop/api/Ipmib/ns-ipmib-_mib_mfe_stats_table_ex_xp)

 

 




