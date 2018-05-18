---
title: Supported file formats
description: The File API supports native and Pfile formats.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'EC831494-7F2C-4C70-9063-B02CDDEA14EE'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
---

# Supported file formats

The File API supports native and Pfile formats.

## Supported File Formats

The current version of the File API supports native protection for Microsoft Office files, Portable Document Files (PDF) and PFile protection for all other file formats. PDF files can optionally have PFile protection applied.

-   **Native protection**. In native protection, the file is encrypted to an AD RMS file format that is based its MIME type (file name extension). Files that are natively protected using File API are consistent with the format expected by AD RMS enabled applications that use native protection; for example, Office 2013, Office 2010, and FoxIt PDF reader. Native protection is supported only on Office files, PDF files, and a select number of other file types. For more information about the file types on which native protection is supported, see [File API configuration](file-api-configuration.md).
-   **PFile protection**. In PFile protection, files are encrypted using AD RMS Protected File (PFile) format. The file is encrypted to a file with an extension of .pfile. PFile protection is supported for all file formats except Office files.

Administrators can set registry keys to configure whether and how files should be protected based on their file name extension. For more information about how to configure file protection when using File API, see [File API configuration](file-api-configuration.md).

## Related topics

<dl> <dt>

[Developer notes](developer-notes.md)
</dt> <dt>

[File API configuration](file-api-configuration.md)
</dt> </dl>

 

 




