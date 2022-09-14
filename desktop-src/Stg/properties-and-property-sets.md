---
title: Properties and Property Sets
description: While the kinds of run-time properties that Automation and Microsoft ActiveX Controls offer are important, they do not directly address the need to store information with objects persistently stored in the file system.
ms.assetid: 350cfb84-2f8e-46e7-a70d-09beb14a8eee
keywords:
- Structured Storage Strctd Stg ,fundamentals,properties and property sets
ms.topic: article
ms.date: 05/31/2018
---

# Properties and Property Sets

While the kinds of run-time properties that Automation and Microsoft ActiveX Controls offer are important, they do not directly address the need to store information with objects persistently stored in the file system. These entities could include files (structured, compound, and so forth), directories, and summary catalogs. COM provides both a standard serialized format for these persistent properties, and a set of interfaces and functions that allow you to create and manipulate the property sets and their properties.

Persistent properties are stored as sets, and one or more sets may be associated with a file system entity. These persistent property sets are intended to be used to store data that is suited to being represented as a collection of fine-grained values. They are not intended to be used as a large data base. They can be used to store summary information about an object on the system, which can then be accessed by any other object that understands how to interpret that property set.

Previous versions of COM specified very little with respect to properties and their usage, but did define a serialized format that allowed developers to store properties and property sets in an [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) instance. The property identifiers and semantics of a single property set, used for summary information about a document, were also defined. At that time, it was necessary to create and manipulate that structure directly as a data stream. See [Structured Storage Serialized Property Set Format](structured-storage-serialized-property-set-format.md).

Now, however, COM defines two primary interfaces to manage property sets:

-   [**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage)
-   [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage)

It is no longer necessary to deal with the serialized format directly when these interfaces are implemented on an object that supports the [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) interface (such as compound files). Writing properties through [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) and [**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage) creates data that exactly conforms to the COM property set format, as viewed through **IStorage** methods. The converse is also true — properties written to the COM property set format using **IStorage** are visible through **IPropertySetStorage** and **IPropertyStorage** (although you cannot expect to write to [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream) and have the properties through **IPropertyStorage** immediately available, or vice versa).

The [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) interface defines methods that create and manage property sets. The [**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage) interface directly manipulates the properties within a property set. By calling the methods of these interfaces, an application developer can manage whatever property sets are appropriate for a given file system entity. Use of these interfaces provides one tuned reading and writing implementation for properties, rather than having an implementation in each application, where there could be performance bottlenecks such as incessant seeking. You can implement the interfaces to enhance performance, so properties can be read and written more quickly by, for example, more efficient caching. Furthermore, **IPropertyStorage** and **IPropertySetStorage** make it possible to manipulate properties on entities that do not support [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage), although in general, most applications will not do so.

This section contains the following topics:

-   [The Summary Information Property Set](the-summary-information-property-set.md)
-   [Predefined Property Set Format Identifiers](predefined-property-set-format-identifiers.md)
-   [The DocumentSummaryInformation and UserDefined Property Sets](the-documentsummaryinformation-and-userdefined-property-sets.md)

## Related topics

<dl> <dt>

[Property Set Implementations in COM](property-set-implementations-in-com.md)
</dt> <dt>

[Property Set Considerations](property-set-considerations.md)
</dt> <dt>

[Managing Properties](managing-properties.md)
</dt> <dt>

[Managing Property Sets](managing-property-sets.md)
</dt> <dt>

[Storing Property Sets](storing-property-sets.md)
</dt> <dt>

[Performance Characteristics](performance-characteristics.md)
</dt> </dl>

 

 




