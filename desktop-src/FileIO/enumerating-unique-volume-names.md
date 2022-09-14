---
description: How to get a volume GUID path for each local volume associated with a drive letter that is currently in use on the computer.
ms.assetid: f6590a46-2e09-472c-8231-bb24c9b0b5f6
title: Enumerating Volume GUID Paths
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Volume GUID Paths

The code example in this topic shows you how to obtain a volume **GUID** path for each local volume associated with a drive letter that is currently in use on the computer.

The code example uses the [**GetVolumeNameForVolumeMountPoint**](/windows/desktop/api/FileAPI/nf-fileapi-getvolumenameforvolumemountpointw) function.


```C++
#include <windows.h>
#include <stdio.h>
#include <tchar.h>

#define BUFSIZE MAX_PATH 

void main(void)
 {
  BOOL bFlag;
  TCHAR Buf[BUFSIZE];           // temporary buffer for volume name
  TCHAR Drive[] = TEXT("c:\\"); // template drive specifier
  TCHAR I;                      // generic loop counter

  // Walk through legal drive letters, skipping floppies.
  for (I = TEXT('c'); I < TEXT('z');  I++ ) 
   {
    // Stamp the drive for the appropriate letter.
    Drive[0] = I;

    bFlag = GetVolumeNameForVolumeMountPoint(
                Drive,     // input volume mount point or directory
                Buf,       // output volume name buffer
                BUFSIZE ); // size of volume name buffer

    if (bFlag) 
     {
      _tprintf (TEXT("The ID of drive \"%s\" is \"%s\"\n"), Drive, Buf);
     }
   }
 }
```



For an example that enumerates all locally attached volumes and displays the device path, volume **GUID** path, and mounted paths (including drive letters), see [Displaying Volume Paths](displaying-volume-paths.md).

 

 



