---
description: Creating an AutoRun-enabled application is a straightforward procedure. This topic uses CD-ROM as an example (it was the first medium to implement this technology) but today there are many different media types that can use it.
title: Creating an AutoRun-Enabled Application
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 0d01f4a2-64c4-4b31-9fc9-361da6825ab8
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Creating an AutoRun-Enabled Application

Creating an AutoRun-enabled application is a straightforward procedure. This topic uses CD-ROM as an example (it was the first medium to implement this technology) but today there are many different media types that can use it.

To enable AutoRun in your application, you simply include two essential files:

- An Autorun.inf file
- A startup application

When a user inserts a disc into a CD-ROM drive on a AutoRun-compatible computer, the system immediately checks to see if the disc has a personal computer file system. If it does, the system searches for a file named [Autorun.inf](#creating-an-autoruninf-file). This file specifies a setup application that will be run, along with a variety of optional settings. The startup application typically installs, uninstalls, configures, and perhaps runs the application.

- [Creating an Autorun.inf File](#creating-an-autoruninf-file)
- [The \[DeviceInstall\] Section](#the-deviceinstall-section)
- [Related topics](#related-topics)

## Creating an Autorun.inf File

Autorun.inf is a text file located in the root directory of the CD-ROM that contains your application. Its primary function is to provide the system with the name and location of the application's startup program that will be run when the disc is inserted.

> [!Note]  
> Autorun.inf files are not supported under Windows XP for drives that return DRIVE\_REMOVABLE from [**GetDriveType**](/windows/win32/api/fileapi/nf-fileapi-getdrivetypea).

 

The Autorun.inf file can also contain optional information including:

- The name of a file that contains an icon that will represent your application's CD-ROM drive. This icon will be displayed by Windows Explorer in place of the standard drive icon.
- Additional commands for the shortcut menu that is displayed when the user right-clicks the CD-ROM icon. You can also specify the default command that is run when the user double-clicks the icon.

Autorun.inf files are similar to .ini files. They consist of one or more sections, each headed by a name enclosed in square brackets. Each section contains a series of commands that will be run by the Shell when the disc is inserted. There are two sections that are currently defined for Autorun.inf files.

- The **\[autorun\]** section contains the default AutoRun commands. All Autorun.inf files must have an **\[autorun\]** section.
- An optional **\[autorun.alpha\]** section can be included for systems running on RISC-based computers. When a disc is inserted in a CD-ROM drive on a RISC-based system, the Shell will run the commands in this section instead of those in the **\[autorun\]** section.

> [!Note]  
> The Shell checks for an architecture-specific section first. If it does not find one, it uses the information in the **\[autorun\]** section. After the Shell finds a section, it ignores all others, so each section must be self-contained.

 

Each section contains a series of commands that determine how the Autorun operation takes place. There are five commands available.



| Command                         | Description                                                                            |
|---------------------------------|----------------------------------------------------------------------------------------|
| [defaulticon](autorun-cmds.md) | Specifies the default icon for the application.                                        |
| [icon](autorun-cmds.md)        | Specifies the path and file name of an application-specific icon for the CD-ROM drive. |
| [open](autorun-cmds.md)        | Specifies the path and file name of the startup application.                           |
| [useautorun](autorun-cmds.md)  | Specifies that Autoplay V2 features should be used if supported.                       |
| [shell](autorun-cmds.md)       | Defines the default command in the CD-ROM's shortcut menu.                             |
| [shell\_verb](autorun-cmds.md) | Adds commands to the CD-ROM's shortcut menu.                                           |



 

The following is an example of a simple Autorun.inf file. It specifies Filename.exe as the startup application. The second icon in Filename.exe will represent the CD-ROM drive instead of the standard drive icon.


```
[autorun] 
open=Filename.exe 
icon=Filename.exe,1
```



This Autorun.inf sample runs different startup applications depending on the type of computer.


```
[autorun] 
open=Filename_x86.exe 
icon=IconFile.ico 

[autorun.alpha] 
open=Filename_RISC.exe 
icon=IconFile.ico
```



## The \[DeviceInstall\] Section

You can use the **\[DeviceInstall\]** section on any removable media. It is supported only under Windows XP. You use **DriverPath** to specify a directory path where Windows XP searches for driver files, which prevents a lengthy search through the entire contents.

You use the **\[DeviceInstall\]** section with a driver installation to specify directories where Windows XP should search the media for driver files. Under Windows XP, entire media are no longer searched by default, therefore requiring **\[DeviceInstall\]** to specify search locations. The following are the only removable media that Windows XP fully searches without a **\[DeviceInstall\]** section in an Autorun.inf file.

- Floppy disks found in drives A or B.
- CD/DVD media less that 1 gigabyte (GB) in size.

All other media must include a **\[DeviceInstall\]** section for Windows XP to detect any drivers stored on that media.

> [!Note]  
> As with the **\[AutoRun\]** section, the **\[DeviceInstall\]** section can be architecture-specific.

 

## Related topics

<dl> <dt>

[How to Implement Autorun Startup Applications](how-to-implement-autorun-startup-applications.md)
</dt> <dt>

[Writing a Device Installation Application](/windows-hardware/drivers/install/writing-a-device-installation-application)
</dt> </dl>

 

 
