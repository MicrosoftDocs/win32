---
Description: 'In order to drive visual updates, the application should use IDirectManipulationCompositor.'
ms.assetid: '6D8FB359-F52B-43F9-8A62-6BB2AEDE4F2B'
title: Composition engine
---

# Composition engine

In order to drive visual updates, the application should use [**IDirectManipulationCompositor**](idirectmanipulationcompositor.md). This object is responsible for updating visuals based on [Direct Manipulation](direct-manipulation-portal.md) updates, driving inertia updates forward, and providing composition timing information to Direct Manipulation Furthermore, an application should use the [DCompManipulationCompositor](direct-manipulation-guids.md) provided by [Direct Manipulation](direct-manipulation-portal.md), which will handle all visual updates on behalf of the application and drive inertia updates.

The [DCompManipulationCompositor](direct-manipulation-guids.md) is an implementation of the [**IDirectManipulationCompositor**](idirectmanipulationcompositor.md) interface that wraps [DirectComposition](directcomp.directcomposition_portal). Rather than having the application apply the output, through this compositor object [Direct Manipulation](direct-manipulation-portal.md) can apply the output by setting the transforms directly on the DirectComposition tree. By using this configuration, input can be processed and output transforms can be applied, regardless of activity on the UI thread.

To give [Direct Manipulation](direct-manipulation-portal.md) information on the timing of the composition engine, the [DCompManipulationCompositor](direct-manipulation-guids.md) class implements the [**IDirectManipulationFrameInfoProvider**](idirectmanipulationframeinfoprovider.md) interface. When creating a viewport, [**QueryInterface**](com.iunknown_queryinterface) the [**IDirectManipulationCompositor**](idirectmanipulationcompositor.md) pointer obtained from [**CoCreateInstance**](com.cocreateinstance) for an instance of **IDirectManipulationFrameInfoProvider**. The **IDirectManipulationFrameInfoProvider** pointer is passed to the [**IDirectManipulationManager::CreateViewport()**](idirectmanipulationmanager-createviewport.md) function.

 

 



