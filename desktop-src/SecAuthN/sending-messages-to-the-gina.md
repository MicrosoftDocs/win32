---
Description: Winlogon sends messages to the GINA while dialog boxes are displayed. These messages are all encapsulated in the WLX\_WM\_SAS message as follows.
ms.assetid: 3da1c3d2-5116-47c3-98e4-f29b33693c69
title: Sending Messages to the GINA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Sending Messages to the GINA

[*Winlogon*](https://msdn.microsoft.com/031c898b-3b4d-4b29-811a-112da37b5e3d) sends messages to the [*GINA*](https://msdn.microsoft.com/c9567a5b-bd56-4ae1-9eac-af0bb5a6842a) while dialog boxes are displayed. These messages are all encapsulated in the WLX\_WM\_SAS message as follows.



| Secure attention sequence type in wParam parameter | Description                                                                                                                                   |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| WLX\_SAS\_TYPE\_CTRL\_ALT\_DEL                     | Indicates that a CTRL+ALT+DEL key sequence was received.                                                                                      |
| WLX\_SAS\_TYPE\_SC\_INSERT                         | Indicates that a [*smart card*](https://msdn.microsoft.com/3e9d7672-2314-45c8-8178-5a0afcfd0c50) has been inserted into a compatible device. |
| WLX\_SAS\_TYPE\_SC\_REMOVE                         | Indicates that a smart card has been removed from a compatible device.                                                                        |
| WLX\_SAS\_TYPE\_USER\_LOGOFF                       | Indicates that a user requested logoff.                                                                                                       |
| WLX\_SAS\_TYPE\_SCRNSVR\_TIMEOUT                   | Indicates that the screen saver should be run due to lack of user input.                                                                      |
| WLX\_SAS\_TYPE\_TIMEOUT                            | Indicates that no user input was received within the specified time-out period.                                                               |



 

For time-outs and logoffs, Winlogon will close the dialog box after the message has been sent. This message is sent so the dialog box operation can respond in a useful manner (for example, by closing itself down if a logoff has occurred).

For input time-outs, the dialog box is closed with the code WLX\_DLG\_INPUT\_TIMEOUT.

For screen saver time-outs, the dialog box is closed with the code WLX\_DLG\_SCREEN\_SAVER\_TIMEOUT.

For logoffs, the dialog box operation is closed with the code WLX\_DLG\_USER\_LOGOFF.

## Related topics

<dl> <dt>

[Initializing Winlogon](initializing-winlogon.md)
</dt> <dt>

[Winlogon States](winlogon-states.md)
</dt> <dt>

[Supported Dialog Box Service Time-out Operations](supported-dialog-box-service-time-out-operations.md)
</dt> <dt>

[Winlogon Support Functions](authentication-functions.md)
</dt> </dl>

 

 



