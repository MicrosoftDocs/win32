---
title: Composition swapchain
description: This API is the initial public release of the composition swapchain API
keywords:
- Composition swapchain
- Composition swapchain API
ms.topic: article
ms.date: 09/10/2021
---

# Composition swapchain

## Overview

This API is the initial public release of the composition swapchain API. It allows applications using Composition APIs (such as [**Windows.UI.Composition**](/uwp/api/windows.ui.composition) and [**DirectComposition**](/windows/win32/directcomp/directcomposition-portal)) to host content that can be independently rendered and presented to. In many ways, this type of presented content is conceptually similar to a DXGI swapchain. Both offer the ability to render to a buffer, and then present that buffer to the screen. However, the composition swapchain API offers the ability for presents to target a specific time to appear (the *PresentAt* time), whereas DXGI doesn't, and the composition swapchain API offers more freedom than DXGI around the ordering of buffers available to be presented.

The focus of the initial version of this API is to enable media frameworks, such as [Windows Media Foundation](/windows/win32/medfound/microsoft-media-foundation-sdk), to effectively use timed presentation.

## In this section

| Topic | Description |
|-|-|
| [Composition swapchain programming guide](comp-swapchain.md) | This API is a spiritual successor to the DXGI swapchain, which allows applications to render and present content to the screen. |
| [Composition swapchain code examples](comp-swapchain-examples.md) | A collection of code examples showing various composition swapchain scenarios. |
| [Composition glossary](comp-swapchain-glossary.md) | A glossary of composition swapchain terms. |
