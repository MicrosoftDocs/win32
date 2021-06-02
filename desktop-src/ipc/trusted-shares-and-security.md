---
description: Network DDE uses trusted shares and security descriptors to control access to shares.
ms.assetid: a22d9fc6-a0c9-442f-b278-1271cfbc636b
title: Trusted Shares and Security
ms.topic: article
ms.date: 05/31/2018
---

# Trusted Shares and Security

\[Network DDE is no longer supported. Nddeapi.dll is present on Windows Vista, but all function calls return NDDE\_NOT\_IMPLEMENTED.\]

Network DDE uses trusted shares and security descriptors to control access to shares.

## Trusted Shares

When a client user connects to a DDE share from a remote computer, network DDE accepts the request only if the following statements are true:

-   The user who created the share has granted trusted status to the share by calling [**NDdeSetTrustedShare**](nddesettrustedshare.md). Only the creator of the share can grant trusted status to the share. Not even an administrator can grant trusted status to a DDE share that was created by a different user.
-   The user who created the share is currently logged on to the server computer.

The process of granting trusted status to a share adds the share to the logged-on user's trusted shares list in the DSDM. This creates a trust relationship between the server and its clients. Once a DDE share has trusted status, clients can connect to it as long as the user that created the share is logged on. When the client connects to the share from a remote computer, network DDE accepts the request only if the share is listed in the logged-on user's trusted shares list in the DSDM.

## Security

Network DDE performs an additional security check when the client requests data or a link. It checks that the server has granted the remote user the necessary permission for the operation. The server controls access to the share through the *pSD* parameter of the [**NDdeShareAdd**](nddeshareadd.md) function. This parameter specifies the security descriptor. If this parameter is **NULL**, the function creates a default security descriptor that grants full access to the creator of the share and grants read and link permission to all other users. To grant or deny additional permissions to individual users or groups of users, create and use a security descriptor. For more information on security descriptors, see [**Access Control**](/windows/desktop/SecAuthZ/access-control).

To obtain the security descriptor for an existing DDE share, call the [**NDdeGetShareSecurity**](nddegetsharesecurity.md) function. You can edit the information and then update the security descriptor for the share by using the [**NDdeSetShareSecurity**](nddesetsharesecurity.md) function.

 

 
