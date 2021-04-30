---
description: This function forcefully terminates the calling program if it is invoked inside a loader callout. Otherwise, it has no effect.
ms.assetid: 5C10BF04-B7C7-4481-A184-FDD418FE5F52
title: LdrFastFailInLoaderCallout function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LdrFastFailInLoaderCallout
api_type: 
- DllExport
api_location: 
- NTDll.dll
---

# LdrFastFailInLoaderCallout function

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

This function forcefully terminates the calling program if it is invoked inside a loader callout. Otherwise, it has no effect.

## Syntax


```C++
VOID NTAPI LdrFastFailInLoaderCallout(void);
```



## Parameters

This function has no parameters.

## Return value

This function does not return a value.

## Remarks

This routine does not catch all potential deadlock cases; it is possible for a thread inside a loader callout to acquire a lock while some thread outside a loader callout holds the same lock and makes a call into the loader. In other words, there can be a lock order inversion between the loader lock and a client lock.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------|
| Library<br/> | <dl> <dt>NTDll.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>NTDll.dll</dt> </dl> |



 

 




