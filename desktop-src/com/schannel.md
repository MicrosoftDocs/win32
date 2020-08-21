---
title: Schannel
description: The Secure Channel (Schannel) security package, whose authentication service identifier is RPC\_C\_AUTHN\_GSS\_SCHANNEL, supports the following public-key based protocols SSL (Secure Sockets Layer) versions 2.0 and 3.0, Transport Layer Security (TLS) 1.0, and Private Communication Technology (PCT) 1.0. TLS 1.0 is a standardized, slightly modified version of SSL 3.0 that was issued by the Internet Engineering Task Force (IETF) in January 1999, in document RFC 2246. Because TLS has been standardized, developers are encouraged to use TLS rather than SSL. PCT is included for backward compatibility only and should not be used for new development. When the Schannel security package is used, DCOM automatically negotiates the best protocol, depending on the client and server capabilities.
ms.assetid: 03a5f987-f668-4f19-9b58-d62711f58734
ms.topic: article
ms.date: 05/31/2018
---

# Schannel

The Secure Channel (Schannel) security package, whose authentication service identifier is RPC\_C\_AUTHN\_GSS\_SCHANNEL, supports the following public-key based protocols: SSL (Secure Sockets Layer) versions 2.0 and 3.0, Transport Layer Security (TLS) 1.0, and Private Communication Technology (PCT) 1.0. TLS 1.0 is a standardized, slightly modified version of SSL 3.0 that was issued by the Internet Engineering Task Force (IETF) in January 1999, in document [RFC 2246](https://www.ietf.org/rfc/rfc2246.txt). Because TLS has been standardized, developers are encouraged to use TLS rather than SSL. PCT is included for backward compatibility only and should not be used for new development. When the Schannel security package is used, DCOM automatically negotiates the best protocol, depending on the client and server capabilities.

The following topics briefly describe the TLS protocol and how it works with DCOM.

-   [When to Use TLS](#when-to-use-tls)
-   [Brief Overview of How TLS Works](#brief-overview-of-how-tls-works)
-   [X.509 Certificates](#x509-certificates)
    -   [Client Certificates](#client-certificates)
-   [Using TLS in COM](#using-tls-in-com)
    -   [How a Server Sets the Security Blanket](#how-a-server-sets-the-security-blanket)
    -   [How a Client Sets the Security Blanket](#how-a-client-sets-the-security-blanket)
    -   [How a Client Changes the Security Blanket](#how-a-client-changes-the-security-blanket)
    -   [Example: Client Changes the Security Blanket](#example-client-changes-the-security-blanket)
-   [Related topics](#related-topics)

> [!Note]  
> All the information about the TLS protocol in these sections also applies to the SSL and PCT protocols.

 

## When to Use TLS

TLS is the only security option available when servers need to prove their identity to anonymous clients. This is particularly important for websites that want to participate in e-commerce because it helps protect the transmission of sensitive information such as credit card numbers. TLS assures that the e-commerce customers can be certain of whom they are doing business with because they are given proof of the server's identity. It also gives the e-commerce server the efficiency of not having to concern itself with authenticating the identity of each of its customers.

TLS requires that all servers prove their identity to clients. Additionally, TLS provides the option of having clients prove their identity to servers. This mutual authentication can be useful in restricting the access of certain webpages in a large corporate intranet.

TLS supports the strongest authentication levels and offers an open architecture that permits encryption strength to increase over time to keep up with technological innovation. TLS is the best choice for environments where the highest level of security is desired for the data in transit.

## Brief Overview of How TLS Works

TLS is built upon a public key infrastructure (PKI), which uses public/private key pairs for enabling data encryption and establishing data integrity, and uses X.509 certificates for authentication.

Many security protocols, such as the Kerberos v5 protocol, depend on a single key to both encrypt and decrypt data. Such protocols therefore depend on the secure exchange of encryption keys; in the Kerberos protocol, this is done through tickets obtained from the Key Distribution Center (KDC). This requires that everyone using the Kerberos protocol be registered with the KDC, which would be an impractical limitation for an e-commerce web server that is intended to attract millions of customers from around the world. TLS therefore relies upon a PKI, which uses two keys for data encryptionâ€”when one key of the pair encrypts the data, only the other key of the pair can decrypt it. The principle benefit of this design is that encryption can be performed without requiring the secure exchange of encryption keys.

A PKI uses a technique where one of the keys is kept private and is available only to the principal to whom it is registered, while the other key is made public for anyone to access. If someone wants to send a private message to the owner of a key pair, the message can be encrypted with the public key and only the private key can be used to decrypt the message.

Key pairs are also used to verify the integrity of the data being sent. To do this, the owner of the key pair can attach a digital signature to the data before sending it. Creating a digital signature involves calculating a hash of the data and encrypting the hash with the private key. Anyone who uses the public key to decrypt the digital signature is assured that the digital signature must have come only from the person who owns the private key. Additionally, the recipient can calculate a hash of the data using the same algorithm as the sender, and if the calculated hash matches the one sent in the digital signature, the recipient can be certain that the data was not modified after it was digitally signed.

One disadvantage of using a PKI for high-volume data encryption is its relatively slow performance. Because of the intensive mathematics involved, encryption and decryption of data using an asymmetric cipher that depends on a key pair can be up to 1,000 times slower than encryption and decryption using a symmetric cipher that depends only on a single key. TLS therefore uses a PKI only for generating digital signatures and for negotiating the session-specific single key that will be used by both the client and the server for bulk data encryption and decryption. TLS supports a wide variety of single-key symmetric ciphers, and additional ciphers may be added in the future.

For more information about the TLS handshake protocol, see [TLS Handshake Protocol](/windows/desktop/SecAuthN/tls-handshake-protocol).

For more details regarding the cryptography behind the TLS protocol, see [Cryptography Essentials](/windows/desktop/SecCrypto/cryptography-essentials).

## X.509 Certificates

A critical issue that must be handled by a PKI is the ability to trust the authenticity of the public key that is being used. When you use a public key issued to a company that you want to do business with, you want to be certain that the key actually belongs to the company rather than to a thief who wants to discover your credit card number.

To guarantee the identity of a principal holding a key pair, the principal is issued an X.509 certificate by a certification authority (CA). This certificate contains information that identifies the principal, contains the principal's public key, and is digitally signed by the CA. This digital signature indicates that the CA believes that the public key contained in the certificate truly belongs to the principal identified by the certificate.

And how do you trust the CA? Because the CA itself holds an X.509 certificate that has been signed by a higher-level CA. This chain of certificate signatures continues until it reaches a root CA, which is a CA that signs its own certificates. If you trust the integrity of the root CA of a certificate, you should be able to trust the authenticity of the certificate itself. Therefore, picking root CAs that you are willing to trust is an important duty for a system administrator.

### Client Certificates

When security transport-layer protocols first emerged, their primary purpose was to guarantee that a client was connecting to an authentic server and help protect the privacy of data while in transit. However, SSL 3.0 and TLS 1.0 also include support for the transmission of a client's certificate during the protocol's handshake. This optional feature enables the mutual authentication of the client and server.

The decision of whether to use a client certificate should be made in the context of the application. Client certificates are unnecessary if the primary requirement is authenticating the server. However, if client authentication is essential, a client's certificate can be used rather than relying on custom authentication within the application. Using client certificates is preferable over custom authentication because it gives users a single sign-on scenario.

## Using TLS in COM

TLS supports only the impersonate (RPC\_C\_IMP\_LEVEL\_IMPERSONATE) level of impersonation. If COM negotiates TLS as the authentication service on a proxy, COM will set the impersonation level to impersonate regardless of the process default. For impersonation to work properly in TLS, the client must provide an X.509 certificate to the server and the server must have that certificate mapped to a particular user account on the server. For more information, see the [Step-by-Step Guide to Mapping Certificates to User Accounts](https://www.microsoft.com/isapi/redir.dll?prd=windows2000&sbp=technicallibrary&ar=security&sba=mappingcertificates).

TLS does not support [cloaking](cloaking.md). If a cloaking flag and TLS are specified in a [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) or a [**IClientSecurity::SetBlanket**](/windows/win32/api/objidl/nf-objidl-iclientsecurity-setblanket) call, E\_INVALIDARG will be returned.

TLS does not work with the authentication level set to None. The handshake between the client and server examines the authentication level set by each and chooses the higher security setting for the connection.

The security parameters for TLS can be set by calling [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) and [**CoSetProxyBlanket**](/windows/desktop/api/combaseapi/nf-combaseapi-cosetproxyblanket). The following sections describe the nuances involved in making those calls.

### How a Server Sets the Security Blanket

If a server wants to use TLS, it must specify Schannel (RPC\_C\_AUTHN\_GSS\_SCHANNEL) as an authentication service in the *asAuthSvc* parameter of [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity). To prevent clients from connecting to the server by using a less secure authentication service, the server should specify only Schannel as an authentication service when it calls **CoInitializeSecurity**. The server cannot change the security blanket after it has called **CoInitializeSecurity**.

To use TLS, the following parameters should be specified when a server calls [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity):

-   *pVoid* should be either a pointer to an [**IAccessControl**](/windows/desktop/api/IAccess/nn-iaccess-iaccesscontrol) object or a pointer to a [**SECURITY\_DESCRIPTOR**](/windows/desktop/api/winnt/ns-winnt-security_descriptor). It should not be **NULL** or a pointer to an AppID.
-   *cAuthSvc* cannot be 0 or -1. COM servers never chooses Schannel when *cAuthSvc*is -1.
-   *asAuthSvc* must specify Schannel as a possible authentication service. This is done by setting the following [**SOLE\_AUTHENTICATION\_SERVICE**](/windows/win32/api/objidlbase/ns-objidlbase-sole_authentication_service) parameters for the Schannel member of the [**SOLE\_AUTHENTICATION\_LIST**](/windows/win32/api/objidlbase/ns-objidlbase-sole_authentication_list):
    -   *dwAuthnSvc* must be RPC\_C\_AUTHN\_GSS\_SCHANNEL.
    -   *dwAuthzSvc* should be RPC\_C\_AUTHZ\_NONE. Currently, it is ignored.
    -   *pPrincipalName* must be a pointer to a [**CERT\_CONTEXT**](/windows/desktop/api/wincrypt/ns-wincrypt-cert_context), cast as a pointer to OLECHAR, which represents the server's X.509 certificate.
-   *dwAuthnLevel* indicates the minimum authentication level that will be accepted from clients for a successful connection. It cannot be RPC\_C\_AUTHN\_LEVEL\_NONE.
-   *dwCapabilities* should not have the EOAC\_APPID flag set. The EOAC\_ACCESS\_CONTROL flag should be set if *pVoid* points to an [**IAccessControl**](/windows/desktop/api/IAccess/nn-iaccess-iaccesscontrol) object; it should not be set if *pVoid* points to a SECURITY\_DESCRIPTOR. For other flags that may be set, see [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity).

For more information about using [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity), see [Setting Processwide Security with CoInitializeSecurity](setting-processwide-security-with-coinitializesecurity.md).

### How a Client Sets the Security Blanket

If a client wants to use TLS, it must specify Schannel (RPC\_C\_AUTHN\_GSS\_SCHANNEL) in its list of authentication services in the *pAuthList* parameter of [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity). If Schannel is not specified as a possible authentication service when **CoInitializeSecurity** is called, a later call to [**CoSetProxyBlanket**](/windows/desktop/api/combaseapi/nf-combaseapi-cosetproxyblanket) (or [**IClientSecurity::SetBlanket**](/windows/win32/api/objidl/nf-objidl-iclientsecurity-setblanket)) will fail if it tries to specify Schannel as the authentication service.

The following parameters should be specified when a client calls [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity):

-   *dwAuthnLevel* specifies the default authentication level that the client wants to use. It cannot be RPC\_C\_AUTHN\_LEVEL\_NONE.
-   *dwImpLevel* must be RPC\_C\_IMP\_LEVEL\_IMPERSONATE.
-   *pAuthList* must have the following [**SOLE\_AUTHENTICATION\_INFO**](/windows/win32/api/objidlbase/ns-objidlbase-sole_authentication_info) parameters as a member of the list:
    -   *dwAuthnSvc* must be RPC\_C\_AUTHN\_GSS\_SCHANNEL.
    -   *dwAuthzSvc* must be RPC\_C\_AUTHZ\_NONE.
    -   *pAuthInfo* is a pointer to a [**CERT\_CONTEXT**](/windows/desktop/api/wincrypt/ns-wincrypt-cert_context), cast as a pointer to void, which represents the client's X.509 certificate. If the client does not have a certificate or does not wish to present its certificate to the server, *pAuthInfo* must be **NULL** and an anonymous connection will be attempted with the server.
-   *dwCapabilities* is a set of flags that indicate additional client capabilities. See [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) for information about which flags should be set.

For more information about using [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity), see [Setting Processwide Security with CoInitializeSecurity](setting-processwide-security-with-coinitializesecurity.md).

### How a Client Changes the Security Blanket

If a client wants to use TLS but change the security blanket after calling [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity), it must call either [**CoSetProxyBlanket**](/windows/desktop/api/combaseapi/nf-combaseapi-cosetproxyblanket) or [**IClientSecurity::SetBlanket**](/windows/win32/api/objidl/nf-objidl-iclientsecurity-setblanket) with parameters similar to those used in the call to **CoInitializeSecurity**, with the following differences:

-   *pServerPrincName* indicates the principal name of the server, in either msstd or fullsic format. For information on these formats, see [Principal Names](/windows/desktop/Rpc/principal-names). If the client has the server's X.509 certificate, it can find the principal name by calling [**RpcCertGeneratePrincipalName**](/windows/desktop/api/rpcssl/nf-rpcssl-rpccertgenerateprincipalname).
-   *pAuthInfo* is a pointer to a [**CERT\_CONTEXT**](/windows/desktop/api/wincrypt/ns-wincrypt-cert_context), cast as a pointer to RPC\_AUTH\_IDENTITY\_HANDLE, which represents the client's X.509 certificate. If the client does not have a certificate or does not wish to present its certificate to the server, *pAuthInfo* must be **NULL** and an anonymous connection will be attempted with the server.
-   *dwCapabilities* consists of flags that indicate additional client capabilities. Only four flags can be used to change security blanket settings: EOAC\_DEFAULT, EOAC\_MUTUAL\_AUTH, EOAC\_ANY\_AUTHORITY (this flag is deprecated), and EOAC\_MAKE\_FULLSIC. For more information, see [**CoSetProxyBlanket**](/windows/desktop/api/combaseapi/nf-combaseapi-cosetproxyblanket).

For more information about using [**CoSetProxyBlanket**](/windows/desktop/api/combaseapi/nf-combaseapi-cosetproxyblanket), see [Setting Security at the Interface Proxy Level](setting-security-at-the-interface-proxy-level.md).

### Example: Client Changes the Security Blanket

The following example demonstrates how a client can change the security blanket to accommodate a request from the server for the client to provide its X.509 certificate. Error handling code is omitted for brevity.


```C++
void ClientChangesSecurity ()
{
  HCRYPTPROV                   provider           = 0;
  HCERTSTORE                   cert_store         = NULL;
  PCCERT_CONTEXT               client_cert        = NULL;
  PCCERT_CONTEXT               server_cert        = NULL;
  WCHAR                        *server_princ_name = NULL;
  ISecret                      *pSecret           = NULL;
  MULTI_QI                     server_instance;
  COSERVERINFO                 server_machine;
  SOLE_AUTHENTICATION_LIST     auth_list;
  SOLE_AUTHENTICATION_INFO     auth_info[1];



  // Specify all the authentication info. 
  // The client is willing to connect using SChannel,
  //   with no client certificate.
  auth_list.cAuthInfo     = 1;
  auth_list.aAuthInfo     = auth_info;
  auth_info[0].dwAuthnSvc = RPC_C_AUTHN_GSS_SCHANNEL;
  auth_info[0].dwAuthzSvc = RPC_C_AUTHZ_NONE;
  auth_info[0].pAuthInfo  = NULL;  // No certificate

  // Initialize client security with no client certificate.
  CoInitializeSecurity( NULL, -1, NULL, NULL,
                        RPC_C_AUTHN_LEVEL_PKT,
                        RPC_C_IMP_LEVEL_IMPERSONATE, &auth_list,
                        EOAC_NONE, NULL );
  
  // Specify info for the proxy.
  server_instance = {&IID_ISecret, NULL, S_OK};
  server_machine  = {0, L"ServerMachineName", NULL, 0};
  
  // Create a proxy.
  CoCreateInstanceEx( CLSID_Secret, NULL, CLSCTX_REMOTE_SERVER, 
                      &server_machine, 1, &server_instance);
  pSecret = (ISecret *) server_instance.pItf;

  //** The client obtained the server's certificate during the handshake.
  //** The server requests a certificate from the client.

  // Get the default certificate provider.
  CryptAcquireContext( &provider, NULL, NULL, PROV_RSA_SCHANNEL, 0 );

  // Open the certificate store.
  cert_store = CertOpenSystemStore( provider, L"my" );

  // Find the client's certificate.
  client_cert = 
    CertFindCertificateInStore( cert_store,
                                X509_ASN_ENCODING | PKCS_7_ASN_ENCODING,
                                0,
                                CERT_FIND_SUBJECT_STR,
                                L"ClientName",  // Use the principal name
                                NULL );

  // Find the fullsic principal name of the server.
  RpcCertGeneratePrincipalName( server_cert, RPC_C_FULL_CERT_CHAIN, 
                                &server_princ_name );

  // Change the client's security: 
  // Increase the authentication level and attach a certificate.
  CoSetProxyBlanket( pSecret, RPC_C_AUTHN_GSS_SCHANNEL,
                     RPC_C_AUTHZ_NONE,
                     server_princ_name, RPC_C_AUTHN_LEVEL_PKT_PRIVACY,
                     RPC_C_IMP_LEVEL_IMPERSONATE, 
                     (RPC_AUTH_IDENTITY_HANDLE *) client_cert,
                     EOAC_NONE );

  cleanup:
  if (server_princ_name != NULL)
    RpcStringFree( &server_princ_name );
  if (client_cert != NULL)
    CertFreeCertificateContext(client_cert);
  if (server_cert != NULL)
    CertFreeCertificateContext(server_cert);
  if (cert_store != NULL)
    CertCloseStore( cert_store, CERT_CLOSE_STORE_CHECK_FLAG );
  if (provider != 0 )
    CryptReleaseContext( provider, 0 );
  if (pSecret != NULL)
    pSecret->Release();
  CoUninitialize();
}
```



## Related topics

<dl> <dt>

[COM and Security Packages](com-and-security-packages.md)
</dt> </dl>

 

 