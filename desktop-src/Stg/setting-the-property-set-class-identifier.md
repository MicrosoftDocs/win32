---
title: Setting the Property Set Class Identifier
description: The IPropertyStorage SetClass method sets both the CLSID of the storage object and the class tag value stored in the COM property set. This occurs when invoked on a nonsimple property storage stored in a structured storage object.
ms.assetid: 3f542a66-5e04-43c1-a386-7d709c615972
keywords:
- Setting the Property Set Class Identifier
ms.topic: article
ms.date: 05/31/2018
---

# Setting the Property Set Class Identifier

The [**IPropertyStorage::SetClass**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-setclass) method sets both the CLSID of the storage object and the class tag value stored in the COM property set. This occurs when invoked on a nonsimple property storage stored in a structured storage object.

This provides consistency and uniformity which creates better interaction with some tools. A property storage object is nonsimple if it is created by calling [**IPropertySetStorage::Create**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-create) with the **PROPSETFLAG\_NONSIMPLE** flag set.

The CLSID of the storage object is set with a call to [**IStorage::SetClass**](/windows/desktop/api/Objidl/nf-objidl-istorage-setclass).

 

 




