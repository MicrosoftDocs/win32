---
Description: In order to drive visual updates, the application should use IDirectManipulationCompositor.
ms.assetid: 6D8FB359-F52B-43F9-8A62-6BB2AEDE4F2B
title: Composition engine
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Composition engine

In order to drive visual updates, the application should use [**IDirectManipulationCompositor**](/previous-versions/windows/desktop/api/DirectManipulation/nn-directmanipulation-idirectmanipulationcompositor). This object is responsible for updating visuals based on [Direct Manipulation](direct-manipulation-portal.md) updates, driving inertia updates forward, and providing composition timing information to Direct Manipulation Furthermore, an application should use the [DCompManipulationCompositor](direct-manipulation-guids.md) provided by [Direct Manipulation](direct-manipulation-portal.md), which will handle all visual updates on behalf of the application and drive inertia updates.

The [DCompManipulationCompositor](direct-manipulation-guids.md) is an implementation of the [**IDirectManipulationCompositor**](/previous-versions/windows/desktop/api/DirectManipulation/nn-directmanipulation-idirectmanipulationcompositor) interface that wraps [DirectComposition](https://msdn.microsoft.com/windows/desktop/40e2d02b-77e8-425f-ac5e-3dcddef08173). Rather than having the application apply the output, through this compositor object [Direct Manipulation](direct-manipulation-portal.md) can apply the output by setting the transforms directly on the DirectComposition tree. By using this configuration, input can be processed and output transforms can be applied, regardless of activity on the UI thread.

To give [Direct Manipulation](direct-manipulation-portal.md) information on the timing of the composition engine, the [DCompManipulationCompositor](direct-manipulation-guids.md) class implements the [**IDirectManipulationFrameInfoProvider**](/previous-versions/windows/desktop/api/DirectManipulation/nn-directmanipulation-idirectmanipulationframeinfoprovider) interface. When creating a viewport, [**QueryInterface**](https://msdn.microsoft.com/windows/desktop/54d5ff80-18db-43f2-b636-f93ac053146d) the [**IDirectManipulationCompositor**](/previous-versions/windows/desktop/api/DirectManipulation/nn-directmanipulation-idirectmanipulationcompositor) pointer obtained from [**CoCreateInstance**](https://msdn.microsoft.com/windows/desktop/7295a55b-12c7-4ed0-a7a4-9ecee16afdec) for an instance of **IDirectManipulationFrameInfoProvider**. The **IDirectManipulationFrameInfoProvider** pointer is passed to the [**IDirectManipulationManager::CreateViewport()**](/previous-versions/windows/desktop/api/DirectManipulation/nf-directmanipulation-idirectmanipulationmanager-createviewport) function.

 

 



