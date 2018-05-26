---
Description: All normal RSA/Schannel and Diffie-Hellman/Schannel operations use the AT\_KEYEXCHANGE public/private key pair.
ms.assetid: e12afdbb-7ba8-444e-a43f-e262b481a353
title: Public/Private Key Pair Usage
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Public/Private Key Pair Usage

All normal [*RSA*](security.r_gly#-security-rsa-gly)/Schannel and [*Diffie-Hellman*](security.d_gly#-security-diffie-hellman-algorithm-gly)/Schannel operations use the AT\_KEYEXCHANGE [*public/private key pair*](security.p_gly#-security-public-private-key-pair-gly). To provide server [*authentication*](security.a_gly#-security-authentication-gly), the server-side of Schannel operations must have access to its [*X.509*](security.x_gly#-security-x-509-gly) certificate containing its public key and access to the matching [*private key*](security.p_gly#-security-private-key-gly). The client-side of [*Schannel*](security.s_gly#-security-schannel-gly) needs its certificate with its public key and access to its private key if client authentication is implemented.

Since Schannel protocol engines never use the AT\_SIGNATURE public/private key pair, that key pair need not be supported by a new CSP supporting only RSA/Schannel or Diffie-Hellman/Schannel.

If a protocol engine uses an SSL 3.0 export cipher suite with an AT\_KEYEXCHANGE key pair larger than 512 bits, the server must use an additional RSA key pair. This additional key pair is always exactly 512 bits and it can be ephemeral. The pair is stored as an AT\_KEYEXCHANGE element in a key container owned by the protocol engine. A handle to this key container is typically acquired at protocol engine startup.

Diffie-Hellman supports only [*CALG\_DH\_EPHEM*](security.c_gly#-security-calg-dh-ephem-gly) and uses normal RSA or DSS public keys.

 

 



