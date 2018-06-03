---
Description: Permits offline system activation using the confirmation ID provided by the Microsoft Clearinghouse license server.
ms.assetid: aa267d03-7df9-418a-aa3d-5e4df20f5a08
title: ActivateOffline method of the Win32\_WindowsProductActivation class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ActivateOffline method of the Win32\_WindowsProductActivation class

The **ActivateOffline** [WMI class](https://msdn.microsoft.com/library/aa393244) method permits offline system activation using the confirmation ID provided by the Microsoft Clearinghouse license server. You must call the [**GetInstallationID**](getinstallationid-method-in-class-win32-windowsproductactivation.md) method before calling this method.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 ActivateOffline(
  [in] string ConfirmationID
);
```



## Parameters

<dl> <dt>

*ConfirmationID* \[in\]
</dt> <dd>

Confirmation ID obtained from the Microsoft Clearinghouse license server. This value is generated from the installation ID.

</dd> </dl>

## Remarks

This method is the scriptable equivalent of manual telephone activation.

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

 

 




