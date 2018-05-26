---
Description: Shadow Copy Provider Registration and Loading
ms.assetid: f9bb72ce-9a2b-43cd-9697-1f6598a46e3e
title: Shadow Copy Provider Registration and Loading
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Shadow Copy Provider Registration and Loading

## Provider Registration

Only VSS calls providers. The provider registers for calls by invoking [**IVssAdmin::RegisterProvider**](/windows/win32/VsAdmin/nf-vsadmin-ivssadmin-registerprovider?branch=master), passing **VSS\_PROV\_HARDWARE** for the *eProviderType* parameter. Once registered, the provider will be involved in shadow copy management until unregistering using [**IVssAdmin::UnregisterProvider**](/windows/win32/VsAdmin/nf-vsadmin-ivssadmin-unregisterprovider?branch=master).

## Provider Loading and Unloading

Providers can be frequently loaded and unloaded. Providers can implement [**IVssProviderNotifications**](/windows/win32/VsProv/nn-vsprov-ivssprovidernotifications?branch=master) to determine when VSS is loading or unloading the provider.

 

 



