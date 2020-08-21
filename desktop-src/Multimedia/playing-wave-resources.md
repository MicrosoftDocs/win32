---
title: Playing WAVE Resources
description: Playing WAVE Resources
ms.assetid: e6129bf4-b83f-4c38-8b96-21aed66ba605
keywords:
- waveform audio,playing WAVE resources
- auxiliary audio,playing WAVE resources
- playing WAVE resources
- PlaySound function,playing WAVE resources
- sndPlaySound function
- PlaySound function,compared to sndPlaySound function
ms.topic: article
ms.date: 05/31/2018
---

# Playing WAVE Resources

You can use the [**PlaySound**](/previous-versions//dd743680(v=vs.85)) function to play a sound that is stored as a resource. Although this is also possible using the [**sndPlaySound**](/previous-versions//dd798676(v=vs.85)) function, **sndPlaySound** requires that you find, load, lock, unlock, and free the resource; **PlaySound** achieves all of this with a single line of code.

## PlaySound Example


```C++
PlaySound("SoundName", hInst, SND_RESOURCE | SND_ASYNC); 
```



## sndPlaySound Example

The SND\_MEMORY flag indicates that the *lpszSoundName* parameter is a pointer to an in-memory image of the WAVE file. To include a WAVE file as a resource in an application, add the following entry to the application's resource script (.RC) file.


```C++
soundName WAVE c:\sounds\bells.wav 
```



The name *soundName* is a placeholder for a name that you supply to refer to this WAVE resource. WAVE resources are loaded and accessed just like other application-defined Windows resources. The PlayResource function in the following example plays a specified WAVE resource.


```C++
BOOL PlayResource(LPSTR lpName) 
{ 
    BOOL bRtn; 
    LPSTR lpRes; 
    HANDLE hResInfo, hRes; 
 
    // Find the WAVE resource. 
 
    hResInfo = FindResource(hInst, lpName, "WAVE"); 
    if (hResInfo == NULL) 
        return FALSE; 
 
    // Load the WAVE resource. 
 
    hRes = LoadResource(hInst, hResInfo); 
    if (hRes == NULL) 
        return FALSE; 
 
    // Lock the WAVE resource and play it. 
 
    lpRes = LockResource(hRes); 
    if (lpRes != NULL) { 
        bRtn = sndPlaySound(lpRes, SND_MEMORY | SND_SYNC | 
            SND_NODEFAULT); 
        UnlockResource(hRes); 
    } 
    else 
        bRtn = 0; 
 
    // Free the WAVE resource and return success or failure. 
 
    FreeResource(hRes); 
    return bRtn; 
} 
```



To play a WAVE resource by using this function, pass to the function a pointer to a string containing the name of the resource, as shown in the following example.


```C++
PlayResource("soundName"); 
```



 

 