---
error-parsing-yaml: 
---

# \_IVMRCClientControlEvents::OnStateChanged method

The **OnStateChanged** method is called when the VMRC client connection state changes.

## Syntax


```C++
HRESULT OnStateChanged(
  [in] VMRCState state
);
```



## Parameters

<dl> <dt>

*state* \[in\]
</dt> <dd>

The current VMRC client connection state.

</dd> </dl>

## Return value

A [**32-bit value**](hresult-codes-specific-to-the-virtual-server.md) that describes an error or warning.

## Remarks

This method is called when the connection state of the VMRC client control object changes. The client program must implement this interface method to receive notification of the event originating from the [**IVMRCClientControl**](ivmrcclientcontrol.md) object.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |



## See also

<dl> <dt>

[**\_IVMRCClientControlEvents**](-ivmrcclientcontrolevents.md)
</dt> </dl>

 

 





