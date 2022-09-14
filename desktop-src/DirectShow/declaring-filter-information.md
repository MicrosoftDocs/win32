---
description: Declaring Filter Information
ms.assetid: ed3c1d44-ccef-4dde-819b-f5d4d3be6d1e
title: Declaring Filter Information
ms.topic: article
ms.date: 05/31/2018
---

# Declaring Filter Information

The first step is to declare the filter information, if needed. DirectShow defines the following structures for describing filters, pins, and media types:



| Structure                                               | Description             |
|---------------------------------------------------------|-------------------------|
| [**AMOVIESETUP\_FILTER**](amoviesetup-filter.md)       | Describes a filter.     |
| [**AMOVIESETUP\_PIN**](amoviesetup-pin.md)             | Describes a pin.        |
| [**AMOVIESETUP\_MEDIATYPE**](amoviesetup-mediatype.md) | Describes a media type. |



 

These structures are nested. The **AMOVEIESETUP\_FILTER** structure has a pointer to an array of **AMOVIESETUP\_PIN** structures, and each of these has a pointer to an array of **AMOVEIESETUP\_MEDIATYPE** structures. Taken together, these structures provide enough information for the [**IFilterMapper2**](/windows/desktop/api/Strmif/nn-strmif-ifiltermapper2) interface to locate a filter. They are not a complete description of a filter. For example, if the filter creates multiple instances of the same pin, you should declare only one [**AMOVIESETUP\_PIN**](amoviesetup-pin.md) structure for that pin. Also, a filter is not required to support every combination of media types that it registers; nor is required to register every media type that it supports.

Declare the set-up structures as global variables within your DLL. The following example shows a filter with one output pin:


```C++
static const WCHAR g_wszName[] = L"Some Filter";

AMOVIESETUP_MEDIATYPE sudMediaTypes[] = {
    { &MEDIATYPE_Video, &MEDIASUBTYPE_RGB24 },
    { &MEDIATYPE_Video, &MEDIASUBTYPE_RGB32 },
};

AMOVIESETUP_PIN sudOutputPin = {
    L"",            // Obsolete, not used.
    FALSE,          // Is this pin rendered?
    TRUE,           // Is it an output pin?
    FALSE,          // Can the filter create zero instances?
    FALSE,          // Does the filter create multiple instances?
    &GUID_NULL,     // Obsolete.
    NULL,           // Obsolete.
    2,              // Number of media types.
    sudMediaTypes   // Pointer to media types.
};

AMOVIESETUP_FILTER sudFilterReg = {
    &CLSID_SomeFilter,      // Filter CLSID.
    g_wszName,              // Filter name.
    MERIT_NORMAL,           // Merit.
    1,                      // Number of pin types.
    &sudOutputPin           // Pointer to pin information.
};
```



The filter name is declared as a static global variable, because it will be used again elsewhere.

## Related topics

<dl> <dt>

[How to Register DirectShow Filters](how-to-register-directshow-filters.md)
</dt> </dl>

 

 



