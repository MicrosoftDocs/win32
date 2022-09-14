---
description: WSCEnableNSProviderWSCEnableNSProvider32WSCInstallNameSpaceWSCInstallNameSpace32WSCInstallNameSpaceExWSCInstallNameSpaceEx32WSCUnInstallNameSpaceWSCUnInstallNameSpace32WSCWriteNameSpaceOrderWSCWriteNameSpaceOrder32
ms.assetid: 3dd289fb-eebb-48b2-a887-eeb60322ab09
title: Namespace Provider Configuration and Installation
ms.topic: article
ms.date: 05/31/2018
---

# Namespace Provider Configuration and Installation

-   [**WSCEnableNSProvider**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscenablensprovider)
-   [**WSCEnableNSProvider32**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscenablensprovider32)
-   [**WSCInstallNameSpace**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscinstallnamespace)
-   [**WSCInstallNameSpace32**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscinstallnamespace32)
-   [**WSCInstallNameSpaceEx**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscinstallnamespaceex)
-   [**WSCInstallNameSpaceEx32**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscinstallnamespaceex32)
-   [**WSCUnInstallNameSpace**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscuninstallnamespace)
-   [**WSCUnInstallNameSpace32**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscuninstallnamespace32)
-   [**WSCWriteNameSpaceOrder**](/windows/desktop/api/Sporder/nf-sporder-wscwritenamespaceorder)
-   [**WSCWriteNameSpaceOrder32**](/windows/desktop/api/Sporder/nf-sporder-wscwritenamespaceorder32)

As mentioned previously, the installation application for a namespace provider must call [**WSCInstallNameSpace**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscinstallnamespace) or [**WSCInstallNameSpaceEx**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscinstallnamespaceex) to register with the Ws2\_32.dll and supply static configuration information. To install into the 32-bit catalog on a 64-bit platform, the namespace provider must call [**WSCInstallNameSpace32**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscinstallnamespace32) or [**WSCInstallNameSpaceEx32**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscinstallnamespaceex32). The Ws2\_32.dll uses this information to accomplish its routing function and in its implementation of [**WSAEnumNameSpaceProviders**](/windows/desktop/api/Winsock2/nf-winsock2-wsaenumnamespaceprovidersa) and [**WSAEnumNameSpaceProvidersEx**](/windows/desktop/api/Winsock2/nf-winsock2-wsaenumnamespaceprovidersexa). The [**WSCUnInstallNameSpace**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscuninstallnamespace) function is used to remove a namespace provider from the registry, and the [**WSCEnableNSProvider**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscenablensprovider) function is used to toggle a provider between the active and inactive states.

On a 64-bit platform, [**WSCUnInstallNameSpace32**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscuninstallnamespace32) and [**WSCEnableNSProvider32**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscenablensprovider32) are similar functions to deal with the 32-bit catalog.

The results of these three operations are not visible to applications that are currently loaded and running. Only applications that begin executing after these operations have occurred will be affected by them.

This architecture explicitly supports the instantiation of multiple namespace providers within a single DLL, however each such provider must have a unique namespace provider identifier (GUID) allocated, and a separate call to [**WSCInstallNameSpace**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscinstallnamespace) or [**WSCInstallNameSpaceEx**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscinstallnamespaceex) must occur for each instantiation (On 64-bit platforms, the functions for the 32-bit catalog are [**WSCInstallNameSpace32**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscinstallnamespace32) and [**WSCInstallNameSpaceEx32**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscinstallnamespaceex32)). Such a provider can determine which instantiation is being invoked because the namespace provider (NSP) identifier appears as a parameter in every NSP function.

 

 



