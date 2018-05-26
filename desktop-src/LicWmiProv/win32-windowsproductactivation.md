---
Description: Contains properties and methods related to Windows Product Activation (WPA), such as activation state and grace period. This class also provides the ability to activate the customers computer online and offline.
ms.assetid: aa267d03-7df9-418a-aa3d-5e4df20f5a08
title: Win32\_WindowsProductActivation class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Win32\_WindowsProductActivation class

The **Win32\_WindowsProductActivation** [WMI class](https://msdn.microsoft.com/library/aa393244) contains properties and methods related to Windows Product Activation (WPA), such as activation state and grace period. This class also provides the ability to activate the customer's computer online and offline.

The following syntax is simplified from MOF code and includes all of the inherited properties, but excludes methods. For reference information about methods, see the table of methods later in this topic.

> [!Note]  
> This class is not supported on platforms beyond Windows XP or Windows Server 2003 R2. On those platforms, it is recommended that you use the [Software Licensing Classes](https://msdn.microsoft.com/library/dn622972) instead.

 

## Syntax

``` syntax
class Win32_WindowsProductActivation : CIM_Setting
{
  uint32 ActivationRequired;
  string Caption;
  string Description;
  uint32 IsNotificationOn;
  string ProductID;
  uint32 RemainingEvaluationPeriod;
  uint32 RemainingGracePeriod;
  string ServerName;
  string SettingID;
};
```

## Members

The **Win32\_WindowsProductActivation** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_WindowsProductActivation** class has these methods.



| Method                                                                                        | Description                                                                                                                                                                                                |
|:----------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ActivateOffline**](activateoffline-method-in-class-win32-windowsproductactivation.md)     | Activates the system offline using the confirmation ID provided by the Microsoft Clearinghouse license server.<br/>                                                                                  |
| [**ActivateOnline**](activateonline-method-in-class-win32-windowsproductactivation.md)       | Exchanges license-related data with the Microsoft Clearinghouse license server. If the method succeeds, it activates the system.<br/>                                                                |
| [**GetInstallationID**](getinstallationid-method-in-class-win32-windowsproductactivation.md) | Retrieves the installation ID which is required to activate a system offline.<br/>                                                                                                                   |
| [**SetNotification**](setnotification-method-in-class-win32-windowsproductactivation.md)     | Enables or disables notification reminders and the activation icon in the notification tray. If activation is not required, or if activation is not pending, calling this method has no effect.<br/> |
| [**SetProductKey**](setproductkey-method-in-class-win32-windowsproductactivation.md)         | Updates the system product key for a computer.<br/>                                                                                                                                                  |



 

### Properties

The **Win32\_WindowsProductActivation** class has these properties.

<dl> <dt>

**ActivationRequired**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If 1 (one), system activation is pending for the system. The system must be activated within the number of days indicated by the **RemainingGracePeriod** property. If 0 (zero), activation is not required during a specific time period.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

Short textual description of the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object. This property is inherited from **CIM\_Setting**.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Textual description of the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object. This property is inherited from **CIM\_Setting**.

</dd> <dt>

**IsNotificationOn**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If not equal to 0 (zero), and product activation is required, notification reminders (message balloons) are enabled and the activation icon appears in the notification tray. If 0 (zero), notification reminders and the activation icon are disabled.

**Windows XP Professional :** This property is not available. It becomes available in Windows XP with SP1.

</dd> <dt>

**ProductID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (1024)
</dt> </dl>

String of 20 characters separated by hyphens in the format, "xxxxx-xxx-xxxxxxx-xxxxx". This is the same product ID that is displayed under the **General** tab of the **System Properties** dialog in Control Panel.

</dd> <dt>

**RemainingEvaluationPeriod**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If this instance represents beta or evaluation media, this represents the number of days remaining before expiration of the media. Otherwise, this property is set to the largest possible unsigned value.

</dd> <dt>

**RemainingGracePeriod**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of days remaining before activation of the system is required, if the **ActivationRequired** property is equal to 1.

</dd> <dt>

**ServerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

System whose WPA properties and methods are to be accessed. This property is a string that specifies the name of the computer or its IP address.

</dd> <dt>

**SettingID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

Identifier by which the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object is known. This property is inherited from **CIM\_Setting**.

</dd> </dl>

## Remarks

The **Win32\_WindowsProductActivation** class is derived from [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461).

> [!Note]  
> Windows Product Activation is not available on the Itanium-based versions of the Windows operating system.

 

For more information on using this class, see [Deploying Windows XP Using Windows Product Activation](http://technet.microsoft.com/library/bb457096.aspx).

## Examples

The [List Windows Product Activation Status](http://gallery.technet.microsoft.com/7f22e040-9fb0-4a14-ba7d-87780e1ee77f) Perl sample returns product activation information for a computer.

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

[Windows Product Activation Provider](windows-product-activation-provider.md)
</dt> <dt>

[**Win32\_Proxy**](win32-proxy.md)
</dt> <dt>

[**Win32\_ComputerSystemWindowsProductActivationSetting**](win32-computersystemwindowsproductactivationsetting.md)
</dt> <dt>

[WMI Tasks: Operating Systems](https://msdn.microsoft.com/library/aa394596)
</dt> </dl>

 

 




