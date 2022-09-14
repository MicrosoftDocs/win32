---
title: ActiveX Controls
description: ActiveX Controls
ms.assetid: e491b66c-d6ba-4476-8413-7a9e41c05e8d
ms.topic: article
ms.date: 05/31/2018
---

# ActiveX Controls

ActiveX controls technology rests on a foundation consisting of COM, connectable objects, compound documents, property pages, OLE automation, object persistence, and system-provided font and picture objects. As summarized below, each of these core technologies plays a role in controls.

<dl> <dt>

<span id="COM"></span><span id="com"></span>COM
</dt> <dd>

A control is essentially a COM object that exposes the [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown) interface, through which clients can obtain pointers to its other interfaces. Controls can support licensing through [**IClassFactory2**](/windows/desktop/api/OCIdl/nn-ocidl-iclassfactory2) and self-registration. See [The Component Object Model](the-component-object-model.md) for more information on COM, licensing, and self-registration.

</dd> <dt>

<span id="Connectable_objects"></span><span id="connectable_objects"></span><span id="CONNECTABLE_OBJECTS"></span>Connectable objects
</dt> <dd>

Controls can support outgoing interfaces through connectable objects so that the control can communicate with its client. For example, an outgoing interface can trigger an action in the client, can notify the client of some change in the control, or can request permission from the client before the control takes some action. See [Events in COM and Connectable Objects](events-in-com-and-connectable-objects.md) for more information on how connectable objects work.

</dd> <dt>

<span id="Uniform_data_transfer"></span><span id="uniform_data_transfer"></span><span id="UNIFORM_DATA_TRANSFER"></span>Uniform data transfer
</dt> <dd>

Controls can support being dragged and dropped within a container with help from their container. See [**IOleInPlaceObjectWindowless::GetDropTarget**](/windows/desktop/api/OCIdl/nf-ocidl-ioleinplaceobjectwindowless-getdroptarget) for more information on drag and drop.

</dd> <dt>

<span id="Compound_documents"></span><span id="compound_documents"></span><span id="COMPOUND_DOCUMENTS"></span>Compound documents
</dt> <dd>

A control can be an in-place active object that can be embedded in a containing client. An end-user activates the control to initiate an action in the container application. See [Compound Documents](compound-documents.md) for more information on in-place activation and other compound document interfaces.

</dd> <dt>

<span id="Property_pages"></span><span id="property_pages"></span><span id="PROPERTY_PAGES"></span>Property pages
</dt> <dd>

Controls can provide property pages so end users can view and change the control's properties. See [Property Pages and Property Sheets](property-pages-and-property-sheets.md) for more information on how property pages work.

</dd> <dt>

<span id="OLE_automation"></span><span id="ole_automation"></span><span id="OLE_AUTOMATION"></span>OLE automation
</dt> <dd>

Controls can provide programmability through OLE automation so clients can take advantage of the control's features through a programming language supplied by the client. See the OLE Automation section for more information on OLE automation.

</dd> <dt>

<span id="Persistent_storage"></span><span id="persistent_storage"></span><span id="PERSISTENT_STORAGE"></span>Persistent storage
</dt> <dd>

A control can implement one or more of several persistence interfaces to support persistence of its state. The control implementer must decide what kinds of persistence are most important and implement the appropriate persistence interfaces. The client decides which interface it prefers to use. See [The Component Object Model](the-component-object-model.md) for more information on all the persistence interfaces.

</dd> <dt>

<span id="Font_and_picture_objects"></span><span id="font_and_picture_objects"></span><span id="FONT_AND_PICTURE_OBJECTS"></span>Font and picture objects
</dt> <dd>

Controls can use these system provided objects to provide a visual representation of themselves within the client. The font object implements several interfaces, including [**IFont**](/windows/desktop/api/OCIdl/nn-ocidl-ifont) and [**IFontDisp**](/windows/win32/api/ocidl/nn-ocidl-ifontdisp). A font object can be created with [**OleCreateFontIndirect**](/windows/desktop/api/OleCtl/nf-olectl-olecreatefontindirect). The picture object also implements several interfaces, including [**IPicture**](/windows/desktop/api/OCIdl/nn-ocidl-ipicture) and [**IPictureDisp**](/windows/win32/api/ocidl/nn-ocidl-ipicturedisp). A picture object can be created using [**OleCreatePictureIndirect**](/windows/desktop/api/OleCtl/nf-olectl-olecreatepictureindirect) and can loaded from a stream with [**OleLoadPicture**](/windows/desktop/api/OleCtl/nf-olectl-oleloadpicture).

</dd> </dl>

It is important to understand that these features can be used in any OLE object. One does not need to implement a control in order to use these features. Also, the only required interface on a control is IUnknown. The control optionally supports other interfaces based on the need to support the related features.

In addition to these features, the following interfaces and functions are specific to controls technology: [**IOleControl**](/windows/desktop/api/OCIdl/nn-ocidl-iolecontrol), [**IOleControlSite**](/windows/desktop/api/OCIdl/nn-ocidl-iolecontrolsite), [**ISimpleFrameSite**](/windows/desktop/api/OCIdl/nn-ocidl-isimpleframesite), and [**OleTranslateColor**](/windows/desktop/api/OleCtl/nf-olectl-oletranslatecolor). Also specific to controls are a set of standards for properties and methods that a control or a control container can support.

> [!Note]  
> The system library OleAut32.dll contains implementations of the functions ([**OleCreatePropertyFrame**](/windows/desktop/api/OleCtl/nf-olectl-olecreatepropertyframe), [**OleCreatePropertyFrameIndirect**](/windows/desktop/api/OleCtl/nf-olectl-olecreatepropertyframeindirect), [**OleCreateFontIndirect**](/windows/desktop/api/OleCtl/nf-olectl-olecreatefontindirect), [**OleCreatePictureIndirect**](/windows/desktop/api/OleCtl/nf-olectl-olecreatepictureindirect), [**OleLoadPicture**](/windows/desktop/api/OleCtl/nf-olectl-oleloadpicture), and [**OleTranslateColor**](/windows/desktop/api/OleCtl/nf-olectl-oletranslatecolor)). In addition, OleAut32.dll contains the implementations of the standard font and picture objects, as well as a type library for all the interfaces used with controls as well as the additional data structures and data types.

 

For more information, see the following topics:

-   [ActiveX Controls Architecture](activex-controls-architecture.md)
-   [ActiveX Controls Interfaces](activex-controls-interfaces.md)
-   [Properties and Methods](properties-and-methods.md)
-   [Control Events](control-events.md)
-   [Visual Representation](visual-representation.md)
-   [Keyboard Handling for Controls](keyboard-handling-for-controls.md)
-   [Persistence](persistence.md)
-   [Registration and Licensing](registration-and-licensing.md)

## Related topics

<dl> <dt>

[ActiveX Control and Control Container Guidelines](activex-control-and-control-container-guidelines.md)
</dt> </dl>

 

 