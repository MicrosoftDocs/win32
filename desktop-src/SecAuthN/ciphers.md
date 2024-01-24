---
description: The following material is valid only when Digest is used as a SASL mechanism. Ciphers and encryption are not available for HTTP authentication using Microsoft Digest.
ms.assetid: 3836b064-241f-4276-af08-557bdc53bb36
title: Ciphers
ms.topic: article
ms.date: 05/31/2018
---

# Ciphers

The following material is valid only when Digest is used as a SASL mechanism. Ciphers and encryption are not available for HTTP authentication using Microsoft Digest.

A Digest SASL challenge's cipher directive contains a list of the ciphers supported by a server that requires confidential communications. The cipher directive can only be included if the qop directive is set to "auth-conf". The ciphers recognized by Microsoft Digest are listed in the following table, in order from strongest to weakest.



| Cipher value | Description                                                                                                                                                                                                                                                                                    |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| "rc4"        | The RC4 cipher with a 128-bit key.                                                                                                                                                                                                                                                             |
| "3des"       | The [*triple DES*](/windows/desktop/SecGloss/t-gly) cipher in [*CBC*](/windows/desktop/SecGloss/c-gly) mode with EDE with the same key for each E stage (two keys mode). Total key length is 112 bits. |
| "rc4-56"     | The RC4 cipher with a 56-bit key.                                                                                                                                                                                                                                                              |
| "rc4-40"     | The RC4 cipher with a 40-bit key.                                                                                                                                                                                                                                                              |
| "des"        | The [*Data Encryption Standard*](/windows/desktop/SecGloss/d-gly) (DES) cipher in [*cipher block chaining*](/windows/desktop/SecGloss/c-gly) (CBC) mode with a 56-bit key. |



 

When a server application requests confidentiality (qop="auth-conf") Microsoft Digest will generate a challenge that offers the client all of the ciphers installed on the server and supported by Digest. The Digest client will select the strongest available cipher. For details on specifying confidentiality, see [Generating the Digest Challenge](generating-the-digest-challenge.md).

 

 
