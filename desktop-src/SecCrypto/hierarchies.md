---
description: Certificate Services supports certification authority (CA) hierarchies.
ms.assetid: bcae26cd-41bc-4436-8f8b-cd8c20e9fcfc
title: Hierarchies
ms.topic: article
ms.date: 05/31/2018
---

# Hierarchies

Certificate Services supports [*certification authority*](../secgloss/c-gly.md) (CA) hierarchies. A [*CA hierarchy*](../secgloss/c-gly.md) consists of a top-level CA (called the Root CA) with one or more subordinate CAs which have been issued certificates by the root CA. A possible CA hierarchy scenario would be in an organization with one root CA, which was used to issue certificates to several subordinate CAs. The subordinate CAs can then issue end-entity certificates, such as certificates issued to a user. The user's certificate will contain a trust path for the CA hierarchy, in this case, including the certificate for both the issuing subordinate CA as well as the root CA.

 

 
