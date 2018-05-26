---
Description: The GetInstallationID&\#8194;WMI class method retrieves the installation ID.
ms.assetid: 90657060-24df-49eb-a824-7ffe0c10672f
title: GetInstallationID method of the Win32\_WindowsProductActivation class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GetInstallationID method of the Win32\_WindowsProductActivation class

The **GetInstallationID** [WMI class](https://msdn.microsoft.com/library/aa393244) method retrieves the installation ID.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 GetInstallationID(
  [out] string InstallationID
);
```



## Parameters

<dl> <dt>

*InstallationID* \[out\]
</dt> <dd>

Receives the installation ID if the method completes successfully. Otherwise, this part will be empty.

The installation ID is a string generated from the product ID (PID) and the computer's hardware ID. This string is identical to the installation ID that is displayed on the telephone activation page and is 50 digits in length. The customer must supply the installation ID to the Microsoft Clearinghouse license server to obtain a confirmation ID. The confirmation ID is required to call the [**ActivateOffline**](activateoffline-method-in-class-win32-windowsproductactivation.md) method.

</dd> </dl>

## Remarks

Note that each call to the **GetInstallationID** method generates a unique installation ID. You must match the confirmation ID with the corresponding installation ID.

> [!Note]  
> Windows Product Activation is not available on the Itanium-based versions of the Windows operating system.

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                        |
| End of client support<br/>    | Windows XP<br/>                                                                 |
| End of server support<br/>    | Windows Server 2003 R2<br/>                                                     |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>Licwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Licwmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_WindowsProductActivation**](win32-windowsproductactivation.md)
</dt> <dt>

[Windows Product Activation Provider](windows-product-activation-provider.md)
</dt> </dl>

 

 




