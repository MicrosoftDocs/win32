---
title: Teredo Addresses
ms.assetid: e2e185c2-e53d-471d-aedb-54d75f9db0bb
description: "Learn more about: Teredo Addresses"
ms.topic: article
ms.date: 05/31/2018
---

# Teredo Addresses

A Teredo address consists of the following:

-   **Teredo prefix**

    The first 32 bits are for the Teredo prefix, which is the same for all Teredo addresses. Windows XP and Windows Server 2003 initially used the 3FFE:831F::/32 Teredo prefix. The prefix defined for Teredo in RFC 4380 is 2001::/32 and is the prefix used by Teredo in Windows Vista and Windows Server 2008. Computers running Windows XP and Windows Server 2003 will use the 2001::/32 Teredo prefix when updated with Microsoft Security Bulletin MS06-064.

-   **Teredo server IPv4 address**

    The next 32 bits contain the IPv4 public address of the Teredo server that helped configure this Teredo address. For more information, see "Initial configuration for Teredo clients" in this article.

-   **Flags**

    The next 16 bits for are reserved for Teredo flags. For Windows XP-based Teredo clients, the only defined flag is the high order bit known as the Cone flag. The Cone flag is set when Teredo client is behind a cone NAT. The determination of whether the NAT connected to the Internet is a cone NAT occurs during the Teredo client's initial configuration. For more information, see "Initial configuration for Teredo clients" in this article.

    For Windows Vista and Windows Server 2008-based Teredo clients, unused bits within the Flags field provide a level of protection from address scans by malicious users. The 16 bits within the Flags field for Windows Vista and Windows Server 2008-based Teredo clients consists of the following: CRAAAAUG AAAAAAAA. The C bit is for the Cone flag. The R bit is reserved for future use. The U bit is for the Universal/Local flag (set to 0). The G bit is Individual/Group flag (set to 0). The A bits are set to a 12-bit randomly generated number. By using a random number for the A bits, a malicious user that has determined the rest of the Teredo address by capturing the initial configuration exchange of packets between the Teredo client and Teredo server will have to try up to 4,096 (212) different addresses to determine a Teredo client's address during an address scan.

-   **Obscured external port**

    The next 16 bits store an obscured version of the external UDP port corresponding to all Teredo traffic for this Teredo client. When the Teredo client sends its initial packet to a Teredo server, the source UDP port of the packet is mapped by the NAT to a different, external UDP port. The Teredo client maintains this port mapping so that it remains in the NAT's translation table. Therefore, all Teredo traffic for the host uses the same external, mapped UDP port. The external UDP port is determined by the Teredo server from the source UDP port of the incoming initial packet sent by the Teredo client and sent back to the Teredo client.

    The external port is obscured by XORing the external port with 0xFFFF. For example, the obscured version of the external port 5000 in hexadecimal format is EC77 (5000 = 0x1388, 0x1388 XOR 0xFFFF = 0xEC77). Obscuring the external port prevents NATs from translating the external port within the payload of the packets that they are forwarding.

-   **Obscured external address**

    The last 32 bits store an obscured version of the external IPv4 address corresponding to all Teredo traffic for this Teredo client. Just like the external port, when the Teredo client sends its initial packet to a Teredo server, the source IP address of the packet is mapped by the NAT to a different, external (public) address. The Teredo client maintains this address mapping so that it remains in the NAT's translation table. Therefore, all Teredo traffic for the host uses the same external, mapped, public IPv4 address. The external IPv4 address is determined by the Teredo server from the source IPv4 address of the incoming initial packet sent by the Teredo client and sent back to the Teredo client.

    The external address is obscured by XORing the external address with 0xFFFFFFFF. For example, the obscured version of the public IPv4 address 131.107.0.1 in colon-hexadecimal format is 7C94:FFFE (131.107.0.1 = 0x836B0001, 0x836B0001 XOR 0xFFFFFFFF = 0x7C94FFFE). Obscuring the external address prevents NATs from translating the external address within the payload of the packets that they are forwarding.

 

 




