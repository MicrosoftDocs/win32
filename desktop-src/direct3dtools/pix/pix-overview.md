---
title: Getting Started with PIX
ms.topic: article
description: An overview of how developers can use PIX to improve their Direct3D 12 applications.
---

# Getting Started with PIX
PIX is a debugging and profiling tool designed for game developers using Direct3D 12. You can [debug rendering issues and analyze frame performance with GPU Captures](pix-gpu-captures.md), or you can take a more [traditional profiling approach with Timing Captures](pix-timing-captures.md).

PIX's CPU profiling capabilities work for any Windows application and the GPU capabilities work on any application using Direct3D 12 (or Direct3D 11 via [Direct3D 11 on 12](~/direct3d12/direct3d-11-on-12.md)). This includes AI and ML workloads using [DirectML](https://github.com/microsoft/DirectML) and games made with popular engines like Unreal, Unity, and Godot.

While PIX can help you with no prior setup, you may want to check out [Instrumenting your Application](pix-instrumenting.md) and [Configuring PIX](pix-configuring.md) to ensure you have the best experience with things like PixEvents and debug symbols.

> [!NOTE]
> PIX is not intended to assist with Direct3D 12 API level issues, such as errors with compiling pipeline state objects. Instead, use [GPU-based validation and the Direct3D 12 Debug Layer](~/direct3d12/using-d3d12-debug-layer-gpu-based-validation.md).

## Installation
There are two ways to install PIX:
- Install from Microsoft at https://devblogs.microsoft.com/pix/download/.
- Install via [winget](/windows/package-manager/winget/): `winget install microsoft.pix`.

Subscribe to this [RSS feed](https://devblogs.microsoft.com/pix/feed/) for notifications on new releases!

## What Next?
Depending on your goals, you can either
- [Debug rendering issues and analyze frame performance with GPU Captures](pix-gpu-captures.md)
- [Profile CPU and GPU Activity with Timing Captures](pix-timing-captures.md)

## Frequently Asked Questions
- **How can I get help?** For bug reports, questions, or any other feedback you can either send us feedback through the application (using the Send Feedback button in the top right, the icon is a broken heart) or by chatting with us in the pix channel of the [DirectX Discord server](https://discord.com/invite/directx).
- **What about the old documentation hosted on [https://devblogs.microsoft.com/pix](https://devblogs.microsoft.com/pix)?**
  We have learned over time that the devblog is not a good fit for product documentation. Moving the documentation to the Microsoft Learn site gives us the ability to provide a better documentation experience.