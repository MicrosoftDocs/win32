---
title: How to Load a Package for Reading
description: This topic shows how to use Packaging APIs to load a package to be read.
ms.assetid: d9651962-71a0-4cd1-ab26-00bc0fa15b62
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# How to Load a Package for Reading

This topic shows how to use Packaging APIs to load a package to be read.

This topic contains the following sections.

-   [Steps to Load a Package](#steps-to-load-a-package)
-   [Calling Your Function](#calling-your-function)
-   [Code Details](#code-details)
-   [Disclaimer](#disclaimer)
-   [Related topics](#related-topics)

Before your application can access the components of a package, it must load the package for reading by using the Packaging API to create a read-only stream over the package.

You can use a stream either to read a package or to write a package, but you cannot use the same stream for both reading and writing. This topic describes how to use a read-only stream to load a package for reading. For an example of reading and writing a package, see the [Set Author Sample](set-author-sample.md) topic.

> \[!Important\]  
> The stream that you use to load a package for reading remains active for the lifetime of the package object with which it is associated. Do not you use the same stream for both read and write operations because this can cause undefined behavior.

 

## Steps to Load a Package

The following steps describe how to access the Packaging API from your application and how to use those APIs to load a package for reading.

1.  Define a function that loads a package:

    ```C++
    HRESULT
    LoadPackage(
        IOpcFactory *factory,
        LPCWSTR packageName,
        IOpcPackage **outPackage
        )
    {
    ```

    

    This example function requires a reference to a Packaging API factory object instance as an input parameter because your application can retain a reference to that instance and use it to call Packaging APIs repeatedly.

2.  Declare a stream:

    ```C++
        IStream * sourceFileStream = NULL;
    ```

    

    This example uses a default implementation of [**IStream**](https://msdn.microsoft.com/library/windows/desktop/aa380034); if you use a custom stream implementation that does not support the [**IStream::Clone**](https://msdn.microsoft.com/library/windows/desktop/aa380035) method, the package is buffered and read sequentially, incurring overhead when an application accesses package components.

3.  Create a read-only stream over the package to be read:

    ```C++
        // Create a read-only stream over the package to prevent errors caused by
        // simultaneously writing and reading from a package.
        HRESULT hr = factory->CreateStreamOnFile(
                        packageName, 
                        OPC_STREAM_IO_READ, 
                        NULL, 
                        0, 
                        &amp;sourceFileStream
                        );
    ```

    

4.  Load the package to be read:

    ```C++
        if (SUCCEEDED(hr))
        {
            // Note: If a part is modified, it is accessed at least twice for
            // reading and writing. Use the OPC_CACHE_ON_ACCESS flag to reduce
            // overhead incurred by accessing a package component (in this case, a
            // part) multiple times.

            // Read the package into a package object.
            // Note: A stream used to read a package is active for the lifetime of
            // the package object into which it is read. 
            hr = factory->ReadPackageFromStream(
                    sourceFileStream, 
                    OPC_CACHE_ON_ACCESS, 
                    outPackage
                    );
        }
    ```

    

    The package object keeps a pointer to the stream for the lifetime of the object so that you can access the data from the stream at any time.

5.  Release references and return:

    ```C++
        if (sourceFileStream)
        {
            sourceFileStream->Release();
            sourceFileStream = NULL;
        }

        return hr;
    }
    ```

    

## Calling Your Function

The following example shows how to call your load function:


```C++
    IOpcPackage * package = NULL;
```

<span codelanguage="ManagedCPlusPlus"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>    IOpcFactory * factory = NULL;

    // Create a new factory.
    HRESULT hr = CoCreateInstance(
                    __uuidof(OpcFactory),
                    NULL,
                    CLSCTX_INPROC_SERVER,
                    __uuidof(IOpcFactory),
                    (LPVOID*)&amp;factory
                    );

    if (SUCCEEDED(hr))
    {
        // Load the package file.
        hr = opclib::LoadPackage(factory, filename, &amp;package);
    }</code></pre></td>
</tr>
</tbody>
</table>



Now that you have loaded a package file, you can use the `package` interface pointer to read from it.

## Code Details

Here are the details of the example function in one convenient block:


```C++
HRESULT
LoadPackage(
    IOpcFactory *factory,
    LPCWSTR packageName,
    IOpcPackage **outPackage
    )
{
    IStream * sourceFileStream = NULL;

    // Note: Do not use a writable stream to overwrite the data of a package
    // that is read.

    // Create a read-only stream over the package to prevent errors caused by
    // simultaneously writing and reading from a package.
    HRESULT hr = factory->CreateStreamOnFile(
                    packageName, 
                    OPC_STREAM_IO_READ, 
                    NULL, 
                    0, 
                    &amp;sourceFileStream
                    );

    if (SUCCEEDED(hr))
    {
        // Note: If a part is modified, it is accessed at least twice for
        // reading and writing. Use the OPC_CACHE_ON_ACCESS flag to reduce
        // overhead incurred by accessing a package component (in this case, a
        // part) multiple times.

        // Read the package into a package object.
        // Note: A stream used to read a package is active for the lifetime of
        // the package object into which it is read. 
        hr = factory->ReadPackageFromStream(
                sourceFileStream, 
                OPC_CACHE_ON_ACCESS, 
                outPackage
                );
    }

    // Release resources
    if (sourceFileStream)
    {
        sourceFileStream->Release();
        sourceFileStream = NULL;
    }

    return hr;
}
```



You can find this function in the [opclib.cpp](opclib-cpp.md) file of the [Set Author Sample](set-author-sample.md).

## Disclaimer

Some code has been omitted. For the complete code, see the [Set Author Sample](set-author-sample.md).

Code examples are not intended to be complete and working programs. The code examples that are referenced on this page, for example, do not perform parameter checking, error checking, or error handling. Use these examples as a starting point, and then add the code necessary to create a robust application. For more information about error handling in COM, see the [Error Handling (COM)](_com_Error_Handling) topic.

## Related topics

<dl> <dt>

[Packages How-To Topics](packages-how-to-topics.md)
</dt> <dt>

**Overviews**
</dt> <dt>

[Getting Started with the Packaging API](packaging-api-overview.md)
</dt> <dt>

[Packages Overview](packages-overview.md)
</dt> <dt>

**Reference**
</dt> <dt>

[**IOpcFactory**](/windows/previous-versions/msopc/nn-msopc-iopcfactory?branch=master)
</dt> <dt>

[**IOpcFactory::CreateStreamOnFile**](/windows/previous-versions/msopc/nf-msopc-iopcfactory-createstreamonfile?branch=master)
</dt> <dt>

[**IOpcFactory::ReadPackageFromStream**](/windows/previous-versions/msopc/nf-msopc-iopcfactory-readpackagefromstream?branch=master)
</dt> <dt>

[**IStream**](https://msdn.microsoft.com/library/windows/desktop/aa380034)
</dt> <dt>

[**IStream::Clone**](https://msdn.microsoft.com/library/windows/desktop/aa380035)
</dt> <dt>

[Packaging API Reference](packaging-programming-reference.md)
</dt> <dt>

**Samples**
</dt> <dt>

[Packaging API Samples](packaging-programming-samples.md)
</dt> <dt>

[Set Author Sample](set-author-sample.md)
</dt> <dt>

[Set Author opclib.h](opclib-h.md)
</dt> <dt>

[Set Author opclib.cpp](opclib-cpp.md)
</dt> </dl>

 

 




