---
title: Parsing Exceptions
description: HTTP Server API provides registry keys to support parsing exceptions to the HTTP/1.1 specification for backward compatibility.
ms.assetid: b93a3b43-c1ca-41ec-9702-72c1b04aec69
keywords:
- Parsing Exceptions
ms.topic: article
ms.date: 05/31/2018
---

# Parsing Exceptions

HTTP Server API provides registry keys to support parsing exceptions to the HTTP/1.1 specification for backward compatibility. These exceptions are not enabled by default and should be enabled only on a case-by-case basis, when the server experiences compatibility issues with HTTP clients. These values are created under the following registry location:

```
HKEY_LOCAL_MACHINE
   System
      CurrentControlSet
         Services
            Http
               Parameters
```

The following table lists registry keys provided to support the exceptions listed. To enable an exception set the corresponding key value to 1 and restart the HTTP service.



| Key name                              | Description                                                                                                                                                                                                                                                                                                                                                                     |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AllowWeakHeaderNameSyntax (DWORD)     | Allows the HTTP parser to accept header names with separator characters such as '?'.                                                                                                                                                                                                                                                                                            |
| AllowWeakHeaderValueSyntax (DWORD)    | Allows the HTTP parser to accept header values with raw (unescaped) control characters in it.                                                                                                                                                                                                                                                                                   |
| AllowCaseInsensitiveVerbs (DWORD)     | Allows the HTTP parser to accept lowercase HTTP methods/verbs such as "get".                                                                                                                                                                                                                                                                                                    |
| AllowUnEscapedRestrictedChars (DWORD) | Allows the HTTP parser to accept control characters in abspath and query strings of the URL. In case of an absolute URL, control characters will not be allowed in the hostname. All flavors of URLs, namely UTF8, DBCS and ANSI, will allow control characters. All ASCII control characters except NUL (0x00), LF (0x0a), CR (0x0d) and Horizontal Tab(0x09) will be allowed. |



 

 

 




