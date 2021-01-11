---
description: The HTAPICALL datatype represents the TAPI opaque handle for a call data structure.
ms.assetid: a2a17b03-5779-411e-8959-6e2de5e53c5a
title: HTAPICALL
ms.topic: article
ms.date: 05/31/2018
---

# HTAPICALL

The **HTAPICALL** datatype represents the TAPI opaque handle for a call data structure. TAPI must resolve a value of this type into a reference to the appropriate data structure instance. The service provider must not attempt to reference through this as if it were a pointer, make assumptions about its values, or interpret its representation in any way other than passing its value to TAPI at appropriate times.

 

 



