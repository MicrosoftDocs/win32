---
title: Finding the Core Properties part
description: This topic shows how to use the Packaging APIs to find the Core Properties part with a relationship type.
ms.assetid: d485d085-b605-41d4-a094-bd1be37d6693
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Finding the Core Properties part

This topic shows how to use the Packaging APIs to find the Core Properties part with a relationship type.

This topic contains the following sections.

-   [Introduction](#introduction)
-   [Finding the Core Properties Part by its Relationship Type](#finding-the-core-properties-part-by-its-relationship-type)
    -   [Steps](#steps)
    -   [`FindCorePropertiesPart` Code Details](#findcorepropertiespart-code-details)
    -   [`FindPartByRelationshipType` Code Details](#findpartbyrelationshiptype-code-details)
-   [Disclaimer](#disclaimer)
-   [Related topics](#related-topics)

## Introduction

This code example shows the `FindCorePropertiesPart` and `FindPartByRelationshipType` functions, which are the primary functions for finding the Core Properties part in the [Set Author Sample](set-author-sample.md).

Both functions are declared in the [opclib.h](opclib-h.md) header file and defined in the [opclib.cpp](opclib-cpp.md) implementation file of the [Set Author Sample](set-author-sample.md). For the complete program, which can load, modify, and save a package, see the Set Author Sample.

## Finding the Core Properties Part by its Relationship Type

The function in the following sections finds the Core Properties part by following the steps outlined in the [Parts Overview](parts-overview.md). For each step, the code is accompanied by additional explanation to show how that step could be implemented.

The step that requires resolving the part name from the URI of a relationship's target is omitted from this topic but is shown in the [Resolving a Part Name from a Relationship's Target URI](resolving-a-part-name-from-a-relationship-s-target-uri.md) topic.

### Steps

1.  Identify and define a constant for the relationship type to be used and for the content type of the part.

    The content type can be used to ensure that part content is the expected content type, which is described in the package-format specification or the OPC.

    To find the Core Properties part, both the core properties relationship type and the Core Properties part content type are required. Both of these are defined in the OPC, and their definitions are shown in the following table.

    | Info to find Core Properties part   | Definition from OPC                                                                   |
    |-------------------------------------|---------------------------------------------------------------------------------------|
    | core properties relationship type   | http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties |
    | Core Properties part's content type | application/vnd.openxmlformats-package.core-properties+xml                            |

    

     

    Define a constant for the core properties relationship type:

    ```C++
    // The relationship type (core-properties relationship type) of the
    // relationship targeting the Core Properties part, as defined by the OPC
    // (ECMA-376 Part 2).
    static const WCHAR g_corePropertiesRelationshipType[] = 
        L"http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties";
    ```

    

    Define a constant for the Core Properties part's content type:

    ```C++
    // The expected content type of the Core Properties part, as defined by the OPC
    // (ECMA-376 Part 2).
    static const WCHAR g_corePropertiesContentType[] = 
        L"application/vnd.openxmlformats-package.core-properties+xml";
    ```

    

2.  Access the package where the part to be found is stored.

    This code example primarily uses two functions to find the Core Properties part: `FindCorePropertiesPart` and `FindPartByRelationshipType`. To find a part, most of the work is done in the body of the `FindPartByRelationshipType` function.

    The `FindCorePropertiesPart` function declaration from the [opclib.h](opclib-h.md) file:

    ```C++
    HRESULT
        FindCorePropertiesPart(
        IOpcPackage *package,
        IOpcPart **part
        );
    ```

    

    The `FindCorePropertiesPart` function takes an [**IOpcPackage**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcpackage) interface pointer representing the package and retrieves an [**IOpcPart**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcpart) interface pointer representing the Core Properties part. It finds the Core Properties part by wrapping a call to `FindPartByRelationshipType`, and by passing in as input arguments the global variables that contain the relationship type and part content type that are needed to find the Core Properties part.

    The body of the `FindCorePropertiesPart` function:

    ```C++
        return FindPartByRelationshipType(
                    package,
                    g_corePropertiesRelationshipType,
                    g_corePropertiesContentType,
                    part
                    );
    ```

    

    In this example, the relationship type that is defined in `g_corePropertiesRelationshipType` identifies a relationship that targets the Core Properties part. The `FindPartByRelationshipType` function is used to find the Core Properties part in this example. It can also be used to find any part targeted by a package relationship if the relevant relationship type and, optionally, content type information is passed to the function.

    The `FindPartByRelationshipType` function declaration from the [opclib.h](opclib-h.md) file:

    ```C++
    HRESULT 
        FindPartByRelationshipType(
        IOpcPackage *package,
        LPCWSTR relationshipType,
        LPCWSTR contentType, // optional
        IOpcPart **part
        );
    ```

    

3.  Find the part. The body of the `FindPartByRelationshipType` function finds the part and is shown in the following code.

    Declare variables that will be used to find the part:

    ```C++
        *part = NULL; // Enable checks against value of *part.

        IOpcRelationshipSet * packageRels = NULL;
        IOpcRelationshipEnumerator * packageRelsEnum = NULL;
        IOpcPartSet * partSet = NULL;
        BOOL hasNext = false;
    
    ```

    

    Get the part set object, which contains the parts in the package (excluding Relationships parts):

    ```C++
        HRESULT hr = package->GetPartSet(&amp;partSet);
    ```

    

    1.  The part to be found is targeted by a package relationship; therefore, a pointer to the relationship set object that represents the Relationships part that stores package relationships must be retrieved.

        Call the [**IOpcPackage::GetRelationshipSet**](/previous-versions/windows/desktop/api/msopc/nf-msopc-iopcpackage-getrelationshipset) method to retrieve a pointer to the relationship set object for package relationships:

        ```C++
            if (SUCCEEDED(hr))
            {
                // Get package relationships stored in the package's Relationships part.
                hr = package->GetRelationshipSet(&amp;packageRels);
            }
        ```

        

    2.  Identify the relationships of the specified relationship type in the set.

        Call the [**IOpcRelationshipSet::GetEnumeratorForType**](/previous-versions/windows/desktop/api/msopc/nf-msopc-iopcrelationshipset-getenumeratorfortype) method to retrieve an enumerator of the interface pointers in the set that represent relationships of the specified relationship type:

        ```C++
            if (SUCCEEDED(hr))
            {
                // Get package relationships of the specified relationship type.
                hr = packageRels->GetEnumeratorForType(
                        relationshipType,
                        &amp;packageRelsEnum
                        );
            }
        ```

        

        > \[!Important\]  
        > If the package format designer described an expected number of relationships of the specified relationship type that are stored in a Relationships part the , check that the number of relationships retrieved conforms to that expectation. For information about the expected number of relationships for a specified relationship type, see the package format specification or the OPC.

         

4.  To find the part, iterate through relationships of the specified relationship type.

    > [!Note]  
    > This example is limited to finding the first, arbitrary part that is the target of a relationship retrieved from the enumerator.

     

    Define a loop to iterate through the enumerator of relationships:

    ```C++
        if (SUCCEEDED(hr))
        {
            // Move pointer to first package relationship.
            hr = packageRelsEnum->MoveNext(&amp;hasNext);
        }

        // Find the first, arbitrary part that is the target of a relationship
        // of the specified type and has the specified content type, if a content
        // type is provided. Abandon search when an error is encountered, when
        // there are no more relationships in the enumerator, or when a part is
        // found.
        while (SUCCEEDED(hr) &amp;&amp; hasNext &amp;&amp; *part == NULL)
        {
            IOpcPartUri * partUri = NULL;
            IOpcRelationship * currentRel = NULL;
            BOOL partExists = FALSE;

            hr = packageRelsEnum->GetCurrent(&amp;currentRel);
    ```

    

    1.  If the target of a relationship is a part, resolve the part name against the URI of the relationship's source:

        ```C++
                if (SUCCEEDED(hr))
                {
                    // There was a relationship of the specified type.
                    // Try to resolve the part name of the relationship's target.
                    hr = ResolveTargetUriToPart(currentRel, &amp;partUri);
                }
        ```

        

        For an example that shows how to resolve a part name from the target URI of a relationship, see [Resolving a Part Name from a Target URI](resolving-a-part-name-from-a-relationship-s-target-uri.md).

    2.  Ensure that a part with the resolved part name exists in the package, as shown in the following code.

        ```C++
                if (SUCCEEDED(hr))
                {
                    // Part name resolved. Check that a part with that part name
                    // exists in the package.
                    hr = partSet->PartExists(partUri, &amp;partExists);
                }
        ```

        

    3.  Get the part.

        Get the [**IOpcPart**](/previous-versions/windows/desktop/api/msopc/nn-msopc-iopcpart) interface pointer to the part object that represents the part, as shown in the following code.

        ```C++
                if (SUCCEEDED(hr) &amp;&amp; partExists)
                {
                    // A part with the resolved part name exists in the package, so
                    // get a pointer to that part.

                    LPWSTR currentContentType = NULL;
                    IOpcPart * currentPart = NULL;

                    hr = partSet->GetPart(partUri, &amp;currentPart);
        ```

        

    4.  If an expected content type is defined for the part by the package designer or the OPC, ensure that the part has the correct content type. If the part has the expected content type, or if no expected content type is defined, the part has been found.

        ```C++
                    if (SUCCEEDED(hr) &amp;&amp; contentType != NULL)
                    {
                        // Content type specified.
                        // Get the content type of the part.
                        hr = currentPart->GetContentType(&amp;currentContentType);

                        // Compare the content type of the part with the specified
                        // content type.
                        if (SUCCEEDED(hr) &amp;&amp;
                            0 == wcscmp(contentType, currentContentType))
                        {
                            // Part content type matches specified content type.
                            // Part found.
                            *part = currentPart;
                            currentPart = NULL;
                        }
                    }
                    if (SUCCEEDED(hr) &amp;&amp; contentType == NULL)
                    {
                        // Content type not specified.
                        // Part found.
                        *part = currentPart;
                        currentPart = NULL;
                    }

                    // Release resources
                    CoTaskMemFree(static_cast<LPVOID>(currentContentType));
                    
                    if (currentPart)
                    {
                        currentPart->Release();
                        currentPart = NULL;
                    }
                }
        ```

        

    Retrieve the next relationship represented in the set and close the loop.

    ```C++
            // Get the next relationship of the specified type.
            if (SUCCEEDED(hr))
            {
                hr = packageRelsEnum->MoveNext(&amp;hasNext);
            }

            // Release resources
            if (partUri)
            {
                partUri->Release();
                partUri = NULL;
            }

            if (currentRel)
            {
                currentRel->Release();
                currentRel = NULL;
            }
        }
    
    ```

    

### `FindCorePropertiesPart` Code Details

The following code example shows the `FindCorePropertiesPart` function definition in one convenient block, found in [opclib.cpp](opclib-cpp.md).

The `FindCorePropertiesPart` function definition:


```C++
HRESULT
FindCorePropertiesPart(
    IOpcPackage *package,
    IOpcPart **part
    )
{
    return FindPartByRelationshipType(
                package,
                g_corePropertiesRelationshipType,
                g_corePropertiesContentType,
                part
                );
}
```



### `FindPartByRelationshipType` Code Details

The following shows the `FindPartByRelationshipType` function definition, which is found in the [opclib.cpp](opclib-cpp.md) file, in one convenient block.

The `FindPartByRelationshipType` function definition:


```C++
HRESULT 
FindPartByRelationshipType(
    IOpcPackage *package,
    LPCWSTR relationshipType, // Relationship type used to find the part.
    LPCWSTR contentType, // Expected content type of part (optional).
    IOpcPart **part
    )
{
    *part = NULL; // Enable checks against value of *part.

    IOpcRelationshipSet * packageRels = NULL;
    IOpcRelationshipEnumerator * packageRelsEnum = NULL;
    IOpcPartSet * partSet = NULL;
    BOOL hasNext = false;

    HRESULT hr = package->GetPartSet(&amp;partSet);
    if (SUCCEEDED(hr))
    {
        // Get package relationships stored in the package's Relationships part.
        hr = package->GetRelationshipSet(&amp;packageRels);
    }
    if (SUCCEEDED(hr))
    {
        // Get package relationships of the specified relationship type.
        hr = packageRels->GetEnumeratorForType(
                relationshipType,
                &amp;packageRelsEnum
                );
    }

    // Note: Though not performed by this sample, it may be necessary to check
    // that the number of retrieved relationships conforms to the expected
    // number of relationships specified by the format designer or in the OPC.

    if (SUCCEEDED(hr))
    {
        // Move pointer to first package relationship.
        hr = packageRelsEnum->MoveNext(&amp;hasNext);
    }

    // Find the first, arbitrary part that is the target of a relationship
    // of the specified type and has the specified content type, if a content
    // type is provided. Abandon search when an error is encountered, when
    // there are no more relationships in the enumerator, or when a part is
    // found.
    while (SUCCEEDED(hr) &amp;&amp; hasNext &amp;&amp; *part == NULL)
    {
        IOpcPartUri * partUri = NULL;
        IOpcRelationship * currentRel = NULL;
        BOOL partExists = FALSE;

        hr = packageRelsEnum->GetCurrent(&amp;currentRel);
        if (SUCCEEDED(hr))
        {
            // There was a relationship of the specified type.
            // Try to resolve the part name of the relationship's target.
            hr = ResolveTargetUriToPart(currentRel, &amp;partUri);
        }
        if (SUCCEEDED(hr))
        {
            // Part name resolved. Check that a part with that part name
            // exists in the package.
            hr = partSet->PartExists(partUri, &amp;partExists);
        }
        if (SUCCEEDED(hr) &amp;&amp; partExists)
        {
            // A part with the resolved part name exists in the package, so
            // get a pointer to that part.

            LPWSTR currentContentType = NULL;
            IOpcPart * currentPart = NULL;

            hr = partSet->GetPart(partUri, &amp;currentPart);
            if (SUCCEEDED(hr) &amp;&amp; contentType != NULL)
            {
                // Content type specified.
                // Get the content type of the part.
                hr = currentPart->GetContentType(&amp;currentContentType);

                // Compare the content type of the part with the specified
                // content type.
                if (SUCCEEDED(hr) &amp;&amp;
                    0 == wcscmp(contentType, currentContentType))
                {
                    // Part content type matches specified content type.
                    // Part found.
                    *part = currentPart;
                    currentPart = NULL;
                }
            }
            if (SUCCEEDED(hr) &amp;&amp; contentType == NULL)
            {
                // Content type not specified.
                // Part found.
                *part = currentPart;
                currentPart = NULL;
            }

            // Release resources
            CoTaskMemFree(static_cast<LPVOID>(currentContentType));
            
            if (currentPart)
            {
                currentPart->Release();
                currentPart = NULL;
            }
        }
        // Get the next relationship of the specified type.
        if (SUCCEEDED(hr))
        {
            hr = packageRelsEnum->MoveNext(&amp;hasNext);
        }

        // Release resources
        if (partUri)
        {
            partUri->Release();
            partUri = NULL;
        }

        if (currentRel)
        {
            currentRel->Release();
            currentRel = NULL;
        }
    }

    if (SUCCEEDED(hr) &amp;&amp; *part == NULL)
    {
        // Loop complete without errors and no part found.
        hr = E_FAIL;
    }

    // Release resources
    if (packageRels)
    {
        packageRels->Release();
        packageRels = NULL;
    }

    if (packageRelsEnum)
    {
        packageRelsEnum->Release();
        packageRelsEnum = NULL;
    }

    if (partSet)
    {
        partSet->Release();
        partSet = NULL;
    }

    return hr;
}
```



## Disclaimer

Code examples are not intended to be complete and working programs. The code examples that are referenced on this page, for example, do not perform parameter checking, error checking, or error handling. Use these examples as a starting point, then add the code necessary to create a robust application. For more information about error handling in COM, see the [Error Handling (COM)](https://www.bing.com/search?q=Error Handling (COM)) topic.

## Related topics

<dl> <dt>

[Parts How-To Topics](parts-how-to-topics.md)
</dt> <dt>

**Overviews**
</dt> <dt>

[Getting Started with the Packaging API](packaging-api-overview.md)
</dt> <dt>

[Parts Overview](parts-overview.md)
</dt> <dt>

[Resolving a Part Name from a Target URI](resolving-a-part-name-from-a-relationship-s-target-uri.md)
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

 

 




