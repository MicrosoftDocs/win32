---
description: If you provide counters on a 64-bit computer, you must install both the 32-bit and 64-bit version of your provider on the computer if you want to support both 32-bit and 64-bit consumers.
ms.assetid: 2dba2c46-0185-4ce6-a7cc-27cdd9b19b70
title: 64-bit Support
ms.topic: article
ms.date: 05/31/2018
---

# 64-bit Support

A 64-bit performance data provider DLL cannot run in a 32-bit consumer process and a 32-bit performance data provider DLL cannot run in a 64-bit process. The provider registration only supports a single `Library` value for the path to your performance data provider DLL so you cannot supply different paths to be used by 32-bit consumers and 64-bit consumers.

The following options are available to support V1 providers on 64-bit operating systems:

- **Recommended:** Install and register the path to the 32-bit version of your provider DLL.
  - 32-bit consumers will work natively: They will load your 32-bit provider DLL into the 32-bit consumer process.
  - 64-bit consumers will work indirectly: They will be unable to load your 32-bit provider DLL into the 64-bit consumer process, but Windows will automatically fall back to creating a 32-bit perfhost process, loading your 32-bit provider DLL into the perfhost process, and sending performance data from the 32-bit perfhost process to the 64-bit consumer process.
- **64-bit only:** Install and register the path to the 64-bit version of your provider DLL.
  - 32-bit consumers will fail: They will be unable to load your 64-bit provider DLL into the 32-bit process.
  - 64-bit consumers will work natively: They will load your 32-bit provider DLL in-process.

> [!NOTE]
> Several built-in Windows performance data providers install a 32-bit DLL into `%systemroot%\syswow64`, install a 64-bit DLL into `%systemroot%\system32`, and register the `Library` path as `%systemroot%\system32\ProviderName.dll`, allowing filesystem redirection to resolve the path to the appropriate DLL. This is supported only for performance data providers that are part of the Windows operating system. Providers that are not part of the Windows operating system must not install files into the `Windows` folder. Unrecognized files in the `Windows` folder may be removed during servicing or upgrade.
