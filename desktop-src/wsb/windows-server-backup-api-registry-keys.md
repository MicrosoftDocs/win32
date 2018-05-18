---
title: Windows Server Backup API Registry Keys
description: To register with the Windows Server Backup feature, an application must contain a Volume Shadow Copy Service (VSS) writer and must set the Application Support and Application Identifier registry keys.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '71615680-b02b-4ca2-940b-9b111f640774'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-server-backup'
ms.tgt_platform: multiple
---

# Windows Server Backup API Registry Keys

To register with the Windows Server Backup feature, an application must contain a Volume Shadow Copy Service (VSS) writer and must set the **Application Support** and **Application Identifier** registry keys. An application that implements an add-in using the [Windows Server Backup API interfaces](windows-server-backup-api-interfaces.md) must also set the **CLSID** key.

Setting these registry keys requires system administrator privilege.

## Application Support

The **Application Support** registry key is used to register the application's VSS writer ID.

If the **Application Support** registry key does not exist, the application should create it under the following registry key:

**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**Windows NT**\\**CurrentVersion**\\**WindowsServerBackup**

Create a subkey with the name **Application Support**. Do not set a value for this key. Under the **Application Support** key, create a subkey with the name ***WriterGUID***, where *WriterGUID* is the writer class ID for the application's VSS writer. Do not set a value for this key.

## Application Identifier

The **Application Identifier** registry key is used to register the application identifier to be used in the Windows Server Backup user interface and command-line interface to identify the application.

If the **Application Identifier** registry key does not exist, the application should create it under the following registry key, where *WriterGUID* is the writer class ID for the application's VSS writer:

**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**Windows NT**\\**CurrentVersion**\\**WindowsServerBackup**\\**Application Support**\\***WriterGUID***

Create a subkey with the name **Application Identifier** and type REG\_SZ. The value should be a string that end users will recognize as the name of the application whose data is to be backed up and recovered. The application identifier string can contain a maximum of 256 characters and must be unique. If two applications register using the same application identifier string, the second registration is ignored. This string will not be localized.

You can use a batch script to set the **Application Support** and **Application Identifier** registry keys. To do so, create a file with a .bat file name extension that contains a **reg add** command in the following format, where:

-   *WriterGUID* is the writer class ID for the application's VSS writer
-   *ApplicationDisplayName* is the application identifier string

 **reg add** **"HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\windows nt\\currentversion\\WindowsServerBackup\\Application Support\\***WriterGUID***â€? /v "Application Identifier" /t REG\_SZ /d** *ApplicationDisplayName* **/f**

In the following example script:

-   {CE4EF7DC-18CE-4A11-B4C9-D7A668637D1B} is the value of *WriterGUID*
-   "My Application" is the value of *ApplicationDisplayName*

 **reg add** **"HKEY\_LOCAL\_MACHINE\\Software\\Microsoft\\windows nt\\currentversion\\WindowsServerBackup\\Application Support\\{CE4EF7DC-18CE-4A11-B4C9-D7A668637D1B}â€? /v "Application Identifier" /t REG\_SZ /d "My Application" /f**

For more information about the **reg add** command, see the TechNet Command-line Reference documentation at <http://go.microsoft.com/fwlink/p/?linkid=169397>. For more information about how to use batch files, see "Using batch files" at <http://go.microsoft.com/fwlink/p/?linkid=169398>.

## CLSID

An application that implements an add-in using the [Windows Server Backup API interfaces](windows-server-backup-api-interfaces.md) must set the **CLSID** registry key in addition to the **Application Support** and **Application Identifier** registry keys. An application that does not include an add-in should not set the **CLSID** registry key.

If the **CLSID** registry key does not exist, the application should create it under the following registry key:

**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**Windows NT**\\**CurrentVersion**\\**WindowsServerBackup**\\**Application Support**\\***WriterGUID***

Create a subkey with the name **CLSID** and type REG\_SZ. The value should be the GUID of the COM coclass that implements the add-in.

## Related topics

<dl> <dt>

[Windows Server Backup API Interfaces](windows-server-backup-api-interfaces.md)
</dt> </dl>

 

 




