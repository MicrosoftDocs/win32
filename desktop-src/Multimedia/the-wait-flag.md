---
title: The Wait Flag
description: The Wait Flag
ms.assetid: b971ccd4-0507-4f05-adb3-d4930496034d
keywords:
- MCI_WAIT flag
ms.topic: article
ms.date: 05/31/2018
---

# The Wait Flag

MCI commands usually return to the user immediately, even if it takes several minutes to complete the action initiated by the command. You can use the "wait" (MCI\_WAIT) flag to direct the device to wait until the requested action is completed before returning control to the application.

For example, the following [**play**](play.md) command will not return control to the application until the playback completes:


```C++
mciSendString("play mydevice from 0 to 100 wait", 
    lpszReturnString, lstrlen(lpszReturnString), NULL);
```



> [!Note]  
> The user can cancel a wait operation by pressing a break key. By default, this key is CTRL+BREAK. Applications can redefine this key by using the [**break**](break.md) ([**MCI\_BREAK**](mci-break.md)) command. (**MCI\_BREAK** uses the [**MCI\_BREAK\_PARMS**](mci-break-parms.md) structure.) When a wait operation is canceled, MCI attempts to return control to the application without interrupting the command associated with the "wait" flag.

 

 

 




