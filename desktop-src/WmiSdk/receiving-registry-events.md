---
description: The System Registry provider attempts to send one notification for every event that occurs.
ms.assetid: 51ef0ccb-02d5-4dac-9c71-a7f4e25a0d00
ms.tgt_platform: multiple
title: Receiving Registry Events
ms.topic: article
ms.date: 05/31/2018
---

# Receiving Registry Events

The System Registry provider attempts to send one notification for every event that occurs. However, the System Registry provider does not guarantee that the consumer will receive any or all events. The exception is that the System Registry provider does ensure that a consumer will receive one notification for each event registration.

For example, suppose a consumer registers for two tree change events, requesting notification for [**RegistryTreeChangeEvent**](/previous-versions/windows/desktop/regprov/registrytreechangeevent) instances. Each registration has the same Hive (subtree) value but a different RootPath value. If keys in both paths change multiple times, the System Registry provider guarantees that the consumer will receive a notification for each path. Depending on the response time of the registry and the System Registry provider, the consumer may receive as many notifications as there were occurrences of events.

## Related topics

<dl> <dt>

[Registering for System Registry Events](registering-for-system-registry-events.md)
</dt> </dl>

 

 
