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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using the Microsoft Windows Media DRM Client Code Examples

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 




