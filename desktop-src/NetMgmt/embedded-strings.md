---
title: Embedded Strings
description: Information structures will not contain embedded strings. This improves the alignment of the information structures and allows for OEM flexibility in the core functions.
ms.assetid: a3272a0a-5352-4847-84fd-113b4467c32c
ms.topic: article
ms.date: 05/31/2018
---

# Embedded Strings

Information structures will not contain embedded strings. This improves the alignment of the information structures and allows for OEM flexibility in the core functions.

Any information field that is returned in an enumeration call that can be subsequently used as a key for the call to a GetInfo network management function is guaranteed to be present in the enumeration buffer. If the variable-length information string that would specify the key field value will not fit, then the entire fixed-length structure for the entry is not returned. Other variable-length fields will be returned as a **NULL** pointer for the case in which the string does not fit.

 

 




