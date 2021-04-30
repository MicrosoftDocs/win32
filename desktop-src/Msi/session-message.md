---
description: The Message method of the Session object performs any enabled logging operations and defers execution to the UI handler object associated with the engine. Logging may be selectively enabled for the various message types. See the EnableLog method.
ms.assetid: 09053700-a641-4970-bf55-d7c81f345257
title: Session.Message method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Session.Message
api_type: 
- COM
api_location: 
- Msi.dll
---

# Session.Message method

The **Message** method of the [**Session**](session-object.md) object performs any enabled logging operations and defers execution to the UI handler object associated with the engine. Logging may be selectively enabled for the various message types. See the [**EnableLog**](installer-enablelog.md) method.

If record field 0 contains a formatting string, it is used to format the data in the other fields. Else if the message is an error, warning, or user message, an attempt is made to find a message template in the Error table for the current database using the error number found in field 1 of the record for message types and return values.

## Syntax


```JScript
Session.Message(
  kind,
  record
)
```



## Parameters

<dl> <dt>

*kind* 
</dt> <dd>

The *kind* parameter is required to be one of the following values. To display a message box with push buttons and icons, calculate the value of *kind* by adding the standard message box styles used by [**MessageBox**](/windows/win32/api/winuser/nf-winuser-messagebox) and [**MessageBoxEx**](/windows/win32/api/winuser/nf-winuser-messageboxexa) to **msiMessageTypeError**, **msiMessageTypeWarning**, or **msiMessageTypeUser**. For more information see the Remarks section below.



| Constant                                                                                                                                                                                                                                                                                                                 | Meaning                                                                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="msiMessageTypeFatalExit"></span><span id="msimessagetypefatalexit"></span><span id="MSIMESSAGETYPEFATALEXIT"></span><dl> <dt>**msiMessageTypeFatalExit**</dt> <dt>&H00000000</dt> </dl>                     | Premature termination, possibly fatal out of memory.<br/>                                                                              |
| <span id="msiMessageTypeError"></span><span id="msimessagetypeerror"></span><span id="MSIMESSAGETYPEERROR"></span><dl> <dt>**msiMessageTypeError**</dt> <dt>&H01000000</dt> </dl>                                     | Formatted error message, \[1\] is message number in [Error table](error-table.md).<br/>                                               |
| <span id="msiMessageTypeWarning"></span><span id="msimessagetypewarning"></span><span id="MSIMESSAGETYPEWARNING"></span><dl> <dt>**msiMessageTypeWarning**</dt> <dt>&H02000000</dt> </dl>                             | Formatted warning message, \[1\] is message number in [Error table](error-table.md).<br/>                                             |
| <span id="msiMessageTypeUser_"></span><span id="msimessagetypeuser_"></span><span id="MSIMESSAGETYPEUSER_"></span><dl> <dt>**msiMessageTypeUser** </dt> <dt>&H03000000</dt> </dl>                                     | User request message, \[1\] is message number in [Error table](error-table.md).<br/>                                                  |
| <span id="msiMessageTypeInfo"></span><span id="msimessagetypeinfo"></span><span id="MSIMESSAGETYPEINFO"></span><dl> <dt>**msiMessageTypeInfo**</dt> <dt>&H04000000</dt> </dl>                                         | Informative message for log, not to be displayed.<br/>                                                                                 |
| <span id="msiMessageTypeFilesInUse"></span><span id="msimessagetypefilesinuse"></span><span id="MSIMESSAGETYPEFILESINUSE"></span><dl> <dt>**msiMessageTypeFilesInUse**</dt> <dt>&H05000000</dt> </dl>                 | List of files in use that need to be replaced.<br/>                                                                                    |
| <span id="msiMessageTypeResolveSource"></span><span id="msimessagetyperesolvesource"></span><span id="MSIMESSAGETYPERESOLVESOURCE"></span><dl> <dt>**msiMessageTypeResolveSource**</dt> <dt>&H06000000</dt> </dl>     | Request to determine a valid source location.<br/>                                                                                     |
| <span id="msiMessageTypeOutOfDiskSpace"></span><span id="msimessagetypeoutofdiskspace"></span><span id="MSIMESSAGETYPEOUTOFDISKSPACE"></span><dl> <dt>**msiMessageTypeOutOfDiskSpace**</dt> <dt>&H07000000</dt> </dl> | Insufficient disk space message.<br/>                                                                                                  |
| <span id="msiMessageTypeActionStart"></span><span id="msimessagetypeactionstart"></span><span id="MSIMESSAGETYPEACTIONSTART"></span><dl> <dt>**msiMessageTypeActionStart**</dt> <dt>&H08000000</dt> </dl>             | Start of action, \[1\] action name, \[2\] description, \[3\] template for ACTIONDATA messages.<br/>                                    |
| <span id="msiMessageTypeActionData"></span><span id="msimessagetypeactiondata"></span><span id="MSIMESSAGETYPEACTIONDATA"></span><dl> <dt>**msiMessageTypeActionData**</dt> <dt>&H09000000</dt> </dl>                 | Action data. Record fields correspond to the template of ACTIONSTART message.<br/>                                                     |
| <span id="msiMessageTypeProgress"></span><span id="msimessagetypeprogress"></span><span id="MSIMESSAGETYPEPROGRESS"></span><dl> <dt>**msiMessageTypeProgress**</dt> <dt>&H0A000000</dt> </dl>                         | Progress bar information. See the description of record fields below.<br/>                                                             |
| <span id="msiMessageTypeCommonData_"></span><span id="msimessagetypecommondata_"></span><span id="MSIMESSAGETYPECOMMONDATA_"></span><dl> <dt>**msiMessageTypeCommonData** </dt> <dt>&H0B000000</dt> </dl>             | To enable the Cancel button set \[1\] to 2 and \[2\] to 1. <br/> To disable the Cancel button set \[1\] to 2 and \[2\] to 0<br/> |



 

</dd> <dt>

*record* 
</dt> <dd>

Required [**Record**](record-object.md) object containing a message-specific field.

</dd> </dl>

## Return value



| Constant                                                                                              | Value         |
|-------------------------------------------------------------------------------------------------------|---------------|
| <dl> <dt>**msiMessageStatusError**</dt> </dl>  | -1<br/> |
| <dl> <dt>**msiMessageStatusNone**</dt> </dl>   | 0<br/>  |
| <dl> <dt>**msiMessageStatusOk**</dt> </dl>     | 1<br/>  |
| <dl> <dt>**msiMessageStatusCancel**</dt> </dl> | 2<br/>  |
| <dl> <dt>**msiMessageStatusAbort**</dt> </dl>  | 3<br/>  |
| <dl> <dt>**msiMessageStatusRetry**</dt> </dl>  | 4<br/>  |
| <dl> <dt>**msiMessageStatusIgnore**</dt> </dl> | 5<br/>  |
| <dl> <dt>**msiMessageStatusYes**</dt> </dl>    | 6<br/>  |
| <dl> <dt>**msiMessageStatusNo**</dt> </dl>     | 7<br/>  |



 

## Remarks

**Message Record Fields**

The following describes the record field definitions when msiMessageTypeProgress is passed as the message type.

Field 1 specifies the type of the progress message. The meaning of the other fields depend upon the value in this field. The possible values that can be set into Field 1 are as follows.



| Message name     | Value | Field 1 description                                                                                                 |
|------------------|-------|---------------------------------------------------------------------------------------------------------------------|
| MasterReset      | 0     | Resets progress bar and sets the expected total number of ticks in the bar.                                         |
| ActionInfo       | 1     | Provides information related to progress messages to be sent by the current action.                                 |
| ProgressReport   | 2     | Increments the progress bar.                                                                                        |
| ProgressAddition | 3     | Enables an action (such as CustomAction) to add ticks to the expected total number of progress of the progress bar. |



 

The meaning of Field 2 depends upon the value in Field 1 as follows.



| Field 1 value | Field 2 description                                                                                        |
|---------------|------------------------------------------------------------------------------------------------------------|
| 0             | Expected total number of ticks in the progress bar.                                                        |
| 1             | Number of ticks the progress bar moves for each ActionData message. This field is ignored if Field 3 is 0. |
| 2             | Number of ticks the progress bar has moved.                                                                |
| 3             | Number of ticks to add to total expected progress.                                                         |



 

The meaning of Field 3 depends upon the value in Field 1 as follows.



| Field 1 value | Field 3 value | Field 3 description                                                                                             |
|---------------|---------------|-----------------------------------------------------------------------------------------------------------------|
| 0             | 0             | Forward progress bar (left to right)                                                                            |
|               | 1             | Backward progress bar (right to left)                                                                           |
| 1             | 0             | The current action will send explicit ProgressReport messages.                                                  |
|               | 1             | Increment the progress bar by the number of ticks specified in Field 2 each time an ActionData message is sent. |
| 2             | Unused        |                                                                                                                 |
| 3             | Unused        |                                                                                                                 |



 

The meaning of Field 4 depends upon the value in Field 1 as follows.



| Field 1 value | Field 4 value | Field 4 description                                                                                                                                 |
|---------------|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| 0             | 0             | Execution is in progress. In this case, the UI could calculate and display the time remaining.                                                      |
|               | 1             | Creating the execution script. In this case, the UI could display a message to please wait while the installer finishes preparing the installation. |
| 1             | Unused        |                                                                                                                                                     |
| 2             | Unused        |                                                                                                                                                     |
| 3             | Unused        |                                                                                                                                                     |



 

**Displaying Message Boxes**

To display a message box with push buttons and icons, calculate the value of *kind* by adding the standard message box styles used by **MessageBox** and **MessageBoxEx** to **msiMessageTypeError**, **msiMessageTypeWarning**, or **msiTypeUser**. The available push button options for VBScript are vbOKOnly (MB\_OK), vbOKCancel (MB\_OKCANCEL), vbAbortRetryIgnore (MB\_ABORTRETRYIGNORE), vbYesNoCancel (MB\_YESNOCANCEL), vbYesNo (MB\_YESNO), and vbRetryCancel (MB\_RETRYCANCEL). The available icon options for VBScript are vbCritical (MB\_ICONERROR), vbQuestion (MB\_ICONQUESTION), vbExclamation (MB\_ICONWARNING), and vbInformation (MB\_ICONINFORMATION).

For example, the following call sends a **msiMessageTypeError** message with the vbExclamation icon and vbYesNo buttons.


```VB
Session.Message &H01000034, record
```



If a custom action calls the **Message** method, the custom action should be capable of handling a cancellation by the user and should return **msiDoActionStatusUserExit**.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                      |
| IID<br/>     | IID\_ISession is defined as 000C109E-0000-0000-C000-000000000046<br/>                                                                                                                                                                             |



 

 
