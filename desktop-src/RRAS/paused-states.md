---
title: Paused States
description: During a connection operation, there can be times when the remote server cannot proceed without additional information from the local user.
ms.assetid: a1a36b2a-33df-4cba-85a6-f4225779cd63
ms.topic: article
ms.date: 05/31/2018
---

# Paused States

During a connection operation, there can be times when the remote server cannot proceed without additional information from the local user. Beginning with Windows NT 3.5, the [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) function supports paused states. A paused state allows the Remote Access Connection Manager to suspend a connection operation so the RAS client application can collect information from the user.

Paused states are useful in the following situations:

-   When the user needs to provide a [callback](callback-connections.md) number.
-   When the user authentication fails, the user can type in a different user name and password.
-   When the user's password has expired, the user can provide a new password.

By default, paused state support is disabled. RAS clients that want to support paused states must set the RDEOPTS\_PausedStates flag in the [**RASDIALEXTENSIONS**](/previous-versions/windows/desktop/legacy/aa377029(v=vs.85)) structure passed as a parameter to [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala).

When a paused state occurs, the Remote Access Connection Manager invokes the client's notification handler. If paused state support is disabled, the notification message indicates an error, and the connection operation fails. If it is enabled, the Connection Manager pauses the connection operation to wait for the RAS client's response. The RAS client can resume the connection operation by a second [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) call, or terminate it by calling the [**RasHangUp**](/windows/desktop/api/Ras/nf-ras-rashangupa) function.

After getting the user's input, the RAS client restarts the connection operation by calling [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) again. This second **RasDial** call must specify the following information:

-   The connection handle that was returned by the original [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) call.
-   The same notification handler as the original [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) call.
-   The user's input in the appropriate members of the [**RASDIALPARAMS**](/previous-versions/windows/desktop/legacy/aa377238(v=vs.85)) structure. Other members of the **RASDIALPARAMS** structure should have the same information as specified in the original [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) call.

The second [**RasDial**](/windows/desktop/api/Ras/nf-ras-rasdiala) call cannot be made from within the notification handler.

 

 