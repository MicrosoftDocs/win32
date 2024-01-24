---
title: Using the Windows Media Format SDK Code Examples
description: Using the Windows Media Format SDK Code Examples
ms.assetid: '1459a438-d42c-4d84-baa8-fc672f5d5d27'
keywords:
- Windows Media Format SDK,code examples
- Windows Media Format SDK,example code
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Using the Windows Media Format SDK Code Examples

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Many of the explanatory sections of this SDK include code examples. The examples are written to be as clear and concise as possible. When reading the examples, you should be aware of the following conventions.

-   All examples are assumed to include windows.h and wmsdk.h. Any other required header files are mentioned in the explanatory text.
-   Error checking has been restricted to breaking out of the function if an error occurs. In an application, you should check for specific error codes and provide some kind of error reporting.

    When checking return values from methods or functions that return an **HRESULT** value, you should use the **FAILED** macro to discover whether the return value indicates failure.

    ```C++
    HRESULT hr;
    hr = SomeFunction();
    if (FAILED(hr))
    {
       // Check for specific error values.
    }
    ```

    

    Many of the examples in this documentation use a macro named GOTO\_EXIT\_IF\_FAILED, which is defined in the following code.

    ```C++
    #ifndef GOTO_EXIT_IF_FAILED
    #define GOTO_EXIT_IF_FAILED(hr) if(FAILED(hr)) goto Exit;
    #endif
    ```

    

    These example functions each have a tag named "Exit:", after which all interfaces and memory allocated in the function are released and the error code, if any, is returned.

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

    

-   Often, you will need to include the logic of one example in another example for the example to be meaningful. In those instances, a TODO comment is included, with a reference to the appropriate code example.
-   To make the code easier to read, none of the example functions in this documentation validate their input parameters. If you copy any of these functions into your code, you should validate any input parameters.

## Related topics

<dl> <dt>

[**Getting Started**](getting-started.md)
</dt> </dl>

 

 




