---
Description: 'Not supported. Use the AcquireGenuineTicket method.'
ms.assetid: '953c2f88-00cd-47d1-8bf1-277bcb64f622'
title: AcquireGenuineTicket method of the SoftwareLicensingService class
---

# AcquireGenuineTicket method of the SoftwareLicensingService class

Not supported. Use the [**AcquireGenuineTicket**](https://msdn.microsoft.com/library/cc534583) method.

**Windows Vista and Windows Server 2008:** Acquires a genuine ticket online.

## Syntax


```mof
uint32 AcquireGenuineTicket(
  [in] string TemplateId,
  [in] string ServerUrl
);
```



## Parameters

<dl> <dt>

*TemplateId* \[in\]
</dt> <dd>

Specifies the template ID.

</dd> <dt>

*ServerUrl* \[in\]
</dt> <dd>

Specifies the server URL.

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
</dt> <dt>

[**AcquireGenuineTicket**](https://msdn.microsoft.com/library/cc534583)
</dt> </dl>

 

 




