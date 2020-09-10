---
title: Placeholder files
description: Placeholder files
ms.assetid: E14655DA-CEA0-4106-B882-C9E9116FC234
ms.topic: article
ms.date: 05/31/2018
---

# Placeholder files

## Platform

**Clients -** Windows 8.1  
**Servers -** Windows Server 2012 R2  

## Description

Placeholder files enable users to view and manage Microsoft OneDrive files regardless of connectivity. Placeholder files represent the OneDrive namespace, even when files are not cached locally. They contain file metadata and thumbnail images of photos.

## Manifestation

To end users and developers, placeholder files look and behave almost the same as the local files.

If your app uses the Common File Dialog to enumerate the file system, your app will not be impacted. When the user tries to open the file from the common /file Dialog, the file content will be downloaded and will be passed to your app.

If your app accesses the file system directly, then your app may take advantage of the placeholder files by using the guidelines below.

## Solution

-   Placeholders are hidden by convention based on attributes
-   Identify placeholders using reparse tag ID IO\_REPARSE\_TAG\_FILE\_PLACEHOLDER

Use the shell data model for seamless behavior:

-   Use SHCreateItemFromParsingName() to create a shell item
-   Bind to the stream using IShellItem::BindToHandler(BHID\_Stream)
-   User property handler for property access (IShellItem2::GetPropertyHandler)
-   User shell thumbnailhandler to get thumbnail images for placeholders
-   Specify SupportedProtocols=\* on your verb implementation if the verb binds to the stream via BindToHandler


```
#include <winnth> //for IO_REPARSE_TAG_FILE_PLACEHOLDER
//  Helper that indicates this is a 
bool IsFilePlaceholder(WIN32_FIND_DATA const &findData)
{
  return (findData.dwFileAttributes & FILE_ATTRIBUTE_REPARSE_POINT) &&
    (findData.dwReserved0 == IO_REPARSE_TAG_FILE_PLACEHOLDER);
}
bool IsFilePlaceholder(_In_PCWSTR filePath)
{
  bool isPlaceholder = false;
  WIN32_FIND_DATA findData;
  HANDLE hFind = FindFirstFile(filePath, &findData);
  if (hFind ! = INVALID_HANDLE_VALUE)
  {
    isPlaceholder = (findData.dwFileAttributes &    FILE_ATTRIBUTE_REPARSE_POINT) &&
    (findData.dwReserved0 == IO_REPARSE_TAG_FILE_PLACEHOLDER);
    FindClose(hFind);
  }
  Return isPlaceholder;
}
```



 

 




