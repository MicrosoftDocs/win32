---
Description: 'An application can search the current directory for all file names that match a given pattern by using the FindFirstFile, FindFirstFileEx, FindNextFile, and FindClose functions.'
ms.assetid: '7edd6c6e-7e8a-415c-866b-2283e5596a62'
title: Searching for One or More Files
---

# Searching for One or More Files

An application can search the current directory for all file names that match a given pattern by using the [**FindFirstFile**](findfirstfile.md), [**FindFirstFileEx**](findfirstfileex.md), [**FindNextFile**](findnextfile.md), and [**FindClose**](findclose.md) functions. The pattern must be a valid file name and can include wildcard characters.

The [**FindFirstFile**](findfirstfile.md) and [**FindFirstFileEx**](findfirstfileex.md) functions create handles that **FindFirstFileEx** uses to search for other files with the same pattern. All functions return information about the file that was found. This information includes the file name, size, attributes, and time.

The [**FindFirstFileEx**](findfirstfileex.md) function also allows an application to search for files based on additional search criteria. The function can limit searches to device names or directory names.

The [**FindClose**](findclose.md) function destroys handles created by [**FindFirstFile**](findfirstfile.md) and [**FindFirstFileEx**](findfirstfileex.md).

An application can search for a single file on a specific path by using the [**SearchPath**](searchpath.md) function.

 

 



