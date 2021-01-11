---
description: Applications can produce user-mode minidump files, which contain a useful subset of the information contained in a crash dump file.
ms.assetid: c5de86a4-6dab-4408-8093-66117eb4de10
title: Minidump Files
ms.topic: article
ms.date: 05/31/2018
---

# Minidump Files

Applications can produce user-mode minidump files, which contain a useful subset of the information contained in a crash dump file. Applications can create minidump files very quickly and efficiently. Because minidump files are small, they can be easily sent over the internet to technical support for the application.

A minidump file does not contain as much information as a full crash dump file, but it contains enough information to perform basic debugging operations. To read a minidump file, you must have the binaries and symbol files available for the debugger.

Current versions of Microsoft Office and Microsoft Windows create minidump files for the purpose of analyzing failures on customers' computers.

The following DbgHelp functions are used with minidump files.

<dl>

[**MiniDumpCallback**](/windows/desktop/api/minidumpapiset/nc-minidumpapiset-minidump_callback_routine)  
[**MiniDumpReadDumpStream**](/windows/desktop/api/minidumpapiset/nf-minidumpapiset-minidumpreaddumpstream)  
[**MiniDumpWriteDump**](/windows/desktop/api/minidumpapiset/nf-minidumpapiset-minidumpwritedump)  
</dl>

 

 



