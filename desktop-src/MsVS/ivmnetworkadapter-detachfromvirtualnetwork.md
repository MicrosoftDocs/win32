---
error-parsing-yaml: 
---

# IVMNetworkAdapter::DetachFromVirtualNetwork method

The **DetachFromVirtualNetwork** method detaches the virtual NIC from its virtual network.

## Syntax


```C++
HRESULT DetachFromVirtualNetwork();
```



## Parameters

This method has no parameters.

## Return value

This method can return one of these values.



| Return code                                                                                         | Description                                  |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt> **S\_OK** </dt> </dl>              | The operation was successful.<br/>     |
| <dl> <dt> **DISP\_E\_EXCEPTION** </dt> </dl> | An unexpected error has occurred.<br/> |



 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMNetworkAdapter**](ivmnetworkadapter.md)
</dt> </dl>

 

 





