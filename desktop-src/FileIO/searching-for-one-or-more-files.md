---
Description: An application can search the current directory for all file names that match a given pattern by using the FindFirstFile, FindFirstFileEx, FindNextFile, and FindClose functions.
ms.assetid: 7edd6c6e-7e8a-415c-866b-2283e5596a62
title: Searching for One or More Files
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Searching for One or More Files

An application can search the current directory for all file names that match a given pattern by using the [**FindFirstFile**](/windows/win32/FileAPI/nf-fileapi-findfirstfilea?branch=master), [**FindFirstFileEx**](/windows/win32/FileAPI/nf-fileapi-findfirstfileexa?branch=master), [**FindNextFile**](/windows/win32/FileAPI/nf-fileapi-findnextfilea?branch=master), and [**FindClose**](/windows/win32/FileAPI/nf-fileapi-findclose?branch=master) functions. The pattern must be a valid file name and can include wildcard characters.

The [**FindFirstFile**](/windows/win32/FileAPI/nf-fileapi-findfirstfilea?branch=master) and [**FindFirstFileEx**](/windows/win32/FileAPI/nf-fileapi-findfirstfileexa?branch=master) functions create handles that **FindFirstFileEx** uses to search for other files with the same pattern. All functions return information about the file that was found. This information includes the file name, size, attributes, and time.

The [**FindFirstFileEx**](/windows/win32/FileAPI/nf-fileapi-findfirstfileexa?branch=master) function also allows an application to search for files based on additional search criteria. The function can limit searches to device names or directory names.

The [**FindClose**](/windows/win32/FileAPI/nf-fileapi-findclose?branch=master) function destroys handles created by [**FindFirstFile**](/windows/win32/FileAPI/nf-fileapi-findfirstfilea?branch=master) and [**FindFirstFileEx**](/windows/win32/FileAPI/nf-fileapi-findfirstfileexa?branch=master).

An application can search for a single file on a specific path by using the [**SearchPath**](/windows/win32/WinBase/?branch=master) function.

 

 



