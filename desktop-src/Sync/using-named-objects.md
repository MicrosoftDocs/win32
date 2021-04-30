---
description: The following example illustrates the use of object names by creating and opening a named mutex.
ms.assetid: 06199f83-8fe0-42b9-9db1-58fe1443db4e
title: Using Named Objects
ms.topic: article
ms.date: 05/31/2018
---

# Using Named Objects

The following example illustrates the use of [object names](object-names.md) by creating and opening a named mutex.

## First Process

The first process uses the [**CreateMutex**](/windows/win32/api/synchapi/nf-synchapi-createmutexa) function to create the mutex object. Note that this function succeeds even if there is an existing object with the same name.


```C++
#include <windows.h>
#include <stdio.h>
#include <conio.h>

// This process creates the mutex object.

int main(void)
{
    HANDLE hMutex; 

    hMutex = CreateMutex( 
        NULL,                        // default security descriptor
        FALSE,                       // mutex not owned
        TEXT("NameOfMutexObject"));  // object name

    if (hMutex == NULL) 
        printf("CreateMutex error: %d\n", GetLastError() ); 
    else 
        if ( GetLastError() == ERROR_ALREADY_EXISTS ) 
            printf("CreateMutex opened an existing mutex\n"); 
        else printf("CreateMutex created a new mutex.\n");

    // Keep this process around until the second process is run
    _getch();

    CloseHandle(hMutex);

    return 0;
}
```



## Second Process

The second process uses the [**OpenMutex**](/windows/win32/api/synchapi/nf-synchapi-openmutexw) function to open a handle to the existing mutex. This function fails if a mutex object with the specified name does not exist. The access parameter requests full access to the mutex object, which is necessary for the handle to be used in any of the wait functions.


```C++
#include <windows.h>
#include <stdio.h>

// This process opens a handle to a mutex created by another process.

int main(void)
{
    HANDLE hMutex; 

    hMutex = OpenMutex( 
        MUTEX_ALL_ACCESS,            // request full access
        FALSE,                       // handle not inheritable
        TEXT("NameOfMutexObject"));  // object name

    if (hMutex == NULL) 
        printf("OpenMutex error: %d\n", GetLastError() );
    else printf("OpenMutex successfully opened the mutex.\n");

    CloseHandle(hMutex);

    return 0;
}
```



## Related topics

<dl> <dt>

[Object Names](object-names.md)
</dt> <dt>

[Using Mutex Objects](using-mutex-objects.md)
</dt> </dl>

 

 
