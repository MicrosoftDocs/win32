---
title: Calling Remote Desktop ActiveX control non-scriptable interfaces
description: Provides guidance for calling non-scriptable Remote Desktop ActiveX controls from native and managed code.
ms.topic: concept-article
ms.date: 09/11/2023
---

# Calling non-scriptable interfaces from native code

The Windows SDK does not provide header files for the Remote Desktop ActiveX control. This article provides guidance for calling the non-scriptable interfaces it exports from both native and managed code.

## Call non-scriptable interfaces from native code

To call non-scriptable interfaces from native code, use the `#import` directive supported by the Microsoft C++ (MSVC) compiler.

```cpp
#import "libid:8C11EFA1-92C3-11D1-BC1E-00C04FA31489"
#include "mstscax.tlh"
```

The `#import`` directive will generate a header file named "mstscax.tlh" for the Remote Desktop ActiveX control type library. The generated header file can then be included. For this snippet to compile, the developer will need to ensure that the folder where the header file is generated is part of the directories searched for include files by the compiler.

## Call scriptable interfaces from managed code

To call the interfaces of the Remote Desktop ActiveX control from managed code, use [the ActiveX Control Importer tool](/dotnet/framework/tools/aximp-exe-windows-forms-activex-control-importer) to generate a .NET assembly.

```powershell
aximp.exe c:\windows\system32\mstscax.dll
```

The generated assembly can then be referenced by a managed code project in Visual Studio.


## Related topics

[Using the Remote Desktop ActiveX control](using-remote-desktop-web-connection.md)


 

 




