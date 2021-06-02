---
description: When variably sized data structures are used to transmit information between TAPI and the application, the application is responsible for allocating the necessary memory.
ms.assetid: f1e2e864-fa10-4058-ba56-faa0ba7363a1
title: Variably Sized Data Structures
ms.topic: article
ms.date: 05/31/2018
---

# Variably Sized Data Structures

When variably sized data structures are used to transmit information between TAPI and the application, the application is responsible for allocating the necessary memory. The amount of memory allocated must be at least large enough for the fixed portion of the data structure, and is set by the application in the **dwTotalSize** member of the data structure. The **dwUsedSize** and **dwNeededSize** members are filled in by TAPI. If **dwTotalSize** is less than the size of the fixed portion, then LINEERR/ PHONEERR\_STRUCTURETOOSMALL is returned. If a function returns success, then all the fields in the fixed portion have been filled in. The **dwUsedSize** and **dwNeededSize** members can be compared to determine if all variable parts have been filled in, and how much space would be required to fill them all in.

If **dwNeededSize** is equal to **dwUsedSize**, then all fixed and variable parts have been filled in. If **dwNeededSize** is larger than **dwUsedSize**, some variable parts may have been filled in, but exactly which variably sized fields have been filled in is undefined. No variable part is ever truncated, and variable parts that would have been truncated due to insufficient space are indicated by having both of their corresponding "Offset" and "Size" parts set to zero. If these are not both zero (and no error was returned), they indicate the offset and size of valid, nontruncated variable-part data.

An application can always guarantee that all variable parts are filled in by allocating and indicating **dwNeededSize** bytes for the structure and calling the "Get" function again until the function returns success and **dwNeededSize** equals **dwUsedSize**. This should happen on the second try except for race conditions that cause changes in the size of variable parts between calls, which should be a rare occurrence.

> [!Note]  
> All text strings, regardless of encoding, in variably sized structures should be **NULL**-terminated according to normal C string-handling conventions.

 

 

 



