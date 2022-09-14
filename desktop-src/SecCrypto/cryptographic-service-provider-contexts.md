---
description: The first CryptoAPI function called by an application that uses any cryptographic APIs is the CryptAcquireContext function.
ms.assetid: ad1ff45c-7d02-431b-a287-e9db765476ce
title: Cryptographic Service Provider Contexts
ms.topic: article
ms.date: 05/31/2018
---

# Cryptographic Service Provider Contexts

The first [*CryptoAPI*](../secgloss/c-gly.md) function called by an application that uses any cryptographic APIs is the [**CryptAcquireContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptacquirecontexta) function. This function returns a handle to a particular CSP which includes the specification of a particular [*key container*](../secgloss/k-gly.md) within the CSP. This key container is either a specifically requested key container or it is the default key container for the currently logged-on user.

[**CryptAcquireContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptacquirecontexta) can also create a new key container. For more information, see [Example C Program: Creating a Key Container and Generating Keys](example-c-program-creating-a-key-container-and-generating-keys.md) and [Example C Program: Using CryptAcquireContext](example-c-program-using-cryptacquirecontext.md).

A [*cryptographic service provider*](../secgloss/c-gly.md) (CSP) has both a name and a type. For example, the name of one of the CSPs currently shipped with the operating system is [Microsoft Base Cryptographic Provider](microsoft-base-cryptographic-provider.md). It is a [PROV\_RSA\_FULL](prov-rsa-full.md) type provider. The name of each provider is unique; the provider type is not.

When an application calls [**CryptAcquireContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptacquirecontexta) to obtain a CSP handle, it specifies a provider type and, optionally, a provider name. If both a type and a name are specified, the function loads the CSP with the matching provider type and provider name. The function returns the CSP's handle which provides access to both the CSP and to a [*key container*](../secgloss/k-gly.md) within the CSP.

When an application calls [**CryptAcquireContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptacquirecontexta) and specifies a provider type but no provider name, the function looks for a named provider, first checking a list of default named providers associated with the logged-on user and, if that fails, from a list of default named providers associated with the computer. After the provider name has been determined, the **CryptAcquireContext** function searches for the CSP for that provider, loads it, and returns its handle.

When you have finished using a CSP handle, release it by calling the [**CryptReleaseContext**](/windows/desktop/api/Wincrypt/nf-wincrypt-cryptreleasecontext) function.

 

 
