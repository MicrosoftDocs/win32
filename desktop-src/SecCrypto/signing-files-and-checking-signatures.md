---
description: Learn how to sign executable files, scripts, catalogs, and other application artifacts and verify their signatures.
ms.assetid: f413ba32-4a5c-44dd-b526-2c583d00cfdf
title: Signing files and checking signatures
ms.topic: concept-article
ms.date: 10/28/2026
---

# Signing files and checking signatures

Digital signatures identify the publisher of a file and detect changes made after signing. Sign every supported executable artifact that an application builds, installs, downloads, or runs. In addition to executable files and DLLs, review installers, scripts, modules, plug-ins, helper tools, update components, uninstallers, and temporary executable content.

[SignTool](signtool.md) signs and time stamps supported files and verifies embedded and catalog signatures. Use authenticated metadata to provide file identity and version information for scripts and other files that don't have Portable Executable (PE) version resources. Use a signed catalog when a collection of existing files can't be individually signed.

For procedures, see:

- [Use SignTool to sign a file](using-signtool-to-sign-a-file.md)
- [Sign scripts and non-PE files with SignTool](sign-scripts-and-non-pe-files.md)
- [Use SignTool to verify a file signature](using-signtool-to-verify-a-file-signature.md)
