---
Description: 'The AreFileApisANSI function determines whether the file I/O functions are using the ANSI or OEM character set code page.'
ms.assetid: '97ed3b08-ca5d-4ac2-bf1a-7eec40f9ffc2'
title: Determining the Current Character Set Code Page
---

# Determining the Current Character Set Code Page

The [**AreFileApisANSI**](arefileapisansi.md) function determines whether the file I/O functions are using the ANSI or OEM character set code page. The [**SetFileApisToANSI**](setfileapistoansi.md) function causes the functions to use the ANSI code page. The [**SetFileApisToOEM**](setfileapistooem.md) function causes the functions to use the OEM code page.

By default, file I/O functions use ANSI file names. Functions exported by Kernel32.dll that accept or return file names are affected by the file code page setting.

Both [**SetFileApisToANSI**](setfileapistoansi.md) and [**SetFileApisToOEM**](setfileapistooem.md) set the code page per process, rather than per thread or per computer.

 

 



