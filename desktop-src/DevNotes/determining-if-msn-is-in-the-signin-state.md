---
description: The following code example shows the usage of a mutex object to determine if MSN Explorer is signed in.
ms.assetid: ec52a61c-9d2c-4327-977b-fb13d042bc37
title: Determining if MSN Is in the Sign-in State
ms.topic: article
ms.date: 05/31/2018
---

# Determining if MSN Is in the Sign-in State

The following code example shows the usage of a mutex object to determine if MSN Explorer is signed in. When you have finished using the handle, be sure to call the [**CloseHandle**](/windows/win32/api/handleapi/nf-handleapi-closehandle) function.

> [!Note]  
> This mutex object is available for use in checking MSN Explorer 7.*x* sign-in status. It may be unavailable in subsequent versions.

 


```C++
    HANDLE hMSNSignedInMutex;

    hMSNSignedInMutex = OpenMutex(SYNCHRONIZE, FALSE, 
        "{ECCC50B5-064B-4693-B104-925714A4C74B}");

    if (hMSNSignedInMutex != NULL)
    {
        // MSN Explorer is signed in
    }
```



 

 
