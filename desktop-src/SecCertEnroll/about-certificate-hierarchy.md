---
description: As the number of issued certificates in a public key infrastructure (PKI) increases, it can become difficult for a single certification authority (CA) to effectively track the certificates it has issued.
ms.assetid: f1642c1c-d2cd-4fa4-8a26-cebf3d6dcf23
title: Certificate Hierarchy
ms.topic: article
ms.date: 05/31/2018
---

# Certificate Hierarchy

As the number of issued certificates in a public key infrastructure (PKI) increases, it can become difficult for a single certification authority (CA) to effectively track the certificates it has issued. One way to address this is to create a certificate hierarchy in which the CA delegates the authority to issue certificates to subordinate authorities which can, in turn, delegate authority to their subordinates. Each CA delegates authority by issuing a CA certificate to a subordinate. The initial CA in the chain is called the root, and it is not necessary for an entity to establish trust with any CA that resides on a different [Certificate Chain](about-certificate-chain.md) from that on which the entity resides.

The following illustration shows a certificate hierarchy made up of one root CA, two CAs subordinate to the root (one for the marketing department and one for the manufacturing department), and CAs that are subordinate to these.

![certificate hierarchy diagram](images/certificate-hierarchy.png)

## Related topics

<dl> <dt>

[Trust Models](about-trust-models.md)
</dt> </dl>

 

 



