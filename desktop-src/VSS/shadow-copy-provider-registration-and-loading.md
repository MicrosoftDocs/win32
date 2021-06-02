---
description: Shadow Copy Provider Registration and Loading
ms.assetid: f9bb72ce-9a2b-43cd-9697-1f6598a46e3e
title: Shadow Copy Provider Registration and Loading
ms.topic: article
ms.date: 05/31/2018
---

# Shadow Copy Provider Registration and Loading

## Provider Registration

Only VSS calls providers. The provider registers for calls by invoking [**IVssAdmin::RegisterProvider**](/windows/desktop/api/VsAdmin/nf-vsadmin-ivssadmin-registerprovider), passing **VSS\_PROV\_HARDWARE** for the *eProviderType* parameter. Once registered, the provider will be involved in shadow copy management until unregistering using [**IVssAdmin::UnregisterProvider**](/windows/desktop/api/VsAdmin/nf-vsadmin-ivssadmin-unregisterprovider).

## Provider Loading and Unloading

Providers can be frequently loaded and unloaded. Providers can implement [**IVssProviderNotifications**](/windows/desktop/api/VsProv/nn-vsprov-ivssprovidernotifications) to determine when VSS is loading or unloading the provider.

 

 



