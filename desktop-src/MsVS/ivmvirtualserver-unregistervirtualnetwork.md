---
error-parsing-yaml: 
---

# IVMVirtualServer::UnregisterVirtualNetwork method

The **UnregisterVirtualNetwork** method unregisters a virtual network configuration without deleting the configuration file.

## Syntax


```C++
HRESULT UnregisterVirtualNetwork(
  [in] IVMVirtualNetwork *virtualNetwork
);
```



## Parameters

<dl> <dt>

*virtualNetwork* \[in\]
</dt> <dd>

Pointer to a [**IVMVirtualNetwork**](ivmvirtualnetwork.md) object representing the virtual network configuration to unregister.

</dd> </dl>

## Return value

This method can return one of these values.

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                       | Description                                                |
|---------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>              | The operation was successful.<br/>                   |
| <dl> <dt>**S\_FALSE**</dt> </dl>           | The specified configuration could not be found.<br/> |
| <dl> <dt>**E\_POINTER**</dt> </dl>         | The *virtualNetwork* parameter was **NULL**.<br/>    |
| <dl> <dt>**DISP\_E\_EXCEPTION**</dt> </dl> | An unexpected error occurred.<br/>                   |



 

## Remarks

The virtual network's configuration file is not deleted by this method.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualServer**](ivmvirtualserver.md)
</dt> </dl>

 

 





