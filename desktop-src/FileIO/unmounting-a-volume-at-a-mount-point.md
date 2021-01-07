---
description: How to delete a mounted folder by using the DeleteVolumeMountPoint function.
ms.assetid: 33049110-acf8-4db5-a9c4-bd4a884c8590
title: Deleting a Mounted Folder
ms.topic: article
ms.date: 05/31/2018
---

# Deleting a Mounted Folder

The code example in this topic shows you how to delete a mounted folder by using the [**DeleteVolumeMountPoint**](/windows/desktop/api/FileAPI/nf-fileapi-deletevolumemountpointw) function. For more information, see [Creating Mounted Folders](mounting-and-dismounting-a-volume.md).


```C++
#define _WIN32_WINNT 0x0501

#include <windows.h>
#include <tchar.h>
#include <stdio.h>

void
Syntax (TCHAR *argv)
{
   _tprintf(TEXT("%s unmounts a volume from a volume mount point\n"), 
          argv);
   _tprintf(TEXT("For example: \"%s c:\\mnt\\fdrive\\\"\n"), argv);
}

int _tmain(int argc, TCHAR *argv[])
{
   BOOL bFlag;

   if (argc != 2)
   {
      Syntax (argv[0]);
      return (-1);
   }

// We should do some error checking on the path argument, such as
// ensuring that there is a trailing backslash.

   bFlag = DeleteVolumeMountPoint(
              argv[1] // Path of the volume mount point
           );

   _tprintf(TEXT("\n%s %s in unmounting the volume at %s\n"), argv[0],
           bFlag ? TEXT("succeeded") : TEXT("failed"), argv[1]);

   return (bFlag);
}
```



 

 



