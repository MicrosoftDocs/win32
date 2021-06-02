---
description: Peer groups require that each member have a specific certificate, which is called a Group Member Certificate (GMC).
ms.assetid: 3966d4eb-4504-4b1e-9c9f-6eab7751d7ed
title: How Group Security Works
ms.topic: article
ms.date: 05/31/2018
---

# How Group Security Works

Peer groups require that each member have a specific certificate, which is called a Group Member Certificate (GMC). The GMC certificate ensures that all records exchanged between peers are digitally signed. The public key of a peer is contained in the structures that are passed as part of the communication between peers—including [**PEER\_CREDENTIAL\_INFO**](/windows/desktop/api/P2P/ns-p2p-peer_credential_info).

A GMC can be issued in a chain. For example, a creator can issue a GMC to administrator A, who can issue a GMC to administrator B, who can issue a GMC to member M. The resulting GMC chain is: creator->A->B->M, which has a length of 4. The chain length is important, because it cannot be longer than 24. If the 24th administrator in a chain attempts to issue a GMC to a member, [**PeerGroupIssueCredentials**](/windows/desktop/api/P2P/nf-p2p-peergroupissuecredentials) or [**PeerGroupCreateInvitation**](/windows/desktop/api/P2P/nf-p2p-peergroupcreateinvitation) returns PEER\_E\_CHAIN\_TOO\_LONG.

A GMC can also be issued by calling [**PeerGroupIssueCredentials**](/windows/desktop/api/P2P/nf-p2p-peergroupissuecredentials). A GMC implies user membership in the group that the GMC is issued for, and can have a finite or infinite lifetime. Group member activity cannot be longer than the lifetime specified in the GMC.

> [!Note]  
> Infinite GMC lifetime is currently set at 1000 years.

 

Group member activity is limited by the GMC lifetime and includes the following:

-   **Record operations** - A peer cannot publish information in a group after the group membership expires, or publish records that have a lifetime longer than the peer's group membership lifetime.
-   **Membership operations** - A group administrator cannot issue a membership that has a lifetime beyond the date specified in the group administrator membership. For example, if an administrator has 500 hours remaining on its GMC lifetime, all memberships issued must be less than 500 hours.

Because a group member cannot have a lifetime longer than the administrator who invites that group member, it is recommended that you set the GMC lifetime of an administrator as infinite, or for a very long lifetime. The group creator has an infinite lifetime by default.

## Renewing Group Membership

To renew the credentials of an administrator or member whose GMC lifetime is ready to expire, you have the following two options:

-   Call [**PeerGroupIssueCredentials**](/windows/desktop/api/P2P/nf-p2p-peergroupissuecredentials) and pass the identity of the member whose lifetime is ready to expire. If the credentials are specified as **NULL** and the peer's membership information is available to the group, the renewal time is set to the same duration that is specified in the previously published member credentials. If a different duration period must be specified, a new [**PEER\_CREDENTIAL\_INFO**](/windows/desktop/api/P2P/ns-p2p-peer_credential_info) structure must be provided that contains the new lifetime duration, and then a new GMC is published for the member.

    The [**PeerGroupIssueCredentials**](/windows/desktop/api/P2P/nf-p2p-peergroupissuecredentials) function optionally takes the PEER\_GROUP\_STORE\_CREDENTIALS flag, which automatically publishes the new credentials of the member in the group database. When the member connects to the group the next time, for either the first time or after going offline, the member obtains the updated GMC from the database.

-   Call [**PeerGroupCreateInvitation**](/windows/desktop/api/P2P/nf-p2p-peergroupcreateinvitation) to pass the identity of the member whose GMC lifetime is ready to expire. If the expiration specified in the invitation is **NULL**, the lifetime duration of the GMC is the same as the administrator GMC who issues membership. If the creator specifies the expiration as **NULL**, a GMC with an infinite lifetime is issued.

    If a peer is issued a GMC that expires before the presence lifetime value, the addresses of the peer are not available in the [**PEER\_MEMBER**](/windows/desktop/api/P2P/ns-p2p-peer_member) structures returned in the enumeration initiated by a call to [**PeerGroupEnumMembers**](/windows/desktop/api/P2P/nf-p2p-peergroupenummembers). This happens because presence information is not published in this case, even if the PEER\_DISABLE\_PRESENCE flag is not set.

 

 



