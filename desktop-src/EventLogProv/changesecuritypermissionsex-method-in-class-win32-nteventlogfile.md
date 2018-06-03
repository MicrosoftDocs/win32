---
Description: Changes the security permissions for the logical file that is specified in the Win32\_NTEventlogFile.Name property (this method is an extended version of the ChangeSecurityPermissions method).
ms.assetid: 00c516aa-77e5-4d30-8a60-e00d6109aa47
title: ChangeSecurityPermissionsEx method of the Win32\_NTEventlogFile class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ChangeSecurityPermissionsEx method of the Win32\_NTEventlogFile class

The **ChangeSecurityPermissionsEx** [WMI class](https://msdn.microsoft.com/library/aa393244) method changes the security permissions for the logical file that is specified in the **Win32\_NTEventlogFile.Name** property (this method is an extended version of the [**ChangeSecurityPermissions**](https://msdn.microsoft.com/library/aa384887) method). If the logical file is a directory, then this method is recursive and changes the security permissions of all of the files and subdirectories that the directory contains.

## Syntax


```mof
uint32 ChangeSecurityPermissionsEx(
  [in]           Win32_SecurityDescriptor SecurityDescriptor,
  [in]           uint32 Option,
  [out]          string StopFileName,
  [in, optional] string StartFileName,
  [in, optional] boolean Recursive
);
```



## Parameters

<dl> <dt>

*SecurityDescriptor* \[in\]
</dt> <dd>

Expression that resolves to an instance of [**Win32\_SecurityDescriptor**](https://msdn.microsoft.com/library/aa394402). This parameter contains new security permissions for the instance of [**Win32\_PageFile**](https://msdn.microsoft.com/library/aa394243).

</dd> <dt>

*Option* \[in\]
</dt> <dd>

Security privilege to be modified. For example, to change the owner and discretionary access control list (DACL) security, use the following:

`Option = 1 + 4`

-or-

`Option = CHANGE_OWNER_SECURITY_INFORMATION | CHANGE_DACL_SECURITY_INFORMATION`



| Value used to set the bit                                                                                                                                                                                                                                                                | Meaning                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| <span id="CHANGE_OWNER_SECURITY_INFORMATION"></span><span id="change_owner_security_information"></span><dl> <dt>**CHANGE\_OWNER\_SECURITY\_INFORMATION**</dt> <dt>1</dt> </dl>       | Change the owner of the logical file. <br/>                             |
| <span id="CHANGE_GROUP_SECURITY_INFORMATION"></span><span id="change_group_security_information"></span><dl> <dt>**CHANGE\_GROUP\_SECURITY\_INFORMATION**</dt> <dt>2</dt> </dl>       | Change the group of the logical file. <br/>                             |
| <span id="CHANGE_DACL_SECURITY_INFORMATION"></span><span id="change_dacl_security_information"></span><dl> <dt>**CHANGE\_DACL\_SECURITY\_INFORMATION**</dt> <dt>4</dt> </dl>          | Change the DACL of the logical file. <br/>                              |
| <span id="CHANGE_SACL_SECURITY_INFORMATION____"></span><span id="change_sacl_security_information____"></span><dl> <dt>**CHANGE\_SACL\_SECURITY\_INFORMATION** </dt> <dt>8</dt> </dl> | Change the system access control list (SACL) of the logical file. <br/> |



 

</dd> <dt>

*StopFileName* \[out\]
</dt> <dd>

Name of the file or directory where the **ChangeSecurityPermissionsEx** method failed. This parameter is null if the method succeeds.

</dd> <dt>

*StartFileName* \[in, optional\]
</dt> <dd>

Names the child file or directory to use as a starting point for **ChangeSecurityPermissionsEx**. Typically, the *StartFileName* parameter is the *StopFileName* parameter that specifies the file or directory where an error occurs from the previous method call. If this parameter is null, the operation is performed on the file or directory specified in the [**ExecMethod**](https://msdn.microsoft.com/library/aa392103) call.

</dd> <dt>

*Recursive* \[in, optional\]
</dt> <dd>

If **true**, the change of ownership is applied recursively to files and directories within the directory specified by the [**CIM\_LogicalFile**](https://msdn.microsoft.com/library/aa387893) instance. For file instances, the *Recursive* input parameter is ignored.

</dd> </dl>

## Return value



| Return code                                                                       | Description                                                    |
|-----------------------------------------------------------------------------------|----------------------------------------------------------------|
| <dl> <dt>**0**</dt> </dl>  | The request is successful.<br/>                          |
| <dl> <dt>**2**</dt> </dl>  | Access is denied.<br/>                                   |
| <dl> <dt>**8**</dt> </dl>  | An unspecified failure occurred.<br/>                    |
| <dl> <dt>**9**</dt> </dl>  | The specified name is not valid.<br/>                    |
| <dl> <dt>**10**</dt> </dl> | The specified object already exists.<br/>                |
| <dl> <dt>**11**</dt> </dl> | The file system is not an NTFS file system.<br/>         |
| <dl> <dt>**12**</dt> </dl> | The platform is not Windows.<br/>                        |
| <dl> <dt>**13**</dt> </dl> | The drive is not the same.<br/>                          |
| <dl> <dt>**14**</dt> </dl> | The directory is not empty.<br/>                         |
| <dl> <dt>**15**</dt> </dl> | There is a sharing violation.<br/>                       |
| <dl> <dt>**16**</dt> </dl> | The specified start file is not valid.<br/>              |
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

 

 




