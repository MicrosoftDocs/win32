---
title: Using the Microsoft Windows Media DRM Client Code Examples
description: Using the Microsoft Windows Media DRM Client Code Examples
ms.assetid: 75db2663-9eb8-406d-b1a9-8f6092c95f9d
keywords:
- Windows Media Format SDK,code examples
- Windows Media Format SDK,example code
- Windows Media Format SDK,DRM code examples
- digital rights management (DRM),code examples
- DRM (digital rights management),code examples
- digital rights management (DRM),example code
- DRM (digital rights management),example code
ms.topic: article
ms.date: 05/31/2018
---

# Using the Microsoft Windows Media DRM Client Code Examples

Code examples are included in this documentation to illustrate the use of components. The examples are written to be as clear and concise as possible. When reading the examples, you should be aware of the following conventions.

-   All examples are assumed to include windows.h and wmdrmsdk.h. The example will include a note if it requires other headers in order to compile.
-   Error checking has been restricted to breaking out of the function if an error occurs. In an application, you should check for specific error codes and provide some kind of error reporting.
-   Interfaces and memory are released in the code examples using macros named SAFE\_RELEASE and SAFE\_ARRAY\_DELETE. These macros are defined in the following code:
    ```C++
    #ifndef SAFE_RELEASE
    #define SAFE_RELEASE(x) \
       if(x != NULL)        \
       {                    \
          x->Release();     \
          x = NULL;         \
       }
    #endif

    #ifndef SAFE_ARRAY_DELETE
    #define SAFE_ARRAY_DELETE(x) \
       if(x != NULL)             \
       {                         \
          delete[] x;            \
          x = NULL;              \
       }
    #endif
    ```

    

## Related topics

<dl> <dt>

[**Getting Started**](drm-getting-started.md)
</dt> </dl>

 

 




