---
Description: 'Winlogon implements two time-out operations, one for secure dialog boxes and the other for screen saver activation and termination.'
ms.assetid: 'b1dfd7dc-cc00-4f1a-a157-c60b5d0f0b13'
title: 'Supported Dialog Box Service Time-out Operations'
---

# Supported Dialog Box Service Time-out Operations

[*Winlogon*](security.w_gly#-security-winlogon-gly) implements two time-out operations, one for secure dialog boxes and the other for screen saver activation and termination.

While displaying a secure dialog box, such as logon or unlocking a workstation, Winlogon can time-out the dialog boxes and return an appropriate result code to the dialog box procedure. Winlogon provides a set of dialog box support functions for the [*GINA*](security.g_gly#-security-gina-gly). The GINA must use these functions instead of their Windows counterparts to ensure that the GINA and Winlogon maintain appropriate control over the dialog boxes. Failure to use the Winlogon versions of these functions could result in unauthorized users gaining access to the system.

Winlogon dialog box services are provided by the following support functions.



| Support function                                               | Description                                                                                      |
|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [**WlxMessageBox**](wlxmessagebox.md)                         | Similar to the Windows [**MessageBox**](_win32_messagebox_cpp) function.                         |
| [**WlxDialogBox**](wlxdialogbox.md)                           | Similar to the Windows [**DialogBox**](_win32_dialogbox_cpp) function.                           |
| [**WlxDialogBoxIndirect**](wlxdialogboxindirect.md)           | Similar to the Windows [**DialogBoxIndirect**](_win32_dialogboxindirect_cpp) function.           |
| [**WlxDialogBoxParam**](wlxdialogboxparam.md)                 | Similar to the Windows [**DialogBoxParam**](_win32_dialogboxparam_cpp) function.                 |
| [**WlxDialogBoxIndirectParam**](wlxdialogboxindirectparam.md) | Similar to the Windows [**DialogBoxIndirectParam**](_win32_dialogboxindirectparam_cpp) function. |



 

GINA DLLs can also receive WLX\_WM\_SAS messages from Winlogon. These messages are sent to active dialog boxes if an [*secure attention sequence*](security.s_gly#-security-secure-attention-sequence-gly) (SAS) is received. This is useful if the GINA is in the process of prompting for the matching PIN for a [*smart card*](security.s_gly#-security-smart-card-gly), and the card is removed from the smart card [*reader*](security.r_gly#-security-reader-gly). Winlogon uses WLX\_DLG\_SAS as the EndDialog result code when an SAS event occurs during a dialog box operation.

Time-outs are also delivered in this manner. A WLX\_WM\_SAS message is sent with WLX\_SAS\_TYPE\_SCRNSVR\_TIMEOUT or WLX\_SAS\_TYPE\_TIMEOUT. The dialog box will end with an appropriate exit code to allow GINA developers to hook the time-out notifications.

GINA dialog boxes can be terminated by Winlogon by using the code WLX\_DLG\_USER\_LOGOFF. This indicates that the user has logged off during the running of the dialog box (for example, by calling the [**ExitWindowsEx**](base.exitwindowsex) function from another thread).

## Related topics

<dl> <dt>

[Initializing Winlogon](initializing-winlogon.md)
</dt> <dt>

[Winlogon States](winlogon-states.md)
</dt> <dt>

[Sending Messages to the GINA](sending-messages-to-the-gina.md)
</dt> <dt>

[Winlogon Support Functions](authentication-functions.md#winlogon-support-functions)
</dt> </dl>

 

 



