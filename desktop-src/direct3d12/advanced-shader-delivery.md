---
title: Advanced Shader Delivery
description: Advanced Shader Delivery precompiles Direct3D 12 shaders and delivers them at download time, reducing first-launch load times, in-game shader compilation stutter, and power consumption.
ms.topic: concept-article
ms.date: 08/18/2026
---

# Advanced Shader Delivery

Advanced Shader Delivery (ASD) is a Windows 11 Direct3D 12 technology that helps games load faster.

Gaming on Windows has evolved in many directions, including high-level shaders. As graphics continue to improve, so does the number of shaders a game compiles — and how those shaders are loaded during startup and gameplay needs to evolve with them. Compiling shaders on the player's device at launch, or "just-in-time" during gameplay, leads to longer load times, in-game shader compilation stutter, and higher power consumption.

ASD moves that work off the device. It captures a game's shader states in a standardized format called a State Object Database (SODB), then precompiles those shaders and delivers them to players at download time, greatly reducing in-game shader compile times. ASD is fully available to all developers building games on PC with Direct3D 12.

## Learn more
For documentation on how to adopt Advanced Shader Delivery for your title, see [Prepare your game for Advanced Shader Delivery](https://aka.ms/xgd-asd-selfservice).

## Related topics

<dl> <dt>

[Direct3D 12 Programming Guide](directx-12-programming-guide.md)
</dt> <dt>

[Advanced Shader Delivery: what's new at GDC 2026](https://devblogs.microsoft.com/directx/advanced-shader-delivery-whats-new-at-gdc-2026/)
</dt> </dl>
