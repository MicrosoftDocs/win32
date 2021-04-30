---
description: ATM falls into the category of rooted data and rooted control planes.
ms.assetid: 8e355efe-2903-49c1-a9b3-792b07bd2995
title: ATM Point to Multipoint
ms.topic: article
ms.date: 05/31/2018
---

# ATM Point to Multipoint

ATM falls into the category of rooted data and rooted control planes. An application acting as the root would create c\_root sockets and counterparts running on leaf nodes would utilize c\_leaf sockets. The root application uses [**WSAJoinLeaf**](/windows/desktop/api/Winsock2/nf-winsock2-wsajoinleaf) to add new leaf nodes. The corresponding applications on the leaf nodes will have set their c\_leaf sockets into listen mode. **WSAJoinLeaf** with a c\_root socket specified is mapped to the Q.2931 ADDPARTY message. The leaf-initiated join is not supported in ATM UNI 3.1, but is supported in ATM UNI 4.0. Thus **WSAJoinLeaf** with a c\_leaf socket specified is mapped to the appropriate ATM UNI 4.0 message.

There are additional considerations to bear in mind for ATM point-to-multipoint:

-   The addition of new leaves to the ATM point-to-multipoint session is invitation-based only. The root invites leaves — which have already their [**accept**](/windows/desktop/api/Winsock2/nf-winsock2-accept) function call — by calling the [**WSAJoinLeaf**](/windows/desktop/api/Winsock2/nf-winsock2-wsajoinleaf) function.
-   The flow of data in an ATM point-to-multipoint session is from root-to-leaves only; leaves cannot use the same session to send information to the root.
-   Only one leaf per ATM adapter is allowed.

 

 



