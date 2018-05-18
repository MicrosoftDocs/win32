---
Description: 'To move a directory to another location, along with the files and subdirectories contained within it, call the MoveFileEx, MoveFileWithProgress, or MoveFileTransacted function.'
ms.assetid: 'ca56c109-d6a3-456e-956c-126ce4aee8ba'
title: Moving Directories
---

# Moving Directories

To move a directory to another location, along with the files and subdirectories contained within it, call the [**MoveFileEx**](movefileex.md), [**MoveFileWithProgress**](movefilewithprogress.md), or [**MoveFileTransacted**](movefiletransacted.md) function. The [**MoveFileWithProgress**](movefilewithprogress.md) function has the same functionality as [**MoveFileEx**](movefileex.md), except that **MoveFileWithProgress** enables you to specify a callback routine that receives notifications on the progress of the operation. The [**MoveFileTransacted**](movefiletransacted.md) function enables you to perform the operation as a transacted operation.

The following example demonstrates the use of the [**MoveFileEx**](movefileex.md) function with a directory.


```C++
#include <windows.h>
#include <tchar.h>
#include <stdio.h>

void __cdecl _tmain(int argc, TCHAR *argv[])
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



 

 



