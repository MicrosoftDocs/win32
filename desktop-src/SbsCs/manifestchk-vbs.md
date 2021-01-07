---
description: The VBScript file Manifestchk.vbs is a validation tool provided in the Microsoft Windows Software Development Kit (SDK) that validates application and assembly manifest files.
ms.assetid: 8269cb92-bd3f-411f-8395-fe06ed550cc5
title: Manifestchk.vbs
ms.topic: article
ms.date: 05/31/2018
---

# Manifestchk.vbs

The VBScript file Manifestchk.vbs is a validation tool provided in the Microsoft Windows Software Development Kit (SDK) that validates application and assembly manifest files.

Running this sample requires Windows Script Host. For more information about Windows Script Host, see the Windows Script Host section of the Windows SDK. Windows Script Host is actually two hosts. CScript.exe is the version that enables you to run scripts from the command prompt. CScript.exe provides command-line switches for setting script properties.

The command-line format is the following:

**Cscript //nologo manifestchk.vbs /s:** *\[drive:\]\[path\]schemafilename* **/m:** *\[drive:\]\[path\]manifestfilename* **\[/q\] /t:** *option*

The flags defined for Manifestchk.vbs are described in the following table.



| Flag | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /s   | Specifies the manifest schema file name to validate manifests against. See the schema at [Manifest File Schema](manifest-file-schema.md).                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| /m   | Specifies the manifest file name to validate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| /q   | Suppresses all output to the console.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| /t   | Specifies the type of manifest file. The valid values are: AM   Validate the [manifest file schema](manifest-file-schema.md) of an [assembly manifest](assembly-manifests.md) or [application manifest](application-manifests.md)<br/> PC   Validate the [publisher configuration file schema](publisher-configuration-file-schema.md) of a [publisher configuration file](publisher-configuration-files.md)<br/> AC   Validate the application configuration file schema of an [application configuration file](application-configuration-files.md).<br/> |



 

If the /q flag is not specified, Manifestchk.vbs displays detailed information about the first error encountered in the file, and displays a message stating whether the validation process was successful or not.

This utility checks for the following:

-   A valid command line.
-   That MSXML version 3 is installed.
-   That the manifest uses well-formed XML.
-   That the manifest agrees with the provided schema. Note that Manifestchk.vbs verifies the manifest file based only on what is specified in the provided schema. For an example of a manifest schema, see [Manifest File Schema](manifest-file-schema.md).

Cscript.exe returns a value of 0 if the validation process was successful and 1 if it was not successful. It returns 2 if there is an error in a command line argument.

## Related topics

<dl> <dt>

[Side-by-Side Assembly Development Tools](side-by-side-assembly-development-tools.md)
</dt> </dl>

 

 




