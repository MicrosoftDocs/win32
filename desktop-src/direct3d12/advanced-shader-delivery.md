---
title: Advanced Shader Delivery overview
description: Advanced Shader Delivery precompiles Direct3D 12 shaders and delivers them at download time to reduce load times, in-game stutter, and power consumption.
ms.topic: concept-article
ms.date: 08/18/2026
#customer intent: As a game developer, I want to understand how Advanced Shader Delivery works so that I can decide whether to adopt it to reduce my game's load times, stutter, and power consumption.
---

# Advanced Shader Delivery

Advanced Shader Delivery (ASD) is a Windows 11 Direct3D 12 technology that helps games load faster. It moves shader compilation off the player's device by precompiling shaders ahead of time and delivering them when a player downloads the game.

As graphics continue to improve, the number of shaders a game compiles grows with them. Compiling those shaders on the player's device at launch, or "just-in-time" during gameplay, leads to longer load times, in-game shader compilation stutter, and higher power consumption. ASD addresses these problems by handling shader compilation before the game reaches the player. ASD is fully available to all developers building games on PC with Direct3D 12.

## How Advanced Shader Delivery works

ASD replaces on-device shader compilation with a pipeline that prepares shaders ahead of time and ships the compiled results to players. The pipeline has three stages:

- **Create a State Object Database (SODB)** for your game, by programmatic generation or manual capture.
- **Test the SODB** by compiling it into a Precompiled Shader Database (PSDB), registering it locally, and confirming its quality.
- **Deploy the SODB** to a storefront.

## Benefits of Advanced Shader Delivery

Moving shader compilation off the device and delivering precompiled shaders provides several benefits:

- **Faster load times.** Shaders are compiled ahead of time, so the game spends less time preparing shaders at first launch.
- **Less in-game stutter.** Precompiling shaders removes the just-in-time compilation that causes shader compilation stutter during gameplay.
- **Lower power consumption.** The player's device no longer spends power compiling shaders locally.

## Learn more

For documentation on how to adopt Advanced Shader Delivery for your title, see [Prepare your game for Advanced Shader Delivery](https://aka.ms/xgd-asd-selfservice).

## Related topics

* [Direct3D 12 Programming Guide](directx-12-programming-guide.md)
* [Advanced Shader Delivery: what's new at GDC 2026](https://devblogs.microsoft.com/directx/advanced-shader-delivery-whats-new-at-gdc-2026/)
