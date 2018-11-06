---
title: Versioning and Fallback Strategies
description: When an application detects a partial update using one of the preceding techniques or reads a set of objects whose effective date has not yet been reached, the application must deal with the situation gracefully.
ms.assetid: 6a34a783-98fd-406e-a96d-8e2a09a51c2d
ms.tgt_platform: multiple
keywords:
- Versioning and Fallback Strategies AD
ms.topic: article
ms.date: 05/31/2018
---

# Versioning and Fallback Strategies

When an application detects a partial update using one of the preceding techniques or reads a set of objects whose effective date has not yet been reached, the application must deal with the situation gracefully. For some applications, the graceful response is to "fall back" to a previous version of the objects in question. Active Directory Domain Services do not provide a versioning facility—applications that want this capability must provide it themselves. Approaches to versioning include keeping the "last known good" values cached locally and storing multiple sets of objects in the directory, for example, in "old," "current," and "new" containers. Many other schemes are possible.

Implementations must take care to avoid unintended consequences. An earlier version of objects should be used only when a partial update is detected or the new objects are not yet "effective." Falling back because something in the application "does not work" might circumvent an administrator's intent. For example, two computers that formerly could communicate might find themselves unable to do so because of a change in Internet Protocol security (IPsec) policy. If this is intentional on the part of the administrator, the affected systems should not fall back to the policy that allowed them to communicate, as this would be a security breach.

 

 




