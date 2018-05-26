---
title: FormatError method of the Msvm\_VirtualSystemManagementService class
description: Returns the formatted error message string for the specified array of embedded Msvm\_Error instances.
ms.assetid: 0b480af5-dc8b-4fd4-b5e8-62ec1a27e5a5
keywords:
- FormatError method Hyper-V
- FormatError method Hyper-V , Msvm_VirtualSystemManagementService class
- Msvm_VirtualSystemManagementService class Hyper-V , FormatError method
topic_type:
- apiref
api_name:
- Msvm_VirtualSystemManagementService.FormatError
api_location:
- Root\Virtualization
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FormatError method of the Msvm\_VirtualSystemManagementService class

Returns the formatted error message string for the specified array of embedded [**Msvm\_Error**](msvm-error.md) instances.

## Syntax


```mof
uint32 FormatError(
  [in]  string Errors[],
  [out] string ErrorMessage
);
```



## Parameters

<dl> <dt>

*Errors* \[in\]
</dt> <dd>

Type: **string\[\]**

An array of strings that contain [**Msvm\_Error**](msvm-error.md) instances used to generate the output error message.

</dd> <dt>

*ErrorMessage* \[out\]
</dt> <dd>

Type: **string**

On output, a string that contains the error message represented by the [**Msvm\_Error**](msvm-error.md) instances passed in the *Errors* parameter.

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



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012<br/>                                                                       |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**FormatError (V2)**](https://msdn.microsoft.com/library/windows/desktop/hh850051)
</dt> <dt>

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> </dl>

 

 





