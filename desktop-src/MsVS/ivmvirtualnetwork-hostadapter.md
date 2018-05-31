---
error-parsing-yaml: 
---

# IVMVirtualNetwork::HostAdapter property

The **HostAdapter** property contains the name of the host Ethernet adapter to which the virtual network is connected.

This property is read/write.

## Syntax


```C++
HRESULT put_HostAdapter(
  [in]  BSTR virtualNetworkAdapterName
);

HRESULT get_HostAdapter(
  [out] BSTR *virtualNetworkAdapterName
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
<td><pre><code>VMVirtualNetwork.HostAdapter( _
  ByRef virtualNetworkAdapterName, _
  ByVal virtualNetworkAdapterName _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The name of the host adapter to which the virtual network is connected.

This property value is read/write.

## Error codes



| Name                                                                                                  | Meaning                                                                                                                                                                                                                                                                    |
|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | The operation was successful.<br/>                                                                                                                                                                                                                                   |
| <dl> <dt>E\_POINTER</dt> </dl>                 | The *virtualNetworkAdapaterName* parameter is **NULL**.<br/>                                                                                                                                                                                                         |
| <dl> <dt>VM\_E\_ADAPTER\_NOT\_FOUND</dt> </dl> | The host Ethernet adapter to which this virtual network was connected is no longer available (get operation) or does not correspond to any Ethernet adapter installed on the host (put operation). The host Ethernet adapter may have been removed or disabled.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>         | An unexpected error has occurred.<br/>                                                                                                                                                                                                                               |



## Remarks

The virtual network adapter allows a virtual network to talk to external networks. There is normally one adapter per Ethernet adapter installed in the host machine. For example, let's say a host machine had an adapter labeled "10/100 ENET". To connect a virtual NIC to the network attached to "10/100 ENET", set the virtual network's Adapter property to "10/100 ENET" and connect the virtual NIC to this virtual network.

If the property is set to an empty string (""), the virtual NIC adapter is connected to a special Guests-Only virtual network. Virtual NICs attached to this Guests-Only virtual network will have no access to external networks on the system host. However, the virtual NICs attached to this virtual network are still able to communicate with each other.

The complete list of adapters can be accessed through the [**IVMHostInfo::NetworkAdapters**](ivmhostinfo-networkadapters.md) property.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualNetwork**](ivmvirtualnetwork.md)
</dt> </dl>

 

 





