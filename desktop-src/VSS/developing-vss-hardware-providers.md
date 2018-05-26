---
Description: Hardware providers implement the IVssProviderCreateSnapshotSet and IVssHardwareSnapshotProvider interfaces.
ms.assetid: 9f40f1d1-a63a-4edc-aa8d-b3998ecb2716
title: Developing VSS Hardware Providers
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Developing VSS Hardware Providers

Hardware providers implement the [**IVssProviderCreateSnapshotSet**](/windows/win32/VsProv/nn-vsprov-ivssprovidercreatesnapshotset?branch=master) and [**IVssHardwareSnapshotProvider**](/windows/win32/VsProv/nn-vsprov-ivsshardwaresnapshotprovider?branch=master) interfaces. **IVssProviderCreateSnapshotSet** implements the shadow copy state sequencing. **IVssHardwareSnapshotProvider** operates on a LUN abstraction. Providers must be implemented as an out-of-process COM server. Providers use provider-specific mechanisms (often private IOCTLs) to communicate with the storage subsystem that instantiates the shadow copy LUNs.

-   [Shadow Copy Provider Registration and Loading](shadow-copy-provider-registration-and-loading.md)
-   [Shadow Copy Creation for Providers](shadow-copy-creation-for-providers.md)
-   [Hardware Provider Interactions and Behaviors](hardware-provider-interactions-and-behaviors.md)

 

 



