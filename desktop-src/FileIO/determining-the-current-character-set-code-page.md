---
description: The AreFileApisANSI function determines whether the file I/O functions are using the ANSI or OEM character set code page.
ms.assetid: 97ed3b08-ca5d-4ac2-bf1a-7eec40f9ffc2
title: Determining the Current Character Set Code Page
ms.topic: article
ms.date: 05/31/2018
---

# Determining the Current Character Set Code Page

The [**AreFileApisANSI**](/windows/desktop/api/fileapi/nf-fileapi-arefileapisansi) function determines whether the file I/O functions are using the ANSI or OEM character set code page. The [**SetFileApisToANSI**](/windows/desktop/api/fileapi/nf-fileapi-setfileapistoansi) function causes the functions to use the ANSI code page. The [**SetFileApisToOEM**](/windows/desktop/api/fileapi/nf-fileapi-setfileapistooem) function causes the functions to use the OEM code page.

By default, file I/O functions use ANSI file names. Functions exported by Kernel32.dll that accept or return file names are affected by the file code page setting.

Both [**SetFileApisToANSI**](/windows/desktop/api/fileapi/nf-fileapi-setfileapistoansi) and [**SetFileApisToOEM**](/windows/desktop/api/fileapi/nf-fileapi-setfileapistooem) set the code page per process, rather than per thread or per computer.

 

 



