---
description: The security model used in Microsoft SMB Protocol is identical to the one used by other variants of SMB, and consists of two levels of security&\#8212;user and share.
ms.assetid: 985aa9fe-af3f-406d-920d-7fd7d0d58674
title: Microsoft SMB Protocol Authentication
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft SMB Protocol Authentication

The security model used in Microsoft SMB Protocol is identical to the one used by other variants of SMB, and consists of two levels of security—user and share. A share is a file, directory, or printer that can be accessed by Microsoft SMB Protocol clients.

User-level authentication indicates that the client attempting to access a share on a server must provide a user name and password. When authenticated, the user can then access all shares on a server not also protected by share-level security. This security level allows system administrators to specifically determine which users and groups can access a share.

Share-level authentication indicates that access to a share is controlled by a password assigned to that share only. Unlike user-level security, this security level does not require a user name for authentication and no user identity is established.

Under both of these security levels, the password is encrypted before it is sent to the server. [NTLM](/windows/desktop/SecAuthN/microsoft-ntlm) and the older LAN Manager (LM) encryption are supported by Microsoft SMB Protocol. Both encryption methods use challenge-response authentication, where the server sends the client a random string and the client returns a computed response string that proves the client has sufficient credentials for access.

 

 
