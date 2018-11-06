---
title: Debugging DirectX apps remotely
description: You can use Visual Studio and the Windows 8 SDK to debug DirectX apps remotely.
ms.assetid: CA471465-47C2-4706-B391-C9E6C2CD69D9
ms.topic: article
ms.date: 05/31/2018
---

# Debugging DirectX apps remotely

You can use Visual Studio and the Windows 8 SDK to debug DirectX apps remotely. The Windows 8 SDK provides a set of components that support DirectX development and provide error checking and parameter validation in addition to the debugging that Visual Studio provides. These components are D3D11\_1SDKLayers.dll, D2D1Debug1.dll, and Dxgidebug.dll.

If you want to debug remotely on a computer without the Windows 8 SDK installed and you want this additional debugging capability, you must install the remote debugging package that is appropriate for the architecture on which you want to debug. The Windows Installer Packages in "C:\\Program Files (x86)\\Windows Kits\\8.0\\Remote\\<arch>" install the appropriate support.

To enable the additional debugging capabilities for Direct2D apps, use this code:


```
        );         
```



To enable the additional debugging capabilities for Direct3D apps, use this code:


```
        );
```



For more info about debugging Direct2D apps, see [Direct2D Debug Layer](https://msdn.microsoft.com/library/windows/desktop/ee794278).

For more info about debugging Direct3D apps, see [Direct3D Debug Layer](https://msdn.microsoft.com/library/windows/desktop/ff476881#debug).

 

 




