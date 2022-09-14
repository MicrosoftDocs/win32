---
description: Some HTTP servers and proxies require authentication before allowing access to resources on the Internet. The Microsoft Windows HTTP Services (WinHTTP) functions support server and proxy authentication for HTTP sessions.
ms.assetid: 077d6275-8600-4091-b78e-419a41a2101a
title: Authentication in WinHTTP
ms.topic: article
ms.date: 05/31/2018
---

# Authentication in WinHTTP

Some HTTP servers and proxies require authentication before allowing access to resources on the Internet. The Microsoft Windows HTTP Services (WinHTTP) functions support server and proxy authentication for HTTP sessions.

## About HTTP Authentication

If authentication is required, the HTTP application receives a status code of 401 (server requires authentication) or 407 (proxy requires authentication). Along with the status code, the proxy or server sends one or more authenticate headers: WWW-Authenticate (for server authentication) or Proxy-Authenticate (for proxy authentication).

Each authenticate header contains a supported authentication scheme and, for the Basic and Digest schemes, a realm. If multiple authentication schemes are supported, the server returns multiple authenticate headers. The realm value is case-sensitive and defines a set of servers or proxies for which the same credentials are accepted. For example, the header "WWW-Authenticate: Basic Realm="example"" might be returned when server authentication is required. This header specifies that user credentials must be supplied for the "example" domain.

An HTTP application can include an authorization header field with a request it sends to the server. The authorization header contains the authentication scheme and the appropriate response required by that scheme. For example, the header "Authorization: Basic \<username:password>" would be added to the request and sent to the server if the client received the response header "WWW-Authenticate: Basic Realm="example"".

> [!Note]  
> Although they are shown here as plain text, the username and password are actually [*base64 encoded*](glossary.md).

 

There are two general types of authentication schemes:

-   Basic authentication scheme, in which the user name and password are sent in clear text to the server.

    The Basic authentication scheme is based on the model that a client must identify itself with a user name and password for each realm. The server services the request only if the request is sent with an authorization header that includes a valid user name and password.

-   Challenge-response schemes, such as Kerberos, in which the server challenges the client with [*authentication data*](glossary.md). The client transforms the data with the user credentials and sends the transformed data back to the server for authentication.

    Challenge-response schemes enable a more secure authentication. In a challenge-response scheme, the username and password are never transmitted over the network. After the client selects a challenge-response scheme, the server returns an appropriate status code with a challenge that contains the [*authentication data*](glossary.md) for that scheme. The client then resends the request with the proper response to obtain the requested service. Challenge-response schemes can take multiple exchanges to complete.

The following table contains the authentication schemes that are supported by WinHTTP, the authentication type, and a description of the scheme.



| Scheme            | Type               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-------------------|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Basic (plaintext) | Basic              | Uses a [*base64 encoded*](glossary.md) string that contains the user name and password.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Digest            | Challenge-response | Challenges using a nonce (a server-specified data string) value. A valid response contains a checksum of the user name, the password, the given nonce value, the [*HTTP verb*](glossary.md), and the requested Uniform Resource Identifier (URI).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| NTLM              | Challenge-response | Requires the [*authentication data*](glossary.md) to be transformed with the user credentials to prove identity. For NTLM authentication to function correctly, several exchanges must take place on the same connection. Therefore, NTLM authentication cannot be used if an intervening proxy does not support keep-alive connections. NTLM authentication also fails if [**WinHttpSetOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetoption) is used with the [**WINHTTP\_DISABLE\_KEEP\_ALIVE**](option-flags.md) flag that disables keep-alive semantics.                                                                                                                                                                                                                                       |
| Passport          | Challenge-response | Uses [Microsoft Passport 1.4](passport-authentication-in-winhttp.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Negotiate         | Challenge-response | If both the server and client are using Windows 2000 or later, Kerberos authentication is used. Otherwise NTLM authentication is used. Kerberos is available in Windows 2000 and later operating systems and is considered to be more secure than NTLM authentication. For Negotiate authentication to function correctly, several exchanges must take place on the same connection. Therefore, Negotiate authentication cannot be used if an intervening proxy does not support keep-alive connections. Negotiate authentication also fails if [**WinHttpSetOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetoption) is used with the [**WINHTTP\_DISABLE\_KEEP\_ALIVE**](option-flags.md) flag that disables keep-alive semantics. The Negotiate authentication scheme is sometimes called Integrated Windows authentication. |



 

## Authentication in WinHTTP Applications

The WinHTTP application programming interface (API) provides two functions used to access Internet resources in situations where authentication is required: [**WinHttpSetCredentials**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetcredentials) and [**WinHttpQueryAuthSchemes**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpqueryauthschemes).

When a response is received with a 401 or 407 status code, [**WinHttpQueryAuthSchemes**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpqueryauthschemes) can be used to parse the authentication headers to determine the supported authentication schemes and the authentication target. The authentication target is the server or proxy that requests authentication. **WinHttpQueryAuthSchemes** also determines the first authentication scheme, from the available schemes, based on the authentication scheme preferences suggested by the server. This method for choosing an authentication scheme is the behavior suggested by [RFC 2616](https://www.ietf.org/rfc/rfc2616.txt).

[**WinHttpSetCredentials**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetcredentials) enables an application to specify the authentication scheme that is used along with a valid username and password for use on the target server or proxy. After setting the credentials and resending the request, the necessary headers are generated and added to the request automatically. Because some authentication schemes require multiple transactions [**WinHttpSendRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsendrequest) could return the error, ERROR\_WINHTTP\_RESEND\_REQUEST. When this error is encountered, the application should continue to resend the request until a response is received that does not contain a 401 or 407 status code. A 200 status code indicates that the resource is available and the request is successful. See [**HTTP Status Codes**](http-status-codes.md) for additional status codes that can be returned.

If an acceptable authentication scheme and credentials are known before a request is sent to the server, an application can call [**WinHttpSetCredentials**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetcredentials) before calling [**WinHttpSendRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsendrequest). In this case, WinHTTP attempts pre-authentication with the server by providing credentials or [*authentication data*](glossary.md) in the initial request to the server. Pre-authentication can decrease the number of exchanges in the authentication process and therefore improve application performance.

Preauthentication can be used with the following authentication schemes:

-   Basic - always possible.
-   Negotiate resolving into Kerberos - very likely possible; the only exception is when the time-skews are off between the client and the domain controller.
-   (Negotiate resolving into NTLM) - never possible.
-   NTLM - possible in Windows Server 2008 R2 only.
-   Digest - never possible.
-   Passport - never possible; after the initial challenge-response, WinHTTP uses cookies to pre-authenticate to Passport.

A typical WinHTTP application completes the following steps in order to handle authentication.

-   Request a resource with [**WinHttpOpenRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpopenrequest) and [**WinHttpSendRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsendrequest).
-   Check the response headers with [**WinHttpQueryHeaders**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpqueryheaders).
-   If a 401 or 407 status code is returned indicating that authentication is required, call [**WinHttpQueryAuthSchemes**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpqueryauthschemes) to find an acceptable scheme.
-   Set the authentication scheme, username, and password with [**WinHttpSetCredentials**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetcredentials).
-   Resend the request with the same request handle by calling [**WinHttpSendRequest**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsendrequest).

The credentials set by [**WinHttpSetCredentials**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetcredentials) are only used for one request. WinHTTP does not cache the credentials to use in other requests, which means that applications must be written that can respond to multiple requests. If an authenticated connection is re-used, other requests may not be challenged, but your code should be able to respond to a request at any time.

### Example: Retrieving a Document

The following sample code attempts to retrieve a specified document from an HTTP server. The status code is retrieved from the response to determine if authentication is required. If a 200 status code is found, the document is available. If a status code of 401 or 407 is found, authentication is required before the document can be retrieved. For any other status code, an error message is displayed. See [**HTTP Status Codes**](http-status-codes.md) for a list of possible status codes.


```C++
#include <windows.h>
#include <winhttp.h>
#include <stdio.h>

#pragma comment(lib, "winhttp.lib")

DWORD ChooseAuthScheme( DWORD dwSupportedSchemes )
{
  //  It is the server's responsibility only to accept 
  //  authentication schemes that provide a sufficient
  //  level of security to protect the servers resources.
  //
  //  The client is also obligated only to use an authentication
  //  scheme that adequately protects its username and password.
  //
  //  Thus, this sample code does not use Basic authentication  
  //  becaus Basic authentication exposes the client's username
  //  and password to anyone monitoring the connection.
  
  if( dwSupportedSchemes & WINHTTP_AUTH_SCHEME_NEGOTIATE )
    return WINHTTP_AUTH_SCHEME_NEGOTIATE;
  else if( dwSupportedSchemes & WINHTTP_AUTH_SCHEME_NTLM )
    return WINHTTP_AUTH_SCHEME_NTLM;
  else if( dwSupportedSchemes & WINHTTP_AUTH_SCHEME_PASSPORT )
    return WINHTTP_AUTH_SCHEME_PASSPORT;
  else if( dwSupportedSchemes & WINHTTP_AUTH_SCHEME_DIGEST )
    return WINHTTP_AUTH_SCHEME_DIGEST;
  else
    return 0;
}

struct SWinHttpSampleGet
{
  LPCWSTR szServer;
  LPCWSTR szPath;
  BOOL fUseSSL;
  LPCWSTR szServerUsername;
  LPCWSTR szServerPassword;
  LPCWSTR szProxyUsername;
  LPCWSTR szProxyPassword;
};

void WinHttpAuthSample( IN SWinHttpSampleGet *pGetRequest )
{
  DWORD dwStatusCode = 0;
  DWORD dwSupportedSchemes;
  DWORD dwFirstScheme;
  DWORD dwSelectedScheme;
  DWORD dwTarget;
  DWORD dwLastStatus = 0;
  DWORD dwSize = sizeof(DWORD);
  BOOL  bResults = FALSE;
  BOOL  bDone = FALSE;

  DWORD dwProxyAuthScheme = 0;
  HINTERNET  hSession = NULL, 
             hConnect = NULL,
             hRequest = NULL;

  // Use WinHttpOpen to obtain a session handle.
  hSession = WinHttpOpen( L"WinHTTP Example/1.0",  
                          WINHTTP_ACCESS_TYPE_DEFAULT_PROXY,
                          WINHTTP_NO_PROXY_NAME, 
                          WINHTTP_NO_PROXY_BYPASS, 0 );

  INTERNET_PORT nPort = ( pGetRequest->fUseSSL ) ? 
                        INTERNET_DEFAULT_HTTPS_PORT  :
                        INTERNET_DEFAULT_HTTP_PORT;

  // Specify an HTTP server.
  if( hSession )
    hConnect = WinHttpConnect( hSession, 
                               pGetRequest->szServer, 
                               nPort, 0 );

  // Create an HTTP request handle.
  if( hConnect )
    hRequest = WinHttpOpenRequest( hConnect, 
                                   L"GET", 
                                   pGetRequest->szPath,
                                   NULL, 
                                   WINHTTP_NO_REFERER, 
                                   WINHTTP_DEFAULT_ACCEPT_TYPES,
                                   ( pGetRequest->fUseSSL ) ? 
                                       WINHTTP_FLAG_SECURE : 0 );

  // Continue to send a request until status code 
  // is not 401 or 407.
  if( hRequest == NULL )
    bDone = TRUE;

  while( !bDone )
  {
    //  If a proxy authentication challenge was responded to, reset
    //  those credentials before each SendRequest, because the proxy  
    //  may require re-authentication after responding to a 401 or  
    //  to a redirect. If you don't, you can get into a 
    //  407-401-407-401- loop.
    if( dwProxyAuthScheme != 0 )
      bResults = WinHttpSetCredentials( hRequest, 
                                        WINHTTP_AUTH_TARGET_PROXY, 
                                        dwProxyAuthScheme, 
                                        pGetRequest->szProxyUsername,
                                        pGetRequest->szProxyPassword,
                                        NULL );
    // Send a request.
    bResults = WinHttpSendRequest( hRequest,
                                   WINHTTP_NO_ADDITIONAL_HEADERS,
                                   0,
                                   WINHTTP_NO_REQUEST_DATA,
                                   0, 
                                   0, 
                                   0 );

    // End the request.
    if( bResults )
      bResults = WinHttpReceiveResponse( hRequest, NULL );

    // Resend the request in case of 
    // ERROR_WINHTTP_RESEND_REQUEST error.
    if( !bResults && GetLastError( ) == ERROR_WINHTTP_RESEND_REQUEST)
        continue;

    // Check the status code.
    if( bResults ) 
      bResults = WinHttpQueryHeaders( hRequest, 
                                      WINHTTP_QUERY_STATUS_CODE |
                                      WINHTTP_QUERY_FLAG_NUMBER,
                                      NULL, 
                                      &dwStatusCode, 
                                      &dwSize, 
                                      NULL );

    if( bResults )
    {
      switch( dwStatusCode )
      {
        case 200: 
          // The resource was successfully retrieved.
          // You can use WinHttpReadData to read the 
          // contents of the server's response.
          printf( "The resource was successfully retrieved.\n" );
          bDone = TRUE;
          break;

        case 401:
          // The server requires authentication.
          printf(" The server requires authentication. Sending credentials...\n" );

          // Obtain the supported and preferred schemes.
          bResults = WinHttpQueryAuthSchemes( hRequest, 
                                              &dwSupportedSchemes, 
                                              &dwFirstScheme, 
                                              &dwTarget );

          // Set the credentials before resending the request.
          if( bResults )
          {
            dwSelectedScheme = ChooseAuthScheme( dwSupportedSchemes);

            if( dwSelectedScheme == 0 )
              bDone = TRUE;
            else
              bResults = WinHttpSetCredentials( hRequest, 
                                        dwTarget, 
                                        dwSelectedScheme,
                                        pGetRequest->szServerUsername,
                                        pGetRequest->szServerPassword,
                                        NULL );
          }

          // If the same credentials are requested twice, abort the
          // request.  For simplicity, this sample does not check
          // for a repeated sequence of status codes.
          if( dwLastStatus == 401 )
            bDone = TRUE;

          break;

        case 407:
          // The proxy requires authentication.
          printf( "The proxy requires authentication.  Sending credentials...\n" );

          // Obtain the supported and preferred schemes.
          bResults = WinHttpQueryAuthSchemes( hRequest, 
                                              &dwSupportedSchemes, 
                                              &dwFirstScheme, 
                                              &dwTarget );

          // Set the credentials before resending the request.
          if( bResults )
            dwProxyAuthScheme = ChooseAuthScheme(dwSupportedSchemes);

          // If the same credentials are requested twice, abort the
          // request.  For simplicity, this sample does not check 
          // for a repeated sequence of status codes.
          if( dwLastStatus == 407 )
            bDone = TRUE;
          break;

        default:
          // The status code does not indicate success.
          printf("Error. Status code %d returned.\n", dwStatusCode);
          bDone = TRUE;
      }
    }

    // Keep track of the last status code.
    dwLastStatus = dwStatusCode;

    // If there are any errors, break out of the loop.
    if( !bResults ) 
        bDone = TRUE;
  }

  // Report any errors.
  if( !bResults )
  {
    DWORD dwLastError = GetLastError( );
    printf( "Error %d has occurred.\n", dwLastError );
  }

  // Close any open handles.
  if( hRequest ) WinHttpCloseHandle( hRequest );
  if( hConnect ) WinHttpCloseHandle( hConnect );
  if( hSession ) WinHttpCloseHandle( hSession );
}

```



## Automatic Logon Policy

The automatic logon (auto-logon) policy determines when it is acceptable for WinHTTP to include the default credentials in a request. The default credentials are either the current thread token or the session token depending on whether WinHTTP is used in synchronous or asynchronous mode. The thread token is used in synchronous mode, and the session token is used in asynchronous mode. These default credentials are often the username and password used to log on to Microsoft Windows.

The auto-logon policy was implemented to prevent these credentials from being casually used to authenticate against an untrusted server. By default, the security level is set to WINHTTP\_AUTOLOGON\_SECURITY\_LEVEL\_MEDIUM, which allows the default credentials to be used only for Intranet requests. The auto-logon policy only applies to the NTLM and Negotiate authentication schemes. Credentials are never automatically transmitted with other schemes.

The auto-logon policy can be set using the [**WinHttpSetOption**](/windows/desktop/api/Winhttp/nf-winhttp-winhttpsetoption) function with the [**WINHTTP\_OPTION\_AUTOLOGON\_POLICY**](option-flags.md) flag. This flag applies only to the request handle. When the policy is set to WINHTTP\_AUTOLOGON\_SECURITY\_LEVEL\_LOW, default credentials can be sent to all servers. When the policy is set to WINHTTP\_AUTOLOGON\_SECURITY\_LEVEL\_HIGH, default credentials cannot be used for authentication. It is strongly recommended that you use the auto-logon at the MEDIUM level.

## Stored User Names and Passwords

Windows XP introduced the concept of Stored User Names and Passwords. If a user's Passport credentials are saved through the **Passport Registration Wizard** or the standard **Credential Dialog**, it is saved in the Stored User Names and Passwords. When using WinHTTP on Windows XP or later, WinHTTP automatically uses the credentials in the Stored User Names and Passwords if credentials are not explicitly set. This is similar to the support of default logon credentials for NTLM/Kerberos. However, use of default Passport credentials is not subject to the automatic logon policy settings.

 

 



