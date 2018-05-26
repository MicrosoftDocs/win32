---
Description: IP Helper extends your abilities to manage network interfaces. There is a one-to-one correspondence between the interfaces and adapters on a given computer. An interface is an IP-level abstraction, whereas an adapter is a datalink-level abstraction.
ms.assetid: 598bbe67-30df-4c02-8f30-2ccf15b5c494
title: Managing Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Managing Interfaces

IP Helper extends your abilities to manage network interfaces. There is a one-to-one correspondence between the interfaces and adapters on a given computer. An interface is an IP-level abstraction, whereas an adapter is a datalink-level abstraction.

Use the functions described in the following paragraphs to manage interfaces on the local computer.

The [**GetNumberOfInterfaces**](/windows/win32/Iphlpapi/nf-iphlpapi-getnumberofinterfaces?branch=master) function returns the number of interfaces on the local computer.

The [**GetInterfaceInfo**](/windows/win32/Iphlpapi/nf-iphlpapi-getinterfaceinfo?branch=master) function returns a table that contains the names and corresponding indexes for the interfaces on the local computer. For code samples involving **GetInterfaceInfo** see [Managing Interfaces Using GetInterfaceInfo](managing-interfaces-using-getinterfaceinfo.md).

The [**GetFriendlyIfIndex**](/windows/win32/Iphlpapi/nf-iphlpapi-getfriendlyifindex?branch=master) function takes an interface index and returns a backward-compatible interface index, that is, one that uses only the lower 24 bits. This type of index is sometimes referred to as a "friendly" interface index.

The [**GetIfEntry**](/windows/win32/Iphlpapi/nf-iphlpapi-getifentry?branch=master) function returns a [**MIB\_IFROW**](mib.mib_ifrow) structure that contains information about a particular interface on the local computer. This function requires the caller to supply the index of the interface.

The [**GetIfTable**](/windows/win32/Iphlpapi/nf-iphlpapi-getiftable?branch=master) function returns a table of [**MIB\_IFROW**](mib.mib_ifrow) entries, one for each interface on the computer.

Use the [**SetIfEntry**](/windows/win32/Iphlpapi/nf-iphlpapi-setifentry?branch=master) function to modify the configuration of a particular interface.

 

 



