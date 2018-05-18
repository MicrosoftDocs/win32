---
title: Property Management Interfaces
description: Property Management Interfaces
ms.assetid: 'aaed9193-42b5-496a-ac01-aed14d9f6a0a'
keywords: ["Windows Movie Maker,interfaces", "Movie Maker,interfaces", "programming reference,Windows Movie Maker interfaces", "reference for Windows Movie Maker,interfaces", "Windows Movie Maker,property management interfaces", "Movie Maker,property management interfaces", "programming reference,Windows Movie Maker property management interfaces", "reference for Windows Movie Maker,property management interfaces", "transforms,property management interfaces"]
---

# Property Management Interfaces

Windows Movie Maker 6.0 passes all the parameters in a transform's XML initialization file to the transform using a set of wrapper interfaces. These are a nested set of interfaces that mimic the nested parameters in the XML file. The values in the wrapped collection can be read and modified during run time, but the changes will not propagate to the physical XML file.

Each parameter element in the XML file is wrapped by an object that exposes two interfaces: [**ITransformProperty**](itransformproperty.md), which describes that parameter, and [**ITransformProperties**](itransformproperties.md), which is a collection of any child parameter elements. Each **ITransformProperty** element also hosts zero or more [**ITransformPropertyPoint**](itransformpropertypoint.md) interface elements, corresponding to the property's **Point** elements.

A top-level **ITransformProperties** interface that contains all properties for the transform is passed to the transform when it is instantiated. The transform can examine all the parameters by calling [**ITransformProperties::get\_PropertyCount**](itransformproperties-get-propertycount.md) to get a count of child parameters, then retrieving each by calling [**ITransformProperties::get\_PropertyByIndex**](itransformproperties-get-propertybyindex.md). Information about each property can be retrieved by the appropriate **ITransformProperty** method. To see if the property hosts child properties, query **ITransformProperty** for **ITransformProperties**, and get a count of child objects.

To see how a transform obtains the top-level **ITransformProperties** collection, see [Creating Custom Transforms Using COM and DirectX](creating-custom-transforms-using-com-and-directx.md).

Windows Movie Maker provides the following interfaces to manage properties.



| Interface                                                        | Description                                                                   |
|------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [**ITransformProperties**](itransformproperties.md)             | The top-level collection interface, containing zero or more properties.       |
| [**ITransformProperty**](itransformproperty.md)                 | A description of a single property, containing zero or more property points.  |
| [**ITransformPropertyPoint**](itransformpropertypoint.md)       | A description of an associated time and value for the property.               |
| [**ITransformPropertiesConfig**](itransformpropertiesconfig.md) | Manages the creation, addition, and deletion of properties in the collection. |



 

## Related topics

<dl> <dt>

[**Windows Movie Maker APIs**](windows-movie-maker-apis.md)
</dt> </dl>

 

 




