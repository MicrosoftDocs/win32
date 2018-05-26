---
title: Standard Picture Object
description: Standard Picture Object
ms.assetid: 2df9e0a7-444b-454c-983a-82e82b9ed9d1
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Standard Picture Object

The standard picture object provides a language-neutral abstraction for GDI images: bitmaps, icons, metafiles, and enhanced metafiles. As with the standard font object, the system provides a standard implementation of this object. Its primary interfaces are [**IPicture**](/windows/win32/OCIdl/nn-ocidl-ipicture?branch=master) and [**IPictureDisp**](/windows/win32/OCIdl/?branch=master), the latter being derived from **IDispatch** to provide access to the picture's properties through OLE automation. A picture object is created new with [**OleCreatePictureIndirect**](/windows/win32/OleCtl/nf-olectl-olecreatepictureindirect?branch=master).

The picture object also supports the outgoing interface [**IPropertyNotifySink**](/windows/win32/OCIdl/nn-ocidl-ipropertynotifysink?branch=master) so that a client can determine when picture properties change. Accordingly, the picture object also supports [**IConnectionPointContainer**](/windows/win32/OCIdl/nn-ocidl-iconnectionpointcontainer?branch=master) and one connection point for **IPropertyNotifySink**.

The picture object also supports [**IPersistStream**](/windows/win32/ObjIdl/nn-objidl-ipersiststream?branch=master) such that it can save and load itself from an instance of [**IStream**](https://msdn.microsoft.com/library/windows/desktop/aa380034). An object that uses a picture object internally would normally save and load the picture as part of the object's own persistence handling. The [**OleLoadPicture**](/windows/win32/OleCtl/nf-olectl-oleloadpicture?branch=master) function simplifies the creation of a picture object based on stream contents.

## Related topics

<dl> <dt>

[Control Properties](control-properties.md)
</dt> </dl>

 

 




