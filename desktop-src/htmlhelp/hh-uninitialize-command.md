---
title: HH\_UNINITIALIZE command
description: HH\_UNINITIALIZE command
ms.assetid: FFE44D4D-C1E6-4469-AB5B-16F029E87F2C
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# HH\_UNINITIALIZE command

This command is called to properly shut down HTML Help. This function should be the last help command the application calls. **HH\_UNINITIALIZE** should not be called during DLL process detach, but during the normal application shutdown process.



| *pszFile*     | *dwData*                                                                                        |
|---------------|-------------------------------------------------------------------------------------------------|
| Must be NULL. | Specifies a cookie. This is the cookie returned by [HH\_INITIALIZE](hh-initialize-command.md). |



 

## Example


```
HtmlHelp(
         NULL,
         NULL,
         HH_UNINITIALIZE,
         (DWORD)dwCookie) ; // Pass in cookie.
```



## Remarks

-   Call **HH\_INITIALIZE** before calling any other command and call **HH\_UNINITIALIZE** only when your application ends. You should call these commands once during the life of your application.
-   Do not call **HH\_UNINITIALIZE** before or at process detach.

## Related topics

<dl> <dt>

[About Commands](about-commands.md)
</dt> <dt>

[HH\_INITIALIZE](hh-initialize-command.md)
</dt> </dl>

 

 




