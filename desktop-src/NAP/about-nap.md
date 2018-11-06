---
title: About NAP
description: About NAP
ms.assetid: c5dc4956-dcb7-4fcf-b4cc-2fac016427dd
ms.topic: article
ms.date: 05/31/2018
---

# About NAP

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

Network Access Protection (NAP) is designed to help administrators maintain the health of the computers on the network, which in turns helps maintain the overall integrity of the network. It is not designed to secure a network from malicious users. For example, if a computer has all the software and configurations that the network access policy requires, the computer is considered healthy or compliant, and it will be granted the appropriate access to the network. NAP does not prevent an authorized user with a compliant computer from uploading a malicious program to the network or engaging in other inappropriate behavior.

To protect access to a network, a network infrastructure needs to provide the following areas of functionality:

-   Health validation: Determines whether the computers are compliant with system health requirements.
-   Network restriction: Restricts access to the network or communication for clients that do not comply with system health requirements.
-   Remediation: Provides necessary updates to allow the computer to correct its noncompliant health state.
-   Ongoing compliance: Permits access to the network as long as the user's computer meets health policy requirements.

Windows XP with Service Pack 3 (SP3), Windows Vista, and Windows Server 2008 provide NAP enforcement methods for Dynamic Host Configuration Protocol (DHCP) address configuration, remote access-based virtual private network (VPN) connections, IEEE 802.1X-authenticated wired and wireless connections, and Internet Protocol security (IPsec)-based communications. The NAP platform additionally supports an architecture through which health validation, network restriction, remediation, and ongoing compliance are supported by additional components that can be supplied by third-party software vendors or by Microsoft.

The NAP platform includes the following components:

-   [NAP Client Architecture](nap-client-architecture.md)
-   [NAP Server-side Architecture](nap-server-side-architecture.md)
-   [NAP Client and Server-side Component Communication](nap-client-and-server-side-component-communication.md)

The NAP client requires Windows Vista, Windows XP with SP3, or Windows Server 2008. The NAP health policy server and NAP enforcement points for DHCP, VPN, and IPsec enforcement require Windows Server 2008.

 

 




