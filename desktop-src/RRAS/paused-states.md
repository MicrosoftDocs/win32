---
title: Paused States
description: During a connection operation, there can be times when the remote server cannot proceed without additional information from the local user.
ms.assetid: a1a36b2a-33df-4cba-85a6-f4225779cd63
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Paused States

During a connection operation, there can be times when the remote server cannot proceed without additional information from the local user. Beginning with Windows NT 3.5, the [**RasDial**](/windows/win32/Ras/nf-ras-rasdiala?branch=master) function supports paused states. A paused state allows the Remote Access Connection Manager to suspend a connection operation so the RAS client application can collect information from the user.

Paused states are useful in the following situations:

-   When the user needs to provide a [callback](callback-connections.md) number.
-   When the user authentication fails, the user can type in a different user name and password.
-   When the user's password has expired, the user can provide a new password.

By default, paused state support is disabled. RAS clients that want to support paused states must set the RDEOPTS\_PausedStates flag in the [**RASDIALEXTENSIONS**](/windows/win32/Ras/?branch=master) structure passed as a parameter to [**RasDial**](/windows/win32/Ras/nf-ras-rasdiala?branch=master).

When a paused state occurs, the Remote Access Connection Manager invokes the client's notification handler. If paused state support is disabled, the notification message indicates an error, and the connection operation fails. If it is enabled, the Connection Manager pauses the connection operation to wait for the RAS client's response. The RAS client can resume the connection operation by a second [**RasDial**](/windows/win32/Ras/nf-ras-rasdiala?branch=master) call, or terminate it by calling the [**RasHangUp**](/windows/win32/Ras/nf-ras-rashangupa?branch=master) function.

After getting the user's input, the RAS client restarts the connection operation by calling [**RasDial**](/windows/win32/Ras/nf-ras-rasdiala?branch=master) again. This second **RasDial** call must specify the following information:

-   The connection handle that was returned by the original [**RasDial**](/windows/win32/Ras/nf-ras-rasdiala?branch=master) call.
-   The same notification handler as the original [**RasDial**](/windows/win32/Ras/nf-ras-rasdiala?branch=master) call.
-   The user's input in the appropriate members of the [**RASDIALPARAMS**](/windows/win32/Ras/?branch=master) structure. Other members of the **RASDIALPARAMS** structure should have the same information as specified in the original [**RasDial**](/windows/win32/Ras/nf-ras-rasdiala?branch=master) call.

The second [**RasDial**](/windows/win32/Ras/nf-ras-rasdiala?branch=master) call cannot be made from within the notification handler.

 

 




