---
error-parsing-yaml: 
---

# IVMDVDDrive::ReleaseImage method

The **ReleaseImage** method releases a captured ISO image from the DVD drive.

## Syntax


```C++
HRESULT ReleaseImage();
```



## Parameters

This method has no parameters.

## Return value

This method can return one of these values.



| Return code                                                                                                | Description                                                                   |
|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK** </dt> </dl>                     | The operation was successful.<br/>                                      |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> </dl>          | The virtual machine could not be found.<br/>                            |
| <dl> <dt> **VM\_E\_MEDIA\_WRONG\_TYPE** </dt> </dl> | The currently captured media is not an ISO image.<br/>                  |
| <dl> <dt> **VM\_E\_DRIVE\_INVALID** </dt> </dl>     | The drive could not be initialized due to an invalid bus location.<br/> |
| <dl> <dt> **DISP\_E\_EXCEPTION** </dt> </dl>        | An unexpected error occurred.<br/>                                      |



 

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

 

 





