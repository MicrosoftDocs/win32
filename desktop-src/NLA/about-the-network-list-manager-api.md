---
title: About the Network List Manager API
description: About the Network List Manager API
ms.assetid: 675cf7ed-9f57-4d62-8091-1f4e8812f2ad
ms.topic: article
ms.date: 05/31/2018
---

# About the Network List Manager API

The Microsoft Windows networking environment allows multihomed computers to connect to several networks simultaneously. There may be multiple wireless networks available along with LAN and dial-up connections. Network List Manager identifies available networks and returns network attribute data to the application.

The Network List Manager API interacts with the Network List Manager service to identify and retrieve properties of each network that the PC connects to. Each network is uniquely identified with a network signature based on the uniquely identifiable properties of that network. When an application registers for Network List Manager notifications, the application receives notifications about the availability of new network connections or changes to existing network connections. Applications can adjust their logic depending on: which network they are connected to; which network connection they are connected to; or what the network properties are. With this information applications can fine tune their actions based on current network conditions

Windows Vista introduces new interfaces that can be used to obtain detailed information about these network characteristics and more. With the [**INetworkListManager**](/windows/desktop/api/Netlistmgr/nn-netlistmgr-inetworklistmanager) interface it is easy to enumerate all networks ([**INetwork**](/windows/desktop/api/Netlistmgr/nn-netlistmgr-inetwork)) a computer has ever seen, or just the connected networks, or just the disconnected networks. The **INetworkListManager** interface also makes it easy to enumerate the network interfaces on a computer.

The [**INetwork**](/windows/desktop/api/Netlistmgr/nn-netlistmgr-inetwork) interface is used to determine the properties of a network connection: name, description, ID, managed/authenticated, connected/disconnected, and more. It is possible that a single network is connected to several interfaces, so through an **INetwork** interface you can also enumerate the instances of the **INetwork** interface being used.

The [**INetwork**](/windows/desktop/api/Netlistmgr/nn-netlistmgr-inetwork) interface tells you the relevant properties of an interface: ID, GUID, Type (managed, authenticated), and State (connected, disconnected, V4 Local, V4 Internet, V6 Local, V6 Internet). V4 Local means Internet Protocol version 4 (IPv4) local access. V4 Internet means IPv4 with internet access. V6 Local and V6 Internet mean IPv6.

The root of the object tree for Network Location is the [**INetworkListManager**](/windows/desktop/api/Netlistmgr/nn-netlistmgr-inetworklistmanager) interface. This interface is implemented on the **CLSID\_NetworkListManager** coclass. In order to use this interface, it is necessary to create the **CLSID\_NetworkListManager** COM object as demonstrated:


```C++
#include <windows.h>
#include <netlistmgr.h>

#pragma comment(lib, "ole32.lib")

void main()
{
    INetworkListManager *pNetworkListManager = NULL; 
    HRESULT hr = CoCreateInstance(CLSID_NetworkListManager, NULL,
            CLSCTX_ALL, IID_INetworkListManager,
            (LPVOID *)&pNetworkListManager);
}
```



 

 




