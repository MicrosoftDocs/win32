---
Description: The SetNotification&\#8194;WMI class method enables or disables the display of notification reminders (message balloons) and the activation icon in the notification tray.
ms.assetid: 5e087174-0ecf-4425-b022-f96ac55fbb60
title: SetNotification method of the Win32\_WindowsProductActivation class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SetNotification method of the Win32\_WindowsProductActivation class

The **SetNotification** [WMI class](https://msdn.microsoft.com/library/aa393244) method enables or disables the display of notification reminders (message balloons) and the activation icon in the notification tray.

Calling this method has no effect on the length of the activation grace period nor does it affect whether system activation is required. If activation is not required, or if activation is not pending, calling this method also has no effect.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 SetNotification(
  [in] uint32 Enable
);
```



## Parameters

<dl> <dt>

*Enable* \[in\]
</dt> <dd>

If not equal to 0 (zero) and activation is required, notification reminders are enabled and the activation icon appears in the notification tray. If 0 (zero), notification reminders and the activation icon are disabled. Note that notifications are enabled by default. For more information, see the following Remarks section.

</dd> </dl>

## Remarks

Enabling or disabling notifications does not affect logon reminders, which begin 7 (seven) days before the activation period expires. Enabling or disabling notifications also does not affect event log reminders.

> [!Note]If you disable notification reminders, you must re-enable them unless you are certain that they will no longer be needed. A user who has not activated a product before the activation grace period expires could be locked out when he or she attempts to log on after the grace period has expired.
>
> If you use drive imaging to replicate hard disk drives, you must ensure that the notification state is correct prior to imaging. If you run the **sysprep** command or the **riprep** command prior to drive imaging, it enables notification reminders, which is the default setting.

 

This method was added to support automated deployment because automated activation may not succeed on the first attempt. The unexpected appearance of notification reminders in the notification tray can be confusing to users.

Windows Product Activation is not available on the Itanium-based versions of the Windows operating system.

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

 

 




