---
description: When an application performs an IPropertyStorage::WriteMultiple operation on any writeable Windows Image Acquisition (WIA) property, the WIA driver performs a validation on the new property value.
ms.assetid: 61ab2b8b-4c0a-40f4-87f0-2dd3ceea70ab
title: WIA Property Validation
ms.topic: article
ms.date: 05/31/2018
---

# WIA Property Validation

When an application performs an [IPropertyStorage::WriteMultiple](/windows/win32/api/propidlbase/nf-propidlbase-ipropertystorage-writemultiple) operation on any writeable Windows Image Acquisition (WIA) property, the WIA driver performs a validation on the new property value. Writing one property may have side affects that change other property values. It is up to the application to read all property values after a write operation to determine that all properties are set to values the application desires.

Multiple properties can be written simultaneously using the [IPropertyStorage::WriteMultiple](/windows/win32/api/propidlbase/nf-propidlbase-ipropertystorage-writemultiple) operation. There may be cases where some property assignments conflict. In such cases, the priority used to resolve conflicts is as follows:

1.  WIA\_IPS\_CUR\_INTENT
2.  WIA\_IPA\_DATATYPE
3.  WIA\_IPA\_DEPTH
4.  WIA\_IPS\_XRES
5.  WIA\_IPS\_YRES
6.  WIA\_IPS\_XPOS
7.  WIA\_IPS\_YPOS
8.  WIA\_IPS\_XEXTENT
9.  WIA\_IPS\_YEXTENT

## Related topics

<dl> <dt>

[**IWiaPropertyStorage**](/windows/desktop/api/wia_xp/nn-wia_xp-iwiapropertystorage)
</dt> </dl>

 

 
