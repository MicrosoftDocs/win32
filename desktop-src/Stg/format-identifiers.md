---
title: Format Identifiers
description: Property set values are stored in a section tagged with a unique FMTID.
ms.assetid: '3ffb6c5e-72ce-4769-847a-72db6f145d61'
keywords:
- Format Identifiers
ms.topic: article
ms.date: 05/31/2018
---

# Format Identifiers

Property set values are stored in a section tagged with a unique FMTID. For example, the FMTID for the COM Summary Information property set is **F29F85E0-4FF9-1068-AB91-08002B27B3D9**.

To define a FMTID for the Summary Information property set, use the **DEFINE\_GUID** macro in an include file for the code that manipulates the property set.


```C++
DEFINE_GUID(FMTID_SummaryInformation, 0xF29F85E0, 0x4FF9, 0x1068, 
0xAB, 0x91, 0x08, 0x00, 0x2B, 0x27, 0xB3, 0xD9);
```



Any code that requires the FMTID for the Summary Information property set, can access it through the *FMTID\_SummaryInformation* variable.

When storing property sets in [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) instances, convert the FMTID to a string name for the storage object.

 

 




