---
title: How to use the Appx module in a netfx host other than powershell.exe
description: Learn how to use the Appx module in a netfx host other than powershell.exe.
ms.topic: how-to
ms.date: 06/13/2024
---

# How to use the Appx module in a netfx host other than powershell.exe

The Appx PowerShell Module has been retargeted to netstandard2.0 in order to make sure it aligns
with the .netcore future while continuing to support .netfx. The result of this retargeting is a
breaking change that means that Appx PS Module cmdlets (when running under a netfx runtime) won’t
work when running from processes other than powershell.exe.

There are two ways to mitigate this change to use the Appx module in a netfx host other than powershell.exe.

**Option 1:** Each process (other than powershell.exe) that wants to use the Appx PS Module cmdlets
in a netfx runtime environment will need to add the following 4 runtime assemblies to a location
accessible to that process. Typically this would be done by placing these four runtime assemblies
next to the process' *.exe file.

* System.Memory.dll (4.0.1.0, netstd, v2.0)
* System.Numerics.Vectors.dll (4.1.4.0, netstd, v2.0)
* System.Runtime.CompilerServices.Unsafe.dll (4.0.4.0, netfx, v4.0)
* System.Security.Principal.Windows.dll (4.1.1.0, netfx, v4.0)

These four runtime assemblies can be found in their respective NuGet packages (version 4.5.0).

**Option 2:** Retarget the process' runtime environment to netcore from netfx. 




 

 
