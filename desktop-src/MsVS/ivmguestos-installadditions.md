---
error-parsing-yaml: 
---

# IVMGuestOS::InstallAdditions method

The **InstallAdditions** method locates and installs the latest Additions into the guest operating system.

## Syntax


```C++
HRESULT InstallAdditions();
```



## Parameters

This method has no parameters.

## Return value

This method can return one of these values.



| Return code                                                                                                | Description                                                                            |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                       | The operation was successful.<br/>                                               |
| <dl> <dt>**VM\_E\_VM\_NOT\_RUNNING**</dt> </dl>     | The virtual machine is not running.<br/>                                         |
| <dl> <dt>**VM\_E\_VM\_UNKNOWN**</dt> </dl>          | The virtual machine could not be found.<br/>                                     |
| <dl> <dt>**VM\_E\_DRIVE\_INVALID**</dt> </dl>       | The virtual machine does not have an empty DVD drive.<br/>                       |
| <dl> <dt>**VM\_E\_MEDIA\_UNMOUNT\_FAIL**</dt> </dl> | The attempt to unmount the media from the virtual machine DVD drive failed.<br/> |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl>          | An unexpected error occurred.<br/>                                               |



 

## Remarks

This method attempts to locate the ISO image for the latest Additions and attach it to a DVD drive in the virtual machine. If the virtual machine is booted and running a Windows-based guest operating system, Windows will autorun the Additions installer. If the virtual machine is not completely booted, or the guest operating system has autorun disabled, or the guest operating system is not Windows-based, you will need to manually launch the Additions installer. The virtual machine must be running and contain an empty DVD drive when this method is invoked. Virtual Server 1.1 only supports Windows Additions. Linux and OS/2 Additions are not available.

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

 

 





