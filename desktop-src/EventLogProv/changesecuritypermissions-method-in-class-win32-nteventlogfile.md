---
Description: 'Changes the security permissions for the logical file specified in the Win32\_NTEventlogFile.Name property.'
ms.assetid: '5730986d-f963-4722-a23c-68e17517cbb4'
title: 'ChangeSecurityPermissions method of the Win32\_NTEventlogFile class'
---

# ChangeSecurityPermissions method of the Win32\_NTEventlogFile class

The **ChangeSecurityPermissions**  [WMI class](https://msdn.microsoft.com/library/aa393244) method changes the security permissions for the logical file specified in the **Win32\_NTEventlogFile.Name** property. If the logical file is a directory, then **ChangeSecurityPermissions** is recursive, and changes the security permissions of all of the files and subdirectories that the directory contains. **ChangeSecurityPermissions** returns an integer value of 0 (zero) if the permissions are changed, and a different number to indicate an error.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 ChangeSecurityPermissions(
  [in] Win32_SecurityDescriptor SecurityDescriptor,
  [in] uint32 Option
);
```



## Parameters

<dl> <dt>

*SecurityDescriptor* \[in\]
</dt> <dd>

Expression that resolves to an instance of [**Win32\_SecurityDescriptor**](https://msdn.microsoft.com/library/aa394402). This descriptor contains new security permissions for the instance of [**Win32\_PageFile**](https://msdn.microsoft.com/library/aa394243).

</dd> <dt>

*Option* \[in\]
</dt> <dd>

Actual security privilege to be modified. For example, to change the owner and discretionary access control list (DACL) security, use:

`Option = 1 + 4`

-or-

`Option = CHANGE_OWNER_SECURITY_INFORMATION | CHANGE_DACL_SECURITY_INFORMATION`



| Value used to set the bit                                                                                                                                                                                                                                                                | Meaning                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| <span id="CHANGE_OWNER_SECURITY_INFORMATION"></span><span id="change_owner_security_information"></span><dl> <dt>**CHANGE\_OWNER\_SECURITY\_INFORMATION**</dt> <dt>1</dt> </dl>       | Change the owner of the logical file. <br/>                             |
| <span id="CHANGE_GROUP_SECURITY_INFORMATION"></span><span id="change_group_security_information"></span><dl> <dt>**CHANGE\_GROUP\_SECURITY\_INFORMATION**</dt> <dt>2</dt> </dl>       | Change the group of the logical file. <br/>                             |
| <span id="CHANGE_DACL_SECURITY_INFORMATION"></span><span id="change_dacl_security_information"></span><dl> <dt>**CHANGE\_DACL\_SECURITY\_INFORMATION**</dt> <dt>4</dt> </dl>          | Change the DACL of the logical file. <br/>                              |
| <span id="CHANGE_SACL_SECURITY_INFORMATION____"></span><span id="change_sacl_security_information____"></span><dl> <dt>**CHANGE\_SACL\_SECURITY\_INFORMATION** </dt> <dt>8</dt> </dl> | Change the system access control list (SACL) of the logical file. <br/> |



 

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
| <dl> <dt>**21**</dt> </dl> | A specified parameter is not valid.<br/>                 |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                       |
| Namespace<br/>                | Root\\CIMV2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Ntevt.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ntevt.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_NTEventlogFile**](win32-nteventlogfile.md)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> <dt>

[**Win32\_NTEventlogFile**](https://msdn.microsoft.com/library/aa394438)
</dt> </dl>

 

 




