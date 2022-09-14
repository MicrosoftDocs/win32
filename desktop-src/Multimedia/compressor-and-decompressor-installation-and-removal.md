---
title: Compressor and Decompressor Installation and Removal
description: Compressor and Decompressor Installation and Removal
ms.assetid: 1f00d86f-a777-4bf8-8290-96cc83b2f331
keywords:
- video compression manager (VCM),installing compressors
- VCM (video compression manager),installing compressors
- ICInstall function
- ICRemove function
ms.topic: article
ms.date: 05/31/2018
---

# Compressor and Decompressor Installation and Removal

An application can use compressors and decompressors that are already installed on a system running the Microsoft Windows operating system. An application can also install compressors and decompressors for general or special uses. Most applications will not need to install or remove compressors or decompressors because they are usually installed by a setup program. An application might, however, install a compressor directly or install a function as a compressor.

An application can install a compressor or decompressor (or a function used as a compressor or decompressor) by using the [**ICInstall**](/windows/desktop/api/Vfw/nf-vfw-icinstall) function. This function creates an entry in the registry identifying the compressor or decompressor. Your application or another application can search the registry to determine if the system contains a compressor or decompressor suitable for its data. Use **ICInstall** to install all compression and decompression drivers.

An application can locate and open an installed compressor or decompressor by using the [**ICLocate**](/windows/desktop/api/Vfw/nf-vfw-iclocate) and [**ICOpen**](/windows/desktop/api/Vfw/nf-vfw-icopen) functions. When an application finishes using a compressor or decompressor, it closes it by using the [**ICClose**](/windows/desktop/api/Vfw/nf-vfw-icclose) function.

An application can remove the registry entry for an installed compressor or decompressor by using the [**ICRemove**](/windows/desktop/api/Vfw/nf-vfw-icremove) function. This function removes the registry entry of a compressor or decompressor that is not currently loaded in memory.

An application can restrict the use of a compressor or decompressor by installing, opening, closing, and removing it.

Alternatively, to use a function internally as a compressor or decompressor without installing it in the registry, an application can use the [**ICOpenFunction**](/windows/desktop/api/Vfw/nf-vfw-icopenfunction) function. This function requires the calling application to have the address of the function to be used as a compressor or decompressor. When the application finishes using the function, it must close it by using **ICClose**. Because the function was not installed, the application does not need to remove the function from the registry.

The internal structure of a function used as a compressor or decompressor should be the same as the [DriverProc](/windows/win32/api/mmiscapi/nc-mmiscapi-driverproc) entry-point function used by installable drivers. For more information about the **DriverProc** entry-point function, see [Installable Drivers](installable-drivers.md).

> [!Note]  
> An application installing a function as a compressor or decompressor must remove the function before the application is closed so other applications do not try to use the function. When removing a function, the application must identify it with the four-character code used to install it.

 

 

 