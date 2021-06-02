---
description: Describes how to read an existing XPS document from a file into an XPS OM.
ms.assetid: 92a8d19f-1c9e-4e02-a3d4-f2869ec871df
title: Read an XPS Document into an XPS OM
ms.topic: article
ms.date: 05/31/2018
---

# Read an XPS Document into an XPS OM

Describes how to read an existing XPS document from a file into an XPS OM.

To create an XPS OM from an XPS document, call the [**IXpsOMObjectFactory::CreatePackageFromFile**](/windows/desktop/api/xpsobjectmodel/nf-xpsobjectmodel-ixpsomobjectfactory-createpackagefromfile) method.

Before using these code examples in your program, read the disclaimer in [Common XPS Document Programming Tasks](common-xps-document-tasks.md).

## Code Example

The following code example assumes that the initialization described in [Initialize an XPS OM](xps-object-model-initialization.md) has succeeded.


```C++
    IXpsOMPackage *package = NULL;

    hr = xpsFactory->CreatePackageFromFile(
        xpsDocumentFilename,
        FALSE,
        &package);

    // package now contains a pointer to the IXpsOMPackage
    // object that has been populated with the contents
    // of the XPS document in xpsDocumentFilename.

    // When finished with the package, release the object.
    if (NULL != package) package->Release();
```



To create an XPS OM from an XPS document that is stored as a stream, call [**IXpsOMObjectFactory::CreatePackageFromStream**](/windows/desktop/api/xpsobjectmodel/nf-xpsobjectmodel-ixpsomobjectfactory-createpackagefromstream).

## Remarks

If you write an XPS OM immediately after you have read an XPS package into it, some of the original content might be lost or changed.

Some of the changes that can occur in such case are listed in the table that follows:

| Document feature                      | Action                                                             |
|---------------------------------------|--------------------------------------------------------------------|
| Digital signatures<br/>         | Removed from the document<br/>                               |
| DiscardControl part<br/>        | Removed from the document<br/>                               |
| Foreign document parts<br/>     | Removed from the document<br/>                               |
| FixedPage markup<br/>           | Modified from the original<br/>                              |
| Resource dictionary markup<br/> | Modified from the original, if Optimization flag is set<br/> |



 

## Related topics

<dl> <dt>

**Next Steps**
</dt> <dt>

[Navigate the XPS OM](navigate-the-xps-om.md)
</dt> <dt>

[Write Text to an XPS OM](write-text-to-an-xps-om.md)
</dt> <dt>

[Draw Graphics in an XPS OM](draw-graphics-in-an-xps-om.md)
</dt> <dt>

[Place Images in an XPS OM](place-images-in-an-xps-om.md)
</dt> <dt>

**Used in This Section**
</dt> <dt>

[**IXpsOMObjectFactory**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomobjectfactory)
</dt> <dt>

[**IXpsOMPackage**](/windows/desktop/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompackage)
</dt> <dt>

**For More Information**
</dt> <dt>

[Initialize an XPS OM](xps-object-model-initialization.md)
</dt> <dt>

[Packaging API](/previous-versions/windows/desktop/opc/packaging)
</dt> <dt>

[XPS Document API Reference](xps-programming-reference.md)
</dt> <dt>

[XML Paper Specification](https://www.ecma-international.org/activities/XML%20Paper%20Specification/XPS%20Standard%20WD%201.6.pdf)
</dt> </dl>

 

