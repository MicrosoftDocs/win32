---
Description: Not supported. Use the SetVLRenewalInterval method.
ms.assetid: b3a2e49e-4753-4a0b-ac65-8d9800fd83c5
title: SetVLRenewalInterval method of the SoftwareLicensingService class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetVLRenewalInterval method of the SoftwareLicensingService class

Not supported. Use the [**SetVLRenewalInterval**](https://msdn.microsoft.com/library/cc534595) method.

**Windows Vista and Windows Server 2008:** Sets the renewal frequency, in minutes, of how often the current machine should contact the key management service machine after the client is licensed. The frequency must be greater than or equal to 15 and less than or equal to 43200. An error is returned if the method is called and the machine is not a key management service.

## Syntax


```mof
uint32 SetVLRenewalInterval(
  [in] uint32 RenewalInterval
);
```



## Parameters

<dl> <dt>

*RenewalInterval* \[in\]
</dt> <dd>

Specifies the renewal interval in minutes.

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

[**SetVLRenewalInterval**](https://msdn.microsoft.com/library/cc534595)
</dt> </dl>

 

 




