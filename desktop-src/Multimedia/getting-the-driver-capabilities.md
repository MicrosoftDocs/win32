---
title: Getting the Driver Capabilities
description: Getting the Driver Capabilities
ms.assetid: 761886db-b2e5-449c-b526-6e992cc1b42f
keywords:
- joysticks,drivers
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Getting the Driver Capabilities

The following example uses [**joyGetNumDevs**](joygetnumdevs.md) and [**joyGetPos**](joygetpos.md) to determine whether the joystick services are available and if a joystick is attached to one of the ports.


```C++
JOYINFO joyinfo; 
UINT wNumDevs, wDeviceID; 
BOOL bDev1Attached, bDev2Attached; 
 
    if((wNumDevs = joyGetNumDevs()) == 0) 
        return ERR_NODRIVER; 
    bDev1Attached = joyGetPos(JOYSTICKID1,&amp;joyinfo) != JOYERR_UNPLUGGED; 
    bDev2Attached = wNumDevs == 2 &amp;&amp; joyGetPos(JOYSTICKID2,&amp;joyinfo) != 
        JOYERR_UNPLUGGED; 
    if(bDev1Attached || bDev2Attached)   // decide which joystick to use 
        wDeviceID = bDev1Attached ? JOYSTICKID1 : JOYSTICKID2; 
    else 
        return ERR_NODEVICE; 

```



 

 




