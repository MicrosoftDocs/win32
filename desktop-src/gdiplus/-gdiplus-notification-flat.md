---
description: Notification Functions
ms.assetid: 44f69e05-1f08-48da-abb7-7e0a96c0cd26
title: Notification Functions
ms.topic: article
ms.date: 05/31/2018
---

# Notification Functions



| Flat function                                                                  | Wrapper method                            | Remarks                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GpStatus WINGDIPAPI GdiplusNotificationHook(OUT ULONG\_PTR \*token)<br/> | Not called by wrapper methods.<br/> | The [**GdiplusStartup**](/windows/desktop/api/Gdiplusinit/nf-gdiplusinit-gdiplusstartup) function returns (in its output parameter) a pointer to a [**GdiplusStartupOutput**](/windows/desktop/api/Gdiplusinit/ns-gdiplusinit-gdiplusstartupoutput) structure. One of the members of the structure is a pointer to a notification hook function that has the same signature as GdiplusNotificationHook.<br/> There are two ways you can call the notification hook function; you can use the pointer returned by [**GdiplusStartup**](/windows/desktop/api/Gdiplusinit/nf-gdiplusinit-gdiplusstartup) or you can call GdiplusNotificationHook. In fact, GdiplusNotificationHook simply verifies that you have suppressed the background thread and then calls the notification hook function that is returned by **GdiplusStartup**.<br/> The token parameter receives an identifier that you should later pass in a corresponding call to the notification unhook function.<br/>                                                                                                                                         |
| VOID WINGDIPAPI GdiplusNotificationUnhook(ULONG\_PTR token)<br/>         | Not called by wrapper methods.<br/> | The [**GdiplusStartup**](/windows/desktop/api/Gdiplusinit/nf-gdiplusinit-gdiplusstartup) function returns (in its output parameter) a pointer to a [**GdiplusStartupOutput**](/windows/desktop/api/Gdiplusinit/ns-gdiplusinit-gdiplusstartupoutput) structure. One of the members of the structure is a pointer to a notification unhook function that has the same signature as GdiplusNotificationUnhook.<br/> There are two ways you can call the notification unhook function; you can use the pointer returned by [**GdiplusStartup**](/windows/desktop/api/Gdiplusinit/nf-gdiplusinit-gdiplusstartup) or you can call GdiplusNotificationUnhook. In fact, GdiplusNotificationUnhook simply verifies that you have suppressed the background thread and then calls the notification unhook function that is returned by **GdiplusStartup**.<br/> When you call the notification unhook function, pass the token that you previously received from a corresponding call to the notification hook function. If you do not do this, there will be resource leaks that won't be cleaned up until the process exits.<br/> |



 

 

 




