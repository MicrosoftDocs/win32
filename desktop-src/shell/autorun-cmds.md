---
description: This topic is a reference for the entries that can be used in an Autorun.inf file. An entry consists of a key and a value.
ms.assetid: 5b8fd559-b1be-4552-a7be-19ad107855af
title: Autorun.inf Entries
ms.topic: article
ms.date: 05/31/2018
---

# Autorun.inf Entries

This topic is a reference for the entries that can be used in an Autorun.inf file. An entry consists of a key and a value.

-   [\[AutoRun\] Keys](#autorun-keys)
    -   [action](#parameters)
    -   [CustomEvent](#customevent)
    -   [icon](#parameters)
    -   [label](#parameters)
    -   [open](#parameters)
    -   [UseAutoPlay](#parameters)
    -   [shellexecute](#shellexecute)
    -   [shell](#autoruninf-entries)
    -   [shell\\verb](#shellverb)
-   [\[Content\] Keys](#content-keys)
-   [\[ExclusiveContentPaths\] Keys](#exclusivecontentpaths-keys)
-   [\[IgnoreContentPaths\] Keys](#ignorecontentpaths-keys)
-   [\[DeviceInstall\] Keys](#deviceinstall-keys)
    -   [DriverPath](#driverpath)

## \[AutoRun\] Keys

-   [action](#parameters)
-   [CustomEvent](#customevent)
-   [icon](#parameters)
-   [label](#parameters)
-   [open](#parameters)
-   [UseAutoPlay](#parameters)
-   [shellexecute](#shellexecute)
-   [shell](#autoruninf-entries)
-   [shell\\verb](#shellverb)

### action

The **action** entry specifies the text that is used in the Autoplay dialog for the handler representing the program specified in the [open](#parameters) or [shellexecute](#shellexecute) entry in the media's Autorun.inf file. The value can be expressed as either text or as a resource stored in a binary.


```
action=ActionText
```




```
action=@[filepath\]filename,-resourceID
```



### Parameters

-   *ActionText*

    Text that is used in the Autoplay dialog for the handler representing the program specified in the [open](#parameters) or [shellexecute](#shellexecute) entry in the media's Autorun.inf file.

-   *filepath*

    A string that contains the fully qualified path of the directory that contains the binary file containing the string. If no path is specified, the file must be in the drive's root directory.

-   *filename*

    A string that contains the binary file's name.

-   *resourceID*

    The ID of the string within the binary file.

### Remarks

The **action** key is only used in Windows XP Service Pack 2 (SP2) or later. It is only supported for drives of type DRIVE\_REMOVABLE and DRIVE\_FIXED. In the case of DRIVE\_REMOVABLE, the **action** key is required. An **action** command in the Autorun.inf file of an audio CD or movie DVD is ignored, and these media continue to behave as in Windows XP Service Pack 1 (SP1) and earlier.

The string displayed in the Autoplay dialog is constructed by combining the text specified in the **action** entry with hard-coded text naming the provider, provided by the Shell. The [icon](#parameters) is displayed next to it. This entry always appears as the first option in the Autoplay dialog and is selected by default. If the user accepts the option, the application specified by the [open](#parameters) or [shellexecute](#shellexecute) entry in the media's Autorun.inf file is launched. The **Always do the selected action** option is not available in this situation.

The [action](#parameters) and [icon](#parameters) keys together define the representation of the application that is seen by the end user in the Autoplay dialog. They should be composed in such a way that users can easily identify them. They should indicate the application to be run, the company that created it, and any associated branding.

For backward compatibility, the **action** entry is optional for devices of type DRIVE\_FIXED. For this type, a default entry is used in the Autoplay dialog if no **action** entry is present in the Autorun.inf file.

The **action** entry is mandatory for devices of type DRIVE\_REMOVABLE, which until now did not have Autorun.inf support. If no **action** entry is present, the Autoplay dialog is displayed but with no option to launch the additional content.

### CustomEvent

The **CustomEvent** entry specifies a custom AutoPlay content event.


```
CustomEvent=CustomEventName
```



### Parameters

-   *CustomEventName*

    A text string containing the name of the AutoPlay content event. The name must be no more than 100 alphanumeric characters.

### Remarks

You can include a custom event name in the Autorun.inf file of a volume. When AutoPlay prompts the user for an application to use with the volume, it displays only applications that have registered for the specified custom event name. For information on how you can register an application as a handler for your custom AutoPlay content event, see [Auto-launching with AutoPlay](/previous-versions/windows/apps/hh452731(v=win.10)) or [How to Register an Event Handler](how-to-register-an-event-handler.md).

The following example specifies the value "MyContentOnArrival" as a new AutoPlay content event.


```
CustomEvent=MyContentOnArrival
```



### icon

The **icon** entry specifies an icon which represents the AutoRun-enabled drive in the Windows user interface.


```
icon=iconfilename[,index]
```



### Parameters

-   *iconfilename*

    Name of an .ico, .bmp, .exe, or .dll file containing the icon information. If a file contains more than one icon, you must also specify zero-based index of the icon.

### Remarks

The icon, together with the label, represents the AutoRun-enabled drive in the Windows user interface. For instance, in Windows Explorer, the drive is represented by this icon instead of the standard drive icon. The icon's file must be in the same directory as the file specified by the [open](#parameters) command.

The following example specifies the second icon in the MyProg.exe file.


```
icon=MyProg.exe,1
```



### label

The **label** entry specifies a text label which represents the AutoRun-enabled drive in the Windows user interface.


```
label=LabelText
```



### Parameters

-   *LabelText*

    A text string containing the label. It can contain spaces and should be no longer than 32 characters.

> [!Note]  
> It is possible to put a value in the **LabelText** parameter which exceeds 32 characters and receive no error message. However, the system only displays the first 32 characters. Any characters after the 32nd are truncated and not displayed. For example, if the **LabelText** is as follows: label="This CD is designed to be the ultimate music CD." the following will be displayed, "This CD is designed to be the ul".

 

### Remarks

The label, together with an icon, represents the AutoRun-enabled drive in the Windows user interface.

The following example specifies the value "My Drive Label" as the drive's label.


```
label=My Drive Label
```



### open

The **open** entry specifies the path and file name of the application that AutoRun launches when a user inserts a disc in the drive.


```
open=[exepath\]exefile [param1 [param2] ...] 
```



### Parameters

-   *exefile*

    Fully qualified path of an executable file that runs when the CD is inserted. If only a file name is specified, it must be in drive's root directory. To locate the file in a subdirectory, you must specify a path. You can also include one or more command-line parameters to pass to the startup application.

### UseAutoPlay

On Windows XP, the **UseAutoPlay** entry specifies that AutoPlay should be used instead of AutoRun.

On Windows Vista and later, this entry causes any actions specified for AutoRun (by using either the **open** or **shellexecute** entries) to be suppressed from the AutoPlay dialog. This entry has no effect on versions of Windows earlier than Windows XP.

On Windows 8 and later, specifying a value of 0 will disable autoplay for this device.

### Parameters

To use this option, add an entry for **UseAutoPlay** to the Autorun.inf file and set the entry equal to 1. No other value is supported on versions of Windows earlier than Windows 8.

On Windows 8 and later, specify a value of 0 to disable autoplay for this device.


```
UseAutoPlay=1
```



### Remarks

Currently, **UseAutoPlay** is applicable only on Windows XP or later and only on a drive that [**GetDriveType**](/windows/win32/api/fileapi/nf-fileapi-getdrivetypea) determines to be of type **DRIVE\_CDROM**.

When **UseAutoPlay** is used, any action specified by the **open** or **shellexecute** entries in Autorun.inf is ignored on Windows XP and omitted from the AutoPlay dialog on Windows Vista.

AutoRun is typically used to automatically run or load something contained on the inserted media, whereas AutoPlay presents a dialog that includes a list of relevant actions that may be taken and enables the user to choose which action to take. For more information about the difference between AutoRun and AutoPlay, see [Creating an AutoRun-enabled CD-ROM Application](autoplay.md) and [Using and Configuring AutoPlay](autoplay2k-using.md), respectively.

### Usage Example

A CD contains three files: Autorun.inf, Readme.txt, and Music.wma. Depending on the version of Windows in use and options specified in Autorun.inf, the CD may be handled by either AutoRun or AutoPlay when it is inserted (assuming AutoRun/AutoPlay is enabled for the drive into which the CD is inserted).

First, consider an Autorun.inf file with the following contents, noting that **UseAutoPlay=1** is not specified:


```
[AutoRun]
shellexecute="Readme.txt"
```



The action taken by the Shell when this CD is inserted depends on the version of Windows in use:

-   On Windows XP or earlier, this CD is handled by AutoRun when it is inserted. In this case, the **shellexecute** entry is read, and the Shell invokes the file handler associated with .txt files; typically this would open Readme.txt in Notepad.
-   On Windows Vista, the presence of an Autorun.inf file with a **shellexecute** entry causes the media to be identified as AutoPlay type "Software and games". In this case the user is presented with an AutoPlay dialog that includes the action specified by the **shellexecute** entry (presented as "Load Readme.txt" in the dialog), along with default actions associated with media of type "Software and games".

To indicate that AutoPlay should be used rather than AutoRun on Windows XP, and that the action specified by the AutoRun shellexecute entry should be suppressed from the AutoPlay dialog on Windows Vista, insert **UseAutoPlay** into the Autorun.inf file as follows:


```
[AutoRun]
shellexecute="Readme.txt"
UseAutoPlay=1
```



Once again, the action taken by the Shell when this CD is inserted depends on the version of Windows in use.

-   On versions of Windows earlier than Windows XP, AutoRun is still used and the action specified by **shellexecute** is performed, as described previously. (Note that only AutoRun is available on versions of Windows earlier than Windows XP.)
-   On Windows XP, the **UseAutoPlay** entry causes AutoPlay to be used in place of AutoRun. In this case, AutoPlay determines that the media contains a Windows Media Audio (.wma) file and categorizes the content as "Music files". The user is presented with an AutoPlay dialog containing registered handlers for the "Music files" AutoPlay media type; the AutoRun shellexecute entry is ignored.

### shellexecute

[Version 5.0.](versions.md) The **shellexecute** entry specifies an application or data file that AutoRun will use to call [**ShellExecuteEx**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa).


```
shellexecute=[filepath\]filename[param1, [param2]...] 
```



### Parameters

-   *filepath*

    A string that contains the fully qualified path of the directory that contains the data or executable file. If no path is specified, the file must be in the drive's root directory.

-   *filename*

    A string that contains the file's name. If it is an executable file, it is launched. If it is a data file, it must be a member of a [file type](fa-file-types.md). [**ShellExecuteEx**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa) launches the default command associated with the file type.

-   *paramx*

    Contains any additional parameters that should be passed to [**ShellExecuteEx**](/windows/desktop/api/Shellapi/nf-shellapi-shellexecuteexa).

### Remarks

This entry is similar to [open](#parameters), but it allows you to use [file association](fa-intro.md) information to run the application.

### shell

The **shell** entry specifies a default command for the drive's shortcut menu.


```
shell=verb
```



### Parameters

-   *verb*

    The verb that corresponds to the menu command. The verb and its associated menu command must be defined in the Autorun.inf file with a [shell\\verb](#shellverb) entry.

### Remarks

When a user right-clicks the drive icon, a shortcut menu appears. If an Autorun.inf file is present, the default shortcut menu command is taken from it. This command also executes when the user double-clicks the drive's icon.

To specify the default shortcut menu command, first define its verb, command string, and menu text with [shell\\verb](#shellverb). Then use shell to make it the default shortcut menu command. Otherwise, the default menu item text will be "AutoPlay", which launches the application specified by the [open](#parameters) entry.

### shell\\verb

The **shell\\verb** entry adds a custom command to the drive's shortcut menu.


```
shell\verb\command=Filename.exe 
shell\verb=MenuText
```



### Parameters

-   *verb*

    The menu command's verb. The **shell\\***verb***\\command** entry associates the verb with an executable file. Verbs must not contain embedded spaces. By default, *verb* is the text that is displayed in the shortcut menu.

-   *Filename.exe*

    The path and file name of the application that performs the action.

-   *MenuText*

    This parameter specifies the text that is displayed in the shortcut menu. If it is omitted, *verb* is displayed. *MenuText* can be mixed-case and can contain spaces. You can set a shortcut key for the menu item by putting an ampersand (&) in front of the letter.

### Remarks

When a user right-clicks the drive icon, a shortcut menu appears. Adding **shell\\verb** entries to the drive's Autorun.inf file allows you to add commands to this shortcut menu.

There are two parts to this entry, which must be on separate lines. The first part is **shell\\***verb***\\command**. It is required. It associates a string, called a *verb*, with the application to launch when the command runs. The second part is the **shell\\***verb* entry. It is optional. You can include it to specify the text that displays in the shortcut menu.

To specify a default shortcut menu command, define the verb with **shell\\verb**, and make it the default command with the [shell](#autoruninf-entries) entry.

The following sample Autorun.inf fragment associates the *readit* verb with the command string "Notepad abc\\readme.txt". The menu text is "Read Me", and 'M' is defined as the item's shortcut key. When the user selects this command, the drive's abc\\readme.txt file opens with Microsoft Notepad.


```
shell\readit\command=notepad abc\readme.txt 
shell\readit=Read &Me
```



## \[Content\] Keys

There are three file type keys: **MusicFiles**, **PictureFiles**, and **VideoFiles**.

If one of these contents is set to true through one the case-insensitive values 1, y, yes, t, or true, the Autoplay UI displays the handlers associated with that content type regardless of whether content of that type exists on the media.

If one of these contents is set to false through one the case-insensitive values 0, n, no, f, or false, the Autoplay UI does not display the handlers associated with that content type even if content of that type is detected on the media.

Use of this section is intended to allow content authors to communicate the intent of content to Autoplay. For instance, a CD can be categorized as containing only music content even though it also has pictures and videos and would otherwise be seen as having mixed content.

The **\[Content\]** section is only supported under Windows Vista and later.


```
[Content]
MusicFiles=Y
PictureFiles=0
VideoFiles=false
```



## \[ExclusiveContentPaths\] Keys

Folders listed in this section limit Autoplay to searching only those folders and their subfolders for content. They can be given with or without a leading backslash (\\). In either case they are taken as absolute paths from the root directory of the media. In the case of folders with spaces in their names, do not enclose them in quotes as the quotes are taken literally as part of the path.

Use of this section is intended to allow content authors both to communicate the intent of content to Autoplay and to shorten its scan time by limiting the scan to certain significant areas of the media.

The following are all valid paths


```
[ExclusiveContentPaths]
\music
\music\more music
music2
```



The **\[ExclusiveContentPaths\]** section is only supported under Windows Vista and later.

## \[IgnoreContentPaths\] Keys

Folders listed in this section, and their subfolders, are ignored by Autoplay when searching a media for content. They can be given with or without a leading backslash (\\). In either case they are taken as absolute paths from the root directory of the media. In the case of folders with spaces in their names, do not enclose them in quotes as the quotes are taken literally as part of the path.

Paths in this section take precedence over paths in the **\[ExclusiveContentPaths\]** section. If a path given in **\[IgnoreContentPaths\]** is a subfolder of a path given in **\[ExclusiveContentPaths\]**, it is still ignored.

Use of this section is intended to allow content authors both to communicate the intent of content to Autoplay and to shorten its scan time by limiting the scan to certain significant areas of the media.

The following are all valid paths


```
[IgnoreContentPaths]
\music
\music\more music
music2
```



The **\[IgnoreContentPaths\]** section is only supported under Windows Vista and later.

## \[DeviceInstall\] Keys

### DriverPath

The **DriverPath** entry specifies a directory to search recursively for driver files. This command is used during a driver installation and is not part of an AutoRun operation. The **\[DeviceInstall\]** section is only supported under Windows XP.


```
[DeviceInstall]
DriverPath=directorypath
```



### Parameters

-   *directorypath*

    A path to a directory that Windows searches for driver files, along with all of its subdirectories.

### Remarks

Do not use drive letters in *directorypath* as they change from one computer to the next.

To search multiple directories, add a **DriverPath** entry for each directory as in this example.


```
[DeviceInstall]
DriverPath=drivers\video 
DriverPath=drivers\audio
```



If no **DriverPath** entry is provided in the **\[DeviceInstall\]** section or the **DriverPath** entry has no value, then that drive is skipped during a search for driver files.

 

 
