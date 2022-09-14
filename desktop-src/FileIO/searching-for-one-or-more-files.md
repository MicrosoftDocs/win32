---
description: An application can search the current directory for all file names that match a given pattern by using the FindFirstFile, FindFirstFileEx, FindNextFile, and FindClose functions.
ms.assetid: 7edd6c6e-7e8a-415c-866b-2283e5596a62
title: Searching for One or More Files
ms.topic: article
ms.date: 05/31/2018
---

# Searching for One or More Files

An application can search the current directory for all file names that match a given pattern by using the [**FindFirstFile**](/windows/desktop/api/FileAPI/nf-fileapi-findfirstfilea), [**FindFirstFileEx**](/windows/desktop/api/FileAPI/nf-fileapi-findfirstfileexa), [**FindNextFile**](/windows/desktop/api/FileAPI/nf-fileapi-findnextfilea), and [**FindClose**](/windows/desktop/api/FileAPI/nf-fileapi-findclose) functions. The pattern must be a valid file name and can include wildcard characters.

The [**FindFirstFile**](/windows/desktop/api/FileAPI/nf-fileapi-findfirstfilea) and [**FindFirstFileEx**](/windows/desktop/api/FileAPI/nf-fileapi-findfirstfileexa) functions create handles that **FindFirstFileEx** uses to search for other files with the same pattern. All functions return information about the file that was found. This information includes the file name, size, attributes, and time.

The [**FindFirstFileEx**](/windows/desktop/api/FileAPI/nf-fileapi-findfirstfileexa) function also allows an application to search for files based on additional search criteria. The function can limit searches to device names or directory names.

The [**FindClose**](/windows/desktop/api/FileAPI/nf-fileapi-findclose) function destroys handles created by [**FindFirstFile**](/windows/desktop/api/FileAPI/nf-fileapi-findfirstfilea) and [**FindFirstFileEx**](/windows/desktop/api/FileAPI/nf-fileapi-findfirstfileexa).

An application can search for a single file on a specific path by using the [**SearchPath**](/windows/win32/api/processenv/nf-processenv-searchpatha) function.

 

 
