---
title: Virtual Private Network Connections
description: The Remote Access Service (RAS) supports Virtual Private Network (VPN) connections in addition to conventional remote access connections that use Point-to-Point Protocol (PPP).
ms.assetid: c1195ebb-3107-4429-bc67-b64577d66268
ms.topic: article
ms.date: 05/31/2018
---

# Virtual Private Network Connections

The Remote Access Service (RAS) supports Virtual Private Network (VPN) connections in addition to conventional remote access connections that use Point-to-Point Protocol (PPP). In a VPN connection, the VPN packets are encapsulated in IP packets and sent across an IP network such as the Internet. Therefore, access to an IP network is a requirement in order to establish a VPN connection. If the client computer has an always-on connection to an IP network, for example a connection to an IP LAN, the client can establish the VPN connection using a single call to the [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) function.

If the client computer does not have an always-on connection to an IP network, two calls to [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) are required to establish the VPN connection. The first call establishes a dial-up connection to the IP network; the second call establishes the VPN connection.

The **szLocalPhoneNumber** member of the [**RASENTRY**](/previous-versions/windows/desktop/legacy/aa377274(v=vs.85)) structure for the VPN connection should contain either the DNS name or IP address of the destination VPN server.

Each connection requires a separate [phone-book](ras-phone-books.md) entry. The first call to [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) specifies the phone-book entry for the IP network. The second call specifies the phone-book entry for the VPN.

The [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) function takes a pointer to a [**RASDIALPARAMS**](/previous-versions/windows/desktop/legacy/aa377238(v=vs.85)) structure as a parameter. This structure specifies the authentication credentials to use for the network specified by the phone-book entry. The credentials required to access the IP network are typically different from those for the VPN. The first call to **RasDial** should specify credentials for the IP network. The second call should specify credentials for the VPN.

If the [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) function is successful, it returns a handle for the connection. Use this handle in a call to [**RasHangUp**](/windows/desktop/api/Ras/nf-ras-rashangupa) to terminate the connection.

In the preceding scenario, the two calls to [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) return separate connection handles for the IP network and the VPN. Calling [**RasHangUp**](/windows/desktop/api/Ras/nf-ras-rashangupa) with the handle for the VPN connection terminates the VPN connection but leaves the connection to the IP network intact.

 

 