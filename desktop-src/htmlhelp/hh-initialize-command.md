---
title: HH\_INITIALIZE command
description: This command initializes the help system for use and must be the first HTML Help command called. It returns a cookie which must be used in the HH\_UNINITIALIZE call.
ms.assetid: 840072DA-A2F5-4593-A8ED-5D9D39EE0603
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# HH\_INITIALIZE command

This command initializes the help system for use and must be the first HTML Help command called. It returns a cookie which must be used in the [HH\_UNINITIALIZE](hh-uninitialize-command.md) call.

**HH\_INITIALIZE** configures HTML Help to run on the same thread as the calling application instead of a secondary thread by setting the global property **HH\_GPROPID\_SINGLETHREAD** to VARIANT\_TRUE. Running HTML Help on the same thread as the calling application requires the calling application to send messages to HTML Help by calling the [HH\_PRETRANSLATEMESSAGE](hh-pretranslatemessage-command.md) command.



| *pszFile*     | *dwData*                                                                                                                                                                         |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Must be NULL. | Specifies a pointer to a DWORD. This call returns a cookie that you must pass as the value of *dwData* when you call [HH\_UNINITIALIZE](hh-uninitialize-command.md).<br/> |



 

## Example


```
DWORD dwCookie = NULL;
HtmlHelp(
         NULL,
         NULL,
         HH_INITIALIZE,
         (DWORD_PTR)&amp;m_dwCookie) ; // Cookie returned by Hhctrl.ocx.
```



## Remarks

-   Call **HH\_INITIALIZE** before calling any other command and call **HH\_UNINITIALIZE** only when your application ends. You should call these commands once during the life of your application.

## Related topics

<dl> <dt>

[About Commands](about-commands.md)
</dt> <dt>

[HH\_PRETRANSLATEMESSAGE](hh-pretranslatemessage-command.md)
</dt> <dt>

[HH\_UNINITIALIZE](hh-uninitialize-command.md)
</dt> </dl>

 

 





