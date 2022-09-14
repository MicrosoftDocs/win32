---
title: WFP Architecture
description: This section provides a brief overview of the Windows Filtering Platform architecture.
ms.assetid: 17a90f5c-ef82-4b14-b7f1-dd025d5f7303
ms.topic: article
ms.date: 05/31/2018
---

# WFP Architecture

The following figure shows the basic architecture of the Windows Filtering Platform (WFP).

![basic architecture of the windows filtering platform diagram](images/wfp-architecture.png)

## Filter Engine

The filter engine contains a user-mode component and a kernel-mode component, which together perform all of the filtering operations on network data. The filter engine contains multiple filtering layers that map loosely to the operating system's networking stack layers. The filter engine layers are divided into user-mode layers and kernel-mode layers based on the filter engine component that owns them.

The user-mode component performs RPC and IPsec filtering. The filter engine contains approximately 10 user-mode filtering layers.

The kernel-mode component performs filtering at the network and transport layers of the TC/IP stack. This component also calls the available callout functions during the [classification](basic-operation.md) process. The filter engine contains approximately 50 kernel-mode filtering layers.

See [**Filtering Layer Identifiers**](management-filtering-layer-identifiers-.md) for a description of each of the filter engine layers.

## Base Filtering Engine

The Base Filtering Engine (BFE) is a user-mode service (bfe.dll running in a svchost.exe process) that coordinates the WFP components. The principal tasks performed by BFE are adding and removing filters from the system, storing filter configuration, and enforcing WFP configuration security. Applications communicate with BFE through the [WFP management functions](fwp-mgmt-functions.md).

## Callout Drivers

Callout drivers provide additional filtering functionality by adding custom callout functions to the filter engine at one or more of the kernel-mode filtering layers. Callouts support deep inspection and packet as well as stream modification. After a callout driver has added its callout functions to the filter engine, filters that specify a given driver's callout function can be added to the filtering process. Such filters can be added by either a user-mode management application or by the callout driver itself. The kernel-mode interface, delivered in the Windows Development Kit, should only be used where needed and not as a substitute for the user-mode API.

> [!Note]  
> For more information on callout drivers, see the Windows Filtering Platform section of the [Windows Development Kit](/windows-hardware/drivers/network/windows-filtering-platform-callout-drivers2).

 

The Windows Filtering Platform includes a number of built-in callout functions that can be used for IPsec secure data communication, stateful filtering settings, and stealth-mode filtering. See [**Built-in Callout Identifiers**](built-in-callout-identifiers.md) for a complete list of built-in callout functions.

## Related topics

<dl> <dt>

[Object Model](object-model.md)
</dt> <dt>

[WFP Operation](basic-operation.md)
</dt> <dt>

[Windows Filtering Platform Callout Drivers - Design Guide](/windows-hardware/drivers/network/windows-filtering-platform-callout-drivers2)
</dt> <dt>

[Windows Filtering Platform Callout Drivers - Reference](/windows-hardware/drivers/ddi/_netvista/)
</dt> </dl>

 

 