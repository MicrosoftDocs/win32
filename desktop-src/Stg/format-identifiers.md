---
title: Format Identifiers
description: Property set values are stored in a section tagged with a unique FMTID.
ms.assetid: '506c9567-62f2-40aa-a8e7-1530e8aed846'
keywords: ["Format Identifiers"]
---

# Format Identifiers

Property set values are stored in a section tagged with a unique FMTID. For example, the FMTID for the COM Summary Information property set is **F29F85E0-4FF9-1068-AB91-08002B27B3D9**.

To define a FMTID for the Summary Information property set, use the **DEFINE\_GUID** macro in an include file for the code that manipulates the property set.


```C++
DEFINE_GUID(FMTID_SummaryInformation, 0xF29F85E0, 0x4FF9, 0x1068, 
0xAB, 0x91, 0x08, 0x00, 0x2B, 0x27, 0xB3, 0xD9);
```



Any code that requires the FMTID for the Summary Information property set, can access it through the *FMTID\_SummaryInformation* variable.

When storing property sets in [**IStorage**](istorage.md) instances, convert the FMTID to a string name for the storage object.

 

 




