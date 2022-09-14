---
description: The following table summarizes the differences between shutdown on Windows Vista and Windows XP.
ms.assetid: da7985d2-85c8-47e1-a172-c9e92f450e24
title: Shutdown Changes for Windows Vista
ms.topic: article
ms.date: 05/31/2018
---

# Shutdown Changes for Windows Vista

The following table summarizes the differences between shutdown on Windows Vista and Windows XP.



| Feature                 | Windows XP                                                                                                                                                                                                                                                                                                                                                                                | Windows Vista                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Blocking shutdown       | Applications can delay responding to [**WM\_QUERYENDSESSION**](wm-queryendsession.md) for 5 seconds, then the system allows the user to terminate the application. Applications that return **TRUE** in response to **WM\_QUERYENDSESSION** can delay responding to [**WM\_ENDSESSION**](wm-endsession.md) for 5 seconds, then the system allows the user to terminate the application. | Applications can delay responding to [**WM\_QUERYENDSESSION**](wm-queryendsession.md) for 5 seconds, then the system allows the user to continue or cancel shutdown. Applications that return **TRUE** in response to **WM\_QUERYENDSESSION** can delay responding to [**WM\_ENDSESSION**](wm-endsession.md) for 5 seconds, then the system allows the user to continue or cancel shutdown.                                                                                                      |
| Canceling shutdown      | If an application returns **FALSE** in response to [**WM\_QUERYENDSESSION**](wm-queryendsession.md), shutdown is canceled in most cases. However, no UI is displayed, so the user may not be aware that shutdown has been canceled.                                                                                                                                                      | If an application returns **FALSE** in response to [**WM\_QUERYENDSESSION**](wm-queryendsession.md), it still appears in the shutdown UI. Note that the system does not allow console applications or applications without a visible window to cancel shutdown. These applications are automatically terminated if they do not respond to **WM\_QUERYENDSESSION** or [**WM\_ENDSESSION**](wm-endsession.md) within 5 seconds or if they return **FALSE** in response to **WM\_QUERYENDSESSION**. |
| Shutdown user interface | The system displays a dialog box for each application blocking shutdown. If the user click the **End Now** button, the application is terminated. If the user clicks the **Cancel** button, shutdown is canceled and the application continues to run.                                                                                                                                    | The system displays a full-screen UI that identifies all applications blocking shutdown and their reasons for doing so (if they have registered a reason using [**ShutdownBlockReasonCreate**](/windows/desktop/api/Winuser/nf-winuser-shutdownblockreasoncreate)).                                                                                                                                                                                                                                                                    |



 

## Best Practices

-   Applications should not block shutdown. Respond to [**WM\_QUERYENDSESSION**](wm-queryendsession.md) as quickly as possible and postpone cleanup activities until processing the [**WM\_ENDSESSION**](wm-endsession.md) message.
-   Applications that must block shutdown should use the new [**ShutdownBlockReasonCreate**](/windows/desktop/api/Winuser/nf-winuser-shutdownblockreasoncreate) function to register a string that explains the reason to the user. The user can decide whether to continue or cancel shutdown.
-   Applications cannot rely on being able to block shutdown.

 

 



