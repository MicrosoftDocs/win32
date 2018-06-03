---
Description: The Win32\_ComputerSystemWindowsProductActivationSetting WMI class represents an association between instances of Win32\_ComputerSystem and Win32\_WindowsProductActivation.
ms.assetid: e1c87d3a-1942-42ab-85ba-9be0f031ac33
title: Win32\_ComputerSystemWindowsProductActivationSetting class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_ComputerSystemWindowsProductActivationSetting class

The **Win32\_ComputerSystemWindowsProductActivationSetting** [WMI class](https://msdn.microsoft.com/library/aa393244) represents an association between instances of [**Win32\_ComputerSystem**](https://msdn.microsoft.com/library/aa394102) and [**Win32\_WindowsProductActivation**](win32-windowsproductactivation.md).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class Win32_ComputerSystemWindowsProductActivationSetting : CIM_ElementSetting
{
  Win32_ComputerSystem           REF Element;
  Win32_WindowsProductActivation REF Setting;
};
```

## Members

The **Win32\_ComputerSystemWindowsProductActivationSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ComputerSystemWindowsProductActivationSetting** class has these properties.

<dl> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to an instance that represents the computer that can be configured with the **Setting** property. This property is inherited from [**CIM\_ElementSetting**](https://msdn.microsoft.com/library/aa387263).

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_WindowsProductActivation**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to an instance that represents the settings that are associated with the referenced computer. This property is inherited from [**CIM\_ElementSetting**](https://msdn.microsoft.com/library/aa387263).

</dd> </dl>

## Remarks

The **Win32\_ComputerSystemWindowsProductActivationSetting** class is derived from [**CIM\_ElementSetting**](https://msdn.microsoft.com/library/aa387263).

> [!Note]  
> Windows Product Activation is not available on the 64-bit versions of the Windows operating system.

 

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

[**Win32\_WindowsProductActivation**](win32-windowsproductactivation.md)
</dt> </dl>

 

 




