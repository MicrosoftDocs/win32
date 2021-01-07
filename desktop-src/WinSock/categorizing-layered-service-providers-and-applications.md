---
title: Categorizing layered service providers and apps
description: Winsock 2 accommodates layered protocols.
ms.assetid: 1c5efd2e-1b42-4c20-a4da-b81a5fc4243c
ms.topic: article
ms.date: 05/31/2018
---

# Categorizing layered service providers and apps

> [!Note]  
> Layered Service Providers are deprecated. Starting with Windows 8 and Windows Server 2012, use [Windows Filtering Platform](../fwp/windows-filtering-platform-start-page.md).

 

Winsock 2 accommodates layered protocols. A layered protocol is one that implements only higher level communications functions, while relying on an underlying transport stack for the actual exchange of data with a remote endpoint. An example of a layered protocol or layered service provider would be a security layer that adds protocol to the connection establishment process in order to perform authentication and to establish a mutually agreed upon encryption scheme. Such a security protocol would generally require the services of an underlying reliable transport protocol such as TCP or SPX. The term base protocol implemented by base provider refers to a Winsock provider that implements a protocol such as TCP or SPX which is capable of performing data communications with a remote endpoint. The term layered protocol is used to describe a protocol that cannot stand alone. These layered protocols are installed as Winsock Layered Service Providers (LSPs).

An example of an LSP is the Microsoft Firewall Client Service Provider installed as part of the Internet Secutity and Authentication Server (ISA) on clients. The Microsoft Firewall Client Service Provider installs over the Winsock base providers for TCP and UDP. A dynamic-link library (DLL) in the ISA Firewall Client software becomes a Winsock layered service provider that all Winsock applications use transparently. This way, the ISA Firewall Client LSP can intercept Winsock function calls from client applications and then route a request to the original underlying base service provider if the destination is local or to the Firewall service on an ISA Server computer if the destination is remote. A similar LSP is installed as part of the Microsoft Forefront Firewall Service and the Threat Management Gateway (TMG) Client on clients.

During LSP initialization, the LSP must provide pointers to a number of Winsock Service Provider Interface (SPI) functions. These functions will be called during normal processing by the layer directly above the LSP (either another LSP or Ws2\_32.DLL).

It is possible to define LSP categories based upon the subset of SPI functions an LSP implements and the nature of the extra processing performed for each of those functions. By classifying LSPs, as well as classifying applications which use Winsock sockets, it becomes possible to selectively determine if an LSP should be involved in a given process at runtime.

On Windows Vista and later, a new method is provided for categorizing both Winsock Layered Service Providers and applications so that only certain LSPs will be loaded. There are several reasons for adding these features.

One of the primary reasons is that certain system critical processes such as winlogon and lsass create sockets, but these processes do not use these sockets to send any traffic on the network. So most LSPs should not be loaded into these processes. A number of cases have also been documented where buggy LSPs can cause *lsass.exe* to crash. If lsass crashes, the system forces a shutdown. A side affect of these system processes loading LSPs is that these processes never exit so when an LSP is installed or removed, a reboot is required.

A secondary reason is that there are some cases where applications may not want to load certain LSPs. For example, some applications may not want to load cryptographic LSPs which could prevent the application from communicating with other systems that do not have the cyptographic LSP installed.

Finally, LSP categories can be used by other LSPs to determine where in the Winsock protocol chain they should install themselves. For years, various LSP developers have wanted a way of knowing how an LSP will behave. For example, an LSP that inspects the data stream would want to be above an LSP that encrypts the data. Of course, this method of LSP categorization isn't fool proof since it relies on third-party LSPs to categorize themselves appropriately.

The LSP categorization and other security enhancements in Windows Vista and later are designed to help prevent users from unintentionally installing malicious LSPs.

## LSP Categories

On Windows Vista and later, an LSP can be classified based on how it interacts with Windows Sockets calls and data. An LSP category is an identifiable group of behaviors on a subset of Winsock SPI functions. For example, an HTTP content filter would be categorized as a data inspector (the LSP\_INSPECTOR category). The LSP\_INSPECTOR category will inspect (but not alter) parameters to data transfer SPI functions. An application can query for the category of an LSP and choose to not load the LSP based on the LSP category and the application's set of permitted LSP categories.

The following table lists categories that an LSP can be classified into.

| LSP Category              | Description                                                     |
|---------------------------|-----------------------------------------------------------------|
| **LSP\_CRYPTO\_COMPRESS** | The LSP is a cryptography or data compression provider.         |
| **LSP\_FIREWALL**         | The LSP is a firewall provider.                                 |
| **LSP\_LOCAL\_CACHE**     | The LSP is a local cache provider.                              |
| **LSP\_INBOUND\_MODIFY**  | The LSP modifies inbound data.                                  |
| **LSP\_INSPECTOR**        | The LSP inspects or filters data.                               |
| **LSP\_OUTBOUND\_MODIFY** | The LSP modifies outbound data.                                 |
| **LSP\_PROXY**            | The LSP acts as a proxy and redirects packets.                  |
| **LSP\_REDIRECTOR**       | The LSP is a network redirector.                                |
| **LSP\_SYSTEM**           | The LSP is acceptable for use in services and system processes. |



 

An LSP may belong to more than one category. For example, a firewall/security LSP could belong to both the inspector (**LSP\_INSPECTOR**) and firewall (**LSP\_FIREWALL**) categories.

If an LSP does not have a category set, it is considered to be in the All Other category. This LSP category will not be loaded in services or system processes (for example, lsass, winlogon, and many svchost processes).

## Categorizing LSPs

Several new functions are available on Windows Vista and later for categorizing an LSP:

-   [**WSCGetProviderInfo**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscgetproviderinfo)
-   [**WSCGetProviderInfo32**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscgetproviderinfo32)
-   [**WSCSetProviderInfo**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscsetproviderinfo)
-   [**WSCSetProviderInfo32**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscsetproviderinfo32)

In order to categorize an LSP, the [**WSCSetProviderInfo**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscsetproviderinfo) or [**WSCSetProviderInfo32**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscsetproviderinfo32) function is called with a GUID to identify the LSP hidden entry, the information class to be set for this LSP protocol entry, and a set of flags used to modify the behavior of the function.

The [**WSCGetProviderInfo**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscgetproviderinfo) or [**WSCGetProviderInfo32**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscgetproviderinfo32) function is similarly used to retrieve the data associated with an information class for an LSP.

## Categorizing Applications

Several new functions are available on Windows Vista and later for categorizing an application:

-   [**WSCGetApplicationCategory**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscgetapplicationcategory)
-   [**WSCSetApplicationCategory**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscsetapplicationcategory)

In order to categorize an application, the [**WSCSetApplicationCategory**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscsetapplicationcategory) function is called with the load path to the executable image to identify the application, the command line arguments used when starting the application, and the LSP categories which are permitted for all instances of this application.

The [**WSCGetApplicationCategory**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscgetapplicationcategory) function is similarly used to retrieve the layered service provider (LSP) categories associated with an application.

## Determining Which LSPs Get Loaded

The final part of LSP categorization is determining which LSPs will be loaded into which processes. When a process loads Winsock, the following comparisons are made of the application category and the LSP categories for all installed LSPs:

-   If the application is not categorized, allow all LSPs to be loaded into the process.
-   If both the application and the LSP have assigned categories, all of the following must be true: <dl> At least one of the LSP categories is present in the application's specified categories.  
    Only categories specified in the application's specified categories are specified in the LSPs categories. For example, if the application specifies a category it must be in the LSP's category.  
    If the LSP\_SYSTEM category is present in the application's category, it must be present in the LSP's categories.  
    </dl>

> [!Note]  
> If an LSP is not categorized, its category is effectively zero. For a match to occur, all the LSP's specified categories must be present in the application's categories (the application's categories must be a superset of the LSP's categories) with the caveat that if LSP\_SYSTEM is present in the application's category it must also be present in the LSP's category.

 

Consider the following example:

The *Foo.exe* application is categorized as LSP\_SYSTEM + LSP\_FIREWALL + LSP\_CRYPTO\_COMPRESS. The application *Bar.exe* is categorized as LSP\_FIREWALL + LSP\_CRYPTO\_COMPRESS. There are four LSPs installed on the system:

-   LSP1 has set a category of LSP\_SYSTEM.
-   LSP2 is not categories set, so its category is zero.
-   LSP3 has set a category of LSP\_FIREWALL.
-   LSP4 has set categories of LSP\_SYSTEM + LSP\_FIREWALL + LSP\_CRYPTO\_COMPRESS + LSP\_INSPECTOR

In this example, the *Foo.exe* application would only load LSP1, while the *Bar.exe* application would load LSP3.

## Determining Winsock Providers Installed

The Microsoft Windows Software Development Kit (SDK) includes a sample Winsock program that can be used to determine the Winsock transport providers installed on a local computer. By default, the source code for this Winsock sample is installed in the following directory of the Windows SDK for Windows 7:

*C:\\Program Files\\Microsoft SDKs\\Windows\\v7.0\\Samples\\NetDs\\winsock\\LSP*

This sample is a utility for installing and testing layered service providers. But it can also be used to programmatically collect detailed information from the Winsock catalog on a local computer. To list all of the current Winsock providers including both base providers and layer service providers, build this Winsock sample and execute the following console command:

**instlsp -p**

The output will be a list of Winsock providers installed on the local computer including layered service providers. The output lists the catalog ID and the string name for the Winsock provider

To collect more detailed information on all Winsock providers, execute the following console command:

**instlsp -p -v**

The output will be a list [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structures supported on the local computer.

For a list of only layered service providers installed on the local computer, execute the following console command:

**instlsp -l**

To map the LSP structure, execute the following console command:

**instlsp -m**

> [!Note]  
> The TDI feature is deprecated and will be removed in future versions of Microsoft Windows. Depending on how you use TDI, use either the Winsock Kernel (WSK) or Windows Filtering Platform (WFP). For more information about WFP and WSK, see [Windows Filtering Platform](../fwp/windows-filtering-platform-start-page.md) and [Winsock Kernel](/windows-hardware/drivers/ddi/_netvista/). For a Windows Core Networking blog entry about WSK and TDI, see [Introduction to Winsock Kernel (WSK)](/archive/blogs/wndp/).

 

 

 
