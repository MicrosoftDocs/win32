---
Description: 'The SetProductKey&\#8194;WMI class method updates the system product key for a computer.'
ms.assetid: 'c725fa8c-ceac-44ca-bbfc-5b2abdd42bbc'
title: 'SetProductKey method of the Win32\_WindowsProductActivation class'
---

# SetProductKey method of the Win32\_WindowsProductActivation class

The **SetProductKey** [WMI class](https://msdn.microsoft.com/library/aa393244) method updates the system product key for a computer.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 SetProductKey(
  [in] string ProductKey
);
```



## Parameters

<dl> <dt>

*ProductKey* \[in\]
</dt> <dd>

Unique product key that is licensed for use on the computer. Product keys are alphanumeric strings of 25 characters formatted as follows: xxxxx-xxxxx-xxxxx-xxxxx-xxxxx. The product key must be valid for the media type. Media types include retail, volume-licensing, and OEM.

</dd> </dl>

## Remarks

This method is only validif the **ActivationRequired** property is equal to 1.

> [!Note]  
> Windows Product Activation is not available on the Itanium-based versions of the Windows operating system.

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                        |
| End of client support<br/>    | Windows XP<br/>                                                                 |
| End of server support<br/>    | Windows Server 2003 R2<br/>                                                     |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>Licwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Licwmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_WindowsProductActivation**](win32-windowsproductactivation.md)
</dt> <dt>

[Windows Product Activation Provider](windows-product-activation-provider.md)
</dt> </dl>

 

 




