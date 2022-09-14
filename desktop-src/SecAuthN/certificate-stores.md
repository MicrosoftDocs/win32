---
description: Both client and server certificates must be stored in a certificate store accessible by the application process.
ms.assetid: 3be91b9b-ecc0-4cf2-88ca-77fd25d2dafc
title: Certificate Stores
ms.topic: article
ms.date: 05/31/2018
---

# Certificate Stores

Both [*client*](/windows/desktop/SecGloss/c-gly) and [*server certificates*](/windows/desktop/SecGloss/s-gly) must be stored in a [*certificate store*](/windows/desktop/SecGloss/c-gly) accessible by the application process. Typically, this is the My store, also known as the personal store. Client applications such as Internet Explorer normally use the My store of the current user while servers such as Internet Information Services (IIS) use the system My store of the local computer.

The Root store and the [*certification authority*](/windows/desktop/SecGloss/c-gly) (CA) store are used when Schannel or an application builds a certificate chain to be sent to the remote computer. These stores are used to validate a received certificate chain. For more information, see [Performing Authentication Using Schannel](performing-authentication-using-schannel.md).

 

 
