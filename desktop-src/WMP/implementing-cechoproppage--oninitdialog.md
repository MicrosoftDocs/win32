---
title: Implementing CEchoPropPage OnInitDialog
description: Implementing CEchoPropPage OnInitDialog
ms.assetid: 568989b0-bc07-480f-8b5c-41bbada713f8
keywords:
- Windows Media Player plug-ins,Echo sample property pages
- plug-ins,Echo sample property pages
- digital signal processing plug-ins,Echo sample property pages
- DSP plug-ins,Echo sample property pages
- Echo DSP plug-in sample,property pages
- Echo DSP plug-in sample,CEchoPropPage OnInitDialog method
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Implementing CEchoPropPage::OnInitDialog

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **CEchoPropPage::OnInitDialog** method is implemented in EchoPropPage.cpp. It executes when the property page dialog box is invoked. The code in this method needs to retrieve the current property values and display them in the correct edit box. The plug-in wizard sample code provides an implementation for a single property. You can modify this code for one of the Echo sample properties, and then add code to retrieve the second property value.

## Declaring the OnInitDialog Method Variables

First, you must remove the declaration of fScaleFactor and replace it with the following variable declarations:


```
DWORD  dwDelayTime = 1000;    // Default delay time.
DWORD  dwWetmix = 50;         // Default wet mix DWORD.
double fWetmix =  0.50;       // Default wet mix double.
```



## Retrieving the Current Values from the Plug-in

The code should next attempt to retrieve the current property values from the Echo plug-in. The following example attempts to retrieve each property:


```
if (m_spEcho)
{
    m_spEcho->get_delay(&dwDelayTime);
    m_spEcho->get_wetmix(&fWetmix);
    // Convert wet mix from double to DWORD.
    dwWetmix = (DWORD)(fWetmix * 100);
}
```



The dialog box displays the effects level value to the user as an integer, but the plug-in stores the value as a floating-point number. Therefore, the code converts the floating-point value to a **DWORD** value.

## Retrieving the Current Values from the Registry

If the property page cannot retrieve the current values from the plug-in, it must attempt to read them from the registry. The following code reads each property value:


```
else // Otherwise, read values from registry
{
    CRegKey key;
    LONG    lResult;

    lResult = key.Open(HKEY_CURRENT_USER, kszPrefsRegKey, KEY_READ);
    if (ERROR_SUCCESS == lResult)
    {
        DWORD   dwValue = 0;

        // Read the delay time.
        lResult = key.QueryValue(dwValue, kszPrefsDelayTime );
        if (ERROR_SUCCESS == lResult)
        {
            dwDelayTime = dwValue;
        }

        // Read the wet mix value.
        lResult = key.QueryValue(dwValue, kszPrefsWetmix );
        if (ERROR_SUCCESS == lResult)
        {
            dwWetmix = dwValue;
        }
    }
}
```



Notice the use of the registry constants you created previously.

## Displaying the Values to the User

Finally, the property page must display the values in the correct edit box controls. The following example code demonstrates this:


```
 TCHAR   szStr[MAXSTRING];

// Display the delay time.
_stprintf_s(szStr, MAXSTRING, _T("%u"), dwDelayTime);
SetDlgItemText(IDC_DELAYTIME, szStr);

// Display the effect level.
_stprintf_s(szStr, MAXSTRING, _T("%u"), dwWetmix);
SetDlgItemText(IDC_WETMIX, szStr);
```



## Related topics

<dl> <dt>

[**Modifying the Echo Sample Property Page**](modifying-the-echo-sample-property-page.md)
</dt> </dl>

 

 




