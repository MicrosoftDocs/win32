---
title: How to Save a Package
description: This topic shows how to use Packaging APIs to save a package.
ms.assetid: 120436c8-7a12-4d48-be84-a02bbb672c7f
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# How to Save a Package

This topic shows how to use Packaging APIs to save a package.

This topic contains the following sections.

-   [Introduction](#introduction)
-   [Saving a Package](#saving-a-package)
    -   [Steps to Save a Package](#steps-to-save-a-package)
    -   [Code Details](#code-details)
-   [Disclaimer](#disclaimer)
-   [Related topics](#related-topics)

## Introduction

The code example shows the details of the `SavePackage` function, which uses Packaging APIs to serialize a package that is represented by a package object.

`SavePackage` is declared in the [opclib.h](opclib-h.md) header file and defined in the [opclib.cpp](opclib-cpp.md) implementation file of the [Set Author Sample](set-author-sample.md). For the complete program, which can load, modify and save a package, see the Set Author Sample.

> \[!Important\]  
> Using the same stream to both deserialize and serialize a package is not recommended and may result in undefined behavior.

 

## Saving a Package

The `SavePackage` function shown in the following sections creates a write-only stream over a new package file and then serializes the package that is represented by a package object. If a stream was used to load package components, that stream may be accessed when package components are serialized.

The `SavePackage` function declaration from [opclib.h](opclib-h.md):


```C++
HRESULT
    SavePackage(
    IOpcFactory *factory,
    IOpcPackage *package,
    LPCWSTR targetFileName
    );
```



### Steps to Save a Package

1.  Define an [**IStream**](https://msdn.microsoft.com/library/windows/desktop/aa380034) variable:

    ```C++
        IStream * targetFileStream = NULL;
    ```

    

2.  Create a write-only stream over the package to be saved:

    ```C++
        // Note: Do not use a writable stream to overwrite the data of a package
        // that is read.

        // Create a writable stream over the specified target file name.
        HRESULT hr = factory->CreateStreamOnFile(
                        targetFileName, 
                        OPC_STREAM_IO_WRITE, 
                        NULL, 
                        0, 
                        &amp;targetFileStream
                        );
    
    ```

    

3.  Serialize the package data using the stream:

    ```C++
        if (SUCCEEDED(hr))
        {
            // After a stream over the specified file is created successfully,
            // write package data to the file.
            hr = factory->WritePackageToStream(
                    package, 
                    OPC_WRITE_DEFAULT, 
                    targetFileStream
                    );
        }

        // Release resources
        if (targetFileStream)
        {
            targetFileStream->Release();
            targetFileStream = NULL;
        }
    
    ```

    

### Code Details

The following shows the `SavePackage` function definition in one convenient block found in [opclib.cpp](opclib-cpp.md).

The `SavePackage` function definition:


```C++
HRESULT
SavePackage(
    IOpcFactory *factory,
    IOpcPackage *package,
    LPCWSTR targetFileName
    )
{
    IStream * targetFileStream = NULL;
    // Note: Do not use a writable stream to overwrite the data of a package
    // that is read.

    // Create a writable stream over the specified target file name.
    HRESULT hr = factory->CreateStreamOnFile(
                    targetFileName, 
                    OPC_STREAM_IO_WRITE, 
                    NULL, 
                    0, 
                    &amp;targetFileStream
                    );

    if (SUCCEEDED(hr))
    {
        // After a stream over the specified file is created successfully,
        // write package data to the file.
        hr = factory->WritePackageToStream(
                package, 
                OPC_WRITE_DEFAULT, 
                targetFileStream
                );
    }

    // Release resources
    if (targetFileStream)
    {
        targetFileStream->Release();
        targetFileStream = NULL;
    }

    return hr;
}
```



## Disclaimer

Code examples are not intended to be complete and working programs. The code examples that are referenced on this page, for example, do not perform parameter checking, error checking, or error handling. Use these examples as a starting point, then add the code necessary to create a robust application. For more information about error handling in COM, see the [Error Handling (COM)](_com_Error_Handling) topic.

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

[**IOpcFactory::WritePackageToStream**](/windows/previous-versions/msopc/nf-msopc-iopcfactory-writepackagetostream?branch=master)
</dt> <dt>

[**IStream**](https://msdn.microsoft.com/library/windows/desktop/aa380034)
</dt> <dt>

[Packaging API Reference](packaging-programming-reference.md)
</dt> <dt>

[Packaging API Samples](packaging-programming-samples.md)
</dt> <dt>

[Set Author Sample](set-author-sample.md)
</dt> <dt>

[Set Author opclib.h](opclib-h.md)
</dt> <dt>

[Set Author opclib.cpp](opclib-cpp.md)
</dt> </dl>

 

 




