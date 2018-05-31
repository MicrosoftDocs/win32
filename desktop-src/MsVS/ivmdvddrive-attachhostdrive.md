---
error-parsing-yaml: 
---

# IVMDVDDrive::AttachHostDrive method

The **AttachHostDrive** method attaches a host DVD drive to the DVD drive within the virtual machine.

## Syntax


```C++
HRESULT AttachHostDrive(
  [in] BSTR driveLetter
);
```



## Parameters

<dl> <dt>

*driveLetter* \[in\]
</dt> <dd>

The letter of the host drive that is to be attached.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                           | Description                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                  | The operation was successful.<br/>                                                                                                                                             |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>          | No drive letter was specified, or the specified drive letter is invalid.<br/>                                                                                                  |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> </dl>     | The virtual machine could not be found.<br/>                                                                                                                                   |
| <dl> <dt>**VM\_E\_DRIVE\_IN\_USE** </dt> </dl> | A host DVD drive or ISO image is already attached to this drive within the virtual machine, or the specified host drive is already in use within another virtual machine.<br/> |
| <dl> <dt>**VM\_E\_DRIVE\_INVALID**</dt> </dl>  | The bus location for this drive is invalid, or the drive does not appear to be a valid DVD drive.<br/>                                                                         |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl>     | An unexpected error occurred.<br/>                                                                                                                                             |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMDVDDrive**](ivmdvddrive.md)
</dt> </dl>

 

 





