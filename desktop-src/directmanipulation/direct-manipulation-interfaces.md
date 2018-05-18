---
Description: 'The topics contained in this section provide the reference specifications for Direct Manipulation interfaces.'
ms.assetid: '03680CE5-A858-4876-B41C-6F2E08C02C22'
title: Direct Manipulation Interfaces
---

# Direct Manipulation Interfaces

The topics contained in this section provide the reference specifications for [Direct Manipulation](direct-manipulation-portal.md) interfaces.

> [!Note]  
> When implementing a [Direct Manipulation](direct-manipulation-portal.md) object, ensure that the [**IUnknown**](com.iunknown) implementation supports multithreading through thread-safe reference counting. For more information, see [**InterlockedIncrement**](base.interlockedincrement) and [**InterlockedDecrement**](base.interlockeddecrement).

 

## In this section



| Topic                                                                                                       | Description                                                                                                                                                                                                                                                                  |
|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IDirectManipulationAutoScrollBehavior**](idirectmanipulationautoscrollbehavior.md)<br/>           | Represents the auto-scroll animation behavior of content as it approaches the boundary of a given axis or axes.<br/>                                                                                                                                                   |
| [**IDirectManipulationCompositor**](idirectmanipulationcompositor.md)<br/>                           | Represents a compositor object that associates manipulated content with a drawing surface, such as [**canvas**](wwa.mdLCanvasElement) (Windows app using JavaScript) or [**Canvas**](w_ui_xaml_ctrl.canvas) (Windows Store app using C++, C\#, or Visual Basic).<br/> |
| [**IDirectManipulationCompositor2**](idirectmanipulationcompositor2.md)<br/>                         | Represents a compositor object that associates manipulated content with drawing surfaces across multiple processes.<br/>                                                                                                                                               |
| [**IDirectManipulationContent**](idirectmanipulationcontent.md)<br/>                                 | Encapsulates content inside a viewport, where content represents a visual surface clipped inside the viewport.<br/>                                                                                                                                                    |
| [**IDirectManipulationDeferContactService**](idirectmanipulationdefercontactservice.md)<br/>         | Represents a service for managing associations between a contact and a viewport.<br/>                                                                                                                                                                                  |
| [**IDirectManipulationDragDropBehavior**](idirectmanipulationdragdropbehavior.md)<br/>               | Represents behaviors for drag and drop interactions, which are triggered by cross-slide or press-and-hold gestures. <br/>                                                                                                                                              |
| [**IDirectManipulationDragDropEventHandler**](idirectmanipulationdragdropeventhandler.md)<br/>       | Defines methods to handle drag-drop behavior events.<br/>                                                                                                                                                                                                              |
| [**IDirectManipulationFrameInfoProvider**](idirectmanipulationframeinfoprovider.md)<br/>             | Represents a time-keeping object that measures the latency of the composition infrastructure used by the application and provides this data to [Direct Manipulation](direct-manipulation-portal.md). <br/>                                                            |
| [**IDirectManipulationInteractionEventHandler**](idirectmanipulationinteractioneventhandler.md)<br/> | Defines methods to handle interactions when they are detected.<br/>                                                                                                                                                                                                    |
| [**IDirectManipulationManager**](idirectmanipulationmanager.md)<br/>                                 | Provides access to all the [Direct Manipulation](direct-manipulation-portal.md) features and APIs available to the client application.<br/>                                                                                                                           |
| [**IDirectManipulationManager2**](idirectmanipulationmanager2.md)<br/>                               | Extends the [**IDirectManipulationManager**](idirectmanipulationmanager.md) interface that provides access to all the [Direct Manipulation](direct-manipulation-portal.md) features and APIs available to the client application. <br/>                              |
| [**IDirectManipulationManager3**](idirectmanipulationmanager3.md)<br/>                               | Extends the [**IDirectManipulationManager2**](idirectmanipulationmanager2.md) interface that provides access to all the [Direct Manipulation](direct-manipulation-portal.md) features and APIs available to the client application. <br/>                            |
| [**IDirectManipulationPrimaryContent**](idirectmanipulationprimarycontent.md)<br/>                   | Encapsulates the primary content inside a viewport.<br/>                                                                                                                                                                                                               |
| [**IDirectManipulationUpdateHandler**](idirectmanipulationupdatehandler.md)<br/>                     | Defines methods for handling manipulation update events.<br/>                                                                                                                                                                                                          |
| [**IDirectManipulationUpdateManager**](idirectmanipulationupdatemanager.md)<br/>                     | Manages how compositor updates are sent to [Direct Manipulation](direct-manipulation-portal.md).<br/>                                                                                                                                                                 |
| [**IDirectManipulationViewport**](idirectmanipulationviewport.md)<br/>                               | Defines a region within a window (referred to as a viewport) that is able to receive and process input from user interactions. <br/>                                                                                                                                   |
| [**IDirectManipulationViewport2**](idirectmanipulationviewport2.md)<br/>                             | Provides management of behaviors on a viewport. A behavior affects the functionality of a particular part of the [Direct Manipulation](direct-manipulation-portal.md) workflow. <br/>                                                                                 |
| [**IDirectManipulationViewportEventHandler**](idirectmanipulationviewporteventhandler.md)<br/>       | Defines methods for handling status and update events for the viewport.<br/>                                                                                                                                                                                           |



 

 

 




