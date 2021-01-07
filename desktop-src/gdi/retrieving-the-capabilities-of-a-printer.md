---
description: Not every output device supports the entire set of graphics functions.
ms.assetid: 7989d393-7be4-47fc-af8d-26dd549c48be
title: Retrieving the Capabilities of a Printer
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving the Capabilities of a Printer

Not every output device supports the entire set of graphics functions. For example, because of hardware limitations, most vector plotters do not support bit-block transfers. An application can determine whether a device supports a particular graphics function by calling the [**GetDeviceCaps**](/windows/desktop/api/Wingdi/nf-wingdi-getdevicecaps) function, specifying the appropriate index, and examining the return value.

The following example shows how an application tests a printer to determine whether it supports bit-block transfers.


```C++
// Examine the raster capabilities of the device  
// identified by hdcPrint to verify that it supports  
// the BitBlt function.  
 
if ((GetDeviceCaps(hdcPrint, RASTERCAPS) 
       & RC_BITBLT) == 0) 
{ 
   DeleteDC(hdcPrint); 
   break; 
} 

else 
{ 
    // Print the bitmap using the printer DC.  
}
```



 

 



