---
description: In order to drive visual updates, the application should use IDirectManipulationCompositor.
ms.assetid: 6D8FB359-F52B-43F9-8A62-6BB2AEDE4F2B
title: Composition engine
ms.topic: article
ms.date: 02/03/2020
---

# Composition engine

In order to drive visual updates, the application should use [**IDirectManipulationCompositor**](/windows/win32/api/DirectManipulation/nn-directmanipulation-idirectmanipulationcompositor). This object is responsible for updating visuals based on [Direct Manipulation](direct-manipulation-portal.md) updates, driving inertia updates forward, and providing composition timing information to Direct Manipulation Furthermore, an application should use the [DCompManipulationCompositor](direct-manipulation-guids.md) provided by [Direct Manipulation](direct-manipulation-portal.md), which will handle all visual updates on behalf of the application and drive inertia updates.

The [DCompManipulationCompositor](direct-manipulation-guids.md) is an implementation of the [**IDirectManipulationCompositor**](/windows/win32/api/DirectManipulation/nn-directmanipulation-idirectmanipulationcompositor) interface that wraps [DirectComposition](../directcomp/directcomposition-portal.md). Rather than having the application apply the output, through this compositor object [Direct Manipulation](direct-manipulation-portal.md) can apply the output by setting the transforms directly on the DirectComposition tree. By using this configuration, input can be processed and output transforms can be applied, regardless of activity on the UI thread.

To give [Direct Manipulation](direct-manipulation-portal.md) information on the timing of the composition engine, the [DCompManipulationCompositor](direct-manipulation-guids.md) class implements the [**IDirectManipulationFrameInfoProvider**](/windows/win32/api/DirectManipulation/nn-directmanipulation-idirectmanipulationframeinfoprovider) interface. When creating a viewport, [**QueryInterface**](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) the [**IDirectManipulationCompositor**](/windows/win32/api/DirectManipulation/nn-directmanipulation-idirectmanipulationcompositor) pointer obtained from [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) for an instance of **IDirectManipulationFrameInfoProvider**. The **IDirectManipulationFrameInfoProvider** pointer is passed to the [**IDirectManipulationManager::CreateViewport()**](/windows/win32/api/DirectManipulation/nf-directmanipulation-idirectmanipulationmanager-createviewport) function.
