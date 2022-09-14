---
description: This page lists some of the programming tasks that are commonly performed with the XPS Document API.
ms.assetid: ced2098f-5462-40d7-a728-4e53f7f41003
title: Common XPS Document Programming Tasks
ms.topic: article
ms.date: 05/31/2018
---

# Common XPS Document Programming Tasks

This page lists some of the programming tasks that are commonly performed with the XPS Document API.

## Common XPS Document Tasks

The following code examples illustrate some of the programming tasks that are commonly performed when the XPS Document API is used for working with an XPS OM.

<dl>

[Initialize an XPS OM](xps-object-model-initialization.md)  
[Create a Blank XPS OM](create-a-blank-xps-om.md)  
[Read an XPS Document into an XPS OM](read-an-xps-document-into-an-xps-om.md)  
[Navigate the XPS OM](navigate-the-xps-om.md)  
[Write Text to an XPS OM](write-text-to-an-xps-om.md)  
[Draw Graphics in an XPS OM](draw-graphics-in-an-xps-om.md)  
[Place Images in an XPS OM](place-images-in-an-xps-om.md)  
[Write an XPS OM to an XPS Document](write-an-xps-om-to-an-xps-document.md)  
[Print an XPS OM](print-an-xps-om.md)  
[Working with XPS OM Collection Interfaces](working-with-xps-object-model-collection-interfaces.md)  
</dl>

## Disclaimer

Code examples are not intended to be complete and working programs. The code examples that are referenced on this page, for example, do not perform parameter checking, error checking, or error handling. Use these examples as a starting point, and then add the code necessary to create a robust application. For more information about **HRESULT** return values and error handling strategies, see [Error Handling in COM](../com/error-handling-in-com.md).

Before XPS OM interfaces can be used, COM must be initialized in the thread, as shown in the following example code.


```C++
    HRESULT hr;
    hr = CoInitializeEx(NULL, COINIT_MULTITHREADED);
```



For clarity, these code examples use a very simple XPS OM, one that might not be complex enough for your application. As a case in point, in the code examples that add content to a page, the visual elements of a page are added directly to the page's list of visual objects; in practice, however, you might want to group visual objects into canvas objects, so that multiple objects could be acted upon as a group. Thus, to enable support of the same content for more than one page size, you could group the visual content of a page into a single canvas object, and then apply a transform to the canvas to scale it to the current page size.

## Related topics

<dl> <dt>

[Error Handling in COM](../com/error-handling-in-com.md)
</dt> <dt>

[XML Paper Specification](https://www.ecma-international.org/activities/XML%20Paper%20Specification/XPS%20Standard%20WD%201.6.pdf)
</dt> </dl>

 

 
