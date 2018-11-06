---
title: Code Pages and Unicode Strings
description: Another consideration in implementing IPropertySetStorage is how Unicode property names are stored in the property ID 0 (the property name dictionary), which does not use Unicode strings.
ms.assetid: 830c90c9-d2a5-4ecf-8cb6-9950ed5320bf
keywords:
- Code Pages and Unicode Strings
ms.topic: article
ms.date: 05/31/2018
---

# Code Pages and Unicode Strings

Another consideration in implementing [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) is how Unicode property names are stored in the property ID 0 (the property name dictionary), which does not use Unicode strings.

Unicode officially has a code page value of 1200. To store Unicode values in the property name dictionary, use a code page value of 1200 for the whole property set (in property ID 1), specified by the absence of the **PROPSETFLAG\_ANSI** flag in [**IPropertySetStorage::Create**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-create). Be aware that this has the side effect of storing all string values in the property set in Unicode. In all code pages, the count found at the start of a **VT\_LPSTR** is a byte count, not a character count. This is necessary to provide for compatibility with earlier-version clients.

The compound file implementation of [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) creates all new property sets completely either in Unicode (code page 1200) or in the current system ANSI code page. This is controlled by the absence or presence of the **PROPSETFLAG\_ANSI** flag in the *grfFlags* parameter of [**IPropertySetStorage::Create**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-create).

Create and open property sets as Unicode. To implement this, do not set the **PROPSETFLAG\_ANSI** flag in the *grfFlags* parameter of [**IPropertySetStorage::Create**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-create). Avoid using **VT\_LPSTR** values, and instead use **VT\_LPWSTR** values. When the code page of the property set is Unicode, **VT\_LPSTR** string values are converted to Unicode when stored, and back to multibyte string values when retrieved.

Setting the **PROPSETFLAG\_ANSI** flag as reported through a call to [**IPropertyStorage::Stat**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-stat) reflects whether the underlying code page is or is not Unicode. Be aware that Property ID 1 can be explicitly read to learn the code page.

You can access Property ID 1 through a call to [**IPropertyStorage::ReadMultiple**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-readmultiple). However, it is read-only, and may not be updated with [**WriteMultiple**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-writemultiple). Furthermore, it may not be deleted with [**DeleteMultiple**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-deletemultiple).

 

 




