---
title: Reinstall method of the Win32\_SoftwareFeature class
description: The Reinstall WMI class method reinstalls the associated instance of Win32\_SoftwareFeature using the specified reinstallation mode.
ms.assetid: 4882772b-23e6-4240-993a-e5e544297af7
keywords:
- Reinstall method
- Reinstall method, Win32_SoftwareFeature class
- Win32_SoftwareFeature class, Reinstall method
topic_type:
- apiref
api_name:
- Win32_SoftwareFeature.Reinstall
api_location:
- Msiprov.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Reinstall method of the Win32\_SoftwareFeature class

The **Reinstall** [WMI class](https://msdn.microsoft.com/library/aa393244) method reinstalls the associated instance of [**Win32\_SoftwareFeature**](win32-softwarefeature.md) using the specified reinstallation mode.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

## Syntax


```mof
uint32 Reinstall(
  [in] uint16 ReinstallMode
);
```



## Parameters

<dl> <dt>

*ReinstallMode* \[in\]
</dt> <dd>

Reinstallation mode. Can be one of the following values.



| Value                                                                                                  | Meaning                     |
|--------------------------------------------------------------------------------------------------------|-----------------------------|
| <span id="1"></span><dl> <dt>**1**</dt> </dl>   | FileMissing<br/>      |
| <span id="2"></span><dl> <dt>**2**</dt> </dl>   | FileOlderVersion<br/> |
| <span id="3"></span><dl> <dt>**3**</dt> </dl>   | FileEqualVersion<br/> |
| <span id="4"></span><dl> <dt>**4**</dt> </dl>   | FileExact<br/>        |
| <span id="5"></span><dl> <dt>**5**</dt> </dl>   | FileVerify<br/>       |
| <span id="6"></span><dl> <dt>**6**</dt> </dl>   | FileReplace<br/>      |
| <span id="7"></span><dl> <dt>**7**</dt> </dl>   | UserData<br/>         |
| <span id="8"></span><dl> <dt>**8**</dt> </dl>   | MachineData<br/>      |
| <span id="9"></span><dl> <dt>**9**</dt> </dl>   | Shortcut<br/>         |
| <span id="10"></span><dl> <dt>**10**</dt> </dl> | Package<br/>          |



 

</dd> </dl>

## Return value



| Return code                                                                               | Description                        |
|-------------------------------------------------------------------------------------------|------------------------------------|
| <dl> <dt>**0**</dt> </dl>          | Successful completion.<br/>  |
| <dl> <dt>**2147549445**</dt> </dl> | RPC Server Fault Error.<br/> |



 

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                         |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>Msi.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>Msiprov.dll</dt> </dl> |



## See also

<dl> <dt>

[Installed Applications Classes](https://msdn.microsoft.com/library/aa390887)
</dt> <dt>

[**Win32\_SoftwareFeature**](win32-softwarefeature.md)
</dt> </dl>

 

 





