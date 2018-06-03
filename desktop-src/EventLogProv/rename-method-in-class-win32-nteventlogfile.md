---
Description: Renames the logical file (or directory) specified in the Win32\_NTEventlogFile.Name property.
ms.assetid: 2455e23d-e1d3-4e23-bfdf-a9cb04549e34
title: Rename method of the Win32\_NTEventlogFile class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Rename method of the Win32\_NTEventlogFile class

The **Rename** [WMI class](https://msdn.microsoft.com/library/aa393244) method renames the logical file (or directory) specified in the **Win32\_NTEventlogFile.Name** property. A rename is not supported if the destination is on another drive or if overwriting an existing logical file is required.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 Rename(
  [in] string FileName
);
```



## Parameters

<dl> <dt>

*FileName* \[in\]
</dt> <dd>

Fully qualified new name of the file (or directory).

Example: c:\\temp\\newfile.txt

</dd> </dl>

## Return value



| Return code                                                                       | Description                                                    |
|-----------------------------------------------------------------------------------|----------------------------------------------------------------|
| <dl> <dt>**0**</dt> </dl>  | The request was successful.<br/>                         |
| <dl> <dt>**2**</dt> </dl>  | Access was denied.<br/>                                  |
| <dl> <dt>**8**</dt> </dl>  | An unspecified failure occurred.<br/>                    |
| <dl> <dt>**9**</dt> </dl>  | The name specified was not valid.<br/>                   |
| <dl> <dt>**10**</dt> </dl> | The object specified already exists.<br/>                |
| <dl> <dt>**11**</dt> </dl> | The file system is not NTFS.<br/>                        |
| <dl> <dt>**12**</dt> </dl> | The platform is not Windows.<br/>                        |
| <dl> <dt>**13**</dt> </dl> | The drive is not the same.<br/>                          |
| <dl> <dt>**14**</dt> </dl> | The directory is not empty.<br/>                         |
| <dl> <dt>**15**</dt> </dl> | There has been a sharing violation.<br/>                 |
| <dl> <dt>**16**</dt> </dl> | The start file specified was not valid.<br/>             |
| <dl> <dt>**17**</dt> </dl> | A privilege required for the operation is not held.<br/> |
| <dl> <dt>**21**</dt> </dl> | A parameter specified is not valid.<br/>                 |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                       |
| Namespace<br/>                | Root\\CIMV2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Ntevt.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ntevt.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> <dt>

[**Win32\_NTEventlogFile**](win32-nteventlogfile.md)
</dt> </dl>

 

 




