---
description: Glossary page
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 08951f9f-d03d-4720-8f18-1413ba72e93d
title: Glossary (WinHTTP)
ms.topic: article
ms.date: 05/31/2018
---

# Glossary (WinHTTP)

<dl> <dt>

<span id="term_authentication_data"></span><span id="TERM_AUTHENTICATION_DATA"></span>**authentication data**
</dt> <dd>

Scheme-specific block of data that is exchanged between the server and client during authentication. To prove its identity, the client encrypts some or all of this data with a user name and password. The client sends the encrypted data to the server, which decrypts the data and compares it to the original. If the decrypted data matches the original data, the client is authenticated.

</dd> <dt>

<span id="term_base64_encoding"></span><span id="TERM_BASE64_ENCODING"></span>**base64 encoding**
</dt> <dd>

Scheme used to transmit binary data. Base64 processes data as 24-bit groups, mapping this data to four encoded characters. It is sometimes referred to as 3-to-4 encoding. Each 6 bits of the 24-bit group is used as an index into a mapping table (the base64 alphabet) to obtain a character for the encoded data. The encoded data has line lengths limited to 76 characters.

</dd> <dt>

<span id="term_certificate_store"></span><span id="TERM_CERTIFICATE_STORE"></span>**certificate store**
</dt> <dd>

Typically, permanent storage where certificates, certificate revocation lists (CRL), and certificate trust lists (CTL) are stored. A certificate store can also be temporary when working with session-based certificates.

</dd> <dt>

<span id="term_cobranding"></span><span id="TERM_COBRANDING"></span>**cobranding**
</dt> <dd>

Ability for a Microsoft Passport participant site to provide its own branding elements and explanations on the Passport network service pages. Cobranding includes customizing the look and feel, specific text, and specific behavior on Passport network pages.

</dd> <dt>

<span id="term_code_page"></span><span id="TERM_CODE_PAGE"></span>**code page**
</dt> <dd>

Table that relates the binary character codes used by a program to keys on the keyboard or to the appearance of characters on the monitor. Using code pages is a way to provide support for character sets and keyboard layouts used in different countries and regions. You can configure devices such as the monitor and the keyboard to use a specific code page and to switch from one code page (such as United States) to another (such as Portugal) at the user's request.

</dd> <dt>

<span id="term_http_verb"></span><span id="TERM_HTTP_VERB"></span>**HTTP verb**
</dt> <dd>

The HTTP verb (or HTTP method) is an instruction sent in a request message that notifies an HTTP server of the action to perform on the specified resource. For example, "GET" specifies that a resource is being retrieved from the server. Common verbs include "GET", "POST", and "HEAD". For more information and a complete list of standard HTTP verbs, see the HTTP/1.1 specification.

</dd> <dt>

<span id="term_ticket"></span><span id="TERM_TICKET"></span>**ticket**
</dt> <dd>

Cookie that contains a user profile for Passport authentication. Each ticket corresponds to one URL. The logon server of a Passport Domain Authority provides tickets that the client sends to a Passport member for authentication.

</dd> <dt>

<span id="term_user_agent"></span><span id="TERM_USER_AGENT"></span>**user agent**
</dt> <dd>

The user agent is the client application that requests a document from an HTTP server. When the client sends a request to an HTTP server, typically it sends the name of the user agent with the request header so that the server can determine the capabilities of the client software.

</dd> </dl>

 

 



