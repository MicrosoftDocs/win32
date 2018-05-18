---
title: Standard Font Object
description: Standard Font Object
ms.assetid: 'f9b54dc4-24d4-4eb7-b43f-c481d64e52df'
---

# Standard Font Object

The standard ambient font property supplied by the container and the standard font property supplied by the control both provide a standard font object. That is, these standard fonts supply an **IDispatch** pointer to a standard font object.

The font object is a system-provided implementation of a set of interfaces on top of the underlying GDI font support. A font object is created through the API function [**OleCreateFontIndirect**](olecreatefontindirect.md) given a [**FONTDESC**](fontdesc.md) structure. The font object supports a number of read/write properties as well as custom methods through its interface [**IFont**](ifont.md), and supports the same set of properties (but not the methods) through a dispinterface [**IFontDisp**](ifontdisp.md). The dispinterface is used for the font properties mentioned previously. The properties correspond to the GDI font attributes that are described in the [**LOGFONT**](_shell_LOGFONT_cpp) structure.

The font object also supports the outgoing interface [**IPropertyNotifySink**](ipropertynotifysink.md) so that a client can determine when font properties change. Since the font object supports at least one outgoing interface, it also implements [**IConnectionPointContainer**](iconnectionpointcontainer.md) and one connection point for **IPropertyNotifySink** for this purpose.

The font object provides an hFont property that is a Windows font handle that conforms to the other attributes specified for the font. The font object delays realizing this font when possible, so consecutively setting two properties on a font won't cause an intermediate font to be realized. In addition, as an optimization, the standard font object maintains a cache of font handles. Two font objects in the same process that have identical properties will return the same font handle. The font object can remove fonts from this cache at will, which introduces special considerations for clients using this hFont property. See [**IFont::get\_hFont**](ifont-get-hfont.md) for more details.

The font object also supports [**IPersistStream**](ipersiststream.md) such that it can save and load itself from an instance of [**IStream**](https://msdn.microsoft.com/library/windows/desktop/aa380034). Any other object that uses a font object internally would normally save and load the font as part of the object's own persistence handling.

In addition, the font object supports [**IDataObject**](idataobject.md) through which it provides a property set containing typed values for each font property.

## Related topics

<dl> <dt>

[Control Properties](control-properties.md)
</dt> </dl>

 

 




