---
title: Variables to Store Properties
description: Variables to Store Properties
ms.assetid: a90a6e21-00fb-46f8-96c8-654d8f205905
keywords:
- Windows Media Player plug-ins,Echo sample properties
- plug-ins,Echo sample properties
- digital signal processing plug-ins,Echo sample properties
- DSP plug-ins,Echo sample properties
- Echo DSP plug-in sample,properties
- Echo DSP plug-in sample,variables for storing properties
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Variables to Store Properties

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

First, you will need a variable to store the delay time. The default sample created by the Windows Media Player Plug-in Wizard provides a variable named m\_fScaleFactor to store the scaling multiplier it uses for processing. This sample no longer needs this variable, so you can change its name and type to store the delay time value.

1.  Replace each instance of m\_fScaleFactor in Echo.h and Echo.cpp with m\_dwDelayTime.
2.  Change the data type for m\_fScaleFactor (now m\_dwDelayTime) from double to DWORD in Echo.h.
3.  In the constructor for CEcho, change the default delay time value to 1000.
    ```C++
    m_dwDelayTime = 1000;   // Default to a delay time of 1000 ms.
    
    ```

    

Next, declare two new member variables to store the percentage of effect signal and the percentage of source signal to be mixed in the final output buffer. The term "wet" refers to the effect, and the term "dry" refers to the source signal. Add the following declarations to Echo.h:


```C++
double  m_fWetMix;    // percentage of effect
double  m_fDryMix;    // percentage of dry signal

```



These values are stored as decimal representations of percentages so they can easily be used as scale factors. For instance, a mixture of 50 percent effect and 50 percent source signal would be represented as a value of 0.50 for each variable. The sum of the values for m\_fWetMix and m\_fDryMix must not be more than 1.0 (100 percent). Eventually, these values will be accessible as properties.

Add the following code to the CEcho constructor to set the default values to 50 percent each:


```C++
m_fWetMix = 0.50;  // default to 50 percent wet
m_fDryMix = 0.50;  // default to 50 percent dry

```



## Related topics

<dl> <dt>

[**Echo Sample Properties**](echo-sample-properties.md)
</dt> </dl>

 

 




