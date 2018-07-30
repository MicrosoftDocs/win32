---
Description: Winlogon implements two time-out operations, one for secure dialog boxes and the other for screen saver activation and termination.
ms.assetid: b1dfd7dc-cc00-4f1a-a157-c60b5d0f0b13
title: Supported Dialog Box Service Time-out Operations
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Supported Dialog Box Service Time-out Operations

[*Winlogon*](https://msdn.microsoft.com/en-us/library/ms721635(v=VS.85).aspx) implements two time-out operations, one for secure dialog boxes and the other for screen saver activation and termination.

While displaying a secure dialog box, such as logon or unlocking a workstation, Winlogon can time-out the dialog boxes and return an appropriate result code to the dialog box procedure. Winlogon provides a set of dialog box support functions for the [*GINA*](https://msdn.microsoft.com/en-us/library/ms721584(v=VS.85).aspx). The GINA must use these functions instead of their Windows counterparts to ensure that the GINA and Winlogon maintain appropriate control over the dialog boxes. Failure to use the Winlogon versions of these functions could result in unauthorized users gaining access to the system.

Winlogon dialog box services are provided by the following support functions.



| Support function                                               | Description                                                                                      |
|----------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [**WlxMessageBox**](https://msdn.microsoft.com/en-us/library/Aa380573(v=VS.85).aspx)                         | Similar to the Windows [**MessageBox**](https://msdn.microsoft.com/library/ms645505(v=VS.85).aspx) function.                         |
| [**WlxDialogBox**](https://msdn.microsoft.com/en-us/library/Aa380554(v=VS.85).aspx)                           | Similar to the Windows [**DialogBox**](https://msdn.microsoft.com/library/ms645452(v=VS.85).aspx) function.                           |
| [**WlxDialogBoxIndirect**](https://msdn.microsoft.com/en-us/library/Aa380556(v=VS.85).aspx)           | Similar to the Windows [**DialogBoxIndirect**](https://msdn.microsoft.com/library/ms645457(v=VS.85).aspx) function.           |
| [**WlxDialogBoxParam**](https://msdn.microsoft.com/en-us/library/Aa380558(v=VS.85).aspx)                 | Similar to the Windows [**DialogBoxParam**](https://msdn.microsoft.com/library/ms645465(v=VS.85).aspx) function.                 |
| [**WlxDialogBoxIndirectParam**](https://msdn.microsoft.com/en-us/library/Aa380557(v=VS.85).aspx) | Similar to the Windows [**DialogBoxIndirectParam**](https://msdn.microsoft.com/library/ms645461(v=VS.85).aspx) function. |



 

GINA DLLs can also receive WLX\_WM\_SAS messages from Winlogon. These messages are sent to active dialog boxes if an [*secure attention sequence*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx) (SAS) is received. This is useful if the GINA is in the process of prompting for the matching PIN for a [*smart card*](https://msdn.microsoft.com/en-us/library/ms721625(v=VS.85).aspx), and the card is removed from the smart card [*reader*](https://msdn.microsoft.com/en-us/library/ms721604(v=VS.85).aspx). Winlogon uses WLX\_DLG\_SAS as the EndDialog result code when an SAS event occurs during a dialog box operation.

Time-outs are also delivered in this manner. A WLX\_WM\_SAS message is sent with WLX\_SAS\_TYPE\_SCRNSVR\_TIMEOUT or WLX\_SAS\_TYPE\_TIMEOUT. The dialog box will end with an appropriate exit code to allow GINA developers to hook the time-out notifications.

GINA dialog boxes can be terminated by Winlogon by using the code WLX\_DLG\_USER\_LOGOFF. This indicates that the user has logged off during the running of the dialog box (for example, by calling the [**ExitWindowsEx**](https://msdn.microsoft.com/en-us/library/Aa376868(v=VS.85).aspx) function from another thread).

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

 

 



