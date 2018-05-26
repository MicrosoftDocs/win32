---
Description: Modifies the setting data for the service.
ms.assetid: 1CA49922-894D-4AA1-B741-6A0DC9F5654E
title: ModifyServiceSettings method of the Msvm\_VirtualSystemManagementService class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ModifyServiceSettings method of the Msvm\_VirtualSystemManagementService class

Modifies the setting data for the service.

## Syntax


```mof
uint32 ModifyServiceSettings(
  [in]  string              SettingData,
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*SettingData* \[in\]
</dt> <dd>

Type: **string**

An embedded instance of the [**Msvm\_VirtualSystemManagementServiceSettingData**](msvm-virtualsystemmanagementservicesettingdata.md) class that contains the modified aspects of the existing service.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Type: **[**CIM\_ConcreteJob**](https://msdn.microsoft.com/library/cc136808)**

If the operation is performed asynchronously, this method will return 4096, and this parameter will contain a reference to an object derived from [**CIM\_ConcreteJob**](https://msdn.microsoft.com/library/cc136808).

</dd> </dl>

## Return value

Type: **uint32**

This method returns one of the following values.

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Failed** (32768)
</dt> <dt>

**Access Denied** (32769)
</dt> <dt>

**Not Supported** (32770)
</dt> <dt>

**Status is unknown** (32771)
</dt> <dt>

**Timeout** (32772)
</dt> <dt>

**Invalid parameter** (32773)
</dt> <dt>

**System is in use** (32774)
</dt> <dt>

**Invalid state for this operation** (32775)
</dt> <dt>

**Incorrect data type** (32776)
</dt> <dt>

**System is not available** (32777)
</dt> <dt>

**Out of memory** (32778)
</dt> </dl>

## Remarks

Access to the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**ModifyServiceSettings (V1)**](https://msdn.microsoft.com/library/cc160709)
</dt> <dt>

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> <dt>

[**CIM\_ConcreteJob**](https://msdn.microsoft.com/library/cc136808)
</dt> </dl>

 

 




