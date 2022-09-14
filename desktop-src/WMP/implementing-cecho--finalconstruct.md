---
title: Implementing CEcho FinalConstruct
description: Implementing CEcho FinalConstruct
ms.assetid: 149e99c5-9f57-4447-b520-39a6dd39fc86
keywords:
- Windows Media Player plug-ins,Echo sample property pages
- plug-ins,Echo sample property pages
- digital signal processing plug-ins,Echo sample property pages
- DSP plug-ins,Echo sample property pages
- Echo DSP plug-in sample,property pages
- Echo DSP plug-in sample,CEcho FinalConstruct method
ms.topic: article
ms.date: 05/31/2018
---

# Implementing CEcho::FinalConstruct

The CEcho::FinalConstruct method is implemented in Echo.cpp. It contains code to read the property values from the registry when Windows Media Player instantiates the DSP plug-in object. This is important because it allows the user settings to persist between instances of the object, as well as between sessions. The plug-in wizard sample code provides implementation to read a single property from the registry. You can modify this code to handle the delay time property, and then add code to read the wet mix property value.

The following example code reads each property value from the registry and stores each in the correct member variable:


```CSharp
CRegKey key;
LONG    lResult;
DWORD   dwValue;

lResult = key.Open(HKEY_CURRENT_USER, kszPrefsRegKey, KEY_READ);
if (ERROR_SUCCESS == lResult)
{
    // Read the delay time from the registry. 
    lResult = key.QueryValue(dwValue, kszPrefsDelayTime );
    if (ERROR_SUCCESS == lResult)
    {
        m_dwDelayTime = dwValue;
    }

    // Read the wet mix value from the registry. 
    lResult = key.QueryValue(dwValue, kszPrefsWetmix );
    if (ERROR_SUCCESS == lResult)
    {
        // Convert the DWORD to a double.
        m_fWetMix = (double)dwValue / 100;
        // Calculate the dry mix value.
        m_fDryMix = 1.0 - m_fWetMix;
    }

}

return S_OK;
```



Notice that the DWORD value for the wet mix is converted to a floating-point value. Also note that the code calculates the correct value for m\_fDryMix.

## Related topics

<dl> <dt>

[**Modifying the Echo Sample Property Page**](modifying-the-echo-sample-property-page.md)
</dt> </dl>

 

 




