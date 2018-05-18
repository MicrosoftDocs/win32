---
title: RAS Common Dialog Boxes
description: Windows provides a set of functions that display the RAS dialog boxes provided by the system.
ms.assetid: '8231511a-7339-4fbb-8a39-f643ac575856'
---

# RAS Common Dialog Boxes

Windows provides a set of functions that display the RAS dialog boxes provided by the system. These functions make it easy for applications to display a familiar user interface so that users can perform RAS tasks. For example, users can establish and monitor connections, or work with phone-book entries. Windows 95 does not currently support these functions.

The [**RasPhonebookDlg**](rasphonebookdlg.md) function displays the main **Dial-Up Networking** dialog box. From this dialog box, the user can dial, edit, or delete a selected phone-book entry, create a new phone-book entry, or specify user preferences. The **RasPhonebookDlg** function uses the [**RASPBDLG**](raspbdlg-str.md) structure to specify additional input and output parameters. For example, you can set members of the structure to control the position of the dialog box on the screen. You can use the **RASPBDLG** structure to specify a [**RasPBDlgFunc**](raspbdlgfunc.md) callback function that receives notifications of user activity while the dialog box is open. For example, RAS calls your **RasPBDlgFunc** function if the user dials, edits, creates, or deletes a phone-book entry.

You can use the [**RasDialDlg**](rasdialdlg.md) function to start a RAS connection operation without displaying the main **Dial-Up Networking** dialog box. With **RasDialDlg**, you specify a phone number or phone-book entry to call. The function displays a stream of dialog boxes that indicate the state of the connection operation. The **RasDialDlg** function uses a [**RASDIALDLG**](rasdialdlg-str.md) structure to specify additional input and output parameters, such as position of the dialog box and the phone-book subentry to call.

To display the **Dial-Up Networking** property sheet, call the [**RasMonitorDlg**](rasmonitordlg.md) function. This dialog box enables the user to monitor the status of existing connections. The **RasMonitorDlg** function uses a [**RASMONITORDLG**](rasmonitordlg-str.md) structure to specify additional input and output parameters, such as the position of the dialog box and the property sheet page to display on top.

You can call the [**RasEntryDlg**](rasentrydlg.md) function to display a property sheet for creating, editing, or copying a phone-book entry. The **RasEntryDlg** function uses a [**RASENTRYDLG**](rasentrydlg-str.md) structure to specify additional input and output parameters, such as the position of the dialog box and the type of phone-book operation.

 

 




