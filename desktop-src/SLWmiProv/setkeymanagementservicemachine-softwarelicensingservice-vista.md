---
Description: Not supported. Use the SetKeyManagementServiceMachine method.
ms.assetid: c87a9924-d2f1-4756-bed2-c09b4516e828
title: SetKeyManagementServiceMachine method of the SoftwareLicensingService class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SetKeyManagementServiceMachine method of the SoftwareLicensingService class

Not supported. Use the [**SetKeyManagementServiceMachine**](https://msdn.microsoft.com/library/cc534593) method.

**Windows Vista and Windows Server 2008:** Sets the name of the key management service (KMS) machine to use for volume activation.

## Syntax


```mof
uint32 SetKeyManagementServiceMachine(
  [in] string MachineName
);
```



## Parameters

<dl> <dt>

*MachineName* \[in\]
</dt> <dd>

Specifies the name of the KMS machine.

</dd> </dl>

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                       |
| End of client support<br/>    | Windows Vista<br/>                                                             |
| End of server support<br/>    | Windows Server 2008<br/>                                                       |
| Namespace<br/>                | Root\\CIMV2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>SLWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SLWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**SoftwareLicensingService**](softwarelicensingservice-vista.md)
</dt> <dt>

[**SetKeyManagementServiceMachine**](https://msdn.microsoft.com/library/cc534593)
</dt> </dl>

 

 




