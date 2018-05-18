---
title: Modifying Part Content
description: This topic shows how to use the Packaging APIs to modify the content of a part in a package.
ms.assetid: 'e00425a6-1e80-40e7-bd49-147658d0d076'
---

# Modifying Part Content

This topic shows how to use the Packaging APIs to modify the content of a part in a package.

This topic contains the following sections.

-   [Introduction](#introduction)
-   [Modifying Core Properties Part Content](#modifying-core-properties-part-content)
    -   [Steps to Modify Core Properties Part Content](#steps-to-modify-core-properties-part-content)
    -   [`SetAuthorAndModifiedBy` Code Details](#setauthorandmodifiedby-code-details)
-   [Disclaimer](#disclaimer)
-   [Related topics](#related-topics)

## Introduction

The following code examples show the `SetAuthorAndModifiedBy` function details. This function uses the Packaging APIs to modify the content of a part in a package.

`SetAuthorAndModifiedBy` is declared in the [opclib.h](opclib-h.md) header file and defined in the [opclib.cpp](opclib-cpp.md) implementation file of the [Set Author Sample](set-author-sample.md). For the complete program, which can load, modify and save a package, see the Set Author Sample.

## Modifying Core Properties Part Content

The `SetAuthorAndModifiedBy` function shown in the following sections modifies the content of the Core Properties part for a package that has been loaded by using the Packaging APIs. For a demonstration of package loading, see [Loading a Package to be Read](loading-a-package.md).

`SetAuthorAndModifiedBy` changes the Author and Modified By properties to values that are specified by the user. Because the content of the part is XML markup, `SetAuthorAndModifiedBy` uses the XML DOM APIs to represent and modify the content. For more information about how the XML DOM APIs are used, see the [Set Author Sample](set-author-sample.md).

The `SetAuthorAndModifiedBy` function declaration that is found in [opclib.h](opclib-h.md):


```C++
HRESULT
    SetAuthorAndModifiedBy(
    IOpcPackage *package,
    LPCWSTR AuthorName
    );
```



### Steps to Modify Core Properties Part Content

1.  Declare the variables that are needed to change part content:

    ```C++
        IOpcPart * corePropertiesPart = NULL;
        IXMLDOMDocument2 * corePropertiesDom = NULL;
        IXMLDOMNode * creatorNode = NULL;
        IXMLDOMNode * modifiedName = NULL;
        IStream * stream = NULL;
    ```

    

2.  Get a pointer to the part to be changed—in this case, the Core Properties part:

    ```C++
        HRESULT hr = FindCorePropertiesPart(
                        package,
                        &amp;corePropertiesPart
                        );
    ```

    

    For information about finding a part in a package, see the [Parts Overview](parts-overview.md). For a demonstration of how to find the Core Properties part, see [Finding the Core Properties Part](finding-the-core-properties-part.md).

3.  Retrieve and change the content as needed for the application:

    ```C++
        if (SUCCEEDED(hr))
        {
            hr = DOMFromPart(
                    corePropertiesPart, 
                    g_corePropertiesSelectionNamespaces, 
                    &amp;corePropertiesDom
                    );
        }

        // Change text of the author and modified by properties to the specified
        // author in the DOM.

        if (SUCCEEDED(hr))
        {
            hr = corePropertiesDom->selectSingleNode(
                    L"//dc:creator",
                    &amp;creatorNode
                    );
        }

        if (SUCCEEDED(hr) &amp;&amp; creatorNode != NULL)
        {
            hr = creatorNode->put_text((BSTR)author);
        }

        if (SUCCEEDED(hr))
        {
            hr = corePropertiesDom->selectSingleNode(
                    L"//cp:lastModifiedBy",
                    &amp;modifiedName
                    );
        }

        if (SUCCEEDED(hr) &amp;&amp; modifiedName != NULL)
        {
            hr = modifiedName->put_text((BSTR)author);
        }
    ```

    

    In the [Set Author Sample](set-author-sample.md), where these code examples originate, a helper function is used to create a DOM to represent part content because the content of the Core Properties part is XML markup. Using the XML DOM APIs in this way facilitates the use of XPath queries to locate content that is to be changed. For the implementation details of `DOMFromPart`, see [opclib.cpp](opclib-cpp.md) of the Set Author Sample.

    If the part content is not XML markup, retrieve the part content stream by calling the [**IOpcPart::GetContentStream**](iopcpart-getcontentstream.md) method and change the data as needed for the application.

    The changes made by using the XML DOM APIs must be explicitly applied to part content by using the part content stream.

4.  Clear content from the part content stream and write the changes to the stream:

    ```C++
        // Write the changes to part content of the Core Properties part.
        if (SUCCEEDED(hr))
        {
            // Get the read/write part content stream
            hr = corePropertiesPart->GetContentStream(&amp;stream);
        }

        if (SUCCEEDED(hr))
        {
            // Clear old part content from the stream.
            ULARGE_INTEGER zero = {0};
            hr = stream->SetSize(zero);
        }

        if (SUCCEEDED(hr))
        {
            AutoVariant vStream;

            vStream.SetObjectValue(stream);

            // Write changes made to core properties data to the part content
            // stream of the Core Properties part.
            hr = corePropertiesDom->save(vStream);
        }
    ```

    

    In the [Set Author Sample](set-author-sample.md), where these code examples originate, the changes are written by using the XML DOM APIs; however, the application may write directly to the part content stream by using [**IStream**](https://msdn.microsoft.com/library/windows/desktop/aa380034) interface methods.

5.  Release resources:

    ```C++
        if (corePropertiesPart)
        {
            corePropertiesPart->Release();
            corePropertiesPart = NULL;
        }

        if (corePropertiesDom)
        {
            corePropertiesDom->Release();
            corePropertiesDom = NULL;
        }

        if (creatorNode)
        {
            creatorNode->Release();
            creatorNode = NULL;
        }

        if (modifiedName)
        {
            modifiedName->Release();
            modifiedName = NULL;
        }

        if (stream)
        {
            stream->Release();
            stream = NULL;
        }
    ```

    

### `SetAuthorAndModifiedBy` Code Details

The following code example shows the `SetAuthorAndModifiedBy` function definition in one convenient block that is found in [opclib.cpp](opclib-cpp.md).

The `SetAuthorAndModifiedBy` function definition:


```C++
//////////////////////////////////////////////////////////////////////////////
// Description:
// Set the modified by and author core properties of a specified package to a
// specified author.
//////////////////////////////////////////////////////////////////////////////
HRESULT
SetAuthorAndModifiedBy(
    IOpcPackage *package,
    LPCWSTR author
    )
{
    IOpcPart * corePropertiesPart = NULL;
    IXMLDOMDocument2 * corePropertiesDom = NULL;
    IXMLDOMNode * creatorNode = NULL;
    IXMLDOMNode * modifiedName = NULL;
    IStream * stream = NULL;
    HRESULT hr = FindCorePropertiesPart(
                    package,
                    &amp;corePropertiesPart
                    );
    if (SUCCEEDED(hr))
    {
        hr = DOMFromPart(
                corePropertiesPart, 
                g_corePropertiesSelectionNamespaces, 
                &amp;corePropertiesDom
                );
    }

    // Change text of the author and modified by properties to the specified
    // author in the DOM.

    if (SUCCEEDED(hr))
    {
        hr = corePropertiesDom->selectSingleNode(
                L"//dc:creator",
                &amp;creatorNode
                );
    }

    if (SUCCEEDED(hr) &amp;&amp; creatorNode != NULL)
    {
        hr = creatorNode->put_text((BSTR)author);
    }

    if (SUCCEEDED(hr))
    {
        hr = corePropertiesDom->selectSingleNode(
                L"//cp:lastModifiedBy",
                &amp;modifiedName
                );
    }

    if (SUCCEEDED(hr) &amp;&amp; modifiedName != NULL)
    {
        hr = modifiedName->put_text((BSTR)author);
    }

    // Note: Changes made using the DOM are not automatically applied to
    // part content.

    // Write the changes to part content of the Core Properties part.
    if (SUCCEEDED(hr))
    {
        // Get the read/write part content stream
        hr = corePropertiesPart->GetContentStream(&amp;stream);
    }

    if (SUCCEEDED(hr))
    {
        // Clear old part content from the stream.
        ULARGE_INTEGER zero = {0};
        hr = stream->SetSize(zero);
    }

    if (SUCCEEDED(hr))
    {
        AutoVariant vStream;

        vStream.SetObjectValue(stream);

        // Write changes made to core properties data to the part content
        // stream of the Core Properties part.
        hr = corePropertiesDom->save(vStream);
    }

    // Release resources
    if (corePropertiesPart)
    {
        corePropertiesPart->Release();
        corePropertiesPart = NULL;
    }

    if (corePropertiesDom)
    {
        corePropertiesDom->Release();
        corePropertiesDom = NULL;
    }

    if (creatorNode)
    {
        creatorNode->Release();
        creatorNode = NULL;
    }

    if (modifiedName)
    {
        modifiedName->Release();
        modifiedName = NULL;
    }

    if (stream)
    {
        stream->Release();
        stream = NULL;
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

 

 




