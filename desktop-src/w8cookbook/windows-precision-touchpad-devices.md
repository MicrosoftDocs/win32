---
title: Windows precision touchpad devices
description: Windows precision touchpad devices
ms.assetid: 026F9940-C985-4F3A-BDBB-2977B14EAB1F
ms.topic: article
ms.date: 05/31/2018
---

# Windows precision touchpad devices

## Platforms

<dl> Clients - Windows 8.1  
</dl>

## Description

The Windows Precision Touchpad is a new class of input devices that provide high precision pointer input and gesture functionality. By default, these devices generate ultra-high precision scroll wheel messages for desktop application consumption.

## Manifestations

Applications that are not designed to handle ultra-high precision scroll wheel messages may either over-scroll or not scroll correctly.

## Mitigation

Application developers should look at the scroll delta in mouse scroll wheel messages and modify their apps accordingly; however, in the interim an application may opt-out of ultra-high precision scroll wheel messages (delta = 1)and elect to receive high precision scroll wheel messages (delta = 40) or standard scroll wheel messages (delta = 120).

## Solution

If the application is capable of handling ultra-high precision scroll wheel messages, nothing needs to be done as this is the default message sent by Windows Precision Touchpads.

If the application is capable of handling high precision scroll wheel messages, but not ultra-high precision wheel messages, add the following to the application manifest:


```
<application xmlns="urn:schemas-microsoft-com:asm.v3">  
    <windowsSettings>  
      <highResolutionScrollingAware xmlns="http://schemas.microsoft.com/SMI/2013/WindowsSettings">true</highResolutionScrollingAware>  
  </windowsSettings>  
</application>  
```



If the application is not capable of handling either high precision scroll wheel messages or ultra-high precision wheel messages, add the following to the application manifest to indicate that standard scroll wheel messages are desired:


```
<application xmlns="urn:schemas-microsoft-com:asm.v3">  
    <windowsSettings>  
      <ultraHighResolutionScrollingAware xmlns="http://schemas.microsoft.com/SMI/2013/WindowsSettings">false</ultraHighResolutionScrollingAware >  
  </windowsSettings>  
</application>  
```



 

 




