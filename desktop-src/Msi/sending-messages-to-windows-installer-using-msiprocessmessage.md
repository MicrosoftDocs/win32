---
description: The messages sent using MsiProcessMessage are the same messages that are received by the INSTALLUI\_HANDLER callback function if MsiSetExternalUI was called.
ms.assetid: ca73bd0a-6f4e-453c-9e38-14cfd602d42c
title: Send Messages to Windows Installer Using MsiProcessMessage
ms.topic: article
ms.date: 05/31/2018
---

# Sending Messages to Windows Installer Using MsiProcessMessage

The messages sent using [**MsiProcessMessage**](/windows/desktop/api/Msiquery/nf-msiquery-msiprocessmessage) are the same messages that are received by the [**INSTALLUI\_HANDLER**](/windows/desktop/api/Msi/nc-msi-installui_handlera) callback function if [**MsiSetExternalUI**](/windows/desktop/api/Msi/nf-msi-msisetexternaluia) was called. Otherwise, Windows Installer handles the messages. For details, see [Parsing Windows Installer Messages](parsing-windows-installer-messages.md).

For example, to send an INSTALLMESSAGE\_ERROR message with the MB\_ICONWARNING icon and the MB\_ABORTRETRYCANCEL buttons:


```C++
PMSIHANDLE hInstall;
PMSIHANDLE hRec;
MsiProcessMessage(hInstall, INSTALLMESSAGE(INSTALLMESSAGE_ERROR|MB_ABORTRETRYIGNORE|MB_ICONWARNING), hRec);
```



Where *hInstall* is the handle to the installation, provided to a custom action or the *hProduct* handle from [**MsiOpenProduct**](/windows/desktop/api/Msi/nf-msi-msiopenproducta) or [**MsiOpenPackage**](/windows/desktop/api/Msi/nf-msi-msiopenpackagea), and *hRec* is the record containing the error information to format. For information on how formatting is performed, see [**MsiFormatRecord**](/windows/desktop/api/Msiquery/nf-msiquery-msiformatrecorda).

By default, if an INSTALLMESSAGE\_ERROR or INSTALLMESSAGE\_FATALEXIT message is sent without specifying button type or icon types, MB\_OK, no icon, and MB\_DEFBUTTON1 are used.

Windows Installer does not label the **ABORT** button with the "Abort" string when displaying a MessageBox with the MB\_ABORTRETRYIGNORE button specification, instead it labels the button with the "Cancel" string. All error messages refrain from using the word "Abort" and instead use the word "Cancel".

The *hRecord* parameter of the [**MsiProcessMessage**](/windows/desktop/api/Msiquery/nf-msiquery-msiprocessmessage) function depends upon the message type sent to the [**MsiProcessMessage**](/windows/desktop/api/Msiquery/nf-msiquery-msiprocessmessage). The following list details the requirements of the record in relation to the message type:

INSTALLMESSAGE\_FATALEXIT

 

INSTALLMESSAGE\_INFO

 

INSTALLMESSAGE\_OUTOFDISKSPACE



| Field         | Description                                                                                                                                                                                                        |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0             | Template for the formatting of the resultant string. See [**MsiFormatRecord**](/windows/desktop/api/Msiquery/nf-msiquery-msiformatrecorda) for more information. The fields of the record are referenced using \[1\] for field 1, \[2\] for field 2, etc. |
| 1 through *n* | All subsequent fields are directly related to the fields referenced by the template in field 0.                                                                                                                    |



 

If field 0 is null, the string received by the UI handler is formatted as: 1: \[data from field 1\] 2: \[data from field 2\] meaning that for each field of the record, the string contains the field number followed by the data stored in the field.

Information messages from [**MsiProcessMessage**](/windows/desktop/api/Msiquery/nf-msiquery-msiprocessmessage) are logged when [**MsiEnableLog**](/windows/desktop/api/Msi/nf-msi-msienableloga), the '/l' [command line option](command-line-options.md), or the [logging policy](logging.md) specify 'I' or INSTALLLOGMODE\_INFO.

INSTALLMESSAGE\_ERROR

 

INSTALLMESSAGE\_WARNING

 

INSTALLMESSAGE\_USER

To use a message from the Error table.



| Field         | Description                                           |
|---------------|-------------------------------------------------------|
| 0             | Must be null.                                         |
| 1             | Message number in the [Error table](error-table.md). |
| 2 through *n* | Related to the specified message in the Error table.  |



 

For example.



| Field | Type   | Data       |
|-------|--------|------------|
| 0     | string | null       |
| 1     | int    | 1304       |
| 2     | string | Myfile.txt |



 

The resulting message received from the UI handler is:

Error 1304. Error writing to file: Myfile.txt. Verify that you have access to that directory.

If field 0 is not null, the message from the error table is overridden. Instead, the field 0 template determines the format of the message.

The message may also specify the buttons, including the default button, and the icon for use with the message as mentioned above. The button and icon types are listed in [**INSTALLUI\_HANDLER**](/windows/desktop/api/Msi/nc-msi-installui_handlera).

INSTALLMESSAGE\_COMMONDATA

This message is sent to enable or disable the **Cancel** button in a progress dialog box.



| Field | Description                                                                                                                                  |
|-------|----------------------------------------------------------------------------------------------------------------------------------------------|
| 0     | Unused.                                                                                                                                      |
| 1     | 2 refers to the **Cancel** button.                                                                                                           |
| 2     | A value of 1 indicates the **Cancel** button should be visible. A value of 0 indicates the **Cancel** button should be invisible.<br/> |



 

For example, to disable or hide the **Cancel** button, the record would appear as follows.



| Field | Type   | Data |
|-------|--------|------|
| 0     | string | null |
| 1     | int    | 2    |
| 2     | int    | 0    |



 

INSTALLMESSAGE\_ACTIONSTART

 

INSTALLMESSAGE\_ACTIONDATA

The INSTALLMESSAGE\_ACTIONSTART record determines the format of the ActionData record.



| Field | Description                                                                                                   |
|-------|---------------------------------------------------------------------------------------------------------------|
| 0     | null                                                                                                          |
| 1     | Action name. The name in this field must be non-null.                                                         |
| 2     | Action description.                                                                                           |
| 3     | Action template. This is used for the ActionData whose message is being formatted according to this template. |



 

Do not reference field 0 in the Action template message.

The INSTALLMESSAGE\_ACTIONDATA record is formatted as follows.



| Field         | Description                                                                                                                                        |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| 0             | null                                                                                                                                               |
| 1 through *n* | Dependent upon field 3 of the corresponding INSTALLMESSAGE\_ACTIONSTART message or template specified in [ActionText table](actiontext-table.md). |



 

For example, the INSTALLMESSAGE\_ACTIONSTART record.



| Field | Type   | Data                                                            |
|-------|--------|-----------------------------------------------------------------|
| 0     | string | null                                                            |
| 1     | string | MyAction                                                        |
| 2     | string | This is the description of "MyAction"                           |
| 3     | string | MyAction template: field1 data is \[1\]. field 2 data is \[2\]. |



 

The template for INSTALLMESSAGE\_ACTIONSTART (field 3) references fields 1 and 2, the INSTALLMESSAGE\_ACTIONDATA record should have 2 fields containing the warranted data. The fields could be either string or integer fields.

INSTALLMESSAGE\_ACTIONDATA record.



| Field | Type   | Data                    |
|-------|--------|-------------------------|
| 0     | string | null                    |
| 1     | int    | 2                       |
| 2     | string | ActionData for MyAction |



 

INSTALLMESSAGE\_FILESINUSE

The FILESINUSE record is a variable length record.



| Field | Description                                                                                                                                                                                                                                                                                                                                                     |
|-------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0     | This field can be null. For an installation using a basic UI, this field may specify static text for display in the [ListBox control](listbox-control.md) of the [FilesInUse dialog](filesinuse-dialog.md). For an installation using a full UI, this field has no effect because the text is specified by the authoring of the custom FilesInUse dialog box. |
| 1     | Name of the file in use.                                                                                                                                                                                                                                                                                                                                        |
| 2     | This field identifies the process holding the file in use.**Windows Installer version 4.0:** The process id (PID) of the process, or the title of the window for the process.<br/> **Windows Installer version 3.1 and earlier:** This field must be the process id (PID) of the process.<br/>                                                      |



 

For example, to send a FilesInUse message showing two files in use, red.exe and blue.exe, the record has four fields plus the 0 field. The format of the record would be as shown in the following table. This example requires Windows Installer version 4.0.

**Windows Installer version 3.1 and earlier:** Fields 2 and 4 in the following example must contain the PIDs of the processes holding red.exe and blue.exe in use.



| Field | Description       |
|-------|-------------------|
| 0     | null              |
| 1     | Red.exe           |
| 2     | Red Window Title  |
| 3     | Blue.exe          |
| 4     | Blue Window Title |



 

> [!Note]  
> On Windows Installer version 4.0, if the PID passed from the service does not have a window title, such as a system tray application, the file is not be displayed and the verbose log contains the following messages.

 

``` syntax
File In Use: -<FileName>- Window could not be found. Process ID: <PID>
No window with title could be found for FilesInUse
```

INSTALLMESSAGE\_RESOLVESOURCE

The INSTALLMESSAGE\_RESOLVESOURCE record has seven fields. For INSTALLMESSAGE\_RESOLVESOURCE to work correctly, an external UI handler may not handle the INSTALLMESSAGE\_RESOLVESOURCE message. Windows Installer must handle the INSTALLMESSAGE\_RESOLVESOURCE message. That is, the external UI handler returns 0 to indicate "no action taken" when filtering the INSTALLMESSAGE\_RESOLVESOURCE message. The best practice is to avoid sending a RESOLVESOURCE message.



| Field | Description                                                                                                                                                        |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0     | null                                                                                                                                                               |
| 1     | null                                                                                                                                                               |
| 2     | Package name.                                                                                                                                                      |
| 3     | Product code.                                                                                                                                                      |
| 4     | Relative path if known, can be null.                                                                                                                               |
| 5     | 0                                                                                                                                                                  |
| 6     | Whether to validate the package code. A value of '1' indicates the package code should be validated. A value of '0' indicates the package should not be validated. |
| 7     | Required disk from media table. A value of '0' indicates that any disk is acceptable.                                                                              |



 

 

 




