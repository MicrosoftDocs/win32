---
Description: WSCEnableNSProviderWSCEnableNSProvider32WSCInstallNameSpaceWSCInstallNameSpace32WSCInstallNameSpaceExWSCInstallNameSpaceEx32WSCUnInstallNameSpaceWSCUnInstallNameSpace32WSCWriteNameSpaceOrderWSCWriteNameSpaceOrder32
ms.assetid: '3dd289fb-eebb-48b2-a887-eeb60322ab09'
title: Namespace Provider Configuration and Installation
---

# Namespace Provider Configuration and Installation

-   [**WSCEnableNSProvider**](wscenablensprovider-2.md)
-   [**WSCEnableNSProvider32**](wscenablensprovider32.md)
-   [**WSCInstallNameSpace**](wscinstallnamespace-2.md)
-   [**WSCInstallNameSpace32**](wscinstallnamespace32.md)
-   [**WSCInstallNameSpaceEx**](wscinstallnamespaceex.md)
-   [**WSCInstallNameSpaceEx32**](wscinstallnamespaceex32.md)
-   [**WSCUnInstallNameSpace**](wscuninstallnamespace-2.md)
-   [**WSCUnInstallNameSpace32**](wscuninstallnamespace32.md)
-   [**WSCWriteNameSpaceOrder**](wscwritenamespaceorder.md)
-   [**WSCWriteNameSpaceOrder32**](wscwritenamespaceorder32.md)

As mentioned previously, the installation application for a namespace provider must call [**WSCInstallNameSpace**](wscinstallnamespace-2.md) or [**WSCInstallNameSpaceEx**](wscinstallnamespaceex.md) to register with the Ws2\_32.dll and supply static configuration information. To install into the 32-bit catalog on a 64-bit platform, the namespace provider must call [**WSCInstallNameSpace32**](wscinstallnamespace32.md) or [**WSCInstallNameSpaceEx32**](wscinstallnamespaceex32.md). The Ws2\_32.dll uses this information to accomplish its routing function and in its implementation of [**WSAEnumNameSpaceProviders**](wsaenumnamespaceproviders-2.md) and [**WSAEnumNameSpaceProvidersEx**](wsaenumnamespaceprovidersex.md). The [**WSCUnInstallNameSpace**](wscuninstallnamespace-2.md) function is used to remove a namespace provider from the registry, and the [**WSCEnableNSProvider**](wscenablensprovider-2.md) function is used to toggle a provider between the active and inactive states.

On a 64-bit platform, [**WSCUnInstallNameSpace32**](wscuninstallnamespace32.md) and [**WSCEnableNSProvider32**](wscenablensprovider32.md) are similar functions to deal with the 32-bit catalog.

The results of these three operations are not visible to applications that are currently loaded and running. Only applications that begin executing after these operations have occurred will be affected by them.

This architecture explicitly supports the instantiation of multiple namespace providers within a single DLL, however each such provider must have a unique namespace provider identifier (GUID) allocated, and a separate call to [**WSCInstallNameSpace**](wscinstallnamespace-2.md) or [**WSCInstallNameSpaceEx**](wscinstallnamespaceex.md) must occur for each instantiation (On 64-bit platforms, the functions for the 32-bit catalog are [**WSCInstallNameSpace32**](wscinstallnamespace32.md) and [**WSCInstallNameSpaceEx32**](wscinstallnamespaceex32.md)). Such a provider can determine which instantiation is being invoked because the namespace provider (NSP) identifier appears as a parameter in every NSP function.

 

 



