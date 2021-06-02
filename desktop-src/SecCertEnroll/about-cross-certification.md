---
description: Cross certification enables entities in one public key infrastructure (PKI) to trust entities in another PKI.
ms.assetid: 93cdb10d-4b77-4511-8c5b-c27b290f9154
title: Cross Certification
ms.topic: article
ms.date: 05/31/2018
---

# Cross Certification

Cross certification enables entities in one public key infrastructure (PKI) to trust entities in another PKI. This mutual trust relationship is typically supported by a cross-certification agreement between the certification authorities (CAs) in each PKI. The agreement establishes the responsibilities and liability of each party.

A mutual trust relationship between two CAs requires that each CA issue a certificate to the other to establish the relationship in both directions. The path of trust is not hierarchal (neither of the governing CAs is subordinate to the other) although the separate PKIs may be certificate hierarchies. After two CAs have established and specified the terms of trust and issued certificates to each other, entities within the separate PKIs can interact subject to the policies specified in the certificates.

![cross certification diagram](images/cross-certification.png)

## Related topics

<dl> <dt>

[Trust Models](about-trust-models.md)
</dt> </dl>

 

 



