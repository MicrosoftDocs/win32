---
title: RAS Common Dialog Boxes
description: Windows provides a set of functions that display the RAS dialog boxes provided by the system.
ms.assetid: 8231511a-7339-4fbb-8a39-f643ac575856
ms.topic: article
ms.date: 05/31/2018
---

# RAS Common Dialog Boxes

Windows provides a set of functions that display the RAS dialog boxes provided by the system. These functions make it easy for applications to display a familiar user interface so that users can perform RAS tasks. For example, users can establish and monitor connections, or work with phone-book entries. Windows 95 does not currently support these functions.

The [**RasPhonebookDlg**](/windows/desktop/api/Rasdlg/nf-rasdlg-rasphonebookdlga) function displays the main **Dial-Up Networking** dialog box. From this dialog box, the user can dial, edit, or delete a selected phone-book entry, create a new phone-book entry, or specify user preferences. The **RasPhonebookDlg** function uses the [**RASPBDLG**](/previous-versions/windows/desktop/legacy/aa377607(v=vs.85)) structure to specify additional input and output parameters. For example, you can set members of the structure to control the position of the dialog box on the screen. You can use the **RASPBDLG** structure to specify a [**RasPBDlgFunc**](/windows/desktop/api/Rasdlg/nc-rasdlg-raspbdlgfunca) callback function that receives notifications of user activity while the dialog box is open. For example, RAS calls your **RasPBDlgFunc** function if the user dials, edits, creates, or deletes a phone-book entry.

You can use the [**RasDialDlg**](/windows/desktop/api/Rasdlg/nf-rasdlg-rasdialdlga) function to start a RAS connection operation without displaying the main **Dial-Up Networking** dialog box. With **RasDialDlg**, you specify a phone number or phone-book entry to call. The function displays a stream of dialog boxes that indicate the state of the connection operation. The **RasDialDlg** function uses a [**RASDIALDLG**](/previous-versions/windows/desktop/legacy/aa377023(v=vs.85)) structure to specify additional input and output parameters, such as position of the dialog box and the phone-book subentry to call.

To display the **Dial-Up Networking** property sheet, call the [**RasMonitorDlg**](/previous-versions/windows/desktop/legacy/aa377584(v=vs.85)) function. This dialog box enables the user to monitor the status of existing connections. The **RasMonitorDlg** function uses a [**RASMONITORDLG**](/previous-versions/windows/desktop/legacy/aa377591(v=vs.85)) structure to specify additional input and output parameters, such as the position of the dialog box and the property sheet page to display on top.

You can call the [**RasEntryDlg**](/windows/desktop/api/Rasdlg/nf-rasdlg-rasentrydlga) function to display a property sheet for creating, editing, or copying a phone-book entry. The **RasEntryDlg** function uses a [**RASENTRYDLG**](/previous-versions/windows/desktop/legacy/aa377260(v=vs.85)) structure to specify additional input and output parameters, such as the position of the dialog box and the type of phone-book operation.

 

 