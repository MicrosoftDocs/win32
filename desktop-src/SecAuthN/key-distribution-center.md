---
description: The Key Distribution Center (KDC) is implemented as a domain service. It uses the Active Directory as its account database and the Global Catalog for directing referrals to KDCs in other domains.
ms.assetid: f2a7c87c-9be7-4fd8-8ecd-4edf1f2336ef
title: Key Distribution Center
ms.topic: article
ms.date: 05/31/2018
---

# Key Distribution Center

The Key Distribution Center (KDC) is implemented as a domain service. It uses the Active Directory as its account database and the Global Catalog for directing referrals to KDCs in other domains.

As in other implementations of the [*Kerberos protocol*](../secgloss/k-gly.md), the KDC is a single process that provides two services:

-   Authentication Service (AS)

    This service issues ticket-granting tickets (TGTs) for connection to the ticket-granting service in its own domain or in any trusted domain. Before a client can ask for a ticket to another computer, it must request a TGT from the authentication service in the client's account domain. The authentication service returns a TGT for the ticket-granting service in the target computer's domain. The TGT can be reused until it expires, but the first access to any domain's ticket-granting service always requires a trip to the authentication service in the client's account domain.

-   Ticket-Granting Service (TGS)

    This service issues tickets for connection to computers in its own domain. When clients want access to a computer, they contact the ticket-granting service in the target computer's domain, present a TGT, and ask for a ticket to the computer. The ticket can be reused until it expires, but the first access to any computer always requires a trip to the ticket-granting service in the target computer's account domain.

The KDC for a domain is located on a domain controller, as is the Active Directory for the domain. Both services are started automatically by the domain controller's [*Local Security Authority*](../secgloss/l-gly.md) (LSA) and run as part of the LSA's process. Neither service can be stopped. If the KDC is unavailable to network clients, then the Active Directory is also unavailable—and the domain controller is no longer controlling the domain. The system ensures availability of these and other domain services by allowing each domain to have several domain controllers, all peers. Any domain controller can accept authentication requests and ticket-granting requests addressed to the domain's KDC.

The [*security principal*](../secgloss/s-gly.md) name used by the KDC in any domain is "krbtgt", as specified by [RFC 4120](https://www.ietf.org/rfc/rfc4120.txt). An account for this security principal is created automatically when a new domain is created. The account cannot be deleted, nor can the name be changed. A random password value is assigned to the account automatically by the system during the creation of the domain. The password for the KDC's account is used to derive a cryptographic key for encrypting and decrypting the TGTs that it issues. The password for a domain trust account is used to derive an inter-realm key for encrypting referral tickets.

All instances of the KDC within a domain use the domain account for the security principal "krbtgt". Clients address messages to a domain's KDC by including both the service's principal name, "krbtgt", and the name of the domain. Both items of information are also used in tickets to identify the issuing authority. For information about name forms and addressing conventions, see [RFC 4120](https://www.ietf.org/rfc/rfc4120.txt).

 

 
