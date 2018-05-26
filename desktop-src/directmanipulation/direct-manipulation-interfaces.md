---
Description: The topics contained in this section provide the reference specifications for Direct Manipulation interfaces.
ms.assetid: 03680CE5-A858-4876-B41C-6F2E08C02C22
title: Direct Manipulation Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Direct Manipulation Interfaces

The topics contained in this section provide the reference specifications for [Direct Manipulation](direct-manipulation-portal.md) interfaces.

> [!Note]  
> When implementing a [Direct Manipulation](direct-manipulation-portal.md) object, ensure that the [**IUnknown**](com.iunknown) implementation supports multithreading through thread-safe reference counting. For more information, see [**InterlockedIncrement**](base.interlockedincrement) and [**InterlockedDecrement**](base.interlockeddecrement).

 

## In this section



| Topic                                                                                                       | Description                                                                                                                                                                                                                                                                  |
|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IDirectManipulationAutoScrollBehavior**](/windows/previous-versions/DirectManipulation/nn-directmanipulation-idirectmanipulationautoscrollbehavior?branch=master)<br/>           | Represents the auto-scroll animation behavior of content as it approaches the boundary of a given axis or axes.<br/>                                                                                                                                                   |
| [**IDirectManipulationCompositor**](/windows/previous-versions/DirectManipulation/nn-directmanipulation-idirectmanipulationcompositor?branch=master)<br/>                           | Represents a compositor object that associates manipulated content with a drawing surface, such as [**canvas**](wwa.mdLCanvasElement) (Windows app using JavaScript) or [**Canvas**](w_ui_xaml_ctrl.canvas) (Windows Store app using C++, C\#, or Visual Basic).<br/> |
| [**IDirectManipulationCompositor2**](/windows/previous-versions/DirectManipulation/nn-directmanipulation-idirectmanipulationcompositor2?branch=master)<br/>                         | Represents a compositor object that associates manipulated content with drawing surfaces across multiple processes.<br/>                                                                                                                                               |
| [**IDirectManipulationContent**](/windows/previous-versions/DirectManipulation/nn-directmanipulation-idirectmanipulationcontent?branch=master)<br/>                                 | Encapsulates content inside a viewport, where content represents a visual surface clipped inside the viewport.<br/>                                                                                                                                                    |
| [**IDirectManipulationDeferContactService**](/windows/previous-versions/DirectManipulation/nn-directmanipulation-idirectmanipulationdefercontactservice?branch=master)<br/>         | Represents a service for managing associations between a contact and a viewport.<br/>                                                                                                                                                                                  |
| [**IDirectManipulationDragDropBehavior**](/windows/previous-versions/DirectManipulation/nn-directmanipulation-idirectmanipulationdragdropbehavior?branch=master)<br/>               | Represents behaviors for drag and drop interactions, which are triggered by cross-slide or press-and-hold gestures. <br/>                                                                                                                                              |
| [**IDirectManipulationDragDropEventHandler**](/windows/previous-versions/DirectManipulation/nn-directmanipulation-idirectmanipulationdragdropeventhandler?branch=master)<br/>       | Defines methods to handle drag-drop behavior events.<br/>                                                                                                                                                                                                              |
| [**IDirectManipulationFrameInfoProvider**](/windows/previous-versions/DirectManipulation/nn-directmanipulation-idirectmanipulationframeinfoprovider?branch=master)<br/>             | Represents a time-keeping object that measures the latency of the composition infrastructure used by the application and provides this data to [Direct Manipulation](direct-manipulation-portal.md). <br/>                                                            |
| [**IDirectManipulationInteractionEventHandler**](/windows/previous-versions/DirectManipulation/nn-directmanipulation-idirectmanipulationinteractioneventhandler?branch=master)<br/> | Defines methods to handle interactions when they are detected.<br/>                                                                                                                                                                                                    |
| [**IDirectManipulationManager**](/windows/previous-versions/DirectManipulation/nn-directmanipulation-idirectmanipulationmanager?branch=master)<br/>                                 | Provides access to all the [Direct Manipulation](direct-manipulation-portal.md) features and APIs available to the client application.<br/>                                                                                                                           |
| [**IDirectManipulationManager2**](/windows/previous-versions/DirectManipulation/nn-directmanipulation-idirectmanipulationmanager2?branch=master)<br/>                               | Extends the [**IDirectManipulationManager**](/windows/previous-versions/DirectManipulation/nn-directmanipulation-idirectmanipulationmanager?branch=master) interface that provides access to all the [Direct Manipulation](direct-manipulation-portal.md) features and APIs available to the client application. <br/>                              |
| [**IDirectManipulationManager3**](/windows/previous-versions/DirectManipulation/nn-directmanipulation-idirectmanipulationmanager3?branch=master)<br/>                               | Extends the [**IDirectManipulationManager2**](/windows/previous-versions/DirectManipulation/nn-directmanipulation-idirectmanipulationmanager2?branch=master) interface that provides access to all the [Direct Manipulation](direct-manipulation-portal.md) features and APIs available to the client application. <br/>                            |
| [**IDirectManipulationPrimaryContent**](/windows/previous-versions/DirectManipulation/nn-directmanipulation-idirectmanipulationprimarycontent?branch=master)<br/>                   | Encapsulates the primary content inside a viewport.<br/>                                                                                                                                                                                                               |
| [**IDirectManipulationUpdateHandler**](/windows/previous-versions/DirectManipulation/nn-directmanipulation-idirectmanipulationupdatehandler?branch=master)<br/>                     | Defines methods for handling manipulation update events.<br/>                                                                                                                                                                                                          |
| [**IDirectManipulationUpdateManager**](/windows/previous-versions/DirectManipulation/nn-directmanipulation-idirectmanipulationupdatemanager?branch=master)<br/>                     | Manages how compositor updates are sent to [Direct Manipulation](direct-manipulation-portal.md).<br/>                                                                                                                                                                 |
| [**IDirectManipulationViewport**](/windows/previous-versions/DirectManipulation/nn-directmanipulation-idirectmanipulationviewport?branch=master)<br/>                               | Defines a region within a window (referred to as a viewport) that is able to receive and process input from user interactions. <br/>                                                                                                                                   |
| [**IDirectManipulationViewport2**](/windows/previous-versions/DirectManipulation/nn-directmanipulation-idirectmanipulationviewport2?branch=master)<br/>                             | Provides management of behaviors on a viewport. A behavior affects the functionality of a particular part of the [Direct Manipulation](direct-manipulation-portal.md) workflow. <br/>                                                                                 |
| [**IDirectManipulationViewportEventHandler**](/windows/previous-versions/DirectManipulation/nn-directmanipulation-idirectmanipulationviewporteventhandler?branch=master)<br/>       | Defines methods for handling status and update events for the viewport.<br/>                                                                                                                                                                                           |



 

 

 




