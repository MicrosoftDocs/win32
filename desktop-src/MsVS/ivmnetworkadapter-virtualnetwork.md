---
error-parsing-yaml: 
---

# IVMNetworkAdapter::VirtualNetwork property

The **VirtualNetwork** property contains the virtual network to which the virtual NIC is attached.

This property is read-only.

## Syntax


```C++
HRESULT get_VirtualNetwork(
  [out] IVMVirtualNetwork **virtualNetwork
);
```

<span codelanguage="VisualBasic"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>VB</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>VMNetworkAdapter.VirtualNetwork( _
  ByRef virtualNetwork _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**VMVirtualNetwork**](ivmvirtualnetwork.md) object which is associated with this virtual NIC.

This property value is read-only.

## Error codes



| Name                                                                                                            | Meaning                                                                                   |
|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                                | The operation was successful.<br/>                                                  |
| <dl> <dt>E\_POINTER</dt> </dl>                           | The parameter *virtualNetwork* was **NULL**.<br/>                                   |
| <dl> <dt>S\_FALSE</dt> </dl>                             | This network interface is unplugged and is not connected to a virtual network.<br/> |
| <dl> <dt>VM\_E\_INVALID\_VIRTUAL\_NETWORK\_ID</dt> </dl> | This interface is connected to a virtual network with an invalid ID.<br/>           |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>                   | An unexpected error has occurred.<br/>                                              |



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

 

 





