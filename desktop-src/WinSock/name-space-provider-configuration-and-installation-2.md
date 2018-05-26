---
Description: WSCEnableNSProviderWSCEnableNSProvider32WSCInstallNameSpaceWSCInstallNameSpace32WSCInstallNameSpaceExWSCInstallNameSpaceEx32WSCUnInstallNameSpaceWSCUnInstallNameSpace32WSCWriteNameSpaceOrderWSCWriteNameSpaceOrder32
ms.assetid: 3dd289fb-eebb-48b2-a887-eeb60322ab09
title: Namespace Provider Configuration and Installation
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Namespace Provider Configuration and Installation

-   [**WSCEnableNSProvider**](/windows/win32/Ws2spi/nf-ws2spi-wscenablensprovider?branch=master)
-   [**WSCEnableNSProvider32**](/windows/win32/Ws2spi/nf-ws2spi-wscenablensprovider32?branch=master)
-   [**WSCInstallNameSpace**](/windows/win32/Ws2spi/nf-ws2spi-wscinstallnamespace?branch=master)
-   [**WSCInstallNameSpace32**](/windows/win32/Ws2spi/nf-ws2spi-wscinstallnamespace32?branch=master)
-   [**WSCInstallNameSpaceEx**](/windows/win32/Ws2spi/nf-ws2spi-wscinstallnamespaceex?branch=master)
-   [**WSCInstallNameSpaceEx32**](/windows/win32/Ws2spi/nf-ws2spi-wscinstallnamespaceex32?branch=master)
-   [**WSCUnInstallNameSpace**](/windows/win32/Ws2spi/nf-ws2spi-wscuninstallnamespace?branch=master)
-   [**WSCUnInstallNameSpace32**](/windows/win32/Ws2spi/nf-ws2spi-wscuninstallnamespace32?branch=master)
-   [**WSCWriteNameSpaceOrder**](/windows/win32/Sporder/nf-sporder-wscwritenamespaceorder?branch=master)
-   [**WSCWriteNameSpaceOrder32**](/windows/win32/Sporder/nf-sporder-wscwritenamespaceorder32?branch=master)

As mentioned previously, the installation application for a namespace provider must call [**WSCInstallNameSpace**](/windows/win32/Ws2spi/nf-ws2spi-wscinstallnamespace?branch=master) or [**WSCInstallNameSpaceEx**](/windows/win32/Ws2spi/nf-ws2spi-wscinstallnamespaceex?branch=master) to register with the Ws2\_32.dll and supply static configuration information. To install into the 32-bit catalog on a 64-bit platform, the namespace provider must call [**WSCInstallNameSpace32**](/windows/win32/Ws2spi/nf-ws2spi-wscinstallnamespace32?branch=master) or [**WSCInstallNameSpaceEx32**](/windows/win32/Ws2spi/nf-ws2spi-wscinstallnamespaceex32?branch=master). The Ws2\_32.dll uses this information to accomplish its routing function and in its implementation of [**WSAEnumNameSpaceProviders**](/windows/win32/Winsock2/nf-winsock2-wsaenumnamespaceprovidersa?branch=master) and [**WSAEnumNameSpaceProvidersEx**](/windows/win32/Winsock2/nf-winsock2-wsaenumnamespaceprovidersexa?branch=master). The [**WSCUnInstallNameSpace**](/windows/win32/Ws2spi/nf-ws2spi-wscuninstallnamespace?branch=master) function is used to remove a namespace provider from the registry, and the [**WSCEnableNSProvider**](/windows/win32/Ws2spi/nf-ws2spi-wscenablensprovider?branch=master) function is used to toggle a provider between the active and inactive states.

On a 64-bit platform, [**WSCUnInstallNameSpace32**](/windows/win32/Ws2spi/nf-ws2spi-wscuninstallnamespace32?branch=master) and [**WSCEnableNSProvider32**](/windows/win32/Ws2spi/nf-ws2spi-wscenablensprovider32?branch=master) are similar functions to deal with the 32-bit catalog.

The results of these three operations are not visible to applications that are currently loaded and running. Only applications that begin executing after these operations have occurred will be affected by them.

This architecture explicitly supports the instantiation of multiple namespace providers within a single DLL, however each such provider must have a unique namespace provider identifier (GUID) allocated, and a separate call to [**WSCInstallNameSpace**](/windows/win32/Ws2spi/nf-ws2spi-wscinstallnamespace?branch=master) or [**WSCInstallNameSpaceEx**](/windows/win32/Ws2spi/nf-ws2spi-wscinstallnamespaceex?branch=master) must occur for each instantiation (On 64-bit platforms, the functions for the 32-bit catalog are [**WSCInstallNameSpace32**](/windows/win32/Ws2spi/nf-ws2spi-wscinstallnamespace32?branch=master) and [**WSCInstallNameSpaceEx32**](/windows/win32/Ws2spi/nf-ws2spi-wscinstallnamespaceex32?branch=master)). Such a provider can determine which instantiation is being invoked because the namespace provider (NSP) identifier appears as a parameter in every NSP function.

 

 



