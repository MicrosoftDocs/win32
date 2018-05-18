---
Description: Shadow Copy Provider Registration and Loading
ms.assetid: 'f9bb72ce-9a2b-43cd-9697-1f6598a46e3e'
title: Shadow Copy Provider Registration and Loading
---

# Shadow Copy Provider Registration and Loading

## Provider Registration

Only VSS calls providers. The provider registers for calls by invoking [**IVssAdmin::RegisterProvider**](ivssadmin-registerprovider.md), passing **VSS\_PROV\_HARDWARE** for the *eProviderType* parameter. Once registered, the provider will be involved in shadow copy management until unregistering using [**IVssAdmin::UnregisterProvider**](ivssadmin-unregisterprovider.md).

## Provider Loading and Unloading

Providers can be frequently loaded and unloaded. Providers can implement [**IVssProviderNotifications**](ivssprovidernotifications.md) to determine when VSS is loading or unloading the provider.

 

 



