---
title: Configuring Compressors and Decompressors
description: Configuring Compressors and Decompressors
ms.assetid: 9cd63470-1591-4de0-b011-d7979539d936
keywords:
- video compression manager (VCM),configuring compressors
- VCM (video compression manager),configuring compressors
- ICQueryConfigure macro
ms.topic: article
ms.date: 05/31/2018
---

# Configuring Compressors and Decompressors

The following example uses the [**ICQueryConfigure**](/windows/desktop/api/Vfw/nf-vfw-icqueryconfigure) macro to demonstrate how to test whether a compressor supports the configuration dialog box and to display it if it does.


```C++
// If the compressor handles a configuration dialog box, display it 
// using our application window as the parent window. 

if (ICQueryConfigure(hIC)) ICConfigure(hIC, hwndApp); 
 
```



The following example shows how to obtain the state data using the [**ICGetState**](/windows/desktop/api/Vfw/nf-vfw-icgetstate) macro.


```C++
dwStateSize = ICGetStateSize(hIC);    // gets size of buffer required 
h = GlobalAlloc(GHND, dwStateSize);   // allocates buffer 
ICGetState(hIC, (LPVOID)lpData, dwStateSize);  // gets the state data 
 
// Store the state data as required. 
 
```



The following example shows how to restore state data using the [**ICSetState**](/windows/desktop/api/Vfw/nf-vfw-icsetstate) macro. State data restored by applications should not contain any changes to the state data obtained from a driver.


```C++
ICSetState(hIC, (LPVOID)lpData, dwStateSize); // sets new state data 
 
```



 

 




