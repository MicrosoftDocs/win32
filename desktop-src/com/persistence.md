---
title: Persistence
description: Persistence
ms.assetid: 4916ea52-a21c-4938-81cb-392b5ca1f6c1
ms.topic: article
ms.date: 05/31/2018
---

# Persistence

A control implements one or more of several persistence interfaces to support persistence of its state. For example, the [**IPersistStreamInit**](/windows/desktop/api/OCIdl/nn-ocidl-ipersiststreaminit) interface supports stream-based persistence of the control's state. **IPersistStreamInit** is a replacement for [**IPersistStream**](/windows/desktop/api/ObjIdl/nn-objidl-ipersiststream) and adds an initialization method, [**InitNew**](/windows/desktop/api/OCIdl/nf-ocidl-ipersiststreaminit-initnew). The other methods are the same in both interfaces. **IPersistStreamInit** is not derived from **IPersistStream**; an object supports only one of the two interfaces based on whether it requires the ability to initialize new instances of itself.

Other persistence interfaces that a control can offer include: [**IPersistStorage**](/windows/desktop/api/ObjIdl/nn-objidl-ipersiststorage), [**IPersistMemory**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768210(v=vs.85)), [**IPersistPropertyBag**](/windows/win32/api/ocidl/nn-ocidl-ipersistpropertybag), [**IPersistMoniker**](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775042(v=vs.85)). The control implementer must decide what kinds of persistence are most important and implement the appropriate persistence interfaces. The control implementer also decides what to save. For example, a control can save the current values of its properties or its location and size within its container. The client decides which interface it prefers to use.

Before loading a control from its persistent state, a client can check the OLEMISC\_SETCLIENTSITEFIRST flag to determine if the control supports getting its client site and ambient properties before loading its persistent state. This optimization can save time when instantiating a control since the control is then free to ignore its persistent values rather than loading them only to have them overridden by ambient properties supplied by the client.

A control can also support saving and restoring its state in an OLE property set, a set of identifiers and values in a specified format. This feature can be useful with containers such as Visual Basic, which saves its programs in a textual form. A control that wants to support this feature implements [**IDataObject::GetData**](/windows/desktop/api/ObjIdl/nf-objidl-idataobject-getdata) and [**IDataObject::SetData**](/windows/desktop/api/ObjIdl/nf-objidl-idataobject-setdata) to pass its property values to and from the container, respectively. It is the container's job to convert this information to text and save it. The identifiers used by the control correspond to the control's property names and the values. See the OLE CDK for the definition of this property set.

## Related topics

<dl> <dt>

[ActiveX Controls](activex-controls.md)
</dt> </dl>

 

 