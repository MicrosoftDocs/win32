---
Description: In order for a namespace provider to be accessible through Windows Sockets it must be properly installed on the system and registered with Windows Sockets.
ms.assetid: c73baf62-b862-476c-b381-be00699e78ca
title: Name Resolution Configuration and Installation
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Name Resolution Configuration and Installation

In order for a namespace provider to be accessible through Windows Sockets it must be properly installed on the system and registered with Windows Sockets. When a namespace provider is installed by invoking a vendor's installation program, configuration information must be added to a configuration database to give the Ws2\_32.dll required information regarding the service provider. The Ws2\_32.dll exports [**WSCInstallNameSpace**](/windows/win32/Ws2spi/nf-ws2spi-wscinstallnamespace?branch=master) for the vendor's installation program to use. This function is used to supply relevant information about the service provider to be installed. This information includes:

-   Provider Name — A string representing the provider for display in Control Panel.
-   Provider Version — The version of this provider.
-   Provider Path — A path name to the provider DLL.
-   Namespace — The namespace supported by the provider.
-   Provider GUID — A unique, vendor-supplied number representing this provider/namespace combination. This is used as a key for all subsequent references to this provider, and for uninstall. These values are created using the Uuidgen.exe utility.
-   Stores all flags — a flag indicating whether this namespace provider will be responsible for retaining all service class schema information for all service classes. If such a provider exists, the Ws2\_32.dll does not need to query each individual namespace provider for this information.

On Windows Vista and later, an enhanced [**WSCInstallNameSpaceEx32**](/windows/win32/Ws2spi/nf-ws2spi-wscinstallnamespaceex32?branch=master) function is provided that allows the namespace provider to pass an additional blob of data specific to the namespace.

On 64-bit platforms, similar [**WSCInstallNameSpace32**](/windows/win32/Ws2spi/nf-ws2spi-wscinstallnamespace32?branch=master) and [**WSCInstallNameSpaceEx32**](/windows/win32/Ws2spi/nf-ws2spi-wscinstallnamespaceex32?branch=master) functions are provided to install a namespace in the 32-bit catalog.

The Ws2\_32.dll also provides a function, [**WSCUnInstallNameSpace**](/windows/win32/Ws2spi/nf-ws2spi-wscuninstallnamespace?branch=master), for a vendor's deinstallation program to remove all the relevant information from the configuration database. The exact location and format of this configuration information is private to the Ws2\_32.dll, and can only be manipulated by the above-mentioned functions.

On 64-bit platforms, a similar [**WSCInstallNameSpace32**](/windows/win32/Ws2spi/nf-ws2spi-wscinstallnamespace32?branch=master) function is provided to uninstall a namespace in the 32-bit catalog.

At any point, an namespace provider is considered to be either active or inactive, with this setting controlled through the [**WSCEnableNSProvider**](/windows/win32/Ws2spi/nf-ws2spi-wscenablensprovider?branch=master) and [**WSCEnableNSProvider32**](/windows/win32/Ws2spi/nf-ws2spi-wscenablensprovider32?branch=master) functions. Namespace providers that are inactive continue to show up when enumerated (using the [**WSAEnumNameSpaceProviders**](/windows/win32/Winsock2/nf-winsock2-wsaenumnamespaceprovidersa?branch=master), [**WSAEnumNameSpaceProvidersEx**](/windows/win32/Winsock2/nf-winsock2-wsaenumnamespaceprovidersexa?branch=master), [**WSCEnumNameSpaceProviders32**](/windows/win32/Ws2spi/nf-ws2spi-wscenumnamespaceproviders32?branch=master), and [**WSCEnumNameSpaceProvidersEx32**](/windows/win32/Ws2spi/nf-ws2spi-wscenumnamespaceprovidersex32?branch=master) functions), but the Ws2\_32.dll will not route any query or service registration operations to these providers. This capability can be useful in situations where more than one of the installed namespace providers can support a given namespace.

When multiple namespace providers are referenced in a single API function, the order in which the order in which the queries and registration operations are routed to namespace providers is unspecified. The order is unrelated to the order in which namespace providers are installed. There are two ways to control which namespace providers are used to resolve a name query. First, the [**WSCEnableNSProvider**](/windows/win32/Ws2spi/nf-ws2spi-wscenablensprovider?branch=master) and [**WSCEnableNSProvider32**](/windows/win32/Ws2spi/nf-ws2spi-wscenablensprovider32?branch=master) functions can be used to enable and disable namespaces in a computer-wide, persistent way. Second, applications can direct an individual query to a particular provider by specifying that provider's identifying GUID as part of the query.

 

 



