---
Description: 'Not supported. Use the SetVLActivationInterval method.'
ms.assetid: '06bb1872-2de0-4182-b527-a44044d2183d'
title: SetVLActivationInterval method of the SoftwareLicensingService class
---

# SetVLActivationInterval method of the SoftwareLicensingService class

Not supported. Use the [**SetVLActivationInterval**](https://msdn.microsoft.com/library/cc534594) method.

**Windows Vista and Windows Server 2008:** Sets the activation frequency, in minutes, of how often the current machine should contact the key management service machine before the client is licensed. The frequency must be greater than or equal to 15 and less than or equal to 43200. An error is returned if the method is called and the machine is not a key management service.

## Syntax


```mof
uint32 SetVLActivationInterval(
  [in] uint32 ActivationInterval
);
```



## Parameters

<dl> <dt>

*ActivationInterval* \[in\]
</dt> <dd>

Specifies the activation interval in minutes.

</dd> </dl>

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                       |
| End of client support<br/>    | Windows Vista<br/>                                                             |
| End of server support<br/>    | Windows Server 2008<br/>                                                       |
| Namespace<br/>                | Root\\CIMV2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>SLWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SLWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**SoftwareLicensingService**](softwarelicensingservice-vista.md)
</dt> </dl>

 

 




