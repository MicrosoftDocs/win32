---
title: Application compatibility layer
description: To run legacy applications in a Remote Desktop Services environment you can use the Remote Desktop Services Application Compatibility layer.
ms.assetid: 6e61ed45-4fcb-4aee-b8cc-638a9b87ce00
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Application compatibility layer

To run legacy applications in a Remote Desktop Services environment you can use the Remote Desktop Services Application Compatibility layer. When the Remote Desktop Session Host (RD Session Host) server loads an application that is not Remote Desktop Services aware, it also loads a DLL that contains compatibility code. To use the Remote Desktop Services Application Compatibility layer, you can set the NOT TSAWARE flag when compiling an application.

If your application is Remote Desktop Services aware, you can avoid the overhead of loading this extra DLL and running the compatibility code.

To indicate that your application is Remote Desktop Services aware, set the **IMAGE\_DLLCHARACTERISTICS\_TERMINAL\_SERVER\_AWARE** flag in the optional header. If you are using the linker that ships with Microsoft Visual C++, you can use the **TSAWARE** linker option to set this flag. The **DUMPBIN** tool that ships with Microsoft Visual C++ provides the */HEADERS* option to determine the state of the **TSAWARE** flag. For more information about using the **DUMPBIN** tool, see [DUMPBIN Reference](/cpp/build/reference/dumpbin-reference).

Be careful when you use the **TSAWARE** flag because it enables your application to bypass any Remote Desktop Services compatibility optimizations. The **TSAWARE** flag should only be used if you are certain that your application is designed for the Remote Desktop Services environment. If your application meets the following criteria, you can safely use the **IMAGE\_DLLCHARACTERISTICS\_TERMINAL\_SERVER\_AWARE** flag.

-   The application does not use .ini files.
-   The application does not write to **HKEY\_CURRENT\_USER** during setup. For more information, see [Storing User-Specific Information](storing-user-specific-information.md).
-   The application does not run as a system service (that is, LUID=System).
-   The application does not expect exclusive access to the Windows or other system directories. This means that the application does not store per user temporary or configuration data in the Windows or other system directories.
-   The application does not write to the **HKEY Local Machine** registry hive for user specific data or configuration.
-   The application follows other Remote Desktop Services compatibility guidelines mentioned in this document.

 

 