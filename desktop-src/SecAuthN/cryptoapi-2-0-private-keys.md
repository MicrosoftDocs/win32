---
Description: 'Schannel credentials are represented internally as CERT\_CONTEXT structures.'
ms.assetid: '3d2deb61-8e86-4461-8f2a-4880ca5b9d34'
title: 'CryptoAPI 2.0 Private Keys'
---

# CryptoAPI 2.0 Private Keys

Schannel credentials are represented internally as [**CERT\_CONTEXT**](https://msdn.microsoft.com/library/windows/desktop/aa377189) structures. Schannel locates the [*private key*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-private-key-gly) associated with a particular certificate context using the certificate's CERT\_KEY\_PROV\_INFO\_PROP\_ID property. Using this property, Schannel accesses the *private key* by calling the [**CryptAcquireContext**](https://msdn.microsoft.com/library/windows/desktop/aa379886) function. For additional details, see [Public/Private Key Pairs](https://msdn.microsoft.com/library/windows/desktop/aa387460).

Every Schannel credential contains a reference to one or more private keys, each associated with a particular certificate. The [*private keys*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-private-key-gly) are handled quite differently depending on whether the credential is for a client or a server.

## Client Private Keys

Client [*private keys*](https://msdn.microsoft.com/library/windows/desktop/ms721603#-security-private-key-gly) are managed by the [*cryptographic service provider*](https://msdn.microsoft.com/library/windows/desktop/ms721572#-security-cryptographic-service-provider-gly) (CSP) in use. Client private keys are typically stored by CSPs of type [PROV\_RSA\_FULL](https://msdn.microsoft.com/library/windows/desktop/aa387448) or PROV\_RSA\_SIGNATURE.

If the client application makes the [**CryptAcquireContext**](https://msdn.microsoft.com/library/windows/desktop/aa379886) call manually then before calling [**AcquireCredentialsHandle**](acquirecredentialshandle--general-.md), the client must bind the CSP's handle to the certificate context using the CERT\_KEY\_PROV\_HANDLE\_PROP\_ID property. If Schannel finds this property set, it does not use the CERT\_KEY\_PROV\_INFO\_PROP\_ID property.

## Server Private Keys

Server private keys are stored by one of the following CSPs:

-   PROV\_RSA\_SCHANNEL
-   PROV\_DH\_SCHANNEL
-   PROV\_FORTEZZA CSP

The choice of CSP depends on the selected [*key exchange algorithm*](https://msdn.microsoft.com/library/windows/desktop/ms721590#-security-key-exchange-algorithm-gly). Server private keys must be of type AT\_KEYEXCHANGE.

 

 



