---
description: Subset of .NET 2.0 Now on Server Core
ms.assetid: f91c4604-b2d6-41e5-be66-bbc8a4f0e28e
title: Subset of .NET 2.0 Now on Server Core
ms.topic: article
ms.date: 05/31/2018
---

# Subset of .NET 2.0 Now on Server Core

## Platform

**Servers** - Windows Server 2008 R2  



## Feature Impact

 **Severity** - Low  
**Frequency** - Low  





## Description

The Server Core installation option for Windows Server 2008 R2 now includes a subset of the .NET Framework 2.0. The subset is the functionality in .NET 2.0 that aligns with the functionality in Server Core; no binaries were added to the Server Core base to allow any portion of .NET 2.0 to function.

There was no .NET support in the Server Core installation option for Windows Server 2008.

## Manifestation of Impact

This allows some .NET 2.0 based-applications to run on Server Core in Windows Server 2008 R2.

## Testing

Verify that the .NET classes your code uses is included in Server Core. Also test any applications that run this code on Server Core.

## Links to Other Resources

-   [Server Core](/previous-versions/windows/desktop/legacy/ms723891(v=vs.85))
-   [Server Core Blog](https://blogs.technet.com/server_core/archive/2008/11/25/net-2-0-and-server-core-in-windows-server-2008-r2.aspx)
-   *See also* the Server Core section of the *Windows Server 2008 R2 SDK* when it becomes available

> [!Note]  
> These resources may not be available in some languages and countries/regions.

 

 

 
