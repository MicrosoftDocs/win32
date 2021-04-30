---
description: To move a directory to another location, along with the files and subdirectories contained within it, call the MoveFileEx, MoveFileWithProgress, or MoveFileTransacted function.
ms.assetid: ca56c109-d6a3-456e-956c-126ce4aee8ba
title: Moving Directories
ms.topic: article
ms.date: 05/31/2018
---

# Moving Directories

To move a directory to another location, along with the files and subdirectories contained within it, call the [**MoveFileEx**](/windows/desktop/api/WinBase/nf-winbase-movefileexa), [**MoveFileWithProgress**](/windows/desktop/api/WinBase/nf-winbase-movefilewithprogressa), or [**MoveFileTransacted**](/windows/desktop/api/WinBase/nf-winbase-movefiletransacteda) function. The [**MoveFileWithProgress**](/windows/desktop/api/WinBase/nf-winbase-movefilewithprogressa) function has the same functionality as [**MoveFileEx**](/windows/desktop/api/WinBase/nf-winbase-movefileexa), except that **MoveFileWithProgress** enables you to specify a callback routine that receives notifications on the progress of the operation. The [**MoveFileTransacted**](/windows/desktop/api/WinBase/nf-winbase-movefiletransacteda) function enables you to perform the operation as a transacted operation.

The following example demonstrates the use of the [**MoveFileEx**](/windows/desktop/api/WinBase/nf-winbase-movefileexa) function with a directory.


```C++
#include <windows.h>
#include <tchar.h>
#include <stdio.h>

int __cdecl _tmain(int argc, TCHAR *argv[])
{
    printf("\n");
    if( argc != 3 )
    {
        printf("ERROR:  Incorrect number of arguments\n\n");
        printf("Description:\n");
        printf("  Moves a directory and its contents\n\n");
        printf("Usage:\n");
        _tprintf(TEXT("  %s [source_dir] [target_dir]\n\n"), argv[0]);
        printf("  The target directory cannot exist already.\n\n");
        return;
    }

    // Move the source directory to the target directory location.
    // The target directory must be on the same drive as the source.
    // The target directory cannot already exist.

    if (!MoveFileEx(argv[1], argv[2], MOVEFILE_WRITE_THROUGH))
    { 
        printf ("MoveFileEx failed with error %d\n", GetLastError());
        return;
    }
    else _tprintf(TEXT("%s has been moved to %s\n"), argv[1], argv[2]);
}
```



 

 



