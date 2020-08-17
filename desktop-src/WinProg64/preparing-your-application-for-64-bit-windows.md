---
title: Preparing Your Application for 64-bit Windows
description: There are several features that make it easier for you to develop applications that will run on both 32- and 64-bit Windows. Most of these, such as the new data types, are described in Getting Ready for 64-bit Windows.
ms.assetid: 6559b0ab-17cf-4bec-bf2d-3a0da0a344d3
keywords:
- 64-bit toolkit 64-bit Windows Programming
ms.topic: article
ms.date: 05/31/2018
---

# Preparing Your Application for 64-bit Windows

There are several features that make it easier for you to develop applications that will run on both 32- and 64-bit Windows. Most of these, such as the new data types, are described in [Getting Ready for 64-bit Windows](getting-ready-for-64-bit-windows.md).

The 64-bit toolkit that ships with the Windows SDK includes a 64-bit MIDL compiler, Midl.exe, for generating native 64-bit stubs, as well as 32-bit stubs. Use the **/env win64** switch to generate 64-bit stubs only. The default is to generate dual stubs that run on both platforms.

Note that the 64-bit MIDL supports the [**/Oicf**](/windows/desktop/Midl/-oi) and [**/Os**](/windows/desktop/Midl/-os) optimization modes only.

 

 