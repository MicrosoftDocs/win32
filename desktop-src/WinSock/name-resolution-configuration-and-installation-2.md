---
Description: 'In order for a namespace provider to be accessible through Windows Sockets it must be properly installed on the system and registered with Windows Sockets.'
ms.assetid: 'c73baf62-b862-476c-b381-be00699e78ca'
title: Name Resolution Configuration and Installation
---

# Name Resolution Configuration and Installation

In order for a namespace provider to be accessible through Windows Sockets it must be properly installed on the system and registered with Windows Sockets. When a namespace provider is installed by invoking a vendor's installation program, configuration information must be added to a configuration database to give the Ws2\_32.dll required information regarding the service provider. The Ws2\_32.dll exports [**WSCInstallNameSpace**](wscinstallnamespace-2.md) for the vendor's installation program to use. This function is used to supply relevant information about the service provider to be installed. This information includes:

-   Provider Name — A string representing the provider for display in Control Panel.
-   Provider Version — The version of this provider.
-   Provider Path — A path name to the provider DLL.
-   Namespace — The namespace supported by the provider.
-   Provider GUID — A unique, vendor-supplied number representing this provider/namespace combination. This is used as a key for all subsequent references to this provider, and for uninstall. These values are created using the Uuidgen.exe utility.
-   Stores all flags — a flag indicating whether this namespace provider will be responsible for retaining all service class schema information for all service classes. If such a provider exists, the Ws2\_32.dll does not need to query each individual namespace provider for this information.

On Windows Vista and later, an enhanced [**WSCInstallNameSpaceEx32**](wscinstallnamespaceex32.md) function is provided that allows the namespace provider to pass an additional blob of data specific to the namespace.

On 64-bit platforms, similar [**WSCInstallNameSpace32**](wscinstallnamespace32.md) and [**WSCInstallNameSpaceEx32**](wscinstallnamespaceex32.md) functions are provided to install a namespace in the 32-bit catalog.

The Ws2\_32.dll also provides a function, [**WSCUnInstallNameSpace**](wscuninstallnamespace-2.md), for a vendor's deinstallation program to remove all the relevant information from the configuration database. The exact location and format of this configuration information is private to the Ws2\_32.dll, and can only be manipulated by the above-mentioned functions.

On 64-bit platforms, a similar [**WSCInstallNameSpace32**](wscinstallnamespace32.md) function is provided to uninstall a namespace in the 32-bit catalog.

At any point, an namespace provider is considered to be either active or inactive, with this setting controlled through the [**WSCEnableNSProvider**](wscenablensprovider-2.md) and [**WSCEnableNSProvider32**](wscenablensprovider32.md) functions. Namespace providers that are inactive continue to show up when enumerated (using the [**WSAEnumNameSpaceProviders**](wsaenumnamespaceproviders-2.md), [**WSAEnumNameSpaceProvidersEx**](wsaenumnamespaceprovidersex.md), [**WSCEnumNameSpaceProviders32**](wscenumnamespaceproviders32.md), and [**WSCEnumNameSpaceProvidersEx32**](wscenumnamespaceprovidersex32.md) functions), but the Ws2\_32.dll will not route any query or service registration operations to these providers. This capability can be useful in situations where more than one of the installed namespace providers can support a given namespace.

When multiple namespace providers are referenced in a single API function, the order in which the order in which the queries and registration operations are routed to namespace providers is unspecified. The order is unrelated to the order in which namespace providers are installed. There are two ways to control which namespace providers are used to resolve a name query. First, the [**WSCEnableNSProvider**](wscenablensprovider-2.md) and [**WSCEnableNSProvider32**](wscenablensprovider32.md) functions can be used to enable and disable namespaces in a computer-wide, persistent way. Second, applications can direct an individual query to a particular provider by specifying that provider's identifying GUID as part of the query.

 

 



