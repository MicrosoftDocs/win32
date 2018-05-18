---
title: What's New in MIB
description: On the Microsoft Windows Software Development Kit (SDK) released for Windows Vista and later, the organization of header files has changed and some of the older MIB structures are defined in the Ipmib.h header file not in the Iprtrmib.h header file.
ms.assetid: '213b88b6-56b0-4d70-9765-c61094f6f9ff'
---

# What's New in MIB

On the Microsoft Windows Software Development Kit (SDK) released for Windows Vista and later, the organization of header files has changed and some of the older MIB structures are defined in the *Ipmib.h* header file not in the *Iprtrmib.h* header file. Note that the *Ipmib.h* header file is automatically included in *Iprtrmib.h* which is automatically included in the *Iphlpapi.h* header file. The new MIB structures introduced with Windows Vista and later are defined in the *Netioapi.h* which is automatically included in the *Iphlpapi.h* header file. The *Ipmib.h*, *Iprtrmib.h*, and *Netioapi.h* header files should never be used directly.

## Windows 8 and Windows Server 2012

The following structure has been added to the Management Information Base for Windows 8 and Windows Server 2012:

-   [**MIB\_IP\_NETWORK\_CONNECTION\_BANDWIDTH\_ESTIMATES**](mib-ip-network-connection-bandwidth-estimates.md)

## Windows Vista

The following structures and enumerations have been added to the Management Information Base for Windows Vista:

-   [**MIB\_ANYCASTIPADDRESS\_ROW**](mib-anycastipaddress-row.md)
-   [**MIB\_ANYCASTIPADDRESS\_TABLE**](mib-anycastipaddress-table.md)
-   [**MIB\_IFSTACK\_ROW**](mib-ifstack-row.md)
-   [**MIB\_IFSTACK\_TABLE**](mib-ifstack-table.md)
-   [**MIB\_IF\_ROW2**](mib-if-row2.md)
-   [**MIB\_IF\_TABLE2**](mib-if-table2.md)
-   [**MIB\_INVERTEDIFSTACK\_ROW**](mib-invertedifstack-row.md)
-   [**MIB\_INVERTEDIFSTACK\_TABLE**](mib-invertedifstack-table.md)
-   [**MIB\_IPFORWARD\_ROW2**](mib-ipforward-row2.md)
-   [**MIB\_IPFORWARD\_TABLE2**](mib-ipforward-table2.md)
-   [**MIB\_IPINTERFACE\_ROW**](mib-ipinterface-row.md)
-   [**MIB\_IPINTERFACE\_TABLE**](mib-ipinterface-table.md)
-   [**MIB\_IPNET\_ROW2**](mib-ipnet-row2.md)
-   [**MIB\_IPNET\_TABLE2**](mib-ipnet-table2.md)
-   [**MIB\_IPPATH\_ROW**](mib-ippath-row.md)
-   [**MIB\_IPPATH\_TABLE**](mib-ippath-table.md)
-   [**MIB\_MULTICASTIPADDRESS\_ROW**](mib-multicastipaddress-row.md)
-   [**MIB\_MULTICASTIPADDRESS\_TABLE**](mib-multicastipaddress-table.md)
-   [**MIB\_NOTIFICATION\_TYPE**](mib-notification-type.md)
-   [**MIB\_TCP6ROW**](mib-tcp6row.md)
-   [**MIB\_TCP6ROW2**](mib-tcp6row2.md)
-   [**MIB\_TCP6TABLE**](mib-tcp6table.md)
-   [**MIB\_TCP6TABLE2**](mib-tcp6table2.md)
-   [**MIB\_TCPROW2**](mib-tcprow2.md)
-   [**MIB\_TCPTABLE2**](mib-tcptable2.md)
-   [**MIB\_UDP6ROW**](mib-udp6row.md)
-   [**MIB\_UDP6TABLE**](mib-udp6table.md)
-   [**MIB\_UNICASTIPADDRESS\_TABLE**](mib-unicastipaddress-table.md)
-   [**NL\_INTERFACE\_OFFLOAD\_ROD**](nl-interface-offload-rod.md)
-   [**TCP\_CONNECTION\_OFFLOAD\_STATE**](tcp-connection-offload-state.md)

## Windows Server 2003 Service Pack 1

The following structures have been added to the Management Information Base for Windows Server 2003 with Service Pack 1 (SP1):

-   [**MIB\_BOUNDARYROW**](mib-boundaryrow.md)
-   [**MIB\_IPMCAST\_BOUNDARY**](mib-ipmcast-boundary.md)
-   [**MIB\_IPMCAST\_BOUNDARY\_TABLE**](mib-ipmcast-boundary-table.md)
-   [**MIB\_IPMCAST\_MFE\_STATS\_EX**](mib-ipmcast-mfe-stats-ex.md)
-   [**MIB\_IPMCAST\_SCOPE**](mib-ipmcast-scope.md)
-   [**MIB\_MCAST\_LIMIT\_ROW**](mib-mcast-limit-row.md)
-   [**MIB\_MFE\_STATS\_TABLE\_EX**](mib-mfe-stats-table-ex.md)

 

 




