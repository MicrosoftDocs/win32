---
description: CAPICOM uses digital certificates to create signatures, encrypt session encryption keys when creating enveloped messages, and decrypt encrypted session keys when an enveloped message is received.
ms.assetid: 018fc41a-19fd-4e4c-bfed-e0215afb5150
title: Using Certificate Stores
ms.topic: article
ms.date: 05/31/2018
---

# Using Certificate Stores

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the .NET Framework to implement security features. For more information, see [Alternatives to Using CAPICOM](alternatives-to-using-capicom.md).\]

CAPICOM uses [*digital certificates*](../secgloss/d-gly.md) to create signatures, encrypt session encryption keys when creating enveloped messages, and decrypt encrypted session keys when an enveloped message is received. By default, CAPICOM uses certificates in the My store that have an associated private key for both [*digital signatures*](../secgloss/d-gly.md) creation and session key decryption. In most cases, an application would never need to open or otherwise directly deal with a certificate store.

However, applications creating enveloped messages use the [*public key*](../secgloss/p-gly.md) of each intended recipient of an enveloped message. These keys are retrieved from the certificates of the intended recipients. Thus, to create enveloped messages for a group of intended recipients, the certificates of those recipients would be collected in a certificate store.

The following table lists the standard certificate stores normally persisted on a user station.



| Store        | Description                                                                                                                                                                                                                                                                                                                                                                 |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| My           | Contains personal certificates. These certificates will usually have an associated private key.                                                                                                                                                                                                                                                                             |
| Other people | Contains the certificates of those that the user normally sends enveloped messages to or receives signed messages from.                                                                                                                                                                                                                                                     |
| Ca and Root  | Contains the [*certificates*](../secgloss/r-gly.md) of certificate authorities that the user trusts to issue certificates to others. Certificates in these stores are normally supplied with the operating system or by the user's network administrator. Certificates in the Root store are typically self-signed. |



 

Additional CAPICOM\_CURRENT\_USER stores can be created, opened, and persisted by giving a different store name as a string. If a store by that name does not exist, an empty store is created and opened. If a store does exist, it is opened and any certificates currently in the store are made available.

The following sections show examples for certificate store tasks:

-   [Opening the Active Directory Store and Retrieving Certificates](opening-the-active-directory-store-and-retrieving-certificates.md)
-   [Adding Certificates to a Certificate Store](adding-certificates-to-a-certificate-store.md)
-   [Using Stores in Different Locations](using-stores-in-different-locations.md)
-   [Collecting and Verifying Certificates](collecting-and-verifying-certificates.md)

 

 
