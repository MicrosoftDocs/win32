---
error-parsing-yaml: 
---

# IVMDVDDriveEvents::OnMediaInsert method

The **OnMediaInsert** method is called when media has been inserted into the drive.

## Syntax


```C++
HRESULT OnMediaInsert(
  [in] BSTR     mediaPath
);
```



## Parameters

<dl> <dt>

 *mediaPath* \[in\]
</dt> <dd>

The host drive letter, or path, to the ISO image.

</dd> </dl>

## Return value

A [**32-bit value**](hresult-codes-specific-to-the-virtual-server.md) that describes an error or warning.

## Remarks

This method is called when media (an ISO image or a disc in a host drive) is inserted. The client program must implement this interface method to receive notification of the [**vmDVDDriveEvent\_OnInsert**](vmdvddriveevent.md) event originating from [**IVMDVDDrive**](ivmdvddrive.md).

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMDVDDriveEvents**](ivmdvddriveevents.md)
</dt> </dl>

 

 





