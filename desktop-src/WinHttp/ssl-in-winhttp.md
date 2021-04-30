---
description: Microsoft Windows HTTP Services (WinHTTP) supports Secure Sockets Layer (SSL) transactions including client certificates. This topic explains concepts involved in an SSL transaction and how they are handled using WinHTTP.
ms.assetid: cb0a04f5-1026-4ad5-bb5b-c854064a5167
title: SSL in WinHTTP
ms.topic: article
ms.date: 05/31/2018
---

# SSL in WinHTTP

Microsoft Windows HTTP Services (WinHTTP) supports Secure Sockets Layer (SSL) transactions including client certificates. This topic explains concepts involved in an SSL transaction and how they are handled using WinHTTP.

## Secure Sockets Layer

SSL is an established standard for ensuring secure HTTP transactions. SSL provides a mechanism to perform up to 128-bit encryption on all transactions between the client and server. It enables the client to verify that the server belongs to a trusted entity through the use of server certificates. It also enables the server to confirm the identity of the client with client certificates.

Each of these issues encryption, server identity, and client identity are negotiated in the SSL handshake that occurs when a client first requests a resource from a Secure Hypertext Transfer Protocol (HTTPS) server. Essentially, the client and server each present a list of required and preferred settings. If a common set of requirements can be agreed upon and met, an SSL connection is established.

WinHTTP provides a high level interface for using SSL. While the details of the SSL handshake and transaction are handled internally, WinHTTP enables you to retrieve encryption levels, specify the security protocol, and interact with server and client certificates. The following sections provide details on creating WinHTTP based applications that elect an SSL protocol version, examine server certificates, and select client certificates to send to HTTPS servers.

## Server Certificates

Server certificates are sent from the server to the client so that the client can obtain a public key for the server and ensure that the server has been verified by a certification authority. Certificates can contain different types of data. For example, an X.509 certificate includes the format of the certificate, the serial number of the certificate, the algorithm used to sign the certificate, the name of the certification authority (CA) that issued the certificate, the name and public key of the entity that requests the certificate, and the CA's signature.

When using the WinHTTP  application programming interface (API), you can retrieve a server certificate by calling [**WinHttpQueryOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpqueryoption) and specifying the [**WINHTTP\_OPTION\_SECURITY\_CERTIFICATE\_STRUCT**](option-flags.md) flag. The server certificate is returned in a [**WINHTTP\_CERTIFICATE\_INFO**](/windows/win32/api/winhttp/ns-winhttp-winhttp_certificate_info) structure. If you prefer to retrieve the certificate context, specify the [**WINHTTP\_OPTION\_SERVER\_CERT\_CONTEXT**](option-flags.md) flag instead.

If a server certificate contains errors, details about the error can be obtained in the status callback function. The [**WINHTTP\_CALLBACK\_STATUS\_SECURE\_FAILURE**](/windows/win32/api/winhttp/nc-winhttp-winhttp_status_callback) notification indicates an error with a server certificate. The *lpvStatusInformation* parameter contains one or more detailed error flags. See [**WINHTTP\_STATUS\_CALLBACK**](/windows/win32/api/winhttp/nc-winhttp-winhttp_status_callback) for more information.

## Client Certificates

During the SSL handshake, the server might require authentication. The client is authenticated by supplying a valid client certificate to the server. WinHTTP enables you to select and send a certificate from a local [*certificate store*](glossary.md). The following sections describe the process that provides client certificates when using either the WinHTTP API or the [**WinHttpRequest**](winhttprequest.md) object.

### WinHTTP API

Both [**WinHttpSendRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsendrequest) and [**WinHttpReceiveResponse**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpreceiveresponse) can fail to indicate that a request was unsuccessful because the HTTPS server requires authentication. In these cases, call [**GetLastError**](/windows/desktop/api/errhandlingapi/nf-errhandlingapi-getlasterror) to returns ERROR\_WINHTTP\_CLIENT\_AUTH\_CERT\_NEEDED. Upon receiving this error, use the appropriate [CryptoAPI](/windows/desktop/SecCrypto/cryptography-functions) functions to find an appropriate certificate. Indicate that this certificate should be sent with the next request by calling [**WinHttpSetOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetoption) with the [**WINHTTP\_OPTION\_CLIENT\_CERT\_CONTEXT**](option-flags.md) flag.

The following code example shows how to open a [*certificate store*](glossary.md) and locate a certificate based on subject name after the ERROR\_WINHTTP\_CLIENT\_AUTH\_CERT\_NEEDED error has been returned.


```C++
  if( !WinHttpReceiveResponse( hRequest, NULL ) )
  {
    if( GetLastError( ) == ERROR_WINHTTP_CLIENT_AUTH_CERT_NEEDED )
    {
      //MY is the store the certificate is in.
      hMyStore = CertOpenSystemStore( 0, TEXT("MY") );
      if( hMyStore )
      {
        pCertContext = CertFindCertificateInStore( hMyStore,
             X509_ASN_ENCODING | PKCS_7_ASN_ENCODING,
             0,
             CERT_FIND_SUBJECT_STR,
             (LPVOID) szCertName, //Subject string in the certificate.
             NULL );
        if( pCertContext )
        {
          WinHttpSetOption( hRequest, 
                            WINHTTP_OPTION_CLIENT_CERT_CONTEXT,
                            (LPVOID) pCertContext, 
                            sizeof(CERT_CONTEXT) );
          CertFreeCertificateContext( pCertContext );
        }
        CertCloseStore( hMyStore, 0 );

        // NOTE: Application should now resend the request.
      }
    }
  }
```



Before resending a request that contains a client certificate, you can determine if the supported level of encryption is acceptable for your application. Call [**WinHttpQueryOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpqueryoption) and specify the [**WINHTTP\_OPTION\_SECURITY\_FLAGS**](option-flags.md) flag to determine the level of encryption that is used.

### Issuer List Retrieval for SSL Client Authentication

When the WinHttp client application sends a request to a secure HTTP server that requires SSL client authentication, WinHttp returns an **ERROR\_WINHTTP\_CLIENT\_AUTH\_CERT\_NEEDED** if the application has not supplied a client certificate. For computers running on Windows Server 2008 and Windows Vista, WinHttp enables the application to retrieve the certificate issuer list supplied by the server in the authentication challenge. The Issuer List specifies a list of Certificate Authorities (CAs) that are authorized by the server to issue client certificates. The application filters the issuer list to obtain the required certificate.

The WinHttp client application retrieves the issuer list when [**WinHttpSendRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsendrequest), or [**WinHttpReceiveResponse**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpreceiveresponse) returns **ERROR\_WINHTTP\_CLIENT\_AUTH\_CERT\_NEEDED**. When this error is returned, the application calls [**WinHttpQueryOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpqueryoption) with the **WINHTTP\_OPTION\_CLIENT\_CERT\_ISSUER\_LIST** option. The *lpBuffer* parameter must be large enough to contain a pointer to the [SecPkgContext\_IssuerListInfoEx](/windows/desktop/api/schannel/ns-schannel-secpkgcontext_issuerlistinfoex) structure. The following code example shows how to retrieve the issuer list.


```C++
#include <windows.h>
#include <winhttp.h>
#include <schannel.h>

//...

void GetIssuerList(HINTERNET hRequest)
{
  SecPkgContext_IssuerListInfoEx* pIssuerList = NULL;
  DWORD dwBufferSize = sizeof(SecPkgContext_IssuerListInfoEx*);

  if (WinHttpQueryOption(hRequest,
           WINHTTP_OPTION_CLIENT_CERT_ISSUER_LIST,
           &pIssuerList,
           &dwBufferSize) == TRUE)
  {
    // Use the pIssuerList for cert store filtering.
    GlobalFree(pIssuerList); // Free the issuer list when done.
  }
}
```



The information in the [SecPkgContext\_IssuerListInfoEx](/windows/desktop/api/schannel/ns-schannel-secpkgcontext_issuerlistinfoex) structure, *cIssuers* and *aIssuers*, can be used to search for the certificate as shown in the code example below. For more information, see [**CertFindChainInStore**](/windows/desktop/api/wincrypt/nf-wincrypt-certfindchaininstore).


```C++
PCERT_CONTEXT pClientCert = NULL;
PCCERT_CHAIN_CONTEXT pClientCertChain = NULL;

CERT_CHAIN_FIND_BY_ISSUER_PARA SrchCriteria;
::ZeroMemory(&SrchCriteria, sizeof(CERT_CHAIN_FIND_BY_ISSUER_PARA));
SrchCriteria.cbSize = sizeof(CERT_CHAIN_FIND_BY_ISSUER_PARA);

SrchCriteria.cIssuer = pIssuerList->cIssuers;
SrchCriteria.rgIssuer = pIssuerList->aIssuers;

pClientCertChain = CertFindChainInStore(
            hClientCertStore,
            X509_ASN_ENCODING,
            CERT_CHAIN_FIND_BY_ISSUER_CACHE_ONLY_URL_FLAG |
            // Do not perform wire download when building chains.
            CERT_CHAIN_FIND_BY_ISSUER_CACHE_ONLY_FLAG,
            // Do not search pCacheEntry->_ClientCertStore 
            // for issuer certs.
            CERT_CHAIN_FIND_BY_ISSUER,
            &SrchCriteria,
            NULL);

if (pClientCertChain)
{
    pClientCert = (PCERT_CONTEXT) pClientCertChain->rgpChain[0]->rgpElement[0]->pCertContext;

    CertDuplicateCertificateContext(pClientCert);

    CertFreeCertificateChain(pClientCertChain);

    pClientCertChain = NULL;
}
```



### Optional Client SSL Certificates

Starting in Windows Server 2008 and Windows Vista, the WinHttp API supports optional client certificates. When the server requests a client certificate, [**WinHttpSendRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsendrequest), or [**WinHttpRecieveResponse**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpreceiveresponse) returns an **ERROR\_WINHTTP\_CLIENT\_AUTH\_CERT\_NEEDED** error. If the server requests the certificate, but does not require it, the application can specify this option to indicate that it does not have a certificate. The server can choose another authentication scheme or allow anonymous access to the server. The application specifies the **WINHTTP\_NO\_CLIENT\_CERT\_CONTEXT** macro in the *lpBuffer* parameter of [**WinHttpSetOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetoption) as shown in the following code example.

``` syntax
BOOL fRet = WinHttpSetOption ( hRequest,
                               WINHTTP_OPTION_CLIENT_CERT_CONTEXT,
                               WINHTTP_NO_CLIENT_CERT_CONTEXT,
                               0);
```

If the **WINHTTP\_NO\_CLIENT\_CERT\_CONTEXT** is set, and the server still requires a client certificate, it may send a 403 HTTP status code. For more information, see the **WINHTTP\_OPTION\_CLIENT\_CERT\_ISSUER\_LIST** option.

### WinHttpRequest Object

Use the [**SetClientCertificate**](iwinhttprequest-setclientcertificate.md) method of the [**WinHttpRequest**](winhttprequest.md) object to select client certificates to send to the server with a request. Select a certificate by specifying a certificate selection string with the [**SetClientCertificate**](iwinhttprequest-setclientcertificate.md) method. The certificate selection string consists of the certificate location, [*certificate store*](glossary.md), and subject name delimited by backslashes. The following table lists components for this selection string.



| Component                                                  | Description                                                                                                                                                                                        | Possible values                                                                                                                                                                                                                                                                                                                       |
|------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Location                                                   | Determines the registry key under which the certificates are stored.                                                                                                                               | The possible values are "LOCAL\_MACHINE" to indicate that the [*certificate store*](glossary.md) is under **HKEY\_LOCAL\_MACHINE**<br/> and "CURRENT\_USER" to indicate that the *certificate store* is under the non-impersonated**HKEY\_CURRENT\_USER.**<br/> This component is case-sensitive. |
| [*Certificate store*](glossary.md) | Indicates the name of the [*certificate store*](glossary.md) that contains the relevant certificate.                                                                       | Typical [*certificate stores*](glossary.md) are "MY", "Root", and "TrustedPeople". This component is case-sensitive.                                                                                                                                                                                          |
| Subject name                                               | Identifies a certificate within the specified [*certificate store*](glossary.md). The first certificate that contains the string specified for this component is selected. | The subject name can be any string. A blank string indicates that the first certificate in the [*certificate store*](glossary.md) should be used. This component is case-insensitive.                                                                                                                         |



 

The [*certificate store*](glossary.md) name and location are optional components. However, if you specify a *certificate store*, you must also specify the location of that *certificate store*. The default location is CURRENT\_USER and the default *certificate store* is "MY".

The following code example shows how to specify that a certificate with the subject "My Middle-Tier Certificate" should be chosen from the "Personal" [*certificate store*](glossary.md) in the registry under **HKEY\_LOCAL\_MACHINE**.

`HttpReq.SetClientCertificate("LOCAL_MACHINE\Personal\My Middle-Tier Certificate")`

> [!Note]  
> In some languages the backslash is an escape character. Remember to modify the certificate selection string to account for this. For example, in Microsoft JScript, use two adjacent backslashes instead of one.

 

If you do not specify a certificate and an HTTPS server requires a client certificate, WinHTTP selects the first certificate in the default [*certificate store*](glossary.md). If no certificates exist, an error is raised. If the certificate is not accepted, the server returns a 403 status code to indicate that the request cannot be fulfilled. You can then choose a more appropriate certificate with [**SetClientCertificate**](iwinhttprequest-setclientcertificate.md) and resend the request.

 

