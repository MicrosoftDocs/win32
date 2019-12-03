---
title: Configuring SAP and RPC
description: Novell NetWare network servers use the Service Advertising Protocol (SAP) to broadcast information about available services on the network to other networked devices.
ms.assetid: 6d6ef481-fc09-4795-8954-33329912ff4f
ms.topic: article
ms.date: 05/31/2018
---

# Configuring SAP and RPC

Novell NetWare network servers use the Service Advertising Protocol (SAP) to broadcast information about available services on the network to other networked devices. A server may send out an SAP broadcast every 60 seconds to inform other network devices about the services it offers. Workstations use SAPs to find services they need on the network.

Windows includes a SAP Agent service to enable Windows-based servers to interact with NetWare servers. The SAP Agent service will listen for network clients' SAP requests for IPX-based services that are installed and running on the server.

Software that is designed to be advertised as a service over the network by means of a SAP broadcast will issue the SAP announcements every 60 seconds, without having the SAP Agent installed. However, in order for network clients to quickly locate an IPX network service, a server that maintains a service database must be available on the network, to respond to the service location request. This service database is usually maintained by a Novell NetWare or by a NetWare compatible server. Microsoft File and Print Services for NetWare will also maintain an IPX network service database.

On a computer running Windows Server, if Gateway Services for NetWare (GSNW) is installed, a SAP Type 640 will broadcast every 60 seconds by the remote procedure call (RPC) service. This SAP broadcast will continue even if the user disables the GSNW and the SAP Agent Service.

The RPC service will do the SAP broadcast if the Client Services for NetWare (CSNW) and the SAP Agent service are installed. This SAP broadcast will continue even if the user disables the SAP agent.

By default, the RPC service will check for the presence of Gateway Services for NetWare and the SAP Agent service on the computer running Windows Server. Installing File and Print services for NetWare installs a SAP Agent.

On the computer running a client version of Windows with CSNW, the RPC service checks for the SAP Agent service. If the services are present, RPC will start its own thread that will do the SAP broadcast Type 640 every minute.

> [!NOTE]
> If you don't want SAP broadcasts on the network every 60 seconds, you can disable SAP broadcasts using the Registry Editor. Be warned that using Registry Editor incorrectly can cause serious problems that may require you to reinstall your operating system. Microsoft cannot guarantee that problems resulting from the incorrect use of Registry Editor can be solved. Use Registry Editor at your own risk. You should back up the registry before you edit it.

 

**To configure for SAP**

1.  Run Registry Editor (Regedt32.exe) and go to the following key in the registry:

    **HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\RPC**

2.  On the **Edit** menu, click **Add Value**, and use the following entry:
    1.  Value Name: AdvertiseRpcService
    2.  Data Type: REG\_SZ
    3.  String: No
3.  Using No for the string turns RPC SAP broadcasting off. Using Yes for the string turns RPC SAP broadcasting on.
4.  Restart the computer for the registry change to take effect.
    > [!NOTE]
    > If the SAP broadcasts continue after following these steps, you may want to try a troubleshooting step. Delete the **Ncacn\_spx** string value in the following registry key:
    >
    > **HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\Rpc\\ServerProtocols\\**

     

> [!NOTE]  
> This should be used only as a troubleshooting step. Deleting this string value completely disables SAP broadcasts which some programs may need in order to function properly.