---
title: Standard Picture Object
description: Standard Picture Object
ms.assetid: 2df9e0a7-444b-454c-983a-82e82b9ed9d1
ms.topic: article
ms.date: 05/31/2018
---

# Standard Picture Object

The standard picture object provides a language-neutral abstraction for GDI images: bitmaps, icons, metafiles, and enhanced metafiles. As with the standard font object, the system provides a standard implementation of this object. Its primary interfaces are [**IPicture**](/windows/desktop/api/OCIdl/nn-ocidl-ipicture) and [**IPictureDisp**](/windows/win32/api/ocidl/nn-ocidl-ipicturedisp), the latter being derived from **IDispatch** to provide access to the picture's properties through OLE automation. A picture object is created new with [**OleCreatePictureIndirect**](/windows/desktop/api/OleCtl/nf-olectl-olecreatepictureindirect).

The picture object also supports the outgoing interface [**IPropertyNotifySink**](/windows/desktop/api/OCIdl/nn-ocidl-ipropertynotifysink) so that a client can determine when picture properties change. Accordingly, the picture object also supports [**IConnectionPointContainer**](/windows/desktop/api/OCIdl/nn-ocidl-iconnectionpointcontainer) and one connection point for **IPropertyNotifySink**.

The picture object also supports [**IPersistStream**](/windows/desktop/api/ObjIdl/nn-objidl-ipersiststream) such that it can save and load itself from an instance of [**IStream**](/windows/desktop/api/objidl/nn-objidl-istream). An object that uses a picture object internally would normally save and load the picture as part of the object's own persistence handling. The [**OleLoadPicture**](/windows/desktop/api/OleCtl/nf-olectl-oleloadpicture) function simplifies the creation of a picture object based on stream contents.

## Related topics

<dl> <dt>

[Control Properties](control-properties.md)
</dt> </dl>

 

 