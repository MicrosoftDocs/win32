---
title: CreateRestorePoint method of the SystemRestore class
description: Creates a restore point.
ms.assetid: 30e1ff03-816c-463f-9f80-6d84149f0e0b
keywords:
- CreateRestorePoint method System Restore
- CreateRestorePoint method System Restore , SystemRestore class
- SystemRestore class System Restore , CreateRestorePoint method
topic_type:
- apiref
api_name:
- SystemRestore.CreateRestorePoint
api_location:
- Root\Default
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# CreateRestorePoint method of the SystemRestore class

Creates a restore point.

This method is the scriptable equivalent of the [**SRSetRestorePoint**](/windows/desktop/api/SRRestorePtAPI/nf-srrestoreptapi-srsetrestorepointa) function.

## Syntax


```mof
uint32 CreateRestorePoint(
  [in] String Description,
  [in] uint32 RestorePointType,
  [in] uint32 EventType
);
```



## Parameters

<dl> <dt>

*Description* \[in\]
</dt> <dd>

The description to be displayed so the user can easily identify a restore point. The maximum length of an ANSI string is MAX\_DESC. The maximum length of a Unicode string is MAX\_DESC\_W. For more information, see [Restore Point Description Text](restore-point-description-text.md).

</dd> <dt>

*RestorePointType* \[in\]
</dt> <dd>

The type of restore point. This member can be one of the following values.



| Restore point type                                                                                                                                                                                                                             | Meaning                                                                                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="APPLICATION_INSTALL"></span><span id="application_install"></span><dl> <dt>**APPLICATION\_INSTALL**</dt> <dt>0</dt> </dl>         | An application has been installed.<br/>                                                                                                                |
| <span id="APPLICATION_UNINSTALL"></span><span id="application_uninstall"></span><dl> <dt>**APPLICATION\_UNINSTALL**</dt> <dt>1</dt> </dl>   | An application has been uninstalled.<br/>                                                                                                              |
| <span id="DEVICE_DRIVER_INSTALL"></span><span id="device_driver_install"></span><dl> <dt>**DEVICE\_DRIVER\_INSTALL**</dt> <dt>10</dt> </dl> | A device driver has been installed.<br/>                                                                                                               |
| <span id="MODIFY_SETTINGS"></span><span id="modify_settings"></span><dl> <dt>**MODIFY\_SETTINGS**</dt> <dt>12</dt> </dl>                    | An application has had features added or removed.<br/>                                                                                                 |
| <span id="CANCELLED_OPERATION"></span><span id="cancelled_operation"></span><dl> <dt>**CANCELLED\_OPERATION**</dt> <dt>13</dt> </dl>        | An application needs to delete the restore point it created. For example, an application would use this flag when a user cancels an installation.<br/> |



 

</dd> <dt>

*EventType* \[in\]
</dt> <dd>

The type of event. This member can be one of the following values.



| Event type                                                                                                                                                                                                                                                      | Meaning                                                                                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="BEGIN_NESTED_SYSTEM_CHANGE"></span><span id="begin_nested_system_change"></span><dl> <dt>**BEGIN\_NESTED\_SYSTEM\_CHANGE**</dt> <dt>102</dt> </dl> | A system change has begun. A subsequent nested call does not create a new restore point. <br/> Subsequent calls must use END\_NESTED\_SYSTEM\_CHANGE, not END\_SYSTEM\_CHANGE.<br/> |
| <span id="BEGIN_SYSTEM_CHANGE"></span><span id="begin_system_change"></span><dl> <dt>**BEGIN\_SYSTEM\_CHANGE**</dt> <dt>100</dt> </dl>                       | A system change has begun. <br/> A subsequent call must use END\_SYSTEM\_CHANGE, not END\_NESTED\_SYSTEM\_CHANGE.<br/>                                                              |
| <span id="END_NESTED_SYSTEM_CHANGE"></span><span id="end_nested_system_change"></span><dl> <dt>**END\_NESTED\_SYSTEM\_CHANGE**</dt> <dt>103</dt> </dl>       | A system change has ended.<br/>                                                                                                                                                           |
| <span id="END_SYSTEM_CHANGE"></span><span id="end_system_change"></span><dl> <dt>**END\_SYSTEM\_CHANGE**</dt> <dt>101</dt> </dl>                             | A system change has ended.<br/>                                                                                                                                                           |



 

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the method returns one of the COM error codes defined in WinError.h.

## Remarks

**Windows 8:  **

A new registry key enables application developers to change the frequency of restore-point creation.

Applications should create this key to use it because it will not preexist in the system. The following will apply by default if the key does not exist. If an application calls the **CreateRestorePoint** method to create a restore point, Windows skips creating this new restore point if any restore points have been created in the last 24 hours. The **CreateRestorePoint** method returns **S\_OK**.

Developers can write applications that create the **DWORD** value **SystemRestorePointCreationFrequency** under the registry key **HKLM\\Software\\Microsoft\\Windows NT\\CurrentVersion\\SystemRestore**. The value of this registry key can change the frequency of restore point creation. The value of this registry key can change the frequency of restore point creation.

If the application calls **CreateRestorePoint** to create a restore point, and the registry key value is 0, system restore does not skip creating the new restore point.

If the application calls **CreateRestorePoint** to create a restore point, and the registry key value is the integer N, system restore skips creating a new restore point if any restore points were created in the previous N minutes.

## Examples


```VB
'CreateRestorePoint Method of the SystemRestore Class
'Creates a restore point. Specifies the beginning and 
'the ending of a set of changes so that System Restore 
'can create a restore point.This method is the 
'scriptable equivalent of the SRSetRestorePoint function.

Set Args = wscript.Arguments
If Args.Count() > 0 Then
    RpName = Args.item(0)
Else 
    RpName = "Vbscript"
End If

Set obj = GetObject("winmgmts:{impersonationLevel=impersonate}!root/default:SystemRestore")

If (obj.CreateRestorePoint(RpName, 0, 100)) = 0 Then
    wscript.Echo "Success"
Else 
    wscript.Echo "Failed"
End If
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | None supported<br/>                                                         |
| Namespace<br/>                | Root\\Default<br/>                                                          |
| MOF<br/>                      | <dl> <dt>Sr.mof</dt> </dl> |



## See also

<dl> <dt>

[**SystemRestore**](systemrestore.md)
</dt> </dl>

 

 





