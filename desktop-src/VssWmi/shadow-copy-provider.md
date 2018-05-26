---
title: Shadow Copy Provider
description: The Shadow Copy provider supplies management functions for the Shadow Copies of the Shared Folders feature.
ms.assetid: 084c6e75-065e-4a36-ba8a-7f8ce50c6670
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Shadow Copy Provider

The Shadow Copy provider supplies management functions for the Shadow Copies of the Shared Folders feature. This feature can produce copies of files that are located on a shared resource, such as a file server. You can use this provider to create and delete shadow copies and shadow copy storage area objects, and to view associations between these objects and volume objects.

**Windows XP:** The Shadow Copy provider is not available.

The Shadow Copy provider has several association classes that relate the original volume, the shadow copies, volumes used to store differential data, and the shadow copy provider. The [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688) instance name for the Shadow provider is "MSVSS\_PROVIDER".

The Shadow provider is an instance and property provider that supports the standard [**IWbemProviderInit**](https://msdn.microsoft.com/library/aa391853) interface, and the following [**IWbemServices**](https://msdn.microsoft.com/library/aa392093) methods:

-   [**CreateInstanceEnumAsync**](https://msdn.microsoft.com/library/aa392098)
-   [**ExecQueryAsync**](https://msdn.microsoft.com/library/aa392108)
-   [**GetObjectAsync**](https://msdn.microsoft.com/library/aa392110)
-   [**PutInstanceAsync**](https://msdn.microsoft.com/library/aa392116)

The Shadow provider supports the following classes that are located in the \\root\\cimv2 namespace:

-   [**Win32\_ShadowProvider**](win32-shadowprovider.md)
-   [**Win32\_ShadowCopy**](win32-shadowcopy.md)
-   [**Win32\_ShadowContext**](win32-shadowcontext.md)

The Shadow provider also supports the following association classes that are located in the \\root\\cimv2 namespace:

-   [**Win32\_ShadowStorage**](win32-shadowstorage.md)
-   [**Win32\_ShadowBy**](win32-shadowby.md)
-   [**Win32\_ShadowFor**](win32-shadowfor.md)
-   [**Win32\_ShadowOn**](win32-shadowon.md)
-   [**Win32\_ShadowVolumeSupport**](win32-shadowvolumesupport.md)
-   [**Win32\_ShadowDiffVolumeSupport**](win32-shadowdiffvolumesupport.md)

 

 




