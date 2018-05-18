---
title: Smart Card Modules
description: Communicates to a specific type of smart card through the Smart Card Resource Manager.
ms.assetid: 'a33e4e23-5f0d-4d03-ae3b-8727cdf57ab7'
---

# Smart Card Modules

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

Smart card modules act as card-specific plug-ins for the [Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md). A smart card module communicates to a specific type of [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly) through the [Smart Card Resource Manager](https://msdn.microsoft.com/library/windows/desktop/aa380148).

A smart card module is implemented as a [*dynamic-link library*](https://msdn.microsoft.com/library/windows/desktop/ms721573#-security-dynamic-link-library-gly). A card module must implement the [**CardAcquireContext**](cardacquirecontext.md) function. A card module must also implement the functions [*DllMain*](https://msdn.microsoft.com/library/windows/desktop/ms682583), [**DllRegisterServer**](https://msdn.microsoft.com/library/windows/desktop/ms682162), and [**DllUnregisterServer**](https://msdn.microsoft.com/library/windows/desktop/ms691457). A card module can also implement any or all of the functions described in [Smart Card API Functions](smart-card-api-functions.md).

The [Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md) initiates communication to a smart card module by calling the [**CardAcquireContext**](cardacquirecontext.md) function implemented by that card module. State information and function pointers that enable communication between a smart card module and the Microsoft Base Smart Card Cryptographic Service Provider are contained in a [**CARD\_DATA**](card-data.md) structure.

## Registering Card Types

The [**DllRegisterServer**](https://msdn.microsoft.com/library/windows/desktop/ms682162) function implemented by a smart card module must call the [**SCardIntroduceCardType**](https://msdn.microsoft.com/library/windows/desktop/aa379784) and [**SCardSetCardTypeProviderName**](https://msdn.microsoft.com/library/windows/desktop/aa379802) functions to register the types of smart cards that the smart card module supports.

The [**DllUnregisterServer**](https://msdn.microsoft.com/library/windows/desktop/ms691457) function implemented by a smart card module must call the [**SCardForgetCardType**](https://msdn.microsoft.com/library/windows/desktop/aa379482) function to unregister the types of smart cards that the smart card module supports.

 

 




