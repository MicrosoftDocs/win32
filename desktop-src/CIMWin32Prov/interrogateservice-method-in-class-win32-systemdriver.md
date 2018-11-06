---
Description: Requests that the system driver service update its state to the service manager.
ms.assetid: 350d9044-39fd-436f-ab15-b30324b2b2e9
ms.tgt_platform: multiple
title: InterrogateService method of the Win32_SystemDriver class
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_SystemDriver.InterrogateService
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# InterrogateService method of the Win32\_SystemDriver class

The **InterrogateService** [WMI class](https://msdn.microsoft.com/library/aa393244) method requests that the system driver service update its state to the service manager.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 InterrogateService();
```



## Parameters

This method has no parameters.

## Return value

Returns a value of 0 (zero) if the **InterrogateService** request was accepted, 1 (one) if the request is not supported, and any other number to indicate an error.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_SystemDriver**](win32-systemdriver.md)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> <dt>

[**Win32\_BaseService**](win32-baseservice.md)
</dt> </dl>

 

 




