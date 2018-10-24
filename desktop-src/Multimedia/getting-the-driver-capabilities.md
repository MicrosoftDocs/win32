---
title: Getting the Driver Capabilities
description: Getting the Driver Capabilities
ms.assetid: 761886db-b2e5-449c-b526-6e992cc1b42f
keywords:
- joysticks,drivers
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Getting the Driver Capabilities

The following example uses [**joyGetNumDevs**](https://msdn.microsoft.com/en-us/library/Dd757106(v=VS.85).aspx) and [**joyGetPos**](https://msdn.microsoft.com/en-us/library/Dd757107(v=VS.85).aspx) to determine whether the joystick services are available and if a joystick is attached to one of the ports.


```C++
JOYINFO joyinfo; 
UINT wNumDevs, wDeviceID; 
BOOL bDev1Attached, bDev2Attached; 
 
    if((wNumDevs = joyGetNumDevs()) == 0) 
        return ERR_NODRIVER; 
    bDev1Attached = joyGetPos(JOYSTICKID1,&joyinfo) != JOYERR_UNPLUGGED; 
    bDev2Attached = wNumDevs == 2 && joyGetPos(JOYSTICKID2,&joyinfo) != 
        JOYERR_UNPLUGGED; 
    if(bDev1Attached || bDev2Attached)   // decide which joystick to use 
        wDeviceID = bDev1Attached ? JOYSTICKID1 : JOYSTICKID2; 
    else 
        return ERR_NODEVICE; 

```



 

 




