---
description: The CurrentCCService property sets or retrieves the current closed captioning service.
ms.assetid: 094cf812-3122-4d5f-af8a-afd1c2264a2b
title: CurrentCCService Property
ms.topic: reference
ms.date: 05/31/2018
---

# CurrentCCService Property

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `CurrentCCService` property sets or retrieves the current closed captioning service.

``` syntax
[ iService = ] MSWebDVD.CurrentCCService
```

## Return Value

Returns an integer value indicating the type of closed captioning service enabled.

## Remarks

The possible values of this property are:



| Value | Description                                                          |
|-------|----------------------------------------------------------------------|
| 0x0   | No current service. This is the default value.                       |
| 0x1   | True captioning, first field. Default service.                       |
| 0x2   | Captioning for secondary language, second field. Generally not used. |



 

This property is read/write.

## See also

<dl> <dt>

[**CCActive**](ccactive-property.md)
</dt> </dl>

 

 



