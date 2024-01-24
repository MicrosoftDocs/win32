---
description: Specifying Schannel Ciphers and Cipher Strengths
ms.assetid: b87d3e72-df7b-4a00-854e-c3706565ed7d
title: Specifying Schannel Ciphers and Cipher Strengths
ms.topic: article
ms.date: 05/31/2018
---

# Specifying Schannel Ciphers and Cipher Strengths

For client/server information exchanges, the default behavior of Schannel is to negotiate the best cipher available based on those enabled in the registry. Applications may limit the ciphers and cipher strengths allowed for a connection by using members of the [**SCHANNEL\_CRED**](/windows/desktop/api/Schannel/ns-schannel-schannel_cred) structure as follows:

1.  Set the **palgSupportedAlgs** member to an array of [**ALG\_ID**](../seccrypto/alg-id.md) containing the allowable ciphers. For more information, see Cipher IDs.
2.  Set the **dwMinimumCipherStrength** and/or **dwMaximumCipherStrength** members to the allowable minimum and maximum strengths. For more information, see Cipher Strength Values.
3.  Pass the [**SCHANNEL\_CRED**](/windows/desktop/api/Schannel/ns-schannel-schannel_cred) structure (by means of the *pAuthData* parameter) in a call to the [**AcquireCredentialsHandle**](/windows/win32/api/sspi/nf-sspi-acquirecredentialshandlea) function. This function returns a credentials handle.
4.  Specify the credentials handle in a call to the client-side [**InitializeSecurityContext (General)**](/windows/win32/api/sspi/nf-sspi-initializesecuritycontexta) function or the server-side [**AcceptSecurityContext (General)**](/windows/win32/api/sspi/nf-sspi-acceptsecuritycontext) function.

## Cipher IDs

The default behavior of Schannel is to request the best cipher available based on Schannel entries in the system registry. Do not change the system registry; the settings it contains for Schannel are used globally and will affect other applications. For the list of valid constants, see [**ALG\_ID**](../seccrypto/alg-id.md).

## Cipher Strength Values

This Schannel feature is typically used to limit a connection to either domestic or export strength ciphers. Domestic strengths include 56, and 128 bits, while export strength is limited to 56 bits. If you set the minimum and maximum values to zero Schannel will use all available cipher strengths.

Using TLS or SSL 3.0, set the **dwMinimumCipherStrength** member to -1 (negative one) to enable the "Null Cipher" cipher suites, which provide signatures but no encryption. If **dwMaximumCipherStrength** is also set to -1 then only the "Null Cipher" suites will be enabled. This setting is intended for development only and should not be used in production systems.

## Querying Cipher Information

To retrieve the cipher strength settings for a credential, call the [**QueryCredentialsAttributes**](/windows/desktop/api/Sspi/nf-sspi-querycredentialsattributesa) function and specify SECPKG\_ATTR\_CIPHER\_STRENGTHS as the *ulAttribute* parameter.

To retrieve the list of supported algorithms for a credential, call the [**QueryCredentialsAttributes**](/windows/desktop/api/Sspi/nf-sspi-querycredentialsattributesa) with SECPKG\_ATTR\_SUPPORTED\_ALGS as the *ulAttribute* parameter.

 

 
