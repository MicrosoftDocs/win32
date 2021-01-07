---
description: Because unnecessary file copying slows an installation, the Windows Installer determines whether the component's key file is already installed before attempting to install the files of any component.
ms.assetid: 8be734c7-4f16-4f54-93db-bb8efb1ea6da
title: Replacing Existing Files
ms.topic: article
ms.date: 05/31/2018
---

# Replacing Existing Files

Because unnecessary file copying slows an installation, the Windows Installer determines whether the component's key file is already installed before attempting to install the files of any component. If the installer finds a file with the same name as the component's key file installed in the target location, it compares the version, date, and language of the two key files and uses file versioning rules to determine whether to install the component provided by the package. If the installer determines it needs to replace the component base upon the key file, then it uses the file versioning rules on each installed file to determine whether to replace the file.

Note that when authoring an installation package with versioned files, the version string in the Version column of the [File table](file-table.md) must always be identical to the version of the file included with the package.

The default file versioning rules can be overridden or modified by using the [**REINSTALLMODE**](reinstallmode.md) property. The installer uses the file versioning rules specified by the **REINSTALLMODE** property when installing, reinstalling, or repairing a file. The following example shows how the installer applies the default [File Versioning Rules](file-versioning-rules.md). The default value of the **REINSTALLMODE** property is "omus".

The following component key files are installed on the system before the component is reinstalled.



| File                                    | Version  | Create date | Modified date | Language    |
|-----------------------------------------|----------|-------------|---------------|-------------|
| FileA                                   | 1.0.0000 | 1/1/99      | 1/1/99        | ENG         |
| FileB                                   | 2.0.0000 | 1/1/99      | 1/1/99        | ENG         |
| FileC                                   | 1.0.0000 | 1/1/99      | 1/1/99        | ENG         |
| FileD                                   | 1.0.0000 | 1/1/99      | 1/2/99        | ENG         |
| FileE                                   | none     | 1/1/99      | 1/1/99        | none        |
| FileF (modified > create)<br/> | none     | 1/1/99      | 1/2/99        | none        |
| FileG                                   | 1.0.0000 | 1/1/99      | 1/1/99        | ENG         |
| FileH                                   | 1.0.0000 | 1/1/99      | 1/1/99        | ENG,FRN,SPN |
| FileI                                   | 1.0.0000 | 1/1/99      | 1/1/99        | ENG,FRN     |
| FileJ                                   | 1.0.0000 | 1/1/99      | 1/1/99        | ENG,GER,ITN |



 

The following component key files are included in the installer package.



| File                               | Version  | Create date | Modified date | Language    |
|------------------------------------|----------|-------------|---------------|-------------|
| FileA (marked same)<br/>     | 1.0.0000 | 1/1/99      | 1/1/99        | ENG         |
| FileB (earlier version)<br/> | 1.0.0000 | 1/1/99      | 1/1/99        | ENG         |
| FileC (later version)<br/>   | 2.0.0000 | 1/1/99      | 1/1/99        | ENG         |
| FileD (later version)<br/>   | 2.0.0000 | 12/31/98    | 1/10/99       | FRN         |
| FileE (marked same)<br/>     | none     | 1/1/99      | 1/1/99        | none        |
| FileF (new file)<br/>        | none     | 1/3/99      | 1/3/99        | none        |
| FileG (new language)<br/>    | 1.0.0000 | 1/1/99      | 1/1/99        | FRN         |
| FileH (new language)<br/>    | 1.0.0000 | 1/1/99      | 1/1/99        | ITN,ENG,GER |
| FileI (more languages)<br/>  | 1.0.0000 | 1/1/99      | 1/1/99        | ENG,FRN,SPN |
| FileJ (fewer languages)<br/> | 1.0.0000 | 1/1/99      | 1/1/99        | GER         |



 

The following component key files stay on the system after the component is reinstalled. The state of the key file determines the state of any other files in the component.



| File                | Version  | Create date | Modified date | Language    |
|---------------------|----------|-------------|---------------|-------------|
| FileA (original)    | 1.0.0000 | 1/1/99      | 1/1/99        | ENG         |
| FileB (original)    | 2.0.0000 | 1/1/99      | 1/1/99        | ENG         |
| FileC (replacement) | 2.0.0000 | 1/1/99      | 1/1/99        | ENG         |
| FileD (replacement) | 2.0.0000 | 12/31/98    | 1/10/99       | FRN         |
| FileE (replacement) | none     | 1/1/99      | 1/1/99        | none        |
| FileF (original)    | none     | 1/1/99      | 1/2/99        | none        |
| FileG (replacement) | 1.0.0000 | 1/1/99      | 1/1/99        | FRN         |
| FileH (replacement) | 1.0.0000 | 1/1/99      | 1/1/99        | ITN,ENG,GER |
| FileI (replacement) | 1.0.0000 | 1/1/99      | 1/1/99        | ENG,FRN,SPN |
| FileJ (original)    | 1.0.0000 | 1/1/99      | 1/1/99        | ENG,GER,ITN |



 

## Related topics

<dl> <dt>

[CRC Checking During an Installation](crc-checking-during-an-installation.md)
</dt> </dl>

 

 




