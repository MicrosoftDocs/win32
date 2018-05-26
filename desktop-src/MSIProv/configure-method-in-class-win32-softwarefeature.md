---
title: Configure method of the Win32\_SoftwareFeature class
description: The Configure WMI class method configures the associated instance of Win32\_SoftwareFeature to the specified install state.
ms.assetid: fc1248db-b2a1-42bc-a99f-f3c4970b38c8
keywords:
- Configure method
- Configure method, Win32_SoftwareFeature class
- Win32_SoftwareFeature class, Configure method
topic_type:
- apiref
api_name:
- Win32_SoftwareFeature.Configure
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

# Configure method of the Win32\_SoftwareFeature class

The **Configure** [WMI class](https://msdn.microsoft.com/library/aa393244) method configures the associated instance of [**Win32\_SoftwareFeature**](win32-softwarefeature.md) to the specified install state.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 Configure(
   uint16 InstallState
);
```



## Parameters

<dl> <dt>

*InstallState* 
</dt> <dd>

Installation state. Can be any of the following values.



| Value                                                                                                | Meaning              |
|------------------------------------------------------------------------------------------------------|----------------------|
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | Default <br/>  |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | Advertise<br/> |
| <span id="3"></span><dl> <dt>**3**</dt> </dl> | Local<br/>     |
| <span id="4"></span><dl> <dt>**4**</dt> </dl> | Absent<br/>    |
| <span id="5"></span><dl> <dt>**5**</dt> </dl> | Source<br/>    |



 

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

 

 





