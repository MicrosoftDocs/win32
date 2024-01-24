---
description: Network Source Authentication
ms.assetid: bffc33ec-0fb0-4bbe-9bac-583b9d4e1153
title: Network Source Authentication
ms.topic: article
ms.date: 05/31/2018
---

# Network Source Authentication

Certain media hosts may require user credentials from client applications before allowing access to the media. User credentials include identification and proof of identification, such as user name and password, which are used by the media server to grant access to the network source it hosts. The network source can provide NTLM, Digest, or Basic authentication.

Applications based on Media Foundation can store user credentials for a specific URL in a *credential* object that exposes the [**IMFNetCredential**](/windows/desktop/api/mfidl/nn-mfidl-imfnetcredential) interface. The credential object stores encrypted credentials and provides methods to return information such as user name, password, and domain.

The credential objects are created and maintained in a cache. The *credential cache* object, exposed by the [**IMFNetCredentialCache**](/windows/desktop/api/mfidl/nn-mfidl-imfnetcredentialcache) interface provides methods for retrieving the credential objects from the credential cache.

An application that supports authentication must implement the [**IMFNetCredentialManager**](/windows/desktop/api/mfidl/nn-mfidl-imfnetcredentialmanager) interface. Media Foundation does not provide a default implementation of this interface. The credential manager is responsible for gathering the required credentials for a URL from user input or reading from persisted storage.

This section contains the following topics:

-   [Setting a Credential Manager](setting-a-credential-manager.md)
-   [Using the Credential Cache](using-the-credential-cache.md)
-   [Implementing IMFNetCredentialManager](implementing-imfnetcredentialmanager.md)

## Related topics

<dl> <dt>

[Networking in Media Foundation](networking-in-media-foundation.md)
</dt> </dl>

 

 



