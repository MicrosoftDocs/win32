---
title: Implementing CEchoPropPage Apply
description: Implementing CEchoPropPage Apply
ms.assetid: e887b851-e623-4ec4-8d8b-165e4b21e116
keywords:
- Windows Media Player plug-ins,Echo sample property pages
- plug-ins,Echo sample property pages
- digital signal processing plug-ins,Echo sample property pages
- DSP plug-ins,Echo sample property pages
- Echo DSP plug-in sample,property pages
- Echo DSP plug-in sample,CEchoPropPage Apply method
ms.topic: article
ms.date: 05/31/2018
---

# Implementing CEchoPropPage::Apply

The CEchoPropPage::Apply method is implemented in EchoPropPage.cpp. It executes when the user clicks **Apply** in the property page dialog box in Windows Media Player. The plug-in wizard sample code provides an implementation to handle a single property. You can modify this code for one of the Echo sample properties, and then add code to store the other property value.

## Declaring the Apply Method Variables

First, you must remove the declaration of fScaleFactor. Then, add variable declarations that you will need. The following example shows the completed variable declarations:


```
TCHAR   szStr[MAXSTRING] = { 0 };
DWORD   dwDelayTime = 1000;  // Initialize the delay time.
DWORD   dwWetmix = 50;       // Initialize a DWORD for effect level.
double  fWetmix = 0.50;      // Initialize a double for effect level.
```



## Retrieving the Values from the Property Page

You must implement code to retrieve and validate the user input. The following code example retrieves the delay time value from the IDC\_DELAYTIME edit box, and then verifies that the value is within a specified range:


```
// Get the delay time value from the dialog box.
GetDlgItemText(IDC_DELAYTIME, szStr, sizeof(szStr) / sizeof(szStr[0]));

dwDelayTime = atoi(szStr);

// Make sure delay time is valid.
if ((dwDelayTime < 10) || (dwDelayTime > 2000))
{
    if (::LoadString(_Module.GetResourceInstance(), IDS_DELAYRANGEERROR, szStr, sizeof(szStr) / sizeof(szStr[0])))
    {
        MessageBox(szStr);
    }

    return E_FAIL;
}
```



If the user input is not in the specified range, the code displays a message box. Notice the use of the string resource you created earlier for the error message.

The following example retrieves the effect level from the IDC\_WETMIX edit box and then verifies that the value is within a specified range:


```
// Get the effects level value from the dialog box.
GetDlgItemText(IDC_WETMIX, szStr, sizeof(szStr) / sizeof(szStr[0]));

dwWetmix = atoi(szStr);

// Make sure wet mix value is valid.
if ((dwWetmix < 0) || (dwWetmix > 100))
{
    if (::LoadString(_Module.GetResourceInstance(), IDS_MIXRANGEERROR, szStr, sizeof(szStr) / sizeof(szStr[0])))
    {
        MessageBox(szStr);
    }

    return E_FAIL;
}
```



## Storing the Property Values in the Registry

Next, your code must persist the new property values to the registry. The following code stores both property values:


```
// update the registry
CRegKey key;
LONG    lResult;

// Write the delay time value to the registry.
lResult = key.Create(HKEY_CURRENT_USER, kszPrefsRegKey);
if (ERROR_SUCCESS == lResult)
{
    lResult = key.SetValue( dwDelayTime , kszPrefsDelayTime );
}

// Write the wet mix value to the registry.
lResult = key.Create(HKEY_CURRENT_USER, kszPrefsRegKey);
if (ERROR_SUCCESS == lResult)
{
    lResult = key.SetValue( dwWetmix , kszPrefsWetmix );
}
```



## Updating the Echo Plug-in Property Values

The **Apply** method must inform the Echo plug-in that the property values have changed. The following code calls the property put method for each property using the interface pointer retrieved in CEchoPropPage::SetObjects:


```
// update the plug-in
if (m_spEcho)
{
    m_spEcho->put_delay(dwDelayTime);

    // Convert the wet mix value from DWORD to double.
    fWetmix = (double)dwWetmix / 100;
    m_spEcho->put_wetmix(fWetmix);
}
```



Notice that the wet mix value is converted to floating point before being passed to the plug-in.

## Disabling the Apply Button

As a final step, your code should disable Apply in the property page dialog box as a signal to the user that the values have been successfully updated. This requires the following single line of code:


```
m_bDirty = FALSE; // Tell the property page to disable Apply.
```



## Related topics

<dl> <dt>

[**Modifying the Echo Sample Property Page**](modifying-the-echo-sample-property-page.md)
</dt> </dl>

 

 




