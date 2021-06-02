---
title: Implementing Render Sample
description: Implementing Render Sample
ms.assetid: 5791f6ea-ddad-49e6-8c6f-8093592895d4
keywords:
- visualizations,Glow sample
- custom visualizations,Glow sample
- programming guide,visualizations
- samples,Glow visualization
- Glow visualization sample
- visualizations,Render function
- custom visualizations,Render function
- Render function,Glow sample
ms.topic: article
ms.date: 05/31/2018
---

# Implementing Render Sample

The following code is used to implement the **Render** function:


```C++
STDMETHODIMP CGlow::Render(TimedLevel *pLevels, HDC hdc, RECT *prc)
{
    COLORREF mycolor;
    int mylevel = pLevels->waveform[0][0];
    
    switch (m_nPreset)
    {
    case PRESET_RED:
        {
        mycolor = RGB( mylevel, 0, 0);    
        }
        break;
    case PRESET_GREEN:
        {
        mycolor = RGB( 0, mylevel, 0);        
        }
        break;
    case PRESET_BLUE:
        {
        mycolor = RGB( 0, 0, mylevel);        
        }
        break;
    }

     HBRUSH hNewBrush = ::CreateSolidBrush( mycolor );
    ::FillRect( hdc, prc, hNewBrush );

    if (hNewBrush)
    {
        ::DeleteObject( hNewBrush );
    }

    return S_OK;
}

```



Here is an explanation of the code:

A variable named *mycolor* is used for the color of the glow and is declared with **COLORREF**. All colors should use the **COLORREF** data type.

A variable named *mylevel* is used for the audio waveform level snapshot. This value will depend on the actual power level at the moment of the snapshot.

The **switch** statement is set by the preset that the user has chosen on Windows Media Player. The choice will set *mycolor* to the desired color (red, green, or blue). However, the exact color will be determined by the audio power level. For example, if the red preset is chosen, the color will be a solid red, but it will be lighter or darker depending on the audio waveform at the moment of the snapshot. Be sure to use the **RBG** macro to create your color.

A brush is created called *hNewBrush*, and it is used to fill the *prc* rectangle provided by Windows Media Player. The drawing surface is the *hdc* device context provided by Windows Media Player.

The brush is deleted by **DeleteObject**. Always be sure to delete any pens or brushes you create.

Once the **Render** code is finished, Windows Media Player will display the *hdc* graphics in a window determined by the skin being used.

## Related topics

<dl> <dt>

[**The Glow Sample**](the-glow-sample.md)
</dt> </dl>

 

 




