---
description: A certificate chain is a hierarchal collection of certificates that leads from the end user or computer back to a root of trust, typically the root certification authority (CA) of an organization.
ms.assetid: 53701ede-269c-4949-b839-3f2b64cb5510
title: Certificate Chain
ms.topic: article
ms.date: 05/31/2018
---

# Certificate Chain

A certificate chain is a hierarchal collection of certificates that leads from the end user or computer back to a root of trust, typically the root certification authority (CA) of an organization. Because all parties presumably trust the root certificate, a party can gain trust in an end-entity certificate by verifying the certificate chain. Verification typically requires establishing that each certificate in the chain:

-   Is signed by the public key in the prior certificate.
-   Has not expired.
-   Has not been revoked.
-   Conforms to the policies specified by prior certificates.

## Related topics

<dl> <dt>

[Certificate Hierarchy](about-certificate-hierarchy.md)
</dt> <dt>

[Cross Certification](about-cross-certification.md)
</dt> <dt>

[Trust Models](about-trust-models.md)
</dt> </dl>

 

 



