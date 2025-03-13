---
title: Get started with PIX
description: An overview of how developers can use PIX to improve their Direct3D 12 applications.
ms.topic: get-started
ms.date: 07/09/2024
---

# Get started with PIX

PIX is a debugging and profiling tool designed for game developers using Direct3D 12. You can [debug rendering issues and analyze frame performance with GPU Captures](pix-gpu-captures.md), or you can take a more [traditional profiling approach with Timing Captures](pix-timing-captures.md).

PIX's CPU profiling capabilities work for any Windows application, and the GPU capabilities work on any application using Direct3D 12 (or Direct3D 11 via [Direct3D 11 on 12](../../direct3d12/direct3d-11-on-12.md)). That includes AI and ML workloads using [DirectML](/windows/ai/directml/dml), and games made with popular engines such as Unreal, Unity, and Godot.

While PIX can help you with no prior setup, you might want to check out [Instrument your app](pix-instrumenting.md) and [Configure PIX](pix-configuring.md) to ensure that you have the best experience with things such as PixEvents and debug symbols.

> [!NOTE]
> PIX is not intended to assist with Direct3D 12 API level issues, such as errors with compiling pipeline state objects. Instead, use [GPU-based validation and the Direct3D 12 debug layer](../../direct3d12/using-d3d12-debug-layer-gpu-based-validation.md).

## Installation

There are two ways to install PIX:
- Install from Microsoft at the blog post [Download](https://devblogs.microsoft.com/pix/download/).
- Install via [winget](/windows/package-manager/winget/). Use the command `winget install microsoft.pix`.

For notifications on new releases, you can subscribe to the [RSS feed for the PIX on Windows blog](https://devblogs.microsoft.com/pix/feed/).

## What next?

Depending on your goals, you can either:
- [Debug rendering issues and analyze frame performance with GPU Captures](pix-gpu-captures.md), or
- [Profile CPU and GPU activity with timing captures](pix-timing-captures.md).

## Frequently-asked questions

- **How can I get help?** For bug reports, questions, or any other feedback, you can either send us feedback through the application (using the **Send Feedback** button in the top-right; the icon is a broken heart), or by chatting with us in the pix channel of the [DirectX Discord server](https://discord.com/invite/directx).
- **What about the old documentation hosted on [https://devblogs.microsoft.com/pix](https://devblogs.microsoft.com/pix)?** We've learned over time that the devblog is not a good fit for product documentation. Moving the documentation to Microsoft Learn gives us the ability to provide a better documentation experience.
