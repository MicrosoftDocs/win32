---
Description: In order to drive visual updates, the application should use IDirectManipulationCompositor.
ms.assetid: 6D8FB359-F52B-43F9-8A62-6BB2AEDE4F2B
title: Composition engine
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Composition engine

In order to drive visual updates, the application should use [**IDirectManipulationCompositor**](/windows/previous-versions/DirectManipulation/nn-directmanipulation-idirectmanipulationcompositor?branch=master). This object is responsible for updating visuals based on [Direct Manipulation](direct-manipulation-portal.md) updates, driving inertia updates forward, and providing composition timing information to Direct Manipulation Furthermore, an application should use the [DCompManipulationCompositor](direct-manipulation-guids.md) provided by [Direct Manipulation](direct-manipulation-portal.md), which will handle all visual updates on behalf of the application and drive inertia updates.

The [DCompManipulationCompositor](direct-manipulation-guids.md) is an implementation of the [**IDirectManipulationCompositor**](/windows/previous-versions/DirectManipulation/nn-directmanipulation-idirectmanipulationcompositor?branch=master) interface that wraps [DirectComposition](directcomp.directcomposition_portal). Rather than having the application apply the output, through this compositor object [Direct Manipulation](direct-manipulation-portal.md) can apply the output by setting the transforms directly on the DirectComposition tree. By using this configuration, input can be processed and output transforms can be applied, regardless of activity on the UI thread.

To give [Direct Manipulation](direct-manipulation-portal.md) information on the timing of the composition engine, the [DCompManipulationCompositor](direct-manipulation-guids.md) class implements the [**IDirectManipulationFrameInfoProvider**](/windows/previous-versions/DirectManipulation/nn-directmanipulation-idirectmanipulationframeinfoprovider?branch=master) interface. When creating a viewport, [**QueryInterface**](com.iunknown_queryinterface) the [**IDirectManipulationCompositor**](/windows/previous-versions/DirectManipulation/nn-directmanipulation-idirectmanipulationcompositor?branch=master) pointer obtained from [**CoCreateInstance**](com.cocreateinstance) for an instance of **IDirectManipulationFrameInfoProvider**. The **IDirectManipulationFrameInfoProvider** pointer is passed to the [**IDirectManipulationManager::CreateViewport()**](/windows/previous-versions/DirectManipulation/nf-directmanipulation-idirectmanipulationmanager-createviewport?branch=master) function.

 

 



