---
title: Structured Storage Serialized Property Set Format
description: Persistent property sets provide an option to store data within file system entities. It is recommended that, to create and manage them, you use the IPropertySetStorage and IPropertyStorage interfaces described in Properties and Property Sets.
ms.assetid: f22abe40-535f-4178-9460-59bbe26ff178
keywords:
- Structured Storage Strctd Stg , fundamentals, serialized property set format
ms.topic: article
ms.date: 05/31/2018
---

# Structured Storage Serialized Property Set Format

Persistent property sets provide an option to store data within file system entities. It is recommended that, to create and manage them, you use the [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) and [**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage) interfaces described in [Properties and Property Sets](properties-and-property-sets.md).

Property sets are composed of a tagged section of values, with the section uniquely identified by a format identifier (FMTID). Every property consists of a property identifier and a type indicator that represents a value. Each value stored in a property set has a unique property identifier that distinguishes the property. The type indicator describes the representation of the data in the value.

When you use the [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) and [**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage) interfaces, you do not have to handle the COM serialized property set format structure. For more information, see the listed topics:

All data elements within a property set are stored in Intel representation (that is, in little-endian byte order).

COM defines a standard, serialized data format for property sets. When handling the serialized format, and not with the interfaces, property sets have the following characteristics:

-   Property sets allow for different applications to create their own independent property sets to serve the application.
-   Property sets can be stored in a single [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream) instance or in an [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) instance that contains multiple streams. Property sets are simply another data type that can be stored in many different forms of an in-memory or on-disk storage. For more information and recommended conventions for creating the string name for the storage object, see [Storage Object Naming Conventions](storage-object-naming-conventions.md).
-   Property sets allow for a dictionary of display names to be included that describe the contents. A set of conventions for choosing property names is recommended. For more information about this optional dictionary, see [Reserved Property Identifiers](reserved-property-identifiers.md), including [Property ID 0](/windows/desktop/Stg/reserved-property-identifiers).

The property set stream is divided into three major parts:

-   Header
-   FORMATID/offset pair
-   Section containing the actual property set values

The overall length of the property set stream must be less than or equal to 256K. The following sections, [Property Set Header](property-set-header.md), [Format Identifier/Offset Pair](format-identifier-offset-pair.md), and [Section](section.md) (including [Property Identifiers/Offset Pairs](property-identifiers-offset-pairs.md)), with supporting topics, describe the individual components that compose the property-set data format.

> [!Note]  
> Previous versions of this document described extensions to the property set stream with more than one section allowed, but that has been revised to provide for one section in the property stream. The one exception is [The DocumentSummaryInformation and UserDefined Property Sets](the-documentsummaryinformation-and-userdefined-property-sets.md).

 

 

 