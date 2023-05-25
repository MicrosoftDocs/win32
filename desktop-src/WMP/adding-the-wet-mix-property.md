---
title: Adding the Wet Mix Property
description: Adding the Wet Mix Property
ms.assetid: 4605d893-8ac0-42fd-a1ac-51430561f174
keywords:
- Windows Media Player plug-ins,Echo sample properties
- plug-ins,Echo sample properties
- digital signal processing plug-ins,Echo sample properties
- DSP plug-ins,Echo sample properties
- Echo DSP plug-in sample,properties
- Echo DSP plug-in sample,wet mix property
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Adding the Wet Mix Property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You must add the code to provide the additional property for the effect level.

The section [Adding Properties to the Sample Audio DSP Plug-in](adding-properties-to-the-sample-audio-dsp-plug-in.md) provides details about how to add a new property using Visual C++. This section shows you how to add the code manually. This entails adding code in the same three places where you modified the code for the delay time property.

Add the prototypes for the get\_wetmix and put\_wetmix methods immediately following the other property method prototypes in Echo.h. Use the following syntax:


```C++
STDMETHOD(get_wetmix)(double *pVal);
STDMETHOD(put_wetmix)(double newVal);

```



Now, add the implementation for each method immediately following the other property implementations in Echo.cpp. The following example shows the code for both methods:


```C++
// Property get to retrieve the wet mix value by using the public interface.
STDMETHODIMP CEcho::get_wetmix(double *pVal)
{
    if ( NULL == pVal )
    {
        return E_POINTER;
    }

    *pVal = m_fWetMix;

    return S_OK;
}

// Property put to store the wet mix value by using the public interface.
STDMETHODIMP CEcho::put_wetmix(double newVal)
{
    m_fWetMix = newVal;

    // Calculate m_fDryMix
    m_fDryMix = 1.0 - m_fWetMix;
    
    return S_OK;
}

```



Notice that the implementation of put\_wetmix includes the code to calculate the correct value for m\_fDryMix. Each time a new value is specified for m\_fWetMix, this calculation is required.

Add the following code in the interface definition just after the code for the delay methods in Echo.idl:


```C++
HRESULT get_wetmix([out] double *pVal);
HRESULT put_wetmix([in] double newVal);

```



## Related topics

<dl> <dt>

[**Echo Sample Properties**](echo-sample-properties.md)
</dt> </dl>

 

 




