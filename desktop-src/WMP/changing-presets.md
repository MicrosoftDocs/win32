---
title: Changing Presets
description: Changing Presets
ms.assetid: f8a5565d-676b-4679-a4cb-4bd7551cf41c
keywords:
- visualizations,Glow sample
- custom visualizations,Glow sample
- programming guide,visualizations
- samples,Glow visualization
- Glow visualization sample
- visualizations,presets
- custom visualizations,presets
- presets in visualizations,Glow sample
ms.topic: article
ms.date: 05/31/2018
---

# Changing Presets

The following preset code sections were changed to allow three presets:

## GetPresetTitle

This code was inserted in place of the generated preset code:


```C++
    switch (nPreset)
    {
    case PRESET_RED:
        bstrTemp.LoadString(IDS_REDPRESETNAME); 
        break;

    case PRESET_GREEN:
        bstrTemp.LoadString(IDS_GREENPRESETNAME); 
        break;

    case PRESET_BLUE:
        bstrTemp.LoadString(IDS_BLUEPRESETNAME); 
        break;
    }

```



## Enumerations

The following enumeration in Glow.h was changed to allow three presets:


```C++
enum {
    PRESET_RED = 0,
    PRESET_GREEN,
    PRESET_BLUE,
    PRESET_COUNT
};

```



## Resource Header

The following resources were defined in Resource.h to allow three presets:


```C++
#define IDS_REDPRESETNAME               102
#define IDS_GREENPRESETNAME             103
#define IDS_BLUEPRESETNAME              104

```



Note that you must also change the resource number of **\_APS\_NEXT\_SYMED\_VALUE** to 106.

## Resource File

The following strings must be changed in the Glowdll.rc file to allow three presets and give them names:


```C++
    IDS_REDPRESETNAME       "Glow Red"
    IDS_GREENPRESETNAME     "Glow Green"
    IDS_BLUEPRESETNAME      "Glow Blue"

```



## Related topics

<dl> <dt>

[**The Glow Sample**](the-glow-sample.md)
</dt> </dl>

 

 




