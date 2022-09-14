---
title: Interfaces (Ribbon Framework)
description: Reference documentation for the Windows Ribbon framework interfaces.
ms.assetid: d5fd6e4f-ca10-4010-aab4-d2728b0ac53c
ms.topic: article
ms.date: 05/31/2018
---

# Interfaces (Ribbon Framework)

Reference documentation for the Windows Ribbon framework interfaces.

### Interfaces



| Topic                                                                                  | Contents                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IUIApplication**](/windows/desktop/api/uiribbon/nn-uiribbon-iuiapplication)                       | The [**IUIApplication**](/windows/desktop/api/uiribbon/nn-uiribbon-iuiapplication) interface is implemented by the application and defines the callback entry-point methods for the Ribbon framework.<br/>                                                                                                                                                                                                              |
| [**IUICollection**](/windows/desktop/api/uiribbon/nn-uiribbon-iuicollection)                         | The [**IUICollection**](/windows/desktop/api/uiribbon/nn-uiribbon-iuicollection) interface is implemented by the Ribbon framework. The **IUICollection** interface defines the methods for dynamically manipulating collection-based controls, such as the various Ribbon [galleries](ribbon-controls-galleries.md) and the Quick Access Toolbar (QAT), at run time.<br/>                                              |
| [**IUICollectionChangedEvent**](/windows/desktop/api/uiribbon/nn-uiribbon-iuicollectionchangedevent) | The [**IUICollectionChangedEvent**](/windows/desktop/api/uiribbon/nn-uiribbon-iuicollectionchangedevent) interface is implemented by the application and defines the method required to handle changes to a collection at run time.<br/>                                                                                                                                                                                |
| [**IUICommandHandler**](/windows/desktop/api/uiribbon/nn-uiribbon-iuicommandhandler)                 | The [**IUICommandHandler**](/windows/desktop/api/uiribbon/nn-uiribbon-iuicommandhandler) interface is implemented by the application and defines the methods for gathering Command information and handling Command events from the Ribbon framework.<br/>                                                                                                                                                              |
| [**IUIContextualUI**](/windows/desktop/api/uiribbon/nn-uiribbon-iuicontextualui)                     | The[**IUIContextualUI**](/windows/desktop/api/uiribbon/nn-uiribbon-iuicontextualui)interface is implemented by the Ribbon framework and provides the core functionality for the[Context Popup](windowsribbon-controls-contextpopup.md)View.<br/>                                                                                                                                                                       |
| [**IUIFramework**](/windows/desktop/api/uiribbon/nn-uiribbon-iuiframework)                           | The [**IUIFramework**](/windows/desktop/api/uiribbon/nn-uiribbon-iuiframework) interface is implemented by the Ribbon framework and defines the methods that provide the core functionality for the framework.<br/>                                                                                                                                                                                                     |
| [**IUIImage**](/windows/desktop/api/uiribbon/nn-uiribbon-iuiimage)                                   | The [**IUIImage**](/windows/desktop/api/uiribbon/nn-uiribbon-iuiimage) interface is implemented by the application and defines the method for retrieving an image to display in the ribbon and context popup UI of the Ribbon framework .<br/>                                                                                                                                                                          |
| [**IUIImageFromBitmap**](/windows/desktop/api/uiribbon/nn-uiribbon-iuiimagefrombitmap)               | [**IUIImageFromBitmap**](/windows/desktop/api/uiribbon/nn-uiribbon-iuiimagefrombitmap) is a factory interface implemented by the Ribbon framework that defines the method for creating an [**IUIImage**](/windows/desktop/api/uiribbon/nn-uiribbon-iuiimage) object.<br/>                                                                                                                                                             |
| [**IUIRibbon**](/windows/desktop/api/uiribbon/nn-uiribbon-iuiribbon)                                 | The [**IUIRibbon**](/windows/desktop/api/uiribbon/nn-uiribbon-iuiribbon) interface is implemented by the Ribbon framework and provides the ability to specify settings and properties for a ribbon. <br/>                                                                                                                                                                                                               |
| [**IUISimplePropertySet**](/windows/desktop/api/uiribbon/nn-uiribbon-iuisimplepropertyset)           | [**IUISimplePropertySet**](/windows/desktop/api/uiribbon/nn-uiribbon-iuisimplepropertyset)is a read-only interface that defines a method for retrieving the value identified by a property key. This interface is implemented by the Ribbon framework and is also implemented by the host application for each item in the[**IUICollection**](/windows/desktop/api/uiribbon/nn-uiribbon-iuicollection)object of an item gallery.<br/> |



 

## Related topics

<dl> <dt>

[Windows Ribbon Framework Reference](windowsribbon-reference-entry.md)
</dt> </dl>

 

