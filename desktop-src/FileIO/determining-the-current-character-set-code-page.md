---
Description: The AreFileApisANSI function determines whether the file I/O functions are using the ANSI or OEM character set code page.
ms.assetid: 97ed3b08-ca5d-4ac2-bf1a-7eec40f9ffc2
title: Determining the Current Character Set Code Page
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Determining the Current Character Set Code Page

The [**AreFileApisANSI**](/windows/win32/fileapi/nf-fileapi-arefileapisansi?branch=master) function determines whether the file I/O functions are using the ANSI or OEM character set code page. The [**SetFileApisToANSI**](/windows/win32/fileapi/nf-fileapi-setfileapistoansi?branch=master) function causes the functions to use the ANSI code page. The [**SetFileApisToOEM**](/windows/win32/fileapi/nf-fileapi-setfileapistooem?branch=master) function causes the functions to use the OEM code page.

By default, file I/O functions use ANSI file names. Functions exported by Kernel32.dll that accept or return file names are affected by the file code page setting.

Both [**SetFileApisToANSI**](/windows/win32/fileapi/nf-fileapi-setfileapistoansi?branch=master) and [**SetFileApisToOEM**](/windows/win32/fileapi/nf-fileapi-setfileapistooem?branch=master) set the code page per process, rather than per thread or per computer.

 

 



