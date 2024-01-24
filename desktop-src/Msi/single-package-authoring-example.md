---
description: The sample PUASample.msi is an example of a dual-purpose Windows Installer 5.0 package that is capable of being installed in either the per-user or per-machine installation context on Windows Server 2008 R2 and Windows 7.
ms.assetid: be018e8a-ca5f-4135-a019-970ec4173f23
title: Single Package Authoring Example
ms.topic: article
ms.date: 05/31/2018
---

# Single Package Authoring Example

The sample PUASample.msi is an example of a dual-purpose Windows Installer 5.0 package that is capable of being installed in either the per-user or per-machine [installation context](installation-context.md) on Windows Server 2008 R2 and Windows 7. This sample package follows the development guidelines described in [Single Package Authoring](single-package-authoring.md).

## Obtaining a copy of the sample

A copy of this sample and a Windows Installer database table editor, Orca.exe, are in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md). The sample and table editor are provided with the Windows Software Development Kit for Windows Server 2008 R2 and Windows 7 as the Windows Installer installation files PUASample1.msi and Orca.msi.

## System Requirements

The database editor, [Orca.exe](orca-exe.md), requires Windows Server 2008 R2 and earlier and Windows 7 and earlier. The dual-purpose package, PUASample1.msi, can be installed in either the per-machine or per-user [installation context](installation-context.md) on Windows Server 2008 R2 and Windows 7. PUASample1.msi can be installed only in the per-machine context on Windows Server 2008 and earlier and Windows Vista and earlier. You can install the database editor to examine the contents of PUASample1.msi without installing the sample. To install the sample or editor packages, ensure that the [DisableMSI](disablemsi.md) policy is not set to a value that blocks application installations.

## Identifying a Dual-Purpose Package

Dual-purpose packages should initialize the value of the [**MSIINSTALLPERUSER**](msiinstallperuser.md) property to 1. This identifies the package as capable of being installed in either the per-machine or per-user context on Windows Server 2008 R2 and Windows 7. Set the **MSIINSTALLPERUSER** property in the package only if it has been written following the development guidelines described in [Single Package Authoring](single-package-authoring.md) and if you intend to provide users with the option to install the package in either the per-user or per-machine context. A dual-purpose package should also initialize the value of the [**ALLUSERS**](allusers.md) property to 2. This specifies per-user as the default installation context for the application. If the value of the **ALLUSERS** property is any value other than 2, Windows Installer ignores the **MSIINSTALLPERUSER** property.

Use a Windows Installer database editor, such as [Orca.exe](orca-exe.md), to examine the contents of PUASample1.msi. The [Property](property-table.md) table in the sample package contains the following two entries.

[Property](property-table.md) Table (partial)

| Property          | Value |
|-------------------|-------|
| ALLUSERS          | 2     |
| MSIINSTALLPERUSER | 1     |



 

## Custom Dialog Box for Installation Context

The [user interface](user-interface.md) of the sample package includes an example of a custom dialog box, VerifyReadyDialog, that enables users to select either the per-user or per-machine installation context at installation time. The [Dialog](dialog-table.md) table contains a record that describes the VerifyReadyDialog dialog box. The value entered in the Attributes field is 39 because this dialog box uses the msidbDialogAttributesVisible (1), msidbDialogAttributesModal (2), msidbDialogAttributesMinimize (4), and msidbDialogAttributesTrackDiskSpace (32) [dialog style bits](dialog-style-bits.md). The title bar of the dialog box displays a title given by the value of the [**ProductName**](productname.md) property.

[Dialog](dialog-table.md) Table (partial) 

| Dialog            | HCentering | VCentering | Width | Height | Attributes | Title           | Control\_First | Control\_Default | Control\_Cancel |
|-------------------|------------|------------|-------|--------|------------|-----------------|----------------|------------------|-----------------|
| VerifyReadyDialog | 50         | 50         | 480   | 280    | 39         | \[ProductName\] | InstallPerUser | Next             | Cancel          |



 

The [Control](control-table.md) table contains entries for the [controls](controls.md) displayed by the VerifyReadyDialog dialog box. The dialog box displays [PushButton](pushbutton-control.md) controls and a [Text](text-control.md) control. All the controls use the msidbControlAttributesEnabled (2) and msidbControlAttributesVisible (1) [control attributes](control-attributes.md). The InstallPerMachine control also uses the [ElevationShield](elevationshield-attribute.md) control attribute, msidbControlAttributesElevationShield (8388608.) This control attribute adds the [*User Account Control*](u-gly.md) (UAC) elevation icon (shield icon) to the InstallPerMachine control and informs the user that UAC credentials are required to install the application in the per-machine context. The value in the Text field of the Control table is the text-style and text displayed by the control. See the description of the Text field in the Control table topic for more information about adding text to a control using predefined styles.

[Control](control-table.md) Table (partial)

| Dialog\_          | Control           | Type       | Attribute | Text                                                   | Control\_Next     |
|-------------------|-------------------|------------|-----------|--------------------------------------------------------|-------------------|
| VerifyReadyDialog | Cancel            | PushButton | 3         | {\\Tahoma10}&Cancel                                    | Next              |
| VerifyReadyDialog | Previous          | PushButton | 3         | {\\Tahoma10}<<&Previous                          | Cancel            |
| VerifyReadyDialog | Next              | PushButton | 3         | {\\Tahoma10}&Next >>                             | InstallPerUser    |
| VerifyReadyDialog | Text2             | Text       | 3         | Are you ready to complete your suspended installation? |                   |
| VerifyReadyDialog | InstallPerUser    | PushButton | 3         | {\\Tahoma10}Install Only for &Me                       | InstallPerMachine |
| VerifyReadyDialog | InstallPerMachine | PushButton | 8388611   | {\\Tahoma10}Install for &Everyone                      | Previous          |
| VerifyReadyDialog | Cancel            | PushButton | 3         | {\\Tahoma10}&Cancel                                    | Next              |



 

The [ControlEvent](controlevent-table.md) table specifies the [ControlEvents](control-events.md), or actions, the installer performs when the user interacts with a control. When a user activates the InstallPerUser pushbutton, the user interface displays an OutOfDisk dialog box if the [**OutOfDiskSpace**](outofdiskspace.md) property is 1, sets the value of the [**MSIINSTALLPERUSER**](msiinstallperuser.md) property to 1, sets the value of the [**ALLUSERS**](allusers.md) property to 2, sets the [**MSIFASTINSTALL**](msifastinstall.md) property to 1, and returns . Because the **MSIFASTINSTALL** property is set, no System Restore point is generated for the installation. When a user activates the InstallPerMachine pushbutton, the user interface displays an OutOfDisk dialog box if the **OutOfDiskSpace** property is 1, sets the value of the **ALLUSERS** property to 1, and returns.

[ControlEvent](controlevent-table.md) Table (partial) 

| Dialog\_          | Control\_         | Event                 | Argument  | Condition                 | Order |
|-------------------|-------------------|-----------------------|-----------|---------------------------|-------|
| VerifyReadyDialog | InstallPerUser    | SpawnDialog           | OutOfDisk | OutOfDiskSpace = 1        | 1     |
| VerifyReadyDialog | InstallPerUser    | EndDialog             | Return    | OutOfDiskSpace <> 1 | 5     |
| VerifyReadyDialog | InstallPerUser    | \[MSIINSTALLPERUSER\] | 1         | 1                         | 2     |
| VerifyReadyDialog | InstallPerUser    | \[ALLUSERS\]          | 2         | 1                         | 3     |
| VerifyReadyDialog | InstallPerMachine | SpawnDialog           | OutOfDisk | OutOfDiskSpace = 1        | 1     |
| VerifyReadyDialog | InstallPerMachine | EndDialog             | Return    | OutOfDiskSpace <> 1 | 3     |
| VerifyReadyDialog | InstallPerMachine | \[ALLUSERS\]          | 1         | 1                         | 2     |
| VerifyReadyDialog | InstallPerUser    | \[MSIFASTINSTALL\]    | 1         | 1                         | 4     |



 

The InstallPerUser control should be removed from the user interface of any installation using a Windows Installer version earlier than Windows Installer Windows Installer 5.0. The [ControlCondition](controlcondition-table.md) table in the sample package contains four entries that disable and hide the InstallPerUser control if the current version is less than Windows Installer 5.0. The table uses the value of the [**VersionMsi**](versionmsi.md) property and the [conditional statement syntax](conditional-statement-syntax.md) to define this condition. The action specified in the Action field is performed only if the statement in the Condition field is true.

[ControlCondition](controlcondition-table.md) Table (partial)

| Dialog\_          | Control\_      | Action  | Condition               |
|-------------------|----------------|---------|-------------------------|
| VerifyReadyDialog | InstallPerUser | Enable  | VersionMsi >= "5.00" |
| VerifyReadyDialog | InstallPerUser | Disable | VersionMsi < "5.00"  |
| VerifyReadyDialog | InstallPerUser | Show    | VersionMsi >= "5.00" |
| VerifyReadyDialog | InstallPerUser | Hide    | VersionMsi < "5.00"  |



 

## Specifying Directory Structure

Use the database editor to examine the [Directory](directory-table.md) table of PUASample1.msi. The record of the Directory Table having an empty string in its Directory\_Parent field represents the root directory of both the source and target directory trees. If the [**TARGETDIR**](targetdir.md) property is undefined, the installer sets its value at installation time to the value of the [**ROOTDRIVE**](rootdrive.md) property. If the [**SourceDir**](sourcedir.md) property is undefined, the installer sets its value to the location of the directory containing the Windows Installer package (.msi file.) The directory names are specified using the short\|long format.

[Directory](directory-table.md) Table (partial)

| Directory          | Directory\_Parent  | DefaultDir               |
|--------------------|--------------------|--------------------------|
| TARGETDIR          |                    | SourceDir                |
| ProgramFilesFolder | TARGETDIR          | .                        |
| ProgramMenuFolder  | TARGETDIR          | .                        |
| INSTALLLOCATION    | MyVendor           | Sample1\|MSDN-PUASample1 |
| MyVendor           | ProgramFilesFolder | Msft\|Microsoft          |



 

At the source, this [Directory](directory-table.md) table resolves to the following directory paths.

<dl> \[SourceDir\]\\Msft\\Sample1  
\[SourceDir\]  
</dl>

At the target, the [Directory](directory-table.md) table resolves to the paths in the following table. The installer sets the values of the [**ProgramFilesFolder**](programfilesfolder.md) and [**ProgramMenuFolder**](programmenufolder.md) properties to locations that depend upon the [installation context](installation-context.md) and whether the system is the 32-bit or 64-bit versions of Windows Server 2008 R2 and Windows 7. The paths to the target folders depend on whether the user selects a per-user or per-machine installation.

| Installation Context | System                                                                              | Example Paths                                                                                                                    |
|----------------------|-------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Per-Machine          | Windows Server 2008 R2 and Windows 7<br/> 32-bit version<br/>           | %ProgramFiles%\\Msft\\Sample1<br/> %ALLUSERSPROFILE%\\Microsoft\\Windows\\Start Menu\\Programs<br/>                  |
| Per-Machine          | Windows Server 2008 R2 and Windows 7<br/> 64-bit version<br/>           | %ProgramFiles(x86)%\\Msft\\Sample1<br/> %ALLUSERSPROFILE%\\Microsoft\\Windows\\Start Menu\\Programs<br/>             |
| Per-User             | Windows Server 2008 R2 and Windows 7<br/> 32-bit or 64-bit version<br/> | %USERPROFILE%\\AppData\\Local\\Programs\\Msft\\Sample1<br/> %APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs<br/> |



 

Per-user applications should be stored in subfolders under the Programs folder specified by the value of [**ProgramFilesFolder**](programfilesfolder.md) property. Typically, the path to the application takes the following form.

%LOCALAPPDATA%\\Programs\\*ISV name*\\*AppName*.

Per-user configuration data should be stored in the Programs folder specified by the value of the [**ProgramMenuFolder**](programmenufolder.md) property. Typically, this folder is located at the following path.

%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs

If installing [32-bit Windows Installer Package](32-bit-windows-installer-packages.md) components, use the [**ProgramFilesFolder**](programfilesfolder.md) and [**CommonFilesFolder**](commonfilesfolder.md) property in the [Directory](directory-table.md) table. If installing [64-bit Windows Installer Package](64-bit-windows-installer-packages.md) components, use the [**ProgramFiles64Folder**](programfiles64folder.md) and [**CommonFiles64Folder**](commonfiles64folder.md) properties. If your application contains 32-bit and 64-bit versions of the same component, with the same name, ensure that these versions are saved in different directories or give them different names.

The following [Directory](directory-table.md) table provides an example of a directory layout compatible with a package that includes 32-bit and 64-bit components and includes some components that are shared across applications.

| Directory            | Directory\_Parent    | DefaultDir                        |
|----------------------|----------------------|-----------------------------------|
| TARGETDIR            |                      | SourceDir                         |
| ProgramFilesFolder   | TARGETDIR            | .:Prog32                          |
| ProgramFiles64Folder | TARGETDIR            | .:Prog64                          |
| CommonFilesFolder    | TARGETDIR            | .:Share32                         |
| CommonFiles64Folder  | TARGETDIR            | .:Share64                         |
| ProgramMenuFolder    | TARGETDIR            | .:Sample1\|MSDN-PUASample1        |
| INSTALLLOCATION      | MyVendor             | Sample1\|MSDN-PUASample1          |
| INSTALLLOCATIONX64   | Vendorx64            | Sample1\|MSDN-PUASample1          |
| SHAREDLOCATION       | ShVendor             | Sample1\|MSDN-PUASample1          |
| SHAREDLOCATIONX64    | ShVendorx64          | Sample1\|MSDN-PUASample1          |
| MyVendor             | ProgramFilesFolder   | Msft\|Microsoft                   |
| Vendorx64            | ProgramFiles64Folder | Msft\|Microsoft                   |
| ShVendor             | CommonFilesFolder    | Msft\|Microsoft                   |
| ShVendorx64          | CommonFiles64Folder  | Msft\|Microsoft                   |
| Shrx86               | SHAREDLOCATION       | x32\|32-bit components            |
| Shrx64               | SHAREDLOCATIONX64    | x64\|64-bit components            |
| Binx86               | INSTALLLOCATION      | x32\|32-bit components            |
| Binx64               | INSTALLLOCATIONX64   | x64\|64-bit components            |
| App32                | Binx86               | myapp\|unshared 32-bit components |
| App64                | Binx64               | myapp\|unshared 64-bit components |
| Share32              | Shrx86               | shared\|shared 32-bit components  |
| Share64              | Shrx64               | shared\|shared 64-bit components  |



 

At the source, this [Directory](directory-table.md) table resolves to the following directory paths.

<dl> \[SourceDir\]Prog32\\Msft\\Sample1\\x32\\myapp  
\[SourceDir\]Share32\\Common Files\\Msft\\Sample1\\x32\\shared  
\[SourceDir\]Prog64\\Msft\\Sample1\\x64\\myapp  
\[SourceDir\]Share64\\Common Files\\Msft\\Sample1\\x64\\shared  
\[SourceDir\]Sample1  
</dl>

At the target, this [Directory](directory-table.md) table resolves to the following directory paths. The target paths depend on the [installation context](installation-context.md) and system.

| Installation Context | System                                                                              | Example Paths                                                                                                                                                                                                                                                                                                                                         |
|----------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Per-Machine          | Windows Server 2008 R2 and Windows 7<br/> 32-bit version<br/>           | %ProgramFiles%\\Msft\\Sample1\\x32\\myapp<br/> %ProgramFiles%\\Common Files\\Msft\\Sample1\\x32\\shared<br/> %ProgramFiles(x86)%\\Msft\\Sample1\\x64\\myapp<br/> %ProgramFiles(x86)%\\Common Files\\Msft\\Sample1\\x64\\shared<br/> %ProgramData%\\Microsoft\\Windows\\Start Menu\\Programs\\Sample1<br/>               |
| Per-Machine          | Windows Server 2008 R2 and Windows 7<br/> 64-bit version<br/>           | %ProgramFiles(x86)%\\Msft\\Sample1\\x32\\myapp<br/> %ProgramFiles(x86)%\\Common Files\\Msft\\Sample1\\x32\\shared<br/> %ProgramFiles%\\Msft\\Sample1\\x64\\myapp<br/> %ProgramFiles%\\Common Files\\Msft\\Sample1\\x64\\shared<br/> %ProgramData%\\Microsoft\\Windows\\Start Menu\\Programs\\Sample1<br/>               |
| Per-User             | Windows Server 2008 R2 and Windows 7<br/> 32-bit or 64-bit version<br/> | %LOCALAPPDATA%\\Programs\\Msft\\Sample1\\x32\\myapp<br/> %LOCALAPPDATA%\\Programs\\Common\\Msft\\Sample1\\x32\\shared<br/> %LOCALAPPDATA%\\Programs\\Msft\\Sample1\\x64\\myapp<br/> %LOCALAPPDATA%\\Programs\\Common\\Msft\\Sample1\\x64\\shared<br/> %APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Sample1<br/> |



 

## Application Registration

The PUASample.msi adds a subkey to the App Paths registry key for the application and performs registrations that enable application information to be saved in the registry under this key. For more information about App Paths and application registration, see the [PerceivedTypes, SystemFileAssociations, and Application Registration](/previous-versions/windows/desktop/legacy/cc144150(v=vs.85)) in the [shell extensibility](https://msdn.microsoft.com/library/bb762762.aspx) section of the [Shell Developer's Guide](/previous-versions/windows/desktop/legacy/bb776778(v=vs.85)). At installation time, the user makes the decision to install the application in either the per-user or per-machine installation context. At the time the dual-purpose package is authored, the package developer cannot know if the registrations should be performed under the HKEY\_LOCAL\_MACHINE or HKEY\_CURRENT\_USER keys.

The package developer defines the file identifier for the application's executable file in the File field of the [File](file-table.md) Table.

[File](file-table.md) Table (partial) 

| File      | Component\_      | FileName                     | FileSize | Version | Language | Attributes | Sequence |
|-----------|------------------|------------------------------|----------|---------|----------|------------|----------|
| MyAppFile | ProductComponent | PUASAMP1.EXE\|PUASample1.exe | 81920    |         |          | 0          | 1        |



 

Values to be saved in the registry can be specified in the Value field of the [Registry](registry-table.md) table as a [Formatted](formatted.md) string. Use the file identifier defined in the File field of the [File](file-table.md) table, and the \[\#*filekey*\] convention of the Formatted type, to specify the default value for the App Paths registry key. The top-level [INSTALL](install-action.md) action performs the actions in the [InstallExecuteSequence](installexecutesequence-table.md) table. After the [CostInitialize](costinitialize-action.md), [FileCost](filecost-action.md), and [InstallFinalize](installfinalize-action.md) actions in this table have completed, the Windows Installer replaces the formatted substring \[\#MyAppFile\] in the Registry table with the full path to the application file.

The sample defines a custom property, RegRoot, to contain the location of the root key and uses a custom action to reset the property value if the user chooses a per-machine installation. Use the custom property, RegRoot, in any formatted string values that reference the root location. In the [Property](property-table.md) table the PUASample.msi package defines the custom property and sets the value of RegRoot to HKCU. This initializes the value of the property for the per-user installation context, the recommended default context for dual-purpose packages.

[Property](property-table.md) Table (partial)

| Property | Value |
|----------|-------|
| RegRoot  | HKCU  |



 

In the [CustomAction](customaction-table.md) table the package defines a custom action named Set\_RegRoot\_HKLM. The value in the Type field identifies this as a [Custom Action Type 51](custom-action-type-51.md) standard custom action. The meaning of the Source and Target fields in the CustomAction table depend upon the custom action type. For more information about the standard types of custom actions, see [Custom Action Types](summary-list-of-all-custom-action-types.md). The Source field for the Set\_RegRoot\_HKLM custom action specifies that the value of the RegRoot property. If the installer performs the Set\_RegRoot\_HKLM custom action, this resets the value of the RegRoot property to HKLM.

[CustomAction](customaction-table.md) Table (partial)

| Action             | Type | Source      | Target |
|--------------------|------|-------------|--------|
| Set\_RegRoot\_HKLM | 51   | \[RegRoot\] | HKLM   |



 

The top-level [INSTALL](install-action.md) action performs the actions in the [InstallExecuteSequence](installexecutesequence-table.md) table, in the sequence specified in the Sequence field of that table. The value authored in the Sequence field for the Set\_RegRoot\_HKLM custom action (1501) specifies that this custom action be performed after the [InstallInitialize](installinitialize-action.md) action (1500) and before the [ProcessComponents](processcomponents-action.md) action (1600.) This sequence ensures that the record for the Set\_RegRoot\_HKLM custom action is evaluated at installation time. For more information about the recommended sequence of actions in the InstallExecuteSequence table, see the [Suggested InstallExecuteSequence](suggested-installexecutesequence.md) topic. The [conditional statement syntax](conditional-statement-syntax.md) authored in the Condition field specifies that the Set\_RegRoot\_HKLM action be performed only if the value of the [**ALLUSERS**](allusers.md) property evaluates to 1 at installation time. An **ALLUSERS** property value of 1 specifies a per-machine installation.

[InstallExecuteSequence](installexecutesequence-table.md) Table (partial)

| Action             | Condition  | Sequence |
|--------------------|------------|----------|
| Set\_RegRoot\_HKLM | ALLUSERS=1 | 1501     |



 

The following records in the [Registry](registry-table.md) table perform the registrations if the ProductComponent component is installed. The value -1 in the Root field is required to perform the registration under HKEY\_LOCAL\_MACHINE for a per-user installation and under HKEY\_CURRENT\_USER for a per-user installation. The record with an empty string in the Registry field adds a subkey for the application under the AppPaths registry key and sets the "(Default)" value to the full path of the application's executable file. The MyAppPathAlias registration maps the executable file to an application alias and enables the application to be launched if the user types the alias "puapct" at a command line prompt. The MyAppPathRegistration registration maps the name of the executable file to the file's full path.



| Registry              | Root | Key                                                                     | Name | Value                                                                            | Component        |
|-----------------------|------|-------------------------------------------------------------------------|------|----------------------------------------------------------------------------------|------------------|
|                       | -1   | Software\\Microsoft\\MyAppPathRegistrationLocation                      |      | \[RegRoot\]\\Software\\Microsoft\\Windows\\CurrentVersion\\App Paths\\PUAPCT.exe | ProductComponent |
| MyAppPathAlias        | -1   | Software\\Microsoft\\Windows\\CurrentVersion\\App Paths\\PUAPCT.exe     |      | \[\#MyAppFile\]                                                                  | ProductComponent |
| MyAppPathRegistration | -1   | Software\\Microsoft\\Windows\\CurrentVersion\\App Paths\\PUASample1.exe |      | \[\#MyAppFile\]                                                                  | ProductComponent |



 

## AutoPlay Cancel Registration

The PUASample.msi performs registrations that enable the application user to prevent [Hardware Autoplay](/previous-versions/windows/desktop/legacy/cc144210(v=vs.85)) from launching for selected devices. For information about registering a handler to cancel Autoplay in response to an event, see the [Preparing Hardware and Software for Use with AutoPlay](/previous-versions//cc144208(v=vs.85)) topic in the [shell extensibility](https://msdn.microsoft.com/library/bb762762.aspx) section of the [Shell Developer's Guide](/previous-versions/windows/desktop/legacy/bb776778(v=vs.85)). The following record registers the handler specified in the Name field when the ProductComponent component is installed. The value -1 in the Root field is required to specify to the Windows Installer that the registration should be redirected to a location that depends upon the installation context.

[Registry](registry-table.md) Table 

| Registry                     | Root | Key                                                                                             | Name                                 | Value | Component        |
|------------------------------|------|-------------------------------------------------------------------------------------------------|--------------------------------------|-------|------------------|
| MyAutoplayCancelRegistration | -1   | SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\AutoplayHandlers\\CancelAutoplay\\CLSID | 66A32FE6-229D-427b-A608-D273F40C034C |       | ProductComponent |



 

## Preview Handler Registration

The PUASample.msi performs registrations that are required to install a [preview handler](../shell/preview-handlers.md) that enables a read-only preview of .pua files without launching the application. For information about registering preview handlers, see the [Registering Preview Handlers](../shell/how-to-register-a-preview-handler.md) topic in the [shell extensibility](https://msdn.microsoft.com/library/bb762762.aspx) section of the [Shell Developer's Guide](/previous-versions/windows/desktop/legacy/bb776778(v=vs.85)). The following records in the [Registry](registry-table.md) table register the handler when the ProductComponent component is installed. The value -1 in the Root field is required to specify to the Windows Installer that the registration should be redirected to a location that depends upon the installation context.

[Registry](registry-table.md) Table

| Registry                       | Root | Key                                                                              | Name                                   | Value                                        | Component        |
|--------------------------------|------|----------------------------------------------------------------------------------|----------------------------------------|----------------------------------------------|------------------|
| MyPreviewHandlerRegistration1  | -1   | Software\\Classes\\.pua                                                          |                                        | puafile                                      | ProductComponent |
| MyPreviewHandlerRegistration2  | -1   | Software\\Microsoft\\Windows\\CurrentVersion\\PreviewHandlers                    | {1531d583-8375-4d3f-b5fb-d23bbd169f22} | Microsoft Windows PUA TEST Preview Handler   | ProductComponent |
| MyPreviewHandlerRegistration3  | -1   | Software\\Classes\\puafile\\ShellEx\\{8895b1c6-b41f-4c1c-a562-0d564250836f}      |                                        | {1531d583-8375-4d3f-b5fb-d23bbd169f22}       | ProductComponent |
| MyPreviewHandlerRegistration4  | -1   | Software\\Classes\\CLSID\\{1531d583-8375-4d3f-b5fb-d23bbd169f22}                 |                                        | Per-User Applicaton Sample 1 Preview Handler | ProductComponent |
| MyPreviewHandlerRegistration5  | -1   | Software\\Classes\\CLSID\\{1531d583-8375-4d3f-b5fb-d23bbd169f22}                 | AppID                                  | {6d2b5079-2f0b-48dd-ab7f-97cec514d30b}       | ProductComponent |
| MyPreviewHandlerRegistration6  | -1   | Software\\Classes\\CLSID\\{1531d583-8375-4d3f-b5fb-d23bbd169f22}                 | DisplayName                            | @shell32,-38242                              | ProductComponent |
| MyPreviewHandlerRegistration7  | -1   | Software\\Classes\\CLSID\\{1531d583-8375-4d3f-b5fb-d23bbd169f22}                 | Icon                                   | notepad.exe,2                                | ProductComponent |
| MyPreviewHandlerRegistration8  | -1   | Software\\Classes\\CLSID\\{1531d583-8375-4d3f-b5fb-d23bbd169f22}\\InProcServer32 | ThreadingModel                         | Apartment                                    | ProductComponent |
| MyPreviewHandlerRegistration9  | -1   | Software\\Classes\\CLSID\\{1531d583-8375-4d3f-b5fb-d23bbd169f22}\\InProcServer32 |                                        | \#%%SystemRoot%\\system32\\shell32.dll       | ProductComponent |
| MyPreviewHandlerRegistration10 | -1   | Software\\Classes\\CLSID\\{1531d583-8375-4d3f-b5fb-d23bbd169f22}\\InProcServer32 | ProgID                                 | puafile                                      | ProductComponent |



 

 

 
