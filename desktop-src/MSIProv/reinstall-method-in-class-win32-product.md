---
title: Reinstall method of the Win32\_Product class
description: Using the specified reinstallation mode, the Reinstall WMI class method reinstalls the associated instance of Win32\_Product.
ms.assetid: 9b835c44-9efe-4131-b9ca-ef2efa567955
keywords:
- Reinstall method
- Reinstall method, Win32_Product class
- Win32_Product class, Reinstall method
topic_type:
- apiref
api_name:
- Win32_Product.Reinstall
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

# Reinstall method of the Win32\_Product class

Using the specified reinstallation mode, the **Reinstall** [WMI class](https://msdn.microsoft.com/library/aa393244) method reinstalls the associated instance of [**Win32\_Product**](win32-product.md).

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

This topic uses Managed Object Format (MOF) syntax. For more information about using this method,see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 Reinstall(
  [in] uint32 ReinstallMode
);
```



## Parameters

<dl> <dt>

*ReinstallMode* \[in\]
</dt> <dd>

The reinstallation mode. Can be one of the following values.



| Value                                                                         | Meaning                     |
|-------------------------------------------------------------------------------|-----------------------------|
| <dl> <dt>1</dt> </dl>  | FileMissing<br/>      |
| <dl> <dt>2</dt> </dl>  | FileOlderVersion<br/> |
| <dl> <dt>3</dt> </dl>  | FileEqualVersion<br/> |
| <dl> <dt>4</dt> </dl>  | FileExact<br/>        |
| <dl> <dt>5</dt> </dl>  | FileVerify<br/>       |
| <dl> <dt>6</dt> </dl>  | FileReplace<br/>      |
| <dl> <dt>7</dt> </dl>  | UserData<br/>         |
| <dl> <dt>8</dt> </dl>  | MachineData<br/>      |
| <dl> <dt>9</dt> </dl>  | Shortcut<br/>         |
| <dl> <dt>10</dt> </dl> | Package<br/>          |



 

</dd> </dl>

## Return value



| Return code                                                                               | Description                       |
|-------------------------------------------------------------------------------------------|-----------------------------------|
| <dl> <dt>**0**</dt> </dl>          | Successful completion<br/>  |
| <dl> <dt>**2147549445**</dt> </dl> | RPC Server Fault Error<br/> |



 

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

[**Win32\_Product**](win32-product.md)
</dt> <dt>

[WMI Tasks: Computer Software](https://msdn.microsoft.com/library/aa394588)
</dt> </dl>

 

 





