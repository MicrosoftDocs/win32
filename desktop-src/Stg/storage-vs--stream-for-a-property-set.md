---
title: Storage and Stream Objects for a Property Set
description: The programmer specifies whether a property set is stored in a storage or a stream when the property set is created.
ms.assetid: d0ca649a-d405-4c34-af02-9c2ca8b2790e
ms.topic: article
ms.date: 05/31/2018
---

# Storage and Stream Objects for a Property Set

The programmer specifies whether a property set is stored in a storage or a stream when the property set is created. The PROPSETFLAG\_NONSIMPLE enumeration value, passed in the *grfFlags* parameter to the [**IPropertySetStorage::Create**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-create) method, indicates this. Setting where the property set is stored provides proper application controls to fully interoperate through the [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) interface with the COM property set.

If the PROPSETFLAG\_NONSIMPLE flag is set, the property set is stored in a storage object, and nonsimple property values can be written to it. Nonsimple values include values with a **VARTYPE** of VT\_STORAGE, VT\_STREAM, VT\_STORED\_OBJECT, or VT\_STREAMED\_OBJECT. For more information about **VARTYPE** values and how to use them, see the [**PROPVARIANT**](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) structure.

If the PROPSETFLAG\_NONSIMPLE flag is not set, only simple values can be written to the property set.

In the storage object of a nonsimple property set, a stream is created named Contents. This is the primary stream of the property set, and holds all simple property values. Nonsimple property values (streams and storages) are stored under the main storage object of the property set as substreams and storages. That is, these nonsimple values are stored as siblings to the Contents stream. The name of the sibling streams and storages is determined by the implementation, and stored in the Contents stream similar to the way a simple string property is stored.

 

 