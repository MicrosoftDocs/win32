---
error-parsing-yaml: 
---

# IVMVirtualServer::UnconnectedNetworkAdapters property

The **UnconnectedNetworkAdapters** property contains a collection of unconnected [**IVMNetworkAdapter**](ivmnetworkadapter.md) objects.

This property is read-only.

## Syntax


```C++
HRESULT get_UnconnectedNetworkAdapters(
  [out] IVMNetworkAdapterCollection **unconnectedNetworkAdapterCollection
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
<td><pre><code>VMVirtualServer.UnconnectedNetworkAdapters( _
  ByRef unconnectedNetworkAdapterCollection _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**IVMNetworkAdapterCollection**](ivmnetworkadaptercollection.md) object associated with Virtual Server.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                       |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                      |
| <dl> <dt>E\_POINTER</dt> </dl>         | *unconnectedNetworkAdapterCollection* is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                      |



## Examples

The following example displays the [**Count**](ivmnetworkadaptercollection-count.md) property of the **UnconnectedNetworkAdapters** object associated with the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")

Wscript.Echo "Name: " & objVS.Name
Set objUNA = objVS.UnconnectedNetworkAdapters
Wscript.Echo "Unconnected network adapters: " & objUNA.Count
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

 

 





