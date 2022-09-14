---
title: Memory-Mapped File Information
description: A memory-mapped file (or file mapping) is the result of associating a file's contents with a portion of the virtual address space of a process. It can be used to share a file or memory between two or more processes.
ms.assetid: b6ec2bc4-c504-4d0b-87f0-39bb1949accd
ms.topic: article
ms.date: 05/31/2018
---

# Memory-Mapped File Information

A *memory-mapped file* (or *file mapping*) is the result of associating a file's contents with a portion of the virtual address space of a process. It can be used to share a file or memory between two or more processes.

The [**GetMappedFileName**](/windows/desktop/api/Psapi/nf-psapi-getmappedfilenamea) function receives a process handle and a pointer to an address as input. If the address is within a memory-mapped file in the virtual address space of the process, the function returns the name of the memory-mapped file. The file names returned by **GetMappedFileName** use device form, rather than drive letters. For example, the file name c:\\winnt\\system32\\ctype.nls would look like this in device form:

\\Device\\Harddisk0\\Partition1\\WINNT\\System32\\ctype.nls

For more information about memory-mapped files, see [File Mapping](/windows/desktop/Memory/file-mapping). For an example that converts file names in device form to drive letters, see [Obtaining a File Name From a File Handle](/windows/desktop/Memory/obtaining-a-file-name-from-a-file-handle).

 

 