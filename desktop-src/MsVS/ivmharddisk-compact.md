---
error-parsing-yaml: 
---

# IVMHardDisk::Compact method

The **Compact** method compacts a dynamically expanding hard disk image.

## Syntax


```C++
HRESULT Compact(
  [out] IVMTask **compactTask
);
```



## Parameters

<dl> <dt>

*compactTask* \[out\]
</dt> <dd>

The task which is used to track the completion the compaction process.

</dd> </dl>

## Return value

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                                  | Description                                                                                                                                        |
|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                         | The operation was successful.<br/>                                                                                                           |
| <dl> <dt>**E\_POINTER**</dt> </dl>                    | The parameter *compactTask* is **NULL**.<br/>                                                                                                |
| <dl> <dt>**VM\_E\_INVALID\_HD\_FILE**</dt> </dl>      | The virtual hard disk image referenced by this **IVMHardDisk** object does not seem to be a valid image.<br/>                                |
| <dl> <dt>**E\_SHARING\_VIOLATION**</dt> </dl>         | The virtual hard disk image referenced by this **IVMHardDisk** object is in use.<br/>                                                        |
| <dl> <dt>**VM\_E\_WRONG\_HD\_IMAGE\_TYPE**</dt> </dl> | The virtual hard disk image referenced by this **IVMHardDisk** object must be a [**vmDiskTypeDynamic**](vmharddisktype.md) image type.<br/> |
| <dl> <dt>**E\_DISK\_FULL**</dt> </dl>                 | The host volume does not have enough space to create a temporary file needed for the compaction of this virtual hard disk image.<br/>        |
| <dl> <dt>**VM\_E\_APP\_SHUTTING\_DOWN**</dt> </dl>    | The virtual hard disk image cannot be compacted because the application is shutting down.<br/>                                               |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl>            | An unexpected error occurred.<br/>                                                                                                           |



 

## Remarks

To compact a dynamically expanding hard disk image, free space on the disk image should first be zeroed.

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

 

 





