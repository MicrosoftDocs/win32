---
description: The WmiRevertToPolicyBrightness method is used to revert the brightness to the policy setting. This method has no effect on the ALS brightness settings.
ms.assetid: 9a520c3f-3563-4ef4-b397-14e487c8e8bb
title: WmiRevertToPolicyBrightness method of the WmiMonitorBrightnessMethods class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WmiMonitorBrightnessMethods.WmiRevertToPolicyBrightness
api_type: 
- COM
api_location: 
- WmiProv.dll
---

# WmiRevertToPolicyBrightness method of the WmiMonitorBrightnessMethods class

The **WmiRevertToPolicyBrightness** method is used to revert the brightness to the policy setting. This method has no effect on the ALS brightness settings.

## Syntax


```mof
uint32 WmiRevertToPolicyBrightness();
```



## Parameters

This method has no parameters.

## Return value

Returns zero (0) to indicate success. Any other number indicates an error. For more information about error codes, see [**WMI Error Constants**](/windows/desktop/WmiSdk/wmi-error-constants) or [**WbemErrorEnum**](/windows/desktop/api/wbemdisp/ne-wbemdisp-wbemerrorenum).

## Requirements



| Requirement | Value |
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

 

