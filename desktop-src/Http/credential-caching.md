---
title: Credential Caching
description: Credential Caching
ms.assetid: 6e411333-56fa-455b-a90a-f2b54f3c9545
ms.topic: article
ms.date: 05/31/2018
---

# Credential Caching

## Credential Caching on NTLM KA Connections

The HTTP Server API caches credentials only on Keep-Alive (KA) connections for NTLM authentication. By default, the HTTP Server API caches the credentials obtained on the first request sent on a KA connection. The client can send subsequent requests on KA connections without an authorization header and obtain authentication based on the previously established context. In this case, the HTTP Server API sends the token based on the cached credential to the application. Credentials for a request sent by a proxy are not cached. The application disables NTLM credential caching by setting the **DisableNTLMCredentialCaching** flag in the [**HTTP\_SERVER\_AUTHENTICATION\_INFO**](/windows/desktop/api/Http/ns-http-http_server_authentication_info) structure that is supplied in calls to HttpSetServerSessionProperty or HttpSetUrlGroupProperty. When credential caching is disabled, the HTTP Server API discards the cached credentials and performs authentication for each request

## NTLM Credential Caching for Specific URLs

The application determines if the request credentials returned by the HTTP Server API are cached by inspecting the Flags parameter of the HTTP\_REQUEST\_AUTH\_INFO structure. This parameter indicates HTTP\_REQUEST\_AUTH\_FLAG\_TOKEN\_FOR\_CACHED\_CRED when the returned NTLM token was retrieved from the cache. Credential caching is specified on a URL group for all the URLs in the group. Credential caching on a per URL basis is not supported, however, applications can determine whether to accept or reject cached credentials on a per URL basis by checking the HTTP\_REQUEST\_AUTH\_FLAG\_TOKEN\_FOR\_CACHED\_CRED flag in the HTTP\_REQUEST\_AUTH\_INFO structure. The application rejects the cached credentials by sending a 401 authentication challenge to the client. The client then resends the request with the authorization headers, triggering a new authentication handshake with the HTTP Server API.

## Basic Authentication

When a Basic authentication header is included in the request, the HTTP Server API parses the header to obtain the user name and password. The user name is then parsed into the user and domain portions. The HTTP Server API caches the access token, obtained for Basic authentication, based on the user name and domain key. When a new request is received, the HTTP Server API retrieves the access token based on the user name and domain. The password in the request is then checked against the cached password. The cached access token is deleted when the time-to-live (TTL) limit is reached.

 

 




