---
description: The ProvideAssembly method of the Installer object returns the installed path of an assembly.
ms.assetid: c99b1934-3834-478b-ab1d-7e7583dba779
title: Installer::ProvideAssembly method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Installer.ProvideAssembly
api_type: 
- COM
api_location: 
- Msi.dll
---

# Installer::ProvideAssembly method

The **ProvideAssembly** method of the [**Installer**](installer-object.md) object returns the installed path of an assembly.

## Syntax


```JScript
retVal = .ProvideAssembly(
  assembly,
  appContext,
  installMode,
  assemblyInfo
)
```



## Parameters

<dl> <dt>

*assembly* 
</dt> <dd>

The strong name of installed assembly that is to be queried.

</dd> <dt>

*appContext* 
</dt> <dd>

Set to null for global assemblies. For private assemblies, set *appContext* to the full path of the application configuration file or to the full path of the executable file of the application to which the assembly has been made private.

</dd> <dt>

*installMode* 
</dt> <dd>

Defines the installation mode. This parameter can be one of the following values.



| Value                                                                                                                                                                                                                                                                                                                                                                              | Meaning                                                                                                                                                                                   |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="msiInstallModeDefault"></span><span id="msiinstallmodedefault"></span><span id="MSIINSTALLMODEDEFAULT"></span><dl> <dt>**msiInstallModeDefault**</dt> <dt>0</dt> </dl>                                                                                                | Provide the component and perform any installation necessary to provide the component. <br/>                                                                                        |
| <span id="msiInstallModeExisting"></span><span id="msiinstallmodeexisting"></span><span id="MSIINSTALLMODEEXISTING"></span><dl> <dt>**msiInstallModeExisting**</dt> <dt>-1</dt> </dl>                                                                                           | Provide the component only if the feature exists. This option will verify that the assembly exists.<br/>                                                                            |
| <span id="msiInstallModeNoDetection"></span><span id="msiinstallmodenodetection"></span><span id="MSIINSTALLMODENODETECTION"></span><dl> <dt>**msiInstallModeNoDetection**</dt> <dt>-2</dt> </dl>                                                                               | Provide the component only if the feature exists. This option does not verify that the assembly exists.<br/>                                                                        |
| <span id="msiInstallModeNoSourceResolution"></span><span id="msiinstallmodenosourceresolution"></span><span id="MSIINSTALLMODENOSOURCERESOLUTION"></span><dl> <dt>**msiInstallModeNoSourceResolution**</dt> <dt>-3</dt> </dl>                                                   | Provides the assembly only if the assembly is installed local.<br/>                                                                                                                 |
| <span id="Combination_of_the_flags_used_by_ReinstallFeature"></span><span id="combination_of_the_flags_used_by_reinstallfeature"></span><span id="COMBINATION_OF_THE_FLAGS_USED_BY_REINSTALLFEATURE"></span><dl> <dt>**Combination of the flags used by [**ReinstallFeature**](installer-reinstallfeature.md)**</dt> </dl> | Calls the [**ReinstallFeature**](installer-reinstallfeature.md) method to reinstall the feature using this parameter for *ReinstallMode*, and then returns the assembly path.<br/> |



 

</dd> <dt>

*assemblyInfo* 
</dt> <dd>

Assembly information and assembly type. Set to one of the following values.



| Value                                                                                                                                                                                                                                                                                       | Meaning                                   |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| <span id="msiProvideAssemblyNet"></span><span id="msiprovideassemblynet"></span><span id="MSIPROVIDEASSEMBLYNET"></span><dl> <dt>**msiProvideAssemblyNet**</dt> <dt>0</dt> </dl>         | A .NET assembly.<br/>               |
| <span id="msiProvideAssemblyWin32"></span><span id="msiprovideassemblywin32"></span><span id="MSIPROVIDEASSEMBLYWIN32"></span><dl> <dt>**msiProvideAssemblyWin32**</dt> <dt>1</dt> </dl> | A Win32 side-by-side assembly.<br/> |



 

</dd> </dl>

## Return value

The path to the installed assembly.

## Remarks

The **ProvideAssembly** method uses the [**MsiProvideAssembly**](/windows/desktop/api/Msi/nf-msi-msiprovideassemblya) function.

## Examples

The following sample script demonstrates the use of the ProvideAssembly method.


```VB
Dim installer
Set installer = CreateObject("WindowsInstaller.Installer")

'
' ProvideAssembly - .NET global
'   
MsgBox Installer.ProvideAssembly("System.Security,Version=""1.0.5000.0"",PublicKeyToken=""b03f5f7f11d50a3a"",Culture=""neutral"",FileVersion=""1.1.4322.573""", vbNullString, 0, 0)

'
' ProvideAssembly - .NET private
'   
MsgBox Installer.ProvideAssembly("Sample,Version=""1.0.0.0"",Culture=""neutral""", "C:\Program Files\Microsoft\Sample\Sample.exe", 0, 0)

'
' ProvideAssembly - win32 global
'
MsgBox Installer.ProvideAssembly("Microsoft.MSXML2,publicKeyToken=""6bd6b9abf345378f"",version=""4.1.0.0"",type=""win32"",processorArchitecture=""x86""", vbNullString , -2, 1)
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer 4.5 on Windows Server 2003 and Windows XP<br/> |
| DLL<br/>     | <dl> <dt>Msi.dll</dt> </dl>                                                                                                                                                                           |
| IID<br/>     | IID\_IInstaller is defined as 000C1090-0000-0000-C000-000000000046<br/>                                                                                                                                                                                |



## See also

<dl> <dt>

[**Installer**](installer-object.md)
</dt> <dt>

[Not Supported in Windows Installer 3.1 and earlier versions](not-supported-in-windows-installer-version-3-1.md)
</dt> </dl>

 

 




