---
title: Adding Properties to the Sample Audio DSP Plug-in
description: Adding Properties to the Sample Audio DSP Plug-in
ms.assetid: 9c6c2a34-4844-476b-8814-a95a236e75bb
keywords:
- Windows Media Player plug-ins,audio DSP
- plug-ins,audio DSP
- digital signal processing plug-ins,audio properties
- DSP plug-ins,audio properties
- audio DSP plug-ins,properties
ms.topic: article
ms.date: 05/31/2018
---

# Adding Properties to the Sample Audio DSP Plug-in

The audio DSP sample code that the Windows Media Player Plug-in Wizard generates uses a single property that represents the scale factor for the audio volume. Your plug-in may require more than one property. You can easily add properties to your DSP plug-in in Visual Studio using the following steps:

-   Define the methods in the interface definition code in the IDL file that is part of the proxy-stub project.
    -   Add the method implementations to the project's main CPP file:

    ```C++
    STDMETHODIMP CYourProject::get_color(COLORREF *pColor)
    {
        if ( NULL == pColor )
        {
            return E_POINTER;
        }

        *pColor = m_Color;

        return S_OK;
    }

    STDMETHODIMP CYourProject::put_color(COLORREF newColor)
    {
        m_Color = newColor;
        
        return S_OK;
    }
    
    ```

    

Finally, to make the properties accessible to the user, you'll want to make changes to the property page implementation.

## Related topics

<dl> <dt>

[**Implementing an Audio DSP Plug-in**](implementing-an-audio-dsp-plug-in.md)
</dt> </dl>

 

 




