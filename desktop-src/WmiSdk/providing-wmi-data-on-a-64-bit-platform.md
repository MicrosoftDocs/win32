---
description: Scripts and applications written for 32-bit operating systems should continue to run properly.
ms.assetid: b437b9ed-b9e4-4fc5-9b86-0eb77bb41b8e
ms.tgt_platform: multiple
title: Providing WMI Data on a 64-bit Platform
ms.topic: article
ms.date: 05/31/2018
---

# Providing WMI Data on a 64-bit Platform

Scripts and applications written for 32-bit operating systems should continue to run properly. If you have an existing 32-bit provider, you can evaluate whether you need to write a 64-bit version for side-by-side operation. Generally, both versions are not necessary and the 64-bit version can service both 32-bit and 64-bit local or remote clients. However, for 32-bit application compatibility mode, use your existing 32-bit WMI provider on a 64-bit system that runs in the 32-bit WOW64 mode.

In rare situations, both the 32-bit and 64-bit providers must run side-by-side on 64-bit systems. In this case, the appropriate version of provider that is loaded depends on whether the caller is 32-bit or 64-bit and local or remote. A caller using the connection object context flags, **\_\_ProviderArchitecture** and **\_\_RequiredArchitecture**, can request that WMI load a nondefault provider. For more information, see [Getting and Providing Data on a 64-bit Computer](getting-and-providing-data-on-a-64-bit-computer.md).

In the unusual case that you must run both the 32-bit and 64-bit providers side-by-side, then you must ensure that install and uninstall scenarios are handled carefully. This is because WMI has only one [*repository*](gloss-w.md) and both the 32-bit and 64-bit versions of [**mofcomp.exe**](mofcomp.md) put the data in the same repository; there is no distinction between a 32-bit or a 64-bit .mof file. Reinstalling one version of the provider will not hurt: the .mof files will be compiled and the classes stored in the repository. However, a second uninstall that deletes a namespace can interfere with the operation of the other provider.

## Related topics

<dl> <dt>

[Getting and Providing Data on a 64-bit Computer](getting-and-providing-data-on-a-64-bit-computer.md)
</dt> <dt>

[Requesting WMI Data on a 64-bit Platform](requesting-wmi-data-on-a-64-bit-platform.md)
</dt> <dt>

[Providing Data to WMI](providing-data-to-wmi.md)
</dt> </dl>

 

 



