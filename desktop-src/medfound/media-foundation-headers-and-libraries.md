---
description: This topic lists the headers and libraries that define all of the Media Foundation APIs.
ms.assetid: 69877842-fafe-408f-b55b-d2ff2277c756
title: Media Foundation Headers and Libraries
ms.topic: article
ms.date: 05/31/2018
---

# Media Foundation Headers and Libraries

This topic lists the headers and libraries that define all of the Media Foundation APIs.

To find the header and library for a specific API element, consult the reference pages in the [Media Foundation Programming Reference](media-foundation-programming-reference.md).

## Headers

-   codecapi.h
-   d3d11.h
-   d3d9.h
-   d3d9caps.h
-   d3d9types.h
-   dxva.h
-   dxva2api.h
-   dxvahd.h
-   evr.h
-   evr9.h
-   mfapi.h
-   mfcaptureengine.h
-   mferrors.h
-   mfidl.h
-   mfmediacapture.h
-   mfmediaengine.h
-   mfmp2dlna.h
-   mfobjects.h
-   mfplat.lib
-   mfplay.h
-   mfreadwrite.h
-   mftransform.h
-   opmapi.h
-   wmcodecdsp.h
-   wmcontainer.h

## Libraries

-   dxva2.lib
-   evr.lib
-   mf.lib
-   mfplat.lib
-   mfplay.lib
-   mfreadwrite.lib
-   mfuuid.lib

## Library Changes in Windows 7

Starting in Windows 7, certain Media Foundation functions are exported from different DLL files than previous versions.

These changes affect the following .lib files:

-   evr.lib
-   mf.lib
-   mfplat.lib

An application that uses any of these functions must link to a different set of .lib files, depending on the SDK version and the target platform.




| SDK Version | Libraries | 
|-------------|-----------|
| Windows SDK for Windows Vista<br /> Windows SDK for Windows Server 2008<br /> | evr.lib<br /> mf.lib<br /> mfplat.lib<br /> | 
| Windows SDK for Windows 7 | If the target platform is Windows Vista or Windows Server 2008, link the following libraries:<br /><ul><li>evr_vista.lib</li><li>mf_vista.lib</li><li>mfplat_vista.lib</li></ul>If the target platform is Windows 7 or later, link the following libraries:<br /><ul><li>evr.lib</li><li>mf.lib</li><li>mfplat.lib</li></ul> | 




 

## Additional Info on Helper Functions

The Windows 8 MFPlat.dll is a component of the Microsoft Windows operating system. It has several functions included in the module.

MFPlat implements helper functionality for low level memory allocation, operation scheduling FIFOs, and win32 file access abstractions. To be more specific, it provides support for the following:

-   allocating and initializing memory buffers (known as ‘samples’) and helpers to simplify managing their lifetimes
-   efficient Data copying functions for memory buffers
-   allocating and initializing operation FIFOs (known as ‘events’)
-   implementing a simple clock object
-   implementing a win32 file wrapper
-   allocating and initializing arrays of memory buffers for CPUs and GPUs

If the [**MFStartup**](/windows/desktop/api/mfapi/nf-mfapi-mfstartup) method succeeds, MFPlat provides the following work queue functionality:

-   internally supporting I/O items (as used by the win32 file wrapper and socket libraries)
-   providing an array of multithreaded work queues with thread priority support
-   supporting work items, timer items, and wait items through the work queues

MFPlat provides helper functionality for finding and creating media transforms and media sources registered on the system, and creating and manipulating media types, though MFPlat itself cannot create the actual media nor play it back.

## Related topics

<dl> <dt>

[About Media Foundation](about-the-media-foundation-sdk.md)
</dt> </dl>

 

 




