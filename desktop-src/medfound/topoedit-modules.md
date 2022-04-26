---
description: TopoEdit Modules
ms.assetid: f3da2d13-a8ad-4db0-9d18-e94857f0abc7
title: TopoEdit Modules
ms.topic: article
ms.date: 05/31/2018
---

# TopoEdit Modules

The TopoEdit tool is provided with the Windows SDK for Windows Server 2008 and later. The tool requires Windows Vista or later.

The TopoEdit modules are located in the Bin folder of the SDK. These modules are:

-   TopoEdit.exe—Application executable
-   TEDUTIL.dll—Extension DLL

The SDK installation registers the DLL. However, if this fails, at a command prompt, run the following.


```C++
Regsvr32 <Install path>\Microsoft SDKs\Windows\v6.0\Bin\TEDUTIL.dll
```



Source code for TopoEdit is also provided as a sample in the Windows SDK. It is located in the following directory:

\<samples root\>\\Multimedia\\Media Foundation\\TopoEdit

## Related topics

<dl> <dt>

[Introduction to TopoEdit](introduction-to-topoedit.md)
</dt> <dt>

[TopoEdit](topoedit.md)
</dt> </dl>

 

 



