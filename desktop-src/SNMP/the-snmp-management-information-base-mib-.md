---
title: The SNMP Management Information Base (MIB)
description: A Management Information Base (MIB) describes a set of managed objects. An SNMP management console application can manipulate the objects on a specific computer if the SNMP service has an extension agent DLL that supports the MIB.
ms.assetid: 684200b6-a5e4-42bb-8a01-fcb6100967c0
ms.topic: article
ms.date: 05/31/2018
---

# The SNMP Management Information Base (MIB)

A Management Information Base (MIB) describes a set of managed objects. An SNMP management console application can manipulate the objects on a specific computer if the SNMP service has an extension agent DLL that supports the MIB.

Each managed object in a MIB has a unique identifier. The identifier includes the object's type (such as counter, string, gauge, or address), the object's access level (such as read or read/write), size restrictions, and range information.

The following table contains a partial list of the MIBs that ship with the system. They are installed with the SNMP service in the %systemroot%\\system32 directory. For a complete listing of MIBs, refer to the Windows Resource Kit.



| MIB         | Description                                                                                                                                      |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| DHCP.MIB    | Microsoft-defined MIB that contains object types for monitoring the network traffic between remote hosts and DHCP servers                        |
| HOSTMIB.MIB | Contains object types for monitoring and managing host resources                                                                                 |
| LMMIB2.MIB  | Covers workstation and server services                                                                                                           |
| MIB\_II.MIB | Contains the Management Information Base (MIB-II), which provides a simple, workable architecture and system for managing TCP/IP-based internets |
| WINS.MIB    | Microsoft-defined MIB for the Windows Internet Name Service (WINS)                                                                               |



 

**Windows NT:** Typically, you can copy a MIB from the SNMP extension agent that supports the particular MIB. Some additional MIBs are available with the Windows NT 4.0 Resource Kit.

The extension agent DLLs for MIB-II, LAN Manager MIB-II, and the Host Resources MIB are installed with the SNMP service. The extension agent DLLs for the other MIBs are installed when their respective services are installed. At service startup time, the SNMP service loads all of the extension agent DLLs that are listed in the registry.

Users can add other extension agent DLLs that implement additional MIBs. To do this, they must add a registry entry for the new DLL under the SNMP service. They must also register the new MIB with the SNMP management console application. For more information, see the documentation included with your management console application.

For more information, see [MIB Name Tree](mib-name-tree.md).

 

 




