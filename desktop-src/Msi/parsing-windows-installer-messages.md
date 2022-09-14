---
description: An external UI handler can process the list of installer messages specified by the dwMessagedFilter parameter of the MsiSetExternalUI function.
ms.assetid: c4405803-9abd-40f4-9090-c075e7dcf293
title: Parsing Windows Installer Messages
ms.topic: article
ms.date: 05/31/2018
---

# Parsing Windows Installer Messages

An external UI handler can process the list of installer messages specified by the *dwMessagedFilter* parameter of the [**MsiSetExternalUI**](/windows/desktop/api/Msi/nf-msi-msisetexternaluia) function. Some of these messages contain strings that can be used directly, and other messages may need to be parsed and processed by the external UI handler to be useful. Your external UI handler may only need to monitor Windows Installer messages without performing any operation that affects the installation.

The following Windows Installer messages contain strings that can be displayed by a dialog box and need no additional processing. These messages contain a list of buttons and icons that are to be displayed by a dialog box. You can use the **MB\_ICONMASK**, **MB\_DEFMASK**, and **MB\_TYPEMASK** values to specify icons and buttons.

<dl> <dt>

<span id="INSTALLMESSAGE_FATALEXIT"></span><span id="installmessage_fatalexit"></span>**INSTALLMESSAGE\_FATALEXIT**
</dt> <dd>

Premature termination of installation has occurred.

</dd> <dt>

<span id="INSTALLMESSAGE_ERROR"></span><span id="installmessage_error"></span>**INSTALLMESSAGE\_ERROR**
</dt> <dd>

Formatted error message.

</dd> <dt>

<span id="INSTALLMESSAGE_WARNING"></span><span id="installmessage_warning"></span>**INSTALLMESSAGE\_WARNING**
</dt> <dd>

Formatted warning message.

</dd> <dt>

<span id="INSTALLMESSAGE_INFO"></span><span id="installmessage_info"></span>**INSTALLMESSAGE\_INFO**
</dt> <dd>

Formatted log message.

</dd> <dt>

<span id="INSTALLMESSAGE_USER"></span><span id="installmessage_user"></span>**INSTALLMESSAGE\_USER**
</dt> <dd>

Formatted user message.

</dd> <dt>

<span id="INSTALLMESSAGE_OUTOFDISKSPACE"></span><span id="installmessage_outofdiskspace"></span>**INSTALLMESSAGE\_OUTOFDISKSPACE**
</dt> <dd>

Formatted message indicating an out of disk space condition

</dd> </dl>

The external user handler can use the following Windows Installer messages to monitor a sequence of the Windows Installer UI. The installer sends these messages at the start of a Windows Installer UI sequence, as each dialog box is displayed, and at the end of the UI sequence. No processing is required to use these messages.

<dl> <dt>

<span id="INSTALLMESSAGE_TERMINATE"></span><span id="installmessage_terminate"></span>INSTALLMESSAGE\_TERMINATE
</dt> <dd>

This message indicates the end of the UI sequence. The string is a null string.

</dd> <dt>

<span id="INSTALLMESSAGE_INITIALIZE"></span><span id="installmessage_initialize"></span>INSTALLMESSAGE\_INITIALIZE
</dt> <dd>

This message indicates that the UI sequence has started. The string is a null string.

</dd> <dt>

<span id="INSTALLMESSAGE_SHOWDIALOG"></span><span id="installmessage_showdialog"></span>INSTALLMESSAGE\_SHOWDIALOG
</dt> <dd>

The string contains the name of the current dialog box.

</dd> </dl>

The following Windows Installer messages require additional processing by the external UI handler.

<dl> <dt>

<span id="INSTALLMESSAGE_RESOLVESOURCE"></span><span id="installmessage_resolvesource"></span>**INSTALLMESSAGE\_RESOLVESOURCE**
</dt> <dd>

The external user interface handler must return 0 and allow Windows Installer to handle the message. The external user interface handler can monitor for this message, but it should not perform any action that affects the installation .

</dd> <dt>

<span id="INSTALLMESSAGE_FILESINUSE"></span><span id="installmessage_filesinuse"></span>**INSTALLMESSAGE\_FILESINUSE**
</dt> <dd>

The external UI should display a [FilesInUse dialog](filesinuse-dialog.md) in response to this message.

</dd> <dt>

<span id="INSTALLMESSAGE_RMFILESINUSE"></span><span id="installmessage_rmfilesinuse"></span>**INSTALLMESSAGE\_RMFILESINUSE**
</dt> <dd>

The external UI should display a [MsiRMFilesInUse dialog](msirmfilesinuse-dialog.md) in response to this message. Available beginning with Windows Installer version 4.0. For more information about this message see [Using Restart Manager with an External UI](using-restart-manager-with-an-external-ui-.md).

</dd> <dt>

<span id="INSTALLMESSAGE_ACTIONSTART"></span><span id="installmessage_actionstart"></span>**INSTALLMESSAGE\_ACTIONSTART**
</dt> <dd>

This message gives information about the current action. The format is Action \[1\]: \[2\]. \[3\], where a colon is used to separate Field 1 and Field 2 and a period is used to separate Field 2 and Field 3. Field \[1\] contains the time the action was started using the [**Time**](time.md) property format. Field \[2\] contains the action's name from the sequence table. Field \[3\] gives the action's description from the [ActionText table](actiontext-table.md) or from the [**MsiProcessMessage**](/windows/desktop/api/Msiquery/nf-msiquery-msiprocessmessage) function.

</dd> <dt>

<span id="INSTALLMESSAGE_ACTIONDATA"></span><span id="installmessage_actiondata"></span>**INSTALLMESSAGE\_ACTIONDATA**
</dt> <dd>

The format of this string is specified by the [Template](template.md) value provided in the [ActionText table](actiontext-table.md) or by the [**MsiProcessMessage**](/windows/desktop/api/Msiquery/nf-msiquery-msiprocessmessage) function. There can be an unlimited number of **INSTALLMESSAGE\_ACTIONDATA** messages after the **INSTALLMESSAGE\_ACTIONSTART** message.

</dd> <dt>

<span id="INSTALLMESSAGE_COMMONDATA"></span><span id="installmessage_commondata"></span>**INSTALLMESSAGE\_COMMONDATA**
</dt> <dd>

This message has three subtypes: Language, Caption, and CancelShow. The string can have three fields delimited by a number followed by a colon. Not all fields are required. The message can be a NULL or empty ("") string.

<dl> <dt>

<span id="Language"></span><span id="language"></span><span id="LANGUAGE"></span>Language
</dt> <dd>

Field 1 contains the value 0 to indicate this string contains language information. Field 2 contains a [Language](language.md) value that is a numeric language identifier (LANGID.) Field 3 is a value that represents an ANSI code page.

</dd> <dt>

<span id="Caption"></span><span id="caption"></span><span id="CAPTION"></span>Caption
</dt> <dd>

Field 1 contains the value 1 to indicate this string contains the text of a caption or title. Field 2 contains text that an external UI handler can use as a caption of title for a dialog box. Field 3 is NULL or an empty ("") string. Field 3 can be absent from a the Caption message.

</dd> <dt>

<span id="CancelShow"></span><span id="cancelshow"></span><span id="CANCELSHOW"></span>CancelShow
</dt> <dd>

Field 1 contains the value 2 to indicate this string contains information about whether to display the cancel button. If the cancel button should be hidden, Field 2 contains the value 0. If the cancel button should be visible, Field 2 contains the value 1.

</dd> </dl> </dd> <dt>

<span id="INSTALLMESSAGE_PROGRESS"></span><span id="installmessage_progress"></span>INSTALLMESSAGE\_PROGRESS
</dt> <dd>

This message has four subtypes: Reset, ActionInfo, ProgressReport, and ProgressAddition. The external handler should not act upon any of these messages until the first a Reset progress message is received. This provides an estimate of the total number of ticks for the progress bar.

<dl> <dt>

<span id="Reset"></span><span id="reset"></span><span id="RESET"></span>Reset
</dt> <dd>

Field 1 contains the value 0 to indicate a reset of the progress bar. Field 2 contains the total number of ticks in the progress bar. Field 3 contains the value 0 for forward progress bar motion. Field 3 contains the value 1 for backward progress bar motion. The value 0 in Field 4 means the installation is in progress and the time remaining may be calculated. The value 1 in Field 4 means script is being run and a "Please wait ..." message can be displayed. The estimate of the total number of ticks is an approximation and may be inaccurate.

</dd> <dt>

<span id="ActionInfo"></span><span id="actioninfo"></span><span id="ACTIONINFO"></span>ActionInfo
</dt> <dd>

Field 1 contains the value 1 to indicate this string contains action information. Field 2 contains the number of ticks the progress bar moves for each ActionData message sent by the current action. If Field 3 contains the value 0, ignore Field 2. If Field 3 contains the value 1, increment the progress bar by the number of ticks in Field 2 for each ActionData message sent by the current action. Field 4 is unused.

</dd> <dt>

<span id="ProgressReport"></span><span id="progressreport"></span><span id="PROGRESSREPORT"></span>ProgressReport
</dt> <dd>

Field 1 contains the value 2 to indicate this string contains progress information. Field 2 contains the number of ticks the progress bar has moved. Field 3 is unused. Field 4 is unused.

</dd> <dt>

<span id="ProgressAddition"></span><span id="progressaddition"></span><span id="PROGRESSADDITION"></span>ProgressAddition
</dt> <dd>

Field 1 contains the value 3 to indicate that an action can add ticks the progress bar. Field 2 contains the number of ticks to add to total expected count of progress ticks. Field 3 is unused. Field 4 is unused.

</dd> </dl> </dd> </dl>

 

 



