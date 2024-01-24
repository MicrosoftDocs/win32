---
description: Properties used in the property system of Windows Vista and later are declared in property schemas.
ms.assetid: 4e301210-df3a-41db-a58e-015ee8d41714
title: Creating Custom Properties
ms.topic: article
ms.date: 05/31/2018
---

# Creating Custom Properties

Properties used in the property system of Windows Vista and later are declared in property schemas. These property schemas are defined in XML files and describe various aspects of a property including its type (including information on its primitive type and whether it is multi-valued), how it can be displayed in the Windows UI, what kind of labels (user-friendly editing strings) are to be used with it, and how it is cached in the search store for faster access. Properties are identified by their Canonical Name or their Property Key (PKEY).

A canonical name is the reader-friendly name of the property and uses a namespace convention similar to that used in Microsoft .NET. For system-defined properties (those that are included with Windows), the convention is `System.GroupName.PropertyName`. Note that the Pascal casing scheme, which capitalizes letters at the beginning of each word, is used in these names. Canonical names are used in various places including property lists and column names in the property cache. They are therefore used in Structured Query Language (SQL) queries to retrieve a property value.

A PKEY is a pair of values consisting of a GUID and a **DWORD**, referred to as a *formatID* and *propID* respectively. It is represented by a [**PROPERTYKEY**](/windows/win32/api/wtypes/ns-wtypes-propertykey) structure. Most of the property system APIs accept these property keys. The Windows Software Development Kit (SDK) includes the header file Propkey.h that includes a macro definition of each of the `System` property keys with the convention of `PKEY_GroupName_PropertyName`. For example, `PKEY_Photo_DateTaken` is the property key for the property with canonical name `System.Photo.DateTaken`. Property values are stored in the form of a [**PROPVARIANT**](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) structure, which is an extension of the OLE VARIANT types.

This section contains the following topic, which is integral to creating custom properties:

-   [Understanding the Property Description Schema](./propdesc-schema-entry.md)

> [!Note]  
> Due to potential difficulties that the indexer may have when consuming the property system's schema, it is critical that you define attributes carefully and strategically for the first release of the schema. Any changes to attributes (type, column width, whether indexible) will not be reflected in the database after a schema has been registered. The only ways to have these changes recognized after the schema has been registered once on a system would be either to rebuild the index and then register the new schema, or to register the schema and then create a new property for each subsequent release; for example `PKEY_GroupName_PropertyNameV2`, `PKEY_GroupName_PropertyNameV3`, and so forth). We do not recommend creating new properties in this manner, because multiple extraneous columns may impact system performance.

 

## Related topics

<dl> <dt>

[Implementing Property Handlers](./building-property-handlers.md)
</dt> <dt>

[Property Description Schema](./propdesc-schema-entry.md)
</dt> </dl>

 

 
