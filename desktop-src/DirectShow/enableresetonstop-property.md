---
description: The EnableResetOnStop property sets or retrieves a value that determines how play will resume when the filter graph makes a transition from a stopped state.
ms.assetid: ff2e2756-e3f3-4ddb-b99d-5fa65ec67f6b
title: EnableResetOnStop Property
ms.topic: reference
ms.date: 05/31/2018
---

# EnableResetOnStop Property

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `EnableResetOnStop` property sets or retrieves a value that determines how play will resume when the filter graph makes a transition from a stopped state.

``` syntax
[ bEnableReset = ] MSWebDVD.EnableResetOnStop
```

## Return Value

Returns a Boolean value indicating where the MSWebDVD object will start playing again after the filter graph is stopped.

## Remarks

This property is read/write.

The possible values of this property are: with a default value of true.



| Value | Description                                                                                       |
|-------|---------------------------------------------------------------------------------------------------|
| true  | DVD Navigator will reset and start play from the beginning of the disc. This is the default value |
| false | DVD Navigator will resume play where it left off.                                                 |



 

 

 



