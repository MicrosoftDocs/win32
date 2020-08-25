---
title: Standard Font Object
description: Standard Font Object
ms.assetid: f9b54dc4-24d4-4eb7-b43f-c481d64e52df
ms.topic: article
ms.date: 05/31/2018
---

# Standard Font Object

The standard ambient font property supplied by the container and the standard font property supplied by the control both provide a standard font object. That is, these standard fonts supply an **IDispatch** pointer to a standard font object.

The font object is a system-provided implementation of a set of interfaces on top of the underlying GDI font support. A font object is created through the API function [**OleCreateFontIndirect**](/windows/desktop/api/OleCtl/nf-olectl-olecreatefontindirect) given a [**FONTDESC**](/windows/win32/api/olectl/ns-olectl-fontdesc) structure. The font object supports a number of read/write properties as well as custom methods through its interface [**IFont**](/windows/desktop/api/OCIdl/nn-ocidl-ifont), and supports the same set of properties (but not the methods) through a dispinterface [**IFontDisp**](/windows/win32/api/ocidl/nn-ocidl-ifontdisp). The dispinterface is used for the font properties mentioned previously. The properties correspond to the GDI font attributes that are described in the [**LOGFONT**](/windows/win32/api/dimm/ns-dimm-logfonta) structure.

The font object also supports the outgoing interface [**IPropertyNotifySink**](/windows/desktop/api/OCIdl/nn-ocidl-ipropertynotifysink) so that a client can determine when font properties change. Since the font object supports at least one outgoing interface, it also implements [**IConnectionPointContainer**](/windows/desktop/api/OCIdl/nn-ocidl-iconnectionpointcontainer) and one connection point for **IPropertyNotifySink** for this purpose.

The font object provides an hFont property that is a Windows font handle that conforms to the other attributes specified for the font. The font object delays realizing this font when possible, so consecutively setting two properties on a font won't cause an intermediate font to be realized. In addition, as an optimization, the standard font object maintains a cache of font handles. Two font objects in the same process that have identical properties will return the same font handle. The font object can remove fonts from this cache at will, which introduces special considerations for clients using this hFont property. See [**IFont::get\_hFont**](/windows/desktop/api/OCIdl/nf-ocidl-ifont-get_hfont) for more details.

The font object also supports [**IPersistStream**](/windows/desktop/api/ObjIdl/nn-objidl-ipersiststream) such that it can save and load itself from an instance of [**IStream**](/windows/desktop/api/objidl/nn-objidl-istream). Any other object that uses a font object internally would normally save and load the font as part of the object's own persistence handling.

In addition, the font object supports [**IDataObject**](/windows/desktop/api/ObjIdl/nn-objidl-idataobject) through which it provides a property set containing typed values for each font property.

## Related topics

<dl> <dt>

[Control Properties](control-properties.md)
</dt> </dl>

 

 