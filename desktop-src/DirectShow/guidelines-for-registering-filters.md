---
description: Guidelines for Registering Filters
ms.assetid: 05945937-9e01-4930-ae95-1931a711b55e
title: Guidelines for Registering Filters
ms.topic: article
ms.date: 05/31/2018
---

# Guidelines for Registering Filters

The filter registry information determines how the Filter Graph Manager functions during [Intelligent Connect](intelligent-connect.md). Thus, it affects every application written for DirectShow, not just the ones that will use your filter. You should make sure that your filter behaves correctly, by following these guidelines.

1.  Do you need the filter data in the registry? For many custom filters, there is no reason to make the filter visible to the Filter Mapper or the System Device Enumerator. As long as you register the DLL, your application can create the filter using **CoCreateInstance**. In that case, simply omit the [**AMOVIESETUP\_FILTER**](amoviesetup-filter.md) structure from the factory template. (One drawback is that your filter will not be visible in GraphEdit. To get around this, you can create a private "Testing" category using the [**IFilterMapper2::CreateCategory**](/windows/desktop/api/Strmif/nf-strmif-ifiltermapper2-createcategory) method. You should only do this for debug builds.)
2.  Choose the correct filter category. The default "DirectShow Filters" category is for general purpose filters. Whenever appropriate, register your filter in a more specific category. When [**IFilterMapper2**](/windows/desktop/api/Strmif/nn-strmif-ifiltermapper2) searches for a filter, it ignores any category whose merit is MERIT\_DO\_NOT\_USE or less. Categories not intended for normal playback have low merit.
3.  Avoid specifying MEDIATYPE\_None, MEDIASUBTYPE\_None, or GUID\_NULL in the [**AMOVIESETUP\_MEDIATYPE**](amoviesetup-mediatype.md) information for a pin. **IFilterMapper2** treats these as wildcards, which can slow the graph-building process.
4.  Choose the lowest merit value possible. Here are some guidelines:

    | Type of filter                                                                                       | Recommended merit                                                                                   |
    |------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
    | Default renderer                                                                                     | MERIT\_PREFERRED. For standard media types, however, a custom renderer should never be the default. |
    | Non-default renderer                                                                                 | MERIT\_DO\_NOT\_USE or MERIT\_UNLIKELY                                                              |
    | Mux                                                                                                  | MERIT\_DO\_NOT\_USE                                                                                 |
    | Decoder                                                                                              | MERIT\_NORMAL                                                                                       |
    | Spitter, parser                                                                                      | MERIT\_NORMAL or lower                                                                              |
    | Special purpose filter; any filter that is created directly by the application                       | MERIT\_DO\_NOT\_USE                                                                                 |
    | Capture                                                                                              | MERIT\_DO\_NOT\_USE                                                                                 |
    | "Fallback" filter; for example, the [Color Space Converter Filter](color-space-converter-filter.md) | MERIT\_UNLIKELY                                                                                     |

    

     

    If you are giving a filter a merit of MERIT\_DO\_NOT\_USE, consider whether you need to register this information in the first place. (See item 1.)

5.  Do not register a filter in the "DirectShow Filters" category that accepts 24-bit RGB. Your filter will interfere with the Color Space Converter filter.

## Related topics

<dl> <dt>

[How to Register DirectShow Filters](how-to-register-directshow-filters.md)
</dt> </dl>

 

 



