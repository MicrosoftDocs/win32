---
description: MFTrace is a tool for generating trace logs for Media Foundation applications.
ms.assetid: 55b421c8-e87c-4dd2-8649-93832c93f999
title: MFTrace
ms.topic: article
ms.date: 05/31/2018
---

# MFTrace

MFTrace is a tool for generating trace logs for Media Foundation applications.

## In this section

-   [Using MFTrace](using-mftrace.md)
-   [MFTrace Keywords](mftrace-keywords.md)
-   [MFTrace Configuration File](mftrace-configuration-file.md)

## Requirements



| Requirement | Value |
|--------------------------|---------------------------------------------------------------------------------------|
| Minimum SDK version      | Microsoft Windows Software Development Kit (SDK) for Windows 7 and .NET Framework 4.0 |
| Minimum operating system | Windows Vista                                                                         |



 

MFTrace requires the following DLLs, which are also provided in the SDK.

-   detoured.dll
-   mfdetours.dll

The SDK provides both 32-bit and 64-bit versions of MFTrace. MFTrace does not support WOW64; to trace a 32-bit process running on 64-bit Windows, use the 32-bit version of MFTrace.

sdk-root on 32 bit systems: \Program Files\Windows Kits\10 
sdk-root on 64 bit system: \Program Files (x86)\Windows Kits\10
You will find mftrace at <sdk-root>\bin\<sdk-version>\<architecture>\mftrace.exe

## Related topics

<dl> <dt>

[Media Foundation Tools](media-foundation-tools.md)
</dt> </dl>

 

 



