---
title: Paused States
description: During a connection operation, there can be times when the remote server cannot proceed without additional information from the local user.
ms.assetid: 'a1a36b2a-33df-4cba-85a6-f4225779cd63'
---

# Paused States

During a connection operation, there can be times when the remote server cannot proceed without additional information from the local user. Beginning with Windows NT 3.5, the [**RasDial**](rasdial.md) function supports paused states. A paused state allows the Remote Access Connection Manager to suspend a connection operation so the RAS client application can collect information from the user.

Paused states are useful in the following situations:

-   When the user needs to provide a [callback](callback-connections.md) number.
-   When the user authentication fails, the user can type in a different user name and password.
-   When the user's password has expired, the user can provide a new password.

By default, paused state support is disabled. RAS clients that want to support paused states must set the RDEOPTS\_PausedStates flag in the [**RASDIALEXTENSIONS**](rasdialextensions-str.md) structure passed as a parameter to [**RasDial**](rasdial.md).

When a paused state occurs, the Remote Access Connection Manager invokes the client's notification handler. If paused state support is disabled, the notification message indicates an error, and the connection operation fails. If it is enabled, the Connection Manager pauses the connection operation to wait for the RAS client's response. The RAS client can resume the connection operation by a second [**RasDial**](rasdial.md) call, or terminate it by calling the [**RasHangUp**](rashangup.md) function.

After getting the user's input, the RAS client restarts the connection operation by calling [**RasDial**](rasdial.md) again. This second **RasDial** call must specify the following information:

-   The connection handle that was returned by the original [**RasDial**](rasdial.md) call.
-   The same notification handler as the original [**RasDial**](rasdial.md) call.
-   The user's input in the appropriate members of the [**RASDIALPARAMS**](rasdialparams-str.md) structure. Other members of the **RASDIALPARAMS** structure should have the same information as specified in the original [**RasDial**](rasdial.md) call.

The second [**RasDial**](rasdial.md) call cannot be made from within the notification handler.

 

 




