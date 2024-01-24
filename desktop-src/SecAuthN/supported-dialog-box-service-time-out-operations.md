---
description: Winlogon implements two time-out operations, one for secure dialog boxes and the other for screen saver activation and termination.
ms.assetid: b1dfd7dc-cc00-4f1a-a157-c60b5d0f0b13
title: Supported Dialog Box Service Time-out Operations
ms.topic: article
ms.date: 05/31/2018
---

# Supported Dialog Box Service Time-out Operations

[*Winlogon*](../secgloss/w-gly.md) implements two time-out operations, one for secure dialog boxes and the other for screen saver activation and termination.

While displaying a secure dialog box, such as logon or unlocking a workstation, Winlogon can time-out the dialog boxes and return an appropriate result code to the dialog box procedure. Winlogon provides a set of dialog box support functions for the [*GINA*](../secgloss/g-gly.md). The GINA must use these functions instead of their Windows counterparts to ensure that the GINA and Winlogon maintain appropriate control over the dialog boxes. Failure to use the Winlogon versions of these functions could result in unauthorized users gaining access to the system.

Winlogon dialog box services are provided by the following support functions.



| Support function                                               | Description                                                                                      |
|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [**WlxMessageBox**](/windows/win32/api/winwlx/nc-winwlx-pwlx_message_box)                         | Similar to the Windows [**MessageBox**](/windows/win32/api/winuser/nf-winuser-messagebox) function.                         |
| [**WlxDialogBox**](/windows/win32/api/winwlx/nc-winwlx-pwlx_dialog_box)                           | Similar to the Windows [**DialogBox**](/windows/win32/api/winuser/nf-winuser-dialogboxa) function.                           |
| [**WlxDialogBoxIndirect**](/windows/win32/api/winwlx/nc-winwlx-pwlx_dialog_box_indirect)           | Similar to the Windows [**DialogBoxIndirect**](/windows/win32/api/winuser/nf-winuser-dialogboxindirecta) function.           |
| [**WlxDialogBoxParam**](/windows/win32/api/winwlx/nc-winwlx-pwlx_dialog_box_param)                 | Similar to the Windows [**DialogBoxParam**](/windows/win32/api/winuser/nf-winuser-dialogboxparama) function.                 |
| [**WlxDialogBoxIndirectParam**](/windows/win32/api/winwlx/nc-winwlx-pwlx_dialog_box_indirect_param) | Similar to the Windows [**DialogBoxIndirectParam**](/windows/win32/api/winuser/nf-winuser-dialogboxindirectparama) function. |



 

GINA DLLs can also receive WLX\_WM\_SAS messages from Winlogon. These messages are sent to active dialog boxes if an [*secure attention sequence*](../secgloss/s-gly.md) (SAS) is received. This is useful if the GINA is in the process of prompting for the matching PIN for a [*smart card*](../secgloss/s-gly.md), and the card is removed from the smart card [*reader*](../secgloss/r-gly.md). Winlogon uses WLX\_DLG\_SAS as the EndDialog result code when an SAS event occurs during a dialog box operation.

Time-outs are also delivered in this manner. A WLX\_WM\_SAS message is sent with WLX\_SAS\_TYPE\_SCRNSVR\_TIMEOUT or WLX\_SAS\_TYPE\_TIMEOUT. The dialog box will end with an appropriate exit code to allow GINA developers to hook the time-out notifications.

GINA dialog boxes can be terminated by Winlogon by using the code WLX\_DLG\_USER\_LOGOFF. This indicates that the user has logged off during the running of the dialog box (for example, by calling the [**ExitWindowsEx**](/windows/win32/api/winuser/nf-winuser-exitwindowsex) function from another thread).

## Related topics

<dl> <dt>

[Initializing Winlogon](initializing-winlogon.md)
</dt> <dt>

[Winlogon States](winlogon-states.md)
</dt> <dt>

[Sending Messages to the GINA](sending-messages-to-the-gina.md)
</dt> <dt>

[Winlogon Support Functions](authentication-functions.md)
</dt> </dl>

 

 
