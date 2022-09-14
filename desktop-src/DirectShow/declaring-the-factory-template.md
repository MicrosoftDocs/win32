---
description: Declaring the Factory Template
ms.assetid: 3060c167-ea23-4061-b32a-16e750f55e6f
title: Declaring the Factory Template
ms.topic: article
ms.date: 05/31/2018
---

# Declaring the Factory Template

The next step is to declare the factory template for your filter. A factory template is a C++ class that contains information for the class factory. In your DLL, declare a global array of [**CFactoryTemplate**](cfactorytemplate.md) objects, one for each filter or COM component in your DLL. The array must be named *g\_Templates*. For more information about factory templates, see [How to Create a DirectShow Filter DLL](how-to-create-a-dll.md).

The **m\_pAMovieSetup\_Filter** member of the factory template is a pointer to the [**AMOVIESETUP\_FILTER**](amoviesetup-filter.md) structure described previously. The following example shows a factory template, using the structure given in the previous example:


```C++
CFactoryTemplate g_Templates[] = {
    {
        g_wszName,                      // Name.
        &CLSID_SomeFilter,              // CLSID.
        CSomeFilter::CreateInstance,    // Creation function.
        NULL,
        &sudFilterReg                   // Pointer to filter information.
    }
};
int g_cTemplates = sizeof(g_Templates) / sizeof(g_Templates[0]);
```



If you did not declare any filter information, **m\_pAMoveSetup\_Filter** can be **NULL**.

## Related topics

<dl> <dt>

[How to Register DirectShow Filters](how-to-register-directshow-filters.md)
</dt> </dl>

 

 



