---
Description: The EmbeddedUIHandler function prototype defines a callback function exported by the embedded UI DLL that is defined in the MsiEmbeddedUI table. Call the EmbeddedUIHandler function once for each message sent to the user interface.
ms.assetid: 456b1db4-2b5b-4dfb-86a4-0bfb82490d83
title: EmbeddedUIHandler callback function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- INSTALLUI_HANDLER
api_type: 
- UserDefined
api_location: 
---

# EmbeddedUIHandler callback function

The *EmbeddedUIHandler* function prototype defines a callback function exported by the embedded UI DLL that is defined in the [MsiEmbeddedUI table](msiembeddedui-table.md). Call the *EmbeddedUIHandler* function once for each message sent to the user interface.

**[Windows Installer 4.0 and earlier](not-supported-in-windows-installer-4-0.md):** Not supported. Available beginning with Windows Installer 4.5.

## Syntax


```C++
INT CALLBACK EmbeddedUIHandler(
   UINT      uiMessageType,
   MSIHANDLE hRecord
);
```



## Parameters

<dl> <dt>

*uiMessageType* 
</dt> <dd>

Specifies a combination of one message box style, one message box icon type, one default button, and one installation message type.

Include one of the following message box styles. If no value is specified, use MB\_OK.



| Message box style                                                                                                                                                               | Meaning                                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| <span id="MB_ABORTRETRYIGNORE"></span><span id="mb_abortretryignore"></span><dl> <dt>**MB\_ABORTRETRYIGNORE**</dt> </dl> | The message box contains the **Abort**, **Retry**, and **Ignore** buttons.<br/> |
| <span id="MB_OK"></span><span id="mb_ok"></span><dl> <dt>**MB\_OK**</dt> </dl>                                           | The message box contains the **OK** button. This is the default.<br/>           |
| <span id="MB_OKCANCEL"></span><span id="mb_okcancel"></span><dl> <dt>**MB\_OKCANCEL**</dt> </dl>                         | The message box contains the **OK** and **Cancel** buttons.<br/>                |
| <span id="MB_RETRYCANCEL"></span><span id="mb_retrycancel"></span><dl> <dt>**MB\_RETRYCANCEL**</dt> </dl>                | The message box contains the **Retry** and **Cancel** buttons.<br/>             |
| <span id="MB_YESNO"></span><span id="mb_yesno"></span><dl> <dt>**MB\_YESNO**</dt> </dl>                                  | The message box contains the **Yes** and **No** buttons.<br/>                   |
| <span id="MB_YESNOCANCEL"></span><span id="mb_yesnocancel"></span><dl> <dt>**MB\_YESNOCANCEL**</dt> </dl>                | The message box contains the **Yes**, **No**, and **Cancel** buttons.<br/>      |



 

Include one of the following message box icon types. If no value is specified, use no icon.



| Message box icon type                                                                                                                                                                                                                      | Meaning                                                     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <span id="MB_ICONEXCLAMATION__MB_ICONWARNING"></span><span id="mb_iconexclamation__mb_iconwarning"></span><dl> <dt>**MB\_ICONEXCLAMATION, MB\_ICONWARNING**</dt> </dl>              | An exclamation point appears in the message box.<br/> |
| <span id="MB_ICONINFORMATION__MB_ICONASTERISK"></span><span id="mb_iconinformation__mb_iconasterisk"></span><dl> <dt>**MB\_ICONINFORMATION, MB\_ICONASTERISK**</dt> </dl>           | The information sign appears in the message box.<br/> |
| <span id="MB_ICONQUESTION"></span><span id="mb_iconquestion"></span><dl> <dt>**MB\_ICONQUESTION**</dt> </dl>                                                                        | A question mark appears in the message box.<br/>      |
| <span id="MB_ICONSTOP__MB_ICONERROR__MB_ICONHAND"></span><span id="mb_iconstop__mb_iconerror__mb_iconhand"></span><dl> <dt>**MB\_ICONSTOP, MB\_ICONERROR, MB\_ICONHAND**</dt> </dl> | A stop sign appears in the message box.<br/>          |



 

Include one of the following default buttons. If no value is specified, use MB\_DEFBUTTON1.



| Default button                                                                                                                                                | Meaning                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <span id="MB_DEFBUTTON1"></span><span id="mb_defbutton1"></span><dl> <dt>**MB\_DEFBUTTON1**</dt> </dl> | The first button is the default button.<br/>  |
| <span id="MB_DEFBUTTON2"></span><span id="mb_defbutton2"></span><dl> <dt>**MB\_DEFBUTTON2**</dt> </dl> | The second button is the default button.<br/> |
| <span id="MB_DEFBUTTON3"></span><span id="mb_defbutton3"></span><dl> <dt>**MB\_DEFBUTTON3**</dt> </dl> | The third button is the default button.<br/>  |



 

Include one of the following installation message types. There is no default installation message type; an installation message type is always specified.



| Installation message type                                                                                                                                                                                     | Meaning                                                                                                                                                                                                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="INSTALLMESSAGE_FATALEXIT"></span><span id="installmessage_fatalexit"></span><dl> <dt>**INSTALLMESSAGE\_FATALEXIT**</dt> </dl>                | Premature termination.<br/>                                                                                                                                                                                              |
| <span id="INSTALLMESSAGE_ERROR"></span><span id="installmessage_error"></span><dl> <dt>**INSTALLMESSAGE\_ERROR**</dt> </dl>                            | Formatted error message.<br/>                                                                                                                                                                                            |
| <span id="INSTALLMESSAGE_WARNING"></span><span id="installmessage_warning"></span><dl> <dt>**INSTALLMESSAGE\_WARNING**</dt> </dl>                      | Formatted warning message.<br/>                                                                                                                                                                                          |
| <span id="INSTALLMESSAGE_USER"></span><span id="installmessage_user"></span><dl> <dt>**INSTALLMESSAGE\_USER**</dt> </dl>                               | User request message.<br/>                                                                                                                                                                                               |
| <span id="INSTALLMESSAGE_INFO"></span><span id="installmessage_info"></span><dl> <dt>**INSTALLMESSAGE\_INFO**</dt> </dl>                               | Informative message for log.<br/>                                                                                                                                                                                        |
| <span id="INSTALLMESSAGE_FILESINUSE"></span><span id="installmessage_filesinuse"></span><dl> <dt>**INSTALLMESSAGE\_FILESINUSE**</dt> </dl>             | List of files currently in use that must be closed before being replaced.<br/>                                                                                                                                           |
| <span id="INSTALLMESSAGE_RESOLVESOURCE"></span><span id="installmessage_resolvesource"></span><dl> <dt>**INSTALLMESSAGE\_RESOLVESOURCE**</dt> </dl>    | Request to determine a valid source location.<br/>                                                                                                                                                                       |
| <span id="INSTALLMESSAGE_RMFILESINUSE"></span><span id="installmessage_rmfilesinuse"></span><dl> <dt>**INSTALLMESSAGE\_RMFILESINUSE**</dt> </dl>       | List of files currently in use that must be closed before being replaced. For more information about this message, see [Using Restart Manager with an External UI](using-restart-manager-with-an-external-ui-.md).<br/> |
| <span id="INSTALLMESSAGE_OUTOFDISKSPACE"></span><span id="installmessage_outofdiskspace"></span><dl> <dt>**INSTALLMESSAGE\_OUTOFDISKSPACE**</dt> </dl> | Insufficient disk space message.<br/>                                                                                                                                                                                    |
| <span id="INSTALLMESSAGE_ACTIONSTART"></span><span id="installmessage_actionstart"></span><dl> <dt>**INSTALLMESSAGE\_ACTIONSTART**</dt> </dl>          | Start of action message. This message includes the action name and description.<br/>                                                                                                                                     |
| <span id="INSTALLMESSAGE_ACTIONDATA"></span><span id="installmessage_actiondata"></span><dl> <dt>**INSTALLMESSAGE\_ACTIONDATA**</dt> </dl>             | Formatted data associated with the individual action item.<br/>                                                                                                                                                          |
| <span id="INSTALLMESSAGE_PROGRESS"></span><span id="installmessage_progress"></span><dl> <dt>**INSTALLMESSAGE\_PROGRESS**</dt> </dl>                   | Progress gauge information. This message includes information on units so far and total number of units.<br/>                                                                                                            |
| <span id="INSTALLMESSAGE_COMMONDATA"></span><span id="installmessage_commondata"></span><dl> <dt>**INSTALLMESSAGE\_COMMONDATA**</dt> </dl>             | Formatted dialog information for the user interface.<br/>                                                                                                                                                                |
| <span id="INSTALLMESSAGE_INITIALIZE"></span><span id="installmessage_initialize"></span><dl> <dt>**INSTALLMESSAGE\_INITIALIZE**</dt> </dl>             | Sent prior to UI initialization, with no string data. <br/>                                                                                                                                                              |
| <span id="INSTALLMESSAGE_TERMINATE"></span><span id="installmessage_terminate"></span><dl> <dt>**INSTALLMESSAGE\_TERMINATE**</dt> </dl>                | Sent after UI termination, with no string data. <br/>                                                                                                                                                                    |
| <span id="INSTALLMESSAGE_SHOWDIALOG"></span><span id="installmessage_showdialog"></span><dl> <dt>**INSTALLMESSAGE\_SHOWDIALOG**</dt> </dl>             | Sent prior to the display of an authored dialog box or wizard.<br/>                                                                                                                                                      |
| <span id="INSTALLMESSAGE_INSTALLSTART"></span><span id="installmessage_installstart"></span><dl> <dt>**INSTALLMESSAGE\_INSTALLSTART**</dt> </dl>       | Sent prior to installation of product.<br/>                                                                                                                                                                              |
| <span id="INSTALLMESSAGE_INSTALLEND"></span><span id="installmessage_installend"></span><dl> <dt>**INSTALLMESSAGE\_INSTALLEND**</dt> </dl>             | Sent after installation of product.<br/>                                                                                                                                                                                 |



 

</dd> <dt>

*hRecord* 
</dt> <dd>

Specifies a handle to a record that contains message data. For information about record objects, see the [Record Processing Functions](database-functions.md).

</dd> </dl>

## Return value

The *EmbeddedUIHandler* function can return the following values.



| Return code                                                                       | Description                                           |
|-----------------------------------------------------------------------------------|-------------------------------------------------------|
| <dl> <dt>**-1**</dt> </dl> | An error was found in the message handler.<br/> |
| <dl> <dt>**0**</dt> </dl>  | No action was taken.<br/>                       |



 

The following return values map to the buttons specified by the message box style:

-   IDOK
-   IDCANCEL
-   IDABORT
-   IDRETRY
-   IDIGNORE
-   IDYES
-   IDNO

## Remarks

For an example of the *EmbeddedUIHandler* function see [Using an Embedded UI](using-an-embedded-ui.md).

## Requirements



|                    |                                                                                                                                                                                                           |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.5 on Windows Server 2008, Windows Vista, Windows Server 2003, and Windows XP<br/> |
| Header<br/>  | <dl> <dt>Msi.h</dt> </dl>                                                                                                                          |



 

 




