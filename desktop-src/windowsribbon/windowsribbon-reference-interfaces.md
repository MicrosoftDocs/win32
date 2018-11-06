---
title: Interfaces
description: Reference documentation for the Windows Ribbon framework interfaces.
ms.assetid: d5fd6e4f-ca10-4010-aab4-d2728b0ac53c
ms.topic: article
ms.date: 05/31/2018
---

# Interfaces

Reference documentation for the Windows Ribbon framework interfaces.

### Interfaces



| Topic                                                                                  | Contents                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IUIApplication**](https://msdn.microsoft.com/library/windows/desktop/dd371528)                       | The [**IUIApplication**](https://msdn.microsoft.com/library/windows/desktop/dd371528) interface is implemented by the application and defines the callback entry-point methods for the Ribbon framework.<br/>                                                                                                                                                                                                              |
| [**IUICollection**](https://msdn.microsoft.com/library/windows/desktop/dd371519)                         | The [**IUICollection**](https://msdn.microsoft.com/library/windows/desktop/dd371519) interface is implemented by the Ribbon framework. The **IUICollection** interface defines the methods for dynamically manipulating collection-based controls, such as the various Ribbon [galleries](ribbon-controls-galleries.md) and the Quick Access Toolbar (QAT), at run time.<br/>                                              |
| [**IUICollectionChangedEvent**](https://msdn.microsoft.com/library/windows/desktop/dd371499) | The [**IUICollectionChangedEvent**](https://msdn.microsoft.com/library/windows/desktop/dd371499) interface is implemented by the application and defines the method required to handle changes to a collection at run time.<br/>                                                                                                                                                                                |
| [**IUICommandHandler**](https://msdn.microsoft.com/library/windows/desktop/dd371491)                 | The [**IUICommandHandler**](https://msdn.microsoft.com/library/windows/desktop/dd371491) interface is implemented by the application and defines the methods for gathering Command information and handling Command events from the Ribbon framework.<br/>                                                                                                                                                              |
| [**IUIContextualUI**](https://msdn.microsoft.com/library/windows/desktop/dd371482)                     | The[**IUIContextualUI**](https://msdn.microsoft.com/library/windows/desktop/dd371482)interface is implemented by the Ribbon framework and provides the core functionality for the[Context Popup](windowsribbon-controls-contextpopup.md)View.<br/>                                                                                                                                                                       |
| [**IUIFramework**](https://msdn.microsoft.com/library/windows/desktop/dd371467)                           | The [**IUIFramework**](https://msdn.microsoft.com/library/windows/desktop/dd371467) interface is implemented by the Ribbon framework and defines the methods that provide the core functionality for the framework.<br/>                                                                                                                                                                                                     |
| [**IUIImage**](https://msdn.microsoft.com/library/windows/desktop/dd371367)                                   | The [**IUIImage**](https://msdn.microsoft.com/library/windows/desktop/dd371367) interface is implemented by the application and defines the method for retrieving an image to display in the ribbon and context popup UI of the Ribbon framework .<br/>                                                                                                                                                                          |
| [**IUIImageFromBitmap**](https://msdn.microsoft.com/library/windows/desktop/dd371365)               | [**IUIImageFromBitmap**](https://msdn.microsoft.com/library/windows/desktop/dd371365) is a factory interface implemented by the Ribbon framework that defines the method for creating an [**IUIImage**](https://msdn.microsoft.com/library/windows/desktop/dd371367) object.<br/>                                                                                                                                                             |
| [**IUIRibbon**](https://msdn.microsoft.com/library/windows/desktop/dd371360)                                 | The [**IUIRibbon**](https://msdn.microsoft.com/library/windows/desktop/dd371360) interface is implemented by the Ribbon framework and provides the ability to specify settings and properties for a ribbon. <br/>                                                                                                                                                                                                               |
| [**IUISimplePropertySet**](https://msdn.microsoft.com/library/windows/desktop/dd371358)           | [**IUISimplePropertySet**](https://msdn.microsoft.com/library/windows/desktop/dd371358)is a read-only interface that defines a method for retrieving the value identified by a property key. This interface is implemented by the Ribbon framework and is also implemented by the host application for each item in the[**IUICollection**](https://msdn.microsoft.com/library/windows/desktop/dd371519)object of an item gallery.<br/> |



 

## Related topics

<dl> <dt>

[Windows Ribbon Framework Reference](windowsribbon-reference-entry.md)
</dt> </dl>

 

 





