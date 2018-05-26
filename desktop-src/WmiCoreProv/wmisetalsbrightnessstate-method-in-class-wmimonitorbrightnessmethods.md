---
Description: Used to control the ambient light sensor brightness state.
ms.assetid: ff400d4e-be8c-450b-ad53-d43b0ab84ab3
title: WmiSetALSBrightnessState method of the WmiMonitorBrightnessMethods class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# WmiSetALSBrightnessState method of the WmiMonitorBrightnessMethods class

The **WmiSetALSBrightnessState** method is used to control the ambient light sensor brightness state. If an active brightness override was established by using the [**WmiSetBrightness**](wmisetbrightness-method-in-class-wmimonitorbrightnessmethods.md) method, that override will take precedence over the ALS brightness set by using this method. For an enabled ALS brightness override to take effect, the brightness policy has to be reverted by using the [**WmiRevertToPolicyBrightness**](wmireverttopolicybrightness-method-in-class-wmimonitorbrightnessmethods.md) method.

## Syntax


```mof
uint32 WmiSetALSBrightnessState(
   boolean State
);
```



## Parameters

<dl> <dt>

*State* 
</dt> <dd>

ALS brightness state. False disables the ALS brightness override and true enables it.

</dd> </dl>

## Return value

Returns zero (0) to indicate success. Any other number indicates an error. For more information about error codes, see [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559) or [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978).

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\wmi<br/>                                                                   |
| MOF<br/>                      | <dl> <dt>WmiCore.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WmiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**WmiMonitorBrightnessMethods**](wmimonitorbrightnessmethods.md)
</dt> <dt>

[**MSMonitorClass**](msmonitorclass.md)
</dt> </dl>

 

 




