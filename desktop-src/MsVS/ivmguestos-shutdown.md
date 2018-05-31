---
error-parsing-yaml: 
---

# IVMGuestOS::Shutdown method

The **Shutdown** method tells the guest operating system to shut down.

## Syntax


```C++
HRESULT Shutdown(
  [out] IVMTask **shutdownTask
);
```



## Parameters

<dl> <dt>

*shutdownTask* \[out\]
</dt> <dd>

Retrieves the task which is used to track the completion of the guest operating system's shutdown process. See [**IVMTask**](ivmtask.md).

</dd> </dl>

## Return value

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                                          | Description                                                                          |
|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                 | The operation was successful.<br/>                                             |
| <dl> <dt>**E\_POINTER**</dt> </dl>                            | The *shutdownTask* parameter is **NULL**.<br/>                                 |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> </dl>                    | The virtual machine could not be found.<br/>                                   |
| <dl> <dt>**VM\_E\_VM\_NOT\_RUNNING**</dt> </dl>               | The virtual machine is not running.<br/>                                       |
| <dl> <dt>**E\_ACCESSDENIED**</dt> </dl>                       | The caller must have execute access permissions for this virtual machine.<br/> |
| <dl> <dt>**VM\_E\_ADDITIONS\_FEATURE\_NOT\_AVAIL**</dt> </dl> | Additions are not installed in this virtual machine.<br/>                      |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl>                    | An unexpected error occurred.<br/>                                             |



 

## Remarks

The virtual machine must be running and Additions must be installed when this method is invoked. This method is only supported for Windows-based guest operating systems.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMGuestOS**](ivmguestos.md)
</dt> </dl>

 

 





