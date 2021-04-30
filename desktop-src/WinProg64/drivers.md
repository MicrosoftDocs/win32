---
title: Drivers (Programming Guide for 64-bit Windows)
description: The 64-bit version of Windows is designed to make it possible for developers to use a single source-code base for their 32-bit and 64-bit applications. To a large extent, this is also true for 32-bit and 64-bit Windows drivers.
ms.assetid: 85d789c9-91dd-4cdc-a10b-c38a455fc940
keywords:
- drivers 64-bit Windows Programming
ms.topic: article
ms.date: 05/31/2018
---

# Drivers (Programming Guide for 64-bit Windows)

The 64-bit version of Windows is designed to make it possible for developers to use a single source-code base for their 32-bit and 64-bit applications. To a large extent, this is also true for 32-bit and 64-bit Windows drivers.

However, 32-bit drivers cannot run on 64-bit Windows and must be ported. For user-mode applications, 64-bit Windows includes WOW64, which enables 32-bit Windows applications to execute (with some loss of performance) on systems running 64-bit Windows. No equivalent translation layer exists for drivers.

For information about porting drivers to 64-bit Windows, see [64-Bit Issues](https://msdn.microsoft.com/library/aa489627.aspx) in the Windows Driver Kit (WDK).

 

 




