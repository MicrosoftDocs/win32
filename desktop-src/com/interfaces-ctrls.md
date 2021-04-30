---
title: Interfaces (Controls and Property Pages)
description: The following interfaces are used to create standard COM objects and property pages.
ms.assetid: f0d655b3-fa92-4553-ba21-617649a922a0
ms.topic: article
ms.date: 05/31/2018
---

# Interfaces (Controls and Property Pages)

The following interfaces are used to create standard COM objects and property pages.



| Interface                                             | Description                                                                                                                                                                                                  |
|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IFont**](/windows/desktop/api/OCIdl/nn-ocidl-ifont)                                | Provides a wrapper around a Windows font object.                                                                                                                                                             |
| [**IFontDisp**](/windows/win32/api/ocidl/nn-ocidl-ifontdisp)                        | Exposes a font object's properties through Automation. It provides a subset of the [**IFont**](/windows/desktop/api/OCIdl/nn-ocidl-ifont) methods.                                                                                           |
| [**IOleControl**](/windows/desktop/api/OCIdl/nn-ocidl-iolecontrol)                    | Provides the features for supporting keyboard mnemonics, ambient properties, and events in control objects.                                                                                                  |
| [**IOleControlSite**](/windows/desktop/api/OCIdl/nn-ocidl-iolecontrolsite)            | Provides the methods that enable a site object to manage each embedded control within a container.                                                                                                           |
| [**IPerPropertyBrowsing**](/windows/desktop/api/OCIdl/nn-ocidl-iperpropertybrowsing)  | Retrieves the information in the property pages offered by an object.                                                                                                                                        |
| [**IPicture**](/windows/desktop/api/OCIdl/nn-ocidl-ipicture)                          | Manages a picture object and its properties. Picture objects provide a language-neutral abstraction for bitmaps, icons, and metafiles.                                                                       |
| [**IPictureDisp**](/windows/win32/api/ocidl/nn-ocidl-ipicturedisp)                  | Exposes the picture object's properties through Automation. It provides a subset of the functionality available through [**IPicture**](/windows/desktop/api/OCIdl/nn-ocidl-ipicture) methods.                                                |
| [**IPointerInactive**](/windows/desktop/api/OCIdl/nn-ocidl-ipointerinactive)          | Enables an object to remain inactive most of the time, yet still participate in interaction with the mouse, including drag and drop.                                                                         |
| [**IPrint**](/windows/desktop/api/DocObj/nn-docobj-iprint)                              | Enables compound documents in general and active documents in particular to support programmatic printing.                                                                                                   |
| [**IPropertyNotifySink**](/windows/desktop/api/OCIdl/nn-ocidl-ipropertynotifysink)    | Implemented by a sink object to receive notifications about property changes from an object that supports [**IPropertyNotifySink**](/windows/desktop/api/OCIdl/nn-ocidl-ipropertynotifysink) as an outgoing interface.                       |
| [**IPropertyPage**](/windows/desktop/api/OCIdl/nn-ocidl-ipropertypage)                | Provides the main features of a property page object that manages a particular page within a property sheet.                                                                                                 |
| [**IPropertyPage2**](/windows/desktop/api/OCIdl/nn-ocidl-ipropertypage2)              | An extension to [**IPropertyPage**](/windows/desktop/api/OCIdl/nn-ocidl-ipropertypage) to support initial selection of a property on a page.                                                                                                 |
| [**IPropertyPageSite**](/windows/desktop/api/OCIdl/nn-ocidl-ipropertypagesite)        | Provides the main features for a property page site object.                                                                                                                                                  |
| [**IQuickActivate**](/windows/desktop/api/OCIdl/nn-ocidl-iquickactivate)              | Enables controls and containers to avoid performance bottlenecks on loading controls. It combines the load-time or initialization-time handshaking between the control and its container into a single call. |
| [**ISimpleFrameSite**](/windows/desktop/api/OCIdl/nn-ocidl-isimpleframesite)          | Provides simple frame controls that act as simple containers for other nested controls.                                                                                                                      |
| [**ISpecifyPropertyPage**](/windows/desktop/api/OCIdl/nn-ocidl-ispecifypropertypages) | Indicates that an object supports property pages.                                                                                                                                                            |



 

 

 
