---
title: Resolving a Part Name from a Target URI
description: This topic shows how to use the Packaging APIs to resolve a part name from the URI of a relationship \ 160;target.
ms.assetid: e95db16f-ac25-4936-babb-20f2afdd2f06
keywords:
- Packaging APIs,parts
- packaging,parts
- packages,parts
- parts,name resolution
- relationships,part name resolution
- ResolveTargetUriToPart function
- parts,ResolveTargetUriToPart function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Resolving a Part Name from a Target URI

This topic shows how to use the Packaging APIs to resolve a part name from the URI of a relationship target.

This topic contains the following sections.

-   [Introduction](#introduction)
-   [Resolving a Part Name from a Relationship Target URI](#resolving-a-part-name-from-a-relationship-target-uri)
    -   [Steps to Resolve a Part Name](#steps-to-resolve-a-part-name)
    -   [`ResolveTargetUriToPart` Code Details](#resolvetargeturitopart-code-details)
-   [Disclaimer](#disclaimer)
-   [Related topics](#related-topics)

## Introduction

The following code example shows the details of the `ResolveTargetUriToPart` function, which resolves a part name from the URI of a relationship's target.

`ResolveTargetUriToPart` is declared in the [opclib.h](opclib-h.md) header file and defined in the [opclib.cpp](opclib-cpp.md) implementation file of the [Set Author Sample](set-author-sample.md). For the complete program, which can load, modify, and save a package, see the Set Author Sample.

## Resolving a Part Name from a Relationship Target URI

In the following sections, the `ResolveTargetUriToPart` function checks the relationship's target mode to confirm that the target is a part. Next, the target URI and source URI of the relationship are retrieved and used to resolve the part name.

The `ResolveTargetUriToPart` function declaration from [opclib.h](opclib-h.md):


```C++
HRESULT
    ResolveTargetUriToPart(
    IOpcRelationship * relativeUri,
    IOpcPartUri **resolvedUri
    );
```



### Steps to Resolve a Part Name

1.  Declare variables that will be used to resolve the part name:

    ```C++
        IOpcUri * sourceUri = NULL;
        IUri * targetUri = NULL;
        OPC_URI_TARGET_MODE targetMode;
    ```

    

2.  Get the target mode of the relationship:

    ```C++
        // Get the target mode of the relationship.
        HRESULT hr = relationship->GetTargetMode(&amp;targetMode);
    ```

    

3.  If the target mode is external, the relationship does not target a part and the function fails:

    ```C++
        if (SUCCEEDED(hr) &amp;&amp; targetMode != OPC_URI_TARGET_MODE_INTERNAL)
        {
            // The target mode of the relationship was not internal.
            // Function fails because the relationship does not target a part
            // therefore, no part name can be resolved.
            hr = E_FAIL;
        }
    ```

    

    Relationships that target parts use the internal target mode.

4.  Get the URI of the relationship  target:

    ```C++
        if (SUCCEEDED(hr))
        {
            // Get a URI for the relationship's target. This URI might be
            // relative to the source of the relationship.
            hr = relationship->GetTargetUri(&amp;targetUri);
        }
    ```

    

    The URI that is retrieved is relative to the URI of the relationship's source.

5.  Get the URI of the relationship  source, as shown in the following code.

    ```C++
        if (SUCCEEDED(hr))
        {
            // Get the URI for the relationship's source.
            hr = relationship->GetSourceUri(&amp;sourceUri);
        }
    ```

    

    If the source of the relationship is a part, the URI retrieved will be a part name. Otherwise, the source is the package itself and the retrieved URI is the package root.

6.  Resolve the part name by calling the [**IOpcUri::CombinePartUri**](/previous-versions/windows/desktop/api/msopc/nf-msopc-iopcuri-combineparturi) method, as shown in the following code.

    ```C++
        if (SUCCEEDED(hr))
        {
            // Form the API representation of the resultant part name.
            hr = sourceUri->CombinePartUri(targetUri, resolvedUri);
        }

        // Release resources
        if (sourceUri)
        {
            sourceUri->Release();
            sourceUri = NULL;
        }

        if (targetUri)
        {
            targetUri->Release();
            targetUri = NULL;
        }
    
    ```

    

    [**IOpcUri::CombinePartUri**](/previous-versions/windows/desktop/api/msopc/nf-msopc-iopcuri-combineparturi) uses the URI in `sourceUri` as the base URI, and resolves the relative URI in `targetUri` against it.

### `ResolveTargetUriToPart` Code Details

The following code shows the `ResolveTargetUriToPart` function definition in one convenient block, found [opclib.cpp](opclib-cpp.md).

The ResolveTargetUriToPart function definition:


```C++
HRESULT
ResolveTargetUriToPart(
    IOpcRelationship *relationship,
    IOpcPartUri **resolvedUri
    )
{
    IOpcUri * sourceUri = NULL;
    IUri * targetUri = NULL;
    OPC_URI_TARGET_MODE targetMode;

    // Get the target mode of the relationship.
    HRESULT hr = relationship->GetTargetMode(&amp;targetMode);
    if (SUCCEEDED(hr) &amp;&amp; targetMode != OPC_URI_TARGET_MODE_INTERNAL)
    {
        // The target mode of the relationship was not internal.
        // Function fails because the relationship does not target a part
        // therefore, no part name can be resolved.
        hr = E_FAIL;
    }
    // Get the segments of the URI and turn it into a valid part URI.
    // The target should be resolved against the source URI of the 
    // relationship to expand relative URIs into part URIs with absolute 
    // paths.
    if (SUCCEEDED(hr))
    {
        // Get a URI for the relationship's target. This URI might be
        // relative to the source of the relationship.
        hr = relationship->GetTargetUri(&amp;targetUri);
    }
    if (SUCCEEDED(hr))
    {
        // Get the URI for the relationship's source.
        hr = relationship->GetSourceUri(&amp;sourceUri);
    }
    if (SUCCEEDED(hr))
    {
        // Form the API representation of the resultant part name.
        hr = sourceUri->CombinePartUri(targetUri, resolvedUri);
    }

    // Release resources
    if (sourceUri)
    {
        sourceUri->Release();
        sourceUri = NULL;
    }

    if (targetUri)
    {
        targetUri->Release();
        targetUri = NULL;
    }

    return hr;
}
```



## Disclaimer

Code examples are not intended to be complete and working programs. The code examples that are referenced on this page, for example, do not perform parameter checking, error checking, or error handling. Use these examples as a starting point, then add the code necessary to create robust application. For more information about error handling in COM, see the [Error Handling (COM)](https://www.bing.com/search?q=Error Handling (COM)) topic.

## Related topics

<dl> <dt>

[Parts How-To Topics](parts-how-to-topics.md)
</dt> <dt>

**Overviews**
</dt> <dt>

[Finding the Core Properties Part](finding-the-core-properties-part.md)
</dt> <dt>

[Getting Started with the Packaging API](packaging-api-overview.md)
</dt> <dt>

[Parts Overview](parts-overview.md)
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

 

 




