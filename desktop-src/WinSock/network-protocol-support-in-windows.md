---
description: The Internet Protocol Suite is the dominant network protocol used in enterprise networks and across the Internet.
ms.assetid: 8c123e09-b11a-4c92-b41e-49cc01be53d3
title: Winsock Network Protocol Support in Windows
ms.topic: article
ms.date: 05/31/2018
---

# Winsock Network Protocol Support in Windows

The Internet Protocol Suite is the dominant network protocol used in enterprise networks and across the Internet. The Internet Protocol Suite represents a large collection of layered network protocols. The Internet Protocol Suite is often referred to as TCP/IP based on two of the most important protocols included in the suite: the Internet Protocol (IP) and the Transmission Control Protocol (TCP).

IPv6 and IPv4 represent the two available versions of the Internet Protocol. TCP is one of several important network services often referred to as IP protocols that operate over IPv6 and IPv4 networks. The User Datagram Protocol (UDP) and Internet Control Message Protocol (ICMP) are other important IP protocols used over IPv6 and IPv4 networks. There are a number of other IP protocols that can be used over IPv6 and IPv4 networks.

Windows Sockets considers each network protocol suite as a unique address family. So the IPv6 protocol is considered the **AF\_INET6** address family and the IPv4 protocol is considered the **AF\_INET** address family. The IPv6 and IPv4 protocols support the use of various layered IP protocols such as TCP, UDP, and ICMP.

Windows Sockets were initially designed to add support for IPv4 to Windows. However, the Windows Sockets programming interface was designed from the onset with the ability to support other network protocol suites. Over time, versions of Windows and the associated Windows Sockets have included native support for other network protocol suites (IPX/SPX and AppleTalk, for example). Support for other network protocols was also available for versions of Windows as third-party software from vendors.

Before the growth and popularity of the Internet, various other network protocol suites were used in networked environments, particularly for local Intranets. The choice of a network protocol suite was often based on the size of the network or the expertise of the IT networking staff. With today's global Internet connectivity linking even the smallest networks to the rest of the world, networking expertise in IPv6 and IPv4 is essential for networking professionals. As a result, other previously important network protocol suites are now in very limited use and have become obviated. Native support for these obviated network protocol suites, often referred to as legacy network protocols, has been dropped from recent versions of Microsoft Windows. Support for some of these legacy protocols may be available as third-party software from vendors (ATM with ATM network hardware, for example).

The following table identifies native Windows support for common network protocol suites. 

| Network Protocol                 | Windows 7                | Windows Server 2008      | Windows Vista            | Windows Server 2003                  | Windows XP                           | Windows 2000                         |
|----------------------------------|--------------------------|--------------------------|--------------------------|--------------------------------------|--------------------------------------|--------------------------------------|
| IPv6<br/>                  | Supported<br/>     | Supported<br/>     | Supported<br/>     | Supported<br/>                 | Supported<br/>                 | Not supported (see Notes)<br/> |
| IPv4<br/>                  | Supported<br/>     | Supported<br/>     | Supported<br/>     | Supported<br/>                 | Supported<br/>                 | Supported<br/>                 |
| NetBIOS (see Notes) <br/>  | Supported<br/>     | Supported<br/>     | Supported<br/>     | Supported<br/>                 | Supported<br/>                 | Supported<br/>                 |
| IrDA (see Notes)<br/>      | Supported<br/>     | Supported<br/>     | Supported<br/>     | Supported<br/>                 | Supported<br/>                 | Supported<br/>                 |
| Bluetooth (see Notes)<br/> | Supported<br/>     | Supported<br/>     | Supported<br/>     | Supported<br/>                 | Supported<br/>                 | Not supported<br/>             |
| IPX/SPX<br/>               | Not supported<br/> | Not supported<br/> | Not supported<br/> | Supported<br/>                 | Supported<br/>                 | Supported<br/>                 |
| AppleTalk<br/>             | Not supported<br/> | Not supported<br/> | Not supported<br/> | Supported<br/>                 | Supported<br/>                 | Supported<br/>                 |
| DLC<br/>                   | Not supported<br/> | Not supported<br/> | Not supported<br/> | Not supported (see Notes)<br/> | Not supported (see Notes)<br/> | Supported<br/>                 |
| ATM<br/>                   | Not supported<br/> | Not supported<br/> | Not supported<br/> | Supported (see Notes)<br/>     | Supported (see Notes)<br/>     | Supported (see Notes)<br/>     |
| NetBEUI<br/>               | Not supported<br/> | Not supported<br/> | Not supported<br/> | Not supported<br/>             | Not supported<br/>             | Supported (see Notes)<br/>     |



 

**IPv6 on Windows 2000:** The IPv6 protocol is supported on Windows 2000 with Service Pack 1 (SP1) and later with the Microsoft IPv6 Technology Preview for Windows 2000.

**NetBIOS:** The NetBIOS protocol is commonly used by naming services on Windows. NetBIOS can use multiple network protocol suites including IP (NetBIOS over TCP/IP), IPX/SPX, and NetBEUI. Winsock supports NetBIOS over TCP/IP (commonly call NetBT) only on the 32-bit versions of Windows 7, Windows Server 2008, and Windows Vista. Winsock supports NetBIOS over TCP/IP and NetBIOS using IPX on Windows Server 2003 and Windows XP. Winsock supports NetBIOS over TCP/IP, NetBIOS using IPX, and NetBIOS using NetBEUI on Windows 2000.

**IrDA:** The Infrared Data Association (IrDA) protocol is supported if the computer has an infrared port and driver installed.

**Bluetooth:** Winsock support for Bluetooth as a network protocol suite includes the Bluetooth Personal Area Network (PAN) and Dial up Networking (DUN) profiles. Bluetooth support in Windows also includes using the Bluetooth Human Interface Device (HID) and other profiles for connecting to keyboards, pointing devices, and other input devices which are unrelated to network protocols.

**DLC on Windows 2003 and Windows XP:** The Data Link Control (DLC) protocol is supported on Windows Server 2003 and Windows XP when the DLC driver included with Microsoft Host Integration Server 2006, Host Integration Server 2004, or Host Integration Server 2000 is installed.

**ATM on Windows 2003, Windows XP, and Windows 2000:** The Asynchronous Transfer Mode (ATM) protocol is supported on Windows Server 2003, Windows XP, and Windows 2000 when an ATM network adapter is installed. The protocol for classical IP over ATM (sometimes abbreviated as CLIP/ATM) is defined in [RFC 2225](https://tools.ietf.org/html/rfc2225) and related documents published by the IETF. Windows Server 2003, Windows XP, and Windows 2000 provide a full implementation of this standard.

**NetBEUI on Windows 2000:** The NetBEUI protocol is not directly supported by Windows sockets. But the NetBIOS protocol which may use multiple network protocols supports using the NetBEUI protocol on Windows 2000.

## Related topics

<dl> <dt>

[ATM Technical Reference](/previous-versions/windows/it-pro/windows-server-2003/cc759707(v=ws.10))
</dt> <dt>

[Bluetooth](../bluetooth/bluetooth-start-page.md)
</dt> <dt>

[IPv6 Technology Preview for Windows 2000](https://www.microsoft.com/downloads/details.aspx?FamilyID=27b1e6a6-bbdd-43c9-af57-dae19795a088)
</dt> <dt>

[IrDA](/previous-versions/windows/desktop/irda/irda-start-page)
</dt> <dt>

[NDIS 5.0 and ATM Support in Windows](/windows-hardware/drivers/network/ndis-version-guide)
</dt> </dl>

 

 
