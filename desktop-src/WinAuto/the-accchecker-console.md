---
title: The AccChecker Console
description: AccChecker Console (AccCheckConsole.exe) is a command-line tool for verifying the accessibility implementation of your application's UI.
ms.assetid: 9E80BFDD-FB5D-45C5-BE69-7036AD29D863
keywords:
- AccChecker Console
- AccChecker command-line tool
- command-line, AccChecker
ms.topic: article
ms.date: 05/31/2018
---

# The AccChecker Console

AccChecker Console (AccCheckConsole.exe) is a command-line tool for verifying the accessibility implementation of your application's UI. The command-line accepts a variety of inputs (such as HWND, window title, and verification routine) and supplies an exit code that corresponds to the error log count.

-   [Command-line Syntax](#command-line-syntax)
-   [Command-line Error Codes](#command-line-error-codes)
-   [Command-line Examples](#command-line-examples)
-   [Related topics](#related-topics)

![accchecker console command-line tool](images/accchecker-console.png)

## Command-line Syntax

AccChecker Console has the following command-line syntax.

**AccCheckConsole \[options\] (-hwnd &lt;hwnd&gt; \| -process &lt;name&gt;) \[&lt;dlls&gt;\]**

The command-line options are as follows.



| Options                                                                                                                                                         | Description                                                                                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| <span id="-hwnd__hwnd_"></span><span id="-HWND__HWND_"></span>-hwnd &lt;hwnd&gt;<br/>                                                                     | Validates the window that has the specified handle (HWND). The handle can be specified in hexidecimal or decimal.<br/> |
| <span id="-window__title_"></span><span id="-WINDOW__TITLE_"></span>-window &lt;title&gt;<br/>                                                            | Validates the window that has the specified title.<br/>                                                                |
| <span id="__________________-process__name_"></span><span id="__________________-PROCESS__NAME_"></span> -process &lt;name&gt;<br/>                       | Validates the main window of the process that has the specified name.<br/>                                             |
| <span id="____________________________-list"></span><span id="____________________________-LIST"></span> -list<br/>                                       | Lists all of the available verification routines.<br/>                                                                 |
| <span id="__________________-enable__name_"></span><span id="__________________-ENABLE__NAME_"></span> -enable &lt;name&gt;<br/>                          | Runs the specified verification routine. This option can be specified more than once.<br/>                             |
| <span id="_____________________________-disable__name_"></span><span id="_____________________________-DISABLE__NAME_"></span> -disable &lt;name&gt;<br/> | Runs all but the specified verification routine. This option can be specified more than once.<br/>                     |
| <span id="___________-log__info_warn_err_"></span><span id="___________-LOG__INFO_WARN_ERR_"></span> -log (info\|warn\|err)<br/>                          | The lowest event rating that will be logged.<br/>                                                                      |
| <span id="__________________-logfile__file_"></span><span id="__________________-LOGFILE__FILE_"></span> -logfile &lt;file&gt;<br/>                       | Write the output to the specified log file. This option can be specified more than once.<br/>                          |
| <span id="-suppress__file_"></span><span id="-SUPPRESS__FILE_"></span>-suppress &lt;file&gt;<br/>                                                         | Use the specified XML file to suppress errors. <br/>                                                                   |
| <span id="-quiet"></span><span id="-QUIET"></span>-quiet<br/>                                                                                             | Do not write logging output to stdout.<br/>                                                                            |
| <span id="-help__________________________________"></span><span id="-HELP__________________________________"></span>-help <br/>                           | Displays quick help. <br/>                                                                                             |



 

## Command-line Error Codes

Following are error codes returned from AccCheckConsole when using "echo %errorlevel%"



| Error code                       | Description                                 |
|----------------------------------|---------------------------------------------|
| <span id="0"></span>0<br/> | No errors and no warnings.<br/>       |
| <span id="1"></span>1<br/> | Usages statement was requested. <br/> |
| <span id="2"></span>2<br/> | Errors and no warnings.<br/>          |
| <span id="3"></span>3<br/> | Errors and warnings.<br/>             |
| <span id="4"></span>4<br/> | Warnings but no errors.<br/>          |
| <span id="5"></span>5<br/> | Invalid command line. <br/>           |



 

## Command-line Examples

Following are several AccChecker Console command-line examples.

-   Run all verifications on a window with a specified name.

    **AccCheckConsole -window "Untitled - Notepad"**

-   Run a subset of the verifications against an HWND, specifying a suppression file.

    **AccCheckConsole -hwnd 0x00382f00 -enable CheckTabbing -enable CheckName -suppress suppress.xml**

-   Run all verifications from a new verification DLL.

    **AccCheckConsole -window "Untitled - Notepad" VerificationRoutine1.dll**

## Related topics

<dl> <dt>

[UI Accessibility Checker](ui-accessibility-checker.md)
</dt> </dl>

 

 





