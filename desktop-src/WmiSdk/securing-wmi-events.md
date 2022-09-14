---
description: WMI events are delivered by the event provider to a temporary or permanent consumer. The WMI event system uses the comparison of security descriptors on events and user account SIDs to control event access.
ms.assetid: 86eaeb5c-c27e-4794-88e2-e0ffbb885290
ms.tgt_platform: multiple
title: Securing WMI Events
ms.topic: article
ms.date: 05/31/2018
---

# Securing WMI Events

WMI events are delivered by the [*event provider*](gloss-e.md) to a [*temporary*](gloss-t.md) or [*permanent*](gloss-p.md) consumer. The WMI event system uses the comparison of [*security descriptors*](gloss-s.md) on events and user account [*SIDs*](gloss-s.md) to control event access.

Events are delivered in the form of an instance of an event class usually, but not necessarily, derived ultimately from [**\_\_Event**](--event.md). WMI supplies several general event classes in the [WMI System Classes](wmi-system-classes.md), such as [**\_\_InstanceModificationEvent**](--instancemodificationevent.md). Providers may also supply their own event classes. For example, the [System Registry Provider](/previous-versions/windows/desktop/regprov/system-registry-provider) has event classes that report the change of a registry key or value, such as [**RegistryKeyChangeEvent**](/previous-versions/windows/desktop/regprov/registrykeychangeevent).

The following topics supply information about securing delivery of events for providers and receiving events securely for client scripts and applications:

-   [Providing Events Securely](providing-events-securely.md)
-   [Receiving Events Securely](receiving-events-securely.md)

## Related topics

<dl> <dt>

[Maintaining WMI Security](maintaining-wmi-security.md)
</dt> </dl>

 

 
