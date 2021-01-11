---
description: In addition to certificates and certificate revocation lists (CRL), the CryptoAPI certificate store supports the certificate trust list (CTL).
ms.assetid: b0f7e7ce-f981-4f3f-83a0-7792224ce0e3
title: Certificate Trust List Overview
ms.topic: article
ms.date: 05/31/2018
---

# Certificate Trust List Overview

In addition to certificates and [*certificate revocation lists*](../secgloss/c-gly.md) (CRL), the [*CryptoAPI*](../secgloss/c-gly.md) [*certificate store*](../secgloss/c-gly.md) supports the [*certificate trust list*](../secgloss/c-gly.md) (CTL). A CTL is a predefined list of items signed by a trusted entity. A CTL is a list of [*hashes*](../secgloss/h-gly.md) of certificates or a list of file names. All the items in the list are authenticated and approved by a trusted signing entity. A [**CTL\_CONTEXT**](/windows/desktop/api/Wincrypt/ns-wincrypt-ctl_context) structure is similar to certificate and CRL context structures. A CTL context can be persisted to the certificate store.

A CryptoAPI CTL is a list of items that has been signed by a trusted entity. The list of items could be anything, such as a list of hashes of certificates, or a list of file names. In most cases, a CTL is a list of hashed certificate contexts. All the items in the list are authenticated and approved by the signing entity. The primary use of CTLs is to verify signed Messages, using the CTL as a source of trusted [*root certificates*](../secgloss/r-gly.md).

The [**CTL\_CONTEXT**](/windows/desktop/api/Wincrypt/ns-wincrypt-ctl_context) structure is similar to the certificate and CRL context structures; however, unlike the certificate and CRL context structures, the **CTL\_CONTEXT** structure contains a **hCryptMsg** member. This handle is opened by a call to any of the functions that return a **CTL\_CONTEXT** structure, making it possible to use the message functions to verify the CTL's signature. This verification is necessary to ensure that a CTL is not a bogus CTL planted by a rogue entity.

For procedures to create a signed CTL and save it to a certificate store, see [Creating, Signing, and Storing a CTL](creating-signing-and-storing-a-ctl.md). Also see [Verifying a CTL](verifying-a-ctl.md) and [Verifying Signed Messages By Using CTLs](verifying-signed-messages-by-using-ctls.md) for step by step verification procedures.

 

 
