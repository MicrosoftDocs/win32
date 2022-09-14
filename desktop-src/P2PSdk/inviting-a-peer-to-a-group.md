---
description: This topic discusses the process of inviting a peer to join a peer group using the Peer Grouping APIs.
ms.assetid: 6afcbfec-b1df-45cd-8a43-221dfe5d8c33
title: Inviting a Peer to a Group
ms.topic: article
ms.date: 05/31/2018
---

# Inviting a Peer to a Group

This topic discusses the process of inviting a peer to join a peer group using the Peer Grouping APIs.

A peer group requires valid credentials to participate. Credentials are issued from outside a group in the form of invitations, or directly to members within a group when credential updates are needed.

## Group Member Certificates

A peer group is created when an application makes a call to [**PeerGroupCreate**](/windows/desktop/api/P2P/nf-p2p-peergroupcreate).

To participate in a peer group, each peer must have a peer identity. Call [**PeerEnumIdentities**](/windows/desktop/api/P2P/nf-p2p-peerenumidentities) until all peer identities defined for the peer have been returned, and select the one that should be used. If a peer identity does not exist, create one by calling [**PeerIdentityCreate**](/windows/desktop/api/P2P/nf-p2p-peeridentitycreate).

Each peer identity is associated with a specific set of credentials that can be used to prove peer group membership when connecting, as well as when publishing records or inviting additional members. These credentials are represented as chains of [X.509 certificates](https://www.ietf.org/rfc/rfc2511.txt) called Group Membership Certificates (GMC).

To create the GMC for a peer identity, you must first obtain its public key. This key is obtained by calling [**PeerIdentityGetXML**](/windows/desktop/api/P2P/nf-p2p-peeridentitygetxml) on the potential invitee and passing in its peer identity. This function returns a base-64 encoded certificate (IDC) that contains the RSA public key used to create the GMC for the peer identity (among other things), encapsulated in an XML blob, in the following format:

``` syntax
<PEERIDENTITYINFO VERSION="1.0">
     <IDC xmlns:dt="urn:schemas-microsoft-com:datatypes" dt:dt="bin.base64">
          <!-- Base-64 encoded certificate  -->
     </IDC>
</PEERIDENTITYINFO>
```

This string can be passed to [**PeerGroupCreateInvitation**](/windows/desktop/api/P2P/nf-p2p-peergroupcreateinvitation), which returns an invitation that contains the GMC for that peer identity. The invitation must be passed to the invitee using a different process such as e-mail, FTP, or a secure file share.

Alternatively, the IDC itself can be placed in a new [**PEER\_CREDENTIAL\_INFO**](/windows/desktop/api/P2P/ns-p2p-peer_credential_info) structure and passed to [**PeerGroupIssueCredentials**](/windows/desktop/api/P2P/nf-p2p-peergroupissuecredentials), which likewise generates an invitation.

Note that applications are not allowed to add tags within the **PEERIDENTITYINFO** tag or modify this XML fragment in any way. Applications are allowed to incorporate this XML fragment into other XML documents, but must strip out all application-specific XML before passing this fragment to the [**PeerGroupCreateInvitation**](/windows/desktop/api/P2P/nf-p2p-peergroupcreateinvitation) or [**PeerGroupIssueCredentials**](/windows/desktop/api/P2P/nf-p2p-peergroupissuecredentials) functions.

Member GMCs are issued by administrators and the peer group creator. Members must obtain new GMCs with extended lifetimes their GMCs before the expiration time has passed. The peer group administrator issues updated credentials by calling [**PeerGroupIssueCredentials**](/windows/desktop/api/P2P/nf-p2p-peergroupissuecredentials) with the existing credentials for that peer.

The [**PEER\_CREDENTIAL\_INFO**](/windows/desktop/api/P2P/ns-p2p-peer_credential_info) structure contains the basic data on a peer's membership status, including the public key for their GMC. Newly-issued credentials can be published to the peer group by setting the PEER\_GROUP\_STORE\_CREDENTIALS flag in the call to [**PeerGroupIssueCredentials**](/windows/desktop/api/P2P/nf-p2p-peergroupissuecredentials). When the recipient of the new credentials joins the peer group, it's existing credentials will be updated by the Peer Grouping Infrastructure.

## Issuing an Invitation

A member is invited to join the peer group in one of the following two ways:

-   A peer group administrator calls [**PeerGroupCreateInvitation**](/windows/desktop/api/P2P/nf-p2p-peergroupcreateinvitation), passing in the identity information XML string obtained from the potential invitee via a common out-of-band mechanism, such as email or an IM session. The invitation is also passed through some external process or mechanism to the peer, who will ultimately receive it as an XML string or text file.
-   A peer group administrator calls [**PeerGroupIssueCredentials**](/windows/desktop/api/P2P/nf-p2p-peergroupissuecredentials). To use this function, the peer must have already published membership information to the peer group ([**PEER\_MEMBER**](/windows/desktop/api/P2P/ns-p2p-peer_member)), or have an available public key (of the RSA key pair used to create the subject identity). In the former case, the [**PEER\_CREDENTIAL\_INFO**](/windows/desktop/api/P2P/ns-p2p-peer_credential_info) structure required for **PeerGroupIssueCredentials** can be obtained from the **PEER\_MEMBER** structure; in the latter case, a new **PEER\_CREDENTIAL\_INFO** structure can be populated with the public key.

After receiving the invitation string, the peer passes it to [**PeerGroupJoin**](/windows/desktop/api/P2P/nf-p2p-peergroupjoin) to join the peer group. If the call to **PeerGroupJoin** is successful, the peer can later open the peer group by calling [**PeerGroupOpen**](/windows/desktop/api/P2P/nf-p2p-peergroupopen).

## Parsing an Invitation

Optionally, an invitation can be parsed by calling [**PeerGroupParseInvitation**](/windows/desktop/api/P2P/nf-p2p-peergroupparseinvitation), which returns a [**PEER\_INVITATION\_INFO**](/windows/desktop/api/P2P/ns-p2p-peer_invitation_info) structure. The fields in the structure can be easily obtained for display purposes.

 

 



