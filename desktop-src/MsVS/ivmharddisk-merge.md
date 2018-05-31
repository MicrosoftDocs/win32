---
error-parsing-yaml: 
---

# IVMHardDisk::Merge method

The **Merge** method merges a differencing hard disk image with its parent disk image.

## Syntax


```C++
HRESULT Merge(
  [out] IVMTask **mergeTask
);
```



## Parameters

<dl> <dt>

*mergeTask* \[out\]
</dt> <dd>

The task which is used to track the completion of the merging process.

</dd> </dl>

## Return value

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                                    | Description                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                           | The operation was successful.<br/>                                                                                                                                                                       |
| <dl> <dt>**E\_POINTER**</dt> </dl>                      | The parameter *mergeTask* is **NULL**.<br/>                                                                                                                                                              |
| <dl> <dt>**E\_SHARING\_VIOLATION**</dt> </dl>           | The virtual hard disk image referenced by this **IVMHardDisk** object is in use or the parent of this virtual hard disk image is in use. Or, these hard disk images could be part of a saved state.<br/> |
| <dl> <dt>**VM\_E\_WRONG\_HD\_IMAGE\_TYPE**</dt> </dl>   | The virtual hard disk image referenced by this **IVMHardDisk** object must be a differencing disk image.<br/>                                                                                            |
| <dl> <dt>**VM\_E\_FILE\_READ\_ONLY**</dt> </dl>         | The parent of virtual hard disk image referenced by this **IVMHardDisk** object is marked as read only.<br/>                                                                                             |
| <dl> <dt>**VM\_E\_PARENT\_PATH\_NOT\_FOUND**</dt> </dl> | The parent of the virtual hard disk referenced by this IVMHardDisk object does not exist.<br/>                                                                                                           |
| <dl> <dt>**VM\_E\_APP\_SHUTTING\_DOWN**</dt> </dl>      | The virtual hard disk image cannot be merged because the application is shutting down.<br/>                                                                                                              |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl>              | An unexpected error occurred.<br/>                                                                                                                                                                       |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMHardDisk**](ivmharddisk.md)
</dt> </dl>

 

 





