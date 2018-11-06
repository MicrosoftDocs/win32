---
Description: Both client and server certificates must be stored in a certificate store accessible by the application process.
ms.assetid: 3be91b9b-ecc0-4cf2-88ca-77fd25d2dafc
title: Certificate Stores
ms.topic: article
ms.date: 05/31/2018
---

# Certificate Stores

Both [*client*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-client-certificate-gly) and [*server certificates*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-server-certificate-gly) must be stored in a [*certificate store*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-certificate-store-gly) accessible by the application process. Typically, this is the My store, also known as the personal store. Client applications such as Internet Explorer normally use the My store of the current user while servers such as Internet Information Services (IIS) use the system My store of the local computer.

The Root store and the [*certification authority*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-certification-authority-gly) (CA) store are used when Schannel or an application builds a certificate chain to be sent to the remote computer. These stores are used to validate a received certificate chain. For more information, see [Performing Authentication Using Schannel](performing-authentication-using-schannel.md).

 

 



