---
description: This program checks the presence and configuration of the MicrosoftTablet PC and Touch Technology core components.
ms.assetid: 0b379dc9-a86f-40c0-9403-d9c9091ca8c3
title: Tablet PC Platform Info Sample
ms.topic: article
ms.date: 05/31/2018
---

# Tablet PC Platform Info Sample

This program checks the presence and configuration of the MicrosoftTablet PC and Touch Technology core components. It determines whether Tablet PC components are enabled in the operating system, listing names and version information for core controls and the default handwriting and speech recognizer.

The application uses the GetSystemMetrics Windows API, passing in SM\_TABLETPC, to determine whether the application running on a Tablet PC. SM\_TABLETPC is defined in WinUser.h.

Of particular interest is the way the application uses the Recognizers collection to provide information about the default recognizer. Before attempting to use the Recognizers collection and Recognizer object, the application tests for their successful creation.

## Components

Using the re-distributable merge module, certain parts of the Tablet PC Platform API may be installed on non-Tablet versions of Vista and Windows XP Professional . The GetSystemMetrics call only indicates that Windows XP Tablet PC Edition is installed. An application should always determine if a given component is available. The proper way to determine if a component of the API is installed is to attempt to create an instance of an object or control and check that it exists before attempting to use it, as shown in the following example.


```C++
IInkRecognizers* pIInkRecognizers = NULL;
HRESULT hr = CoCreateInstance(CLSID_InkRecognizers,
                              NULL, 
                              CLSCTX_INPROC_SERVER, 
                              IID_IInkRecognizers, 
                              (void **)&pIInkRecognizers);
if (SUCCEEDED(hr)) 
{
  // use the component
} else
{
  // component unavailable
}
```



The application finds out about the installed speech components by looking in the appropriate registry key:


```C++
const WCHAR* gc_wszSpeechKey = L"Software\\Microsoft\\Speech\\Recognizers";
//...
if (RegOpenKeyExW(HKEY_LOCAL_MACHINE, gc_wszSpeechKey, 0, KEY_READ, 
                  &hkeySpeech) == ERROR_SUCCESS) 
```



The key is read using RegQueryValueExW.

Finally, the sample finds out which controls are installed.


```C++
LPCOLESTR gc_wszProgId[NUM_CONTROLS] = {L"InkEd.InkEdit", L"msinkaut.InkOverlay"};
// ...
for (int i = 0, j = 0; i < NUM_CONTROLS; i++)
{
    // Get the component info
    CLSID clsid;
    if (SUCCEEDED(CLSIDFromProgID(gc_wszProgId[i], &clsid)) && GetComponentInfo(clsid, info) == TRUE)
    {
        SetDlgItemTextW(hwnd, gc_uiCtrlId[j][0], info.wchName);
        SetDlgItemTextW(hwnd, gc_uiCtrlId[j][1], info.wchVersion);
        j++;
    }
}
```



 

 



