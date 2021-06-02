---
description: The CurrentDomain property retrieves the DVD domain that the MSWebDVD object is in.
ms.assetid: 9d545438-9a3d-4c57-a3df-5e75af2e4d1b
title: CurrentDomain Property
ms.topic: reference
ms.date: 05/31/2018
---

# CurrentDomain Property

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `CurrentDomain` property retrieves the DVD domain that the MSWebDVD object is in.

``` syntax
[ iDomain = ] MSWebDVD.CurrentDomain
```

## Return Value

Returns an integer value representing the current domain.

## Remarks

The possible values of the property are:



| Value | Description          |
|-------|----------------------|
| 1     | First play           |
| 2     | Video Manager Menu   |
| 3     | Video Title Set Menu |
| 4     | Title                |
| 5     | Stop                 |



 

Call this method to ensure that the DVD Navigator is in a valid domain for the method you are about to call. For example, before calling [**PlayTitle**](playtitle-method.md), check the `CurrentDomain` property to make sure that the DVD Navigator is not in the Stop or First Play domain.

 

 



