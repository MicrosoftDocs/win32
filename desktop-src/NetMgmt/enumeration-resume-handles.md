---
title: Enumeration Resume Handles
description: Enumeration resume handles are identifiers for the actual resume key contained in the instance data for the function. This is required for security, interoperability, and to simplify the caller code for the function.
ms.assetid: 6734e99b-7f8c-43c9-96e3-44c9783960dd
ms.topic: article
ms.date: 05/31/2018
---

# Enumeration Resume Handles

Enumeration resume handles are identifiers for the actual resume key contained in the instance data for the function. This is required for security, interoperability, and to simplify the caller code for the function.

If a **NULL** is passed for the pointer to the resume handle, no handle is stored and the enumeration search cannot be continued. This is useful in cases where the application does not want to enumerate all the items.

If an error is returned from an enumeration call, the resume handle must be treated as invalid and not used for any subsequent enumeration calls. When this occurs you must restart the enumeration from the beginning.

 

 




