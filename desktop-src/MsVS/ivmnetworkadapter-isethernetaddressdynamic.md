---
error-parsing-yaml: 
---

# IVMNetworkAdapter::IsEthernetAddressDynamic property

The **IsEthernetAddressDynamic** property contains whether the Ethernet (MAC/Physical/Network) address of a virtual NIC can either be set to a static address or it can be generated dynamically to avoid conflicts with other virtual machines.

This property is read/write.

## Syntax


```C++
HRESULT put_IsEthernetAddressDynamic(
  [in]  VARIANT_BOOL isDynamic
);

HRESULT get_IsEthernetAddressDynamic(
  [out] VARIANT_BOOL *isDynamic
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
<td><pre><code>VMNetworkAdapter.IsEthernetAddressDynamic( _
  ByRef isDynamic, _
  ByVal isDynamic _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if the Ethernet address is dynamically generated, **vbFalse** if the Ethernet address is static.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                                                                                                                                              |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                                                                                                                             |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *isDynamic* parameter was **NULL**.<br/>                                                                                                                   |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The virtual machine was not found. This may occur if the machine was removed after the [**IVMNetworkAdapter**](ivmnetworkadapter.md) object was created.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>                                                                                                                         |



## Remarks

This property is used to determine whether the Ethernet address will be generated dynamically.

The DynamicEthernetAddress property should be set to **TRUE** (default) for most virtual network interfaces. If software in the guest requires a static Ethernet address, this property should be set to **FALSE**.

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

 

 





