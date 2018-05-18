---
title: Interfaces
description: The following interfaces are used to create standard COM objects and property pages.
ms.assetid: 'f0d655b3-fa92-4553-ba21-617649a922a0'
---

# Interfaces

The following interfaces are used to create standard COM objects and property pages.



| Interface                                             | Description                                                                                                                                                                                                  |
|-------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IFont**](ifont.md)                                | Provides a wrapper around a Windows font object.                                                                                                                                                             |
| [**IFontDisp**](ifontdisp.md)                        | Exposes a font object's properties through Automation. It provides a subset of the [**IFont**](ifont.md) methods.                                                                                           |
| [**IOleControl**](iolecontrol.md)                    | Provides the features for supporting keyboard mnemonics, ambient properties, and events in control objects.                                                                                                  |
| [**IOleControlSite**](iolecontrolsite.md)            | Provides the methods that enable a site object to manage each embedded control within a container.                                                                                                           |
| [**IPerPropertyBrowsing**](iperpropertybrowsing.md)  | Retrieves the information in the property pages offered by an object.                                                                                                                                        |
| [**IPicture**](ipicture.md)                          | Manages a picture object and its properties. Picture objects provide a language-neutral abstraction for bitmaps, icons, and metafiles.                                                                       |
| [**IPictureDisp**](ipicturedisp.md)                  | Exposes the picture object's properties through Automation. It provides a subset of the functionality available through [**IPicture**](ipicture.md) methods.                                                |
| [**IPointerInactive**](ipointerinactive.md)          | Enables an object to remain inactive most of the time, yet still participate in interaction with the mouse, including drag and drop.                                                                         |
| [**IPrint**](iprint.md)                              | Enables compound documents in general and active documents in particular to support programmatic printing.                                                                                                   |
| [**IPropertyNotifySink**](ipropertynotifysink.md)    | Implemented by a sink object to receive notifications about property changes from an object that supports [**IPropertyNotifySink**](ipropertynotifysink.md) as an outgoing interface.                       |
| [**IPropertyPage**](ipropertypage.md)                | Provides the main features of a property page object that manages a particular page within a property sheet.                                                                                                 |
| [**IPropertyPage2**](ipropertypage2.md)              | An extension to [**IPropertyPage**](ipropertypage.md) to support initial selection of a property on a page.                                                                                                 |
| [**IPropertyPageSite**](ipropertypagesite.md)        | Provides the main features for a property page site object.                                                                                                                                                  |
| [**IQuickActivate**](iquickactivate.md)              | Enables controls and containers to avoid performance bottlenecks on loading controls. It combines the load-time or initialization-time handshaking between the control and its container into a single call. |
| [**ISimpleFrameSite**](isimpleframesite.md)          | Provides simple frame controls that act as simple containers for other nested controls.                                                                                                                      |
| [**ISpecifyPropertyPage**](ispecifypropertypages.md) | Indicates that an object supports property pages.                                                                                                                                                            |



 

 

 




