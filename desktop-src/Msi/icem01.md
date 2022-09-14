---
description: ICEM01 validates that the ICE mechanism is working. This ICE uses the Time property to get the time and returns either the system time or None.
ms.assetid: f3b7677d-6b2e-4aa0-92eb-1b1e62cdf0a6
title: ICEM01
ms.topic: article
ms.date: 05/31/2018
---

# ICEM01

ICEM01 validates that the ICE mechanism is working. This ICE uses the [**Time**](time.md) property to get the time and returns either the system time or None.

Merge module ICEs are stored in a merge module .cub file called Mergemod.cub and not in the .cub file containing the ICEs used for package validation.

## Result

ICEM01 posts a message giving the time the installer called ICEM01. This ICE should never return an error.

## Related topics

<dl> <dt>

[Merge Module ICE Reference](merge-module-ice-reference.md)
</dt> </dl>

 

 



