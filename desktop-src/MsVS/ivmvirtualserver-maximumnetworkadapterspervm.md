---
error-parsing-yaml: 
---

# IVMVirtualServer::MaximumNetworkAdaptersPerVM property

The **MaximumNetworkAdaptersPerVM** property contains the maximum number of network interfaces per virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_MaximumNetworkAdaptersPerVM(
  [out] long *maxNetworkAdapters
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
<td><pre><code>VMVirtualServer.MaximumNetworkAdaptersPerVM( _
  ByRef maxNetworkAdapters _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The maximum number of network interfaces per virtual machine.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                      |
|-----------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>     |
| <dl> <dt>E\_POINTER</dt> </dl>         | *maxNetworkAdapters* is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>     |



## Examples

The following example displays the **MaximumNetworkAdaptersPerVM** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")

Wscript.Echo "Name: " & objVS.Name
Wscript.Echo "Maximum network adapters per VM: " & _
             objVS.MaximumNetworkAdaptersPerVM
```



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

 

 





