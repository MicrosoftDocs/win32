---
title: Interfaces
description: The following interfaces are used to create standard COM objects and property pages.
ms.assetid: f0d655b3-fa92-4553-ba21-617649a922a0
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Interfaces

The following interfaces are used to create standard COM objects and property pages.



| Interface                                             | Description                                                                                                                                                                                                  |
|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IFont**](/windows/win32/OCIdl/nn-ocidl-ifont?branch=master)                                | Provides a wrapper around a Windows font object.                                                                                                                                                             |
| [**IFontDisp**](/windows/win32/OCIdl/?branch=master)                        | Exposes a font object's properties through Automation. It provides a subset of the [**IFont**](/windows/win32/OCIdl/nn-ocidl-ifont?branch=master) methods.                                                                                           |
| [**IOleControl**](/windows/win32/OCIdl/nn-ocidl-iolecontrol?branch=master)                    | Provides the features for supporting keyboard mnemonics, ambient properties, and events in control objects.                                                                                                  |
| [**IOleControlSite**](/windows/win32/OCIdl/nn-ocidl-iolecontrolsite?branch=master)            | Provides the methods that enable a site object to manage each embedded control within a container.                                                                                                           |
| [**IPerPropertyBrowsing**](/windows/win32/OCIdl/nn-ocidl-iperpropertybrowsing?branch=master)  | Retrieves the information in the property pages offered by an object.                                                                                                                                        |
| [**IPicture**](/windows/win32/OCIdl/nn-ocidl-ipicture?branch=master)                          | Manages a picture object and its properties. Picture objects provide a language-neutral abstraction for bitmaps, icons, and metafiles.                                                                       |
| [**IPictureDisp**](/windows/win32/OCIdl/?branch=master)                  | Exposes the picture object's properties through Automation. It provides a subset of the functionality available through [**IPicture**](/windows/win32/OCIdl/nn-ocidl-ipicture?branch=master) methods.                                                |
| [**IPointerInactive**](/windows/win32/OCIdl/nn-ocidl-ipointerinactive?branch=master)          | Enables an object to remain inactive most of the time, yet still participate in interaction with the mouse, including drag and drop.                                                                         |
| [**IPrint**](/windows/win32/DocObj/nn-docobj-iprint?branch=master)                              | Enables compound documents in general and active documents in particular to support programmatic printing.                                                                                                   |
| [**IPropertyNotifySink**](/windows/win32/OCIdl/nn-ocidl-ipropertynotifysink?branch=master)    | Implemented by a sink object to receive notifications about property changes from an object that supports [**IPropertyNotifySink**](/windows/win32/OCIdl/nn-ocidl-ipropertynotifysink?branch=master) as an outgoing interface.                       |
| [**IPropertyPage**](/windows/win32/OCIdl/nn-ocidl-ipropertypage?branch=master)                | Provides the main features of a property page object that manages a particular page within a property sheet.                                                                                                 |
| [**IPropertyPage2**](/windows/win32/OCIdl/nn-ocidl-ipropertypage2?branch=master)              | An extension to [**IPropertyPage**](/windows/win32/OCIdl/nn-ocidl-ipropertypage?branch=master) to support initial selection of a property on a page.                                                                                                 |
| [**IPropertyPageSite**](/windows/win32/OCIdl/nn-ocidl-ipropertypagesite?branch=master)        | Provides the main features for a property page site object.                                                                                                                                                  |
| [**IQuickActivate**](/windows/win32/OCIdl/nn-ocidl-iquickactivate?branch=master)              | Enables controls and containers to avoid performance bottlenecks on loading controls. It combines the load-time or initialization-time handshaking between the control and its container into a single call. |
| [**ISimpleFrameSite**](/windows/win32/OCIdl/nn-ocidl-isimpleframesite?branch=master)          | Provides simple frame controls that act as simple containers for other nested controls.                                                                                                                      |
| [**ISpecifyPropertyPage**](/windows/win32/OCIdl/nn-ocidl-ispecifypropertypages?branch=master) | Indicates that an object supports property pages.                                                                                                                                                            |



 

 

 




