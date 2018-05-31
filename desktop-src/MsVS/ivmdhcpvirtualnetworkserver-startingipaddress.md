---
error-parsing-yaml: 
---

# IVMDHCPVirtualNetworkServer::StartingIPAddress property

The **StartingIPAddress** property contains the first TCP/IP address that the server can dynamically assign to a client on the Virtual Network.

This property is read-only.

## Syntax


```C++
HRESULT get_StartingIPAddress(
  [out] BSTR *startingIPAddress
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
<td><pre><code>VMDHCPVirtualNetworkServer.StartingIPAddress( _
  ByRef startingIPAddress _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Retrieves the TCP/IP address formatted as a string in dotted-decimal notation, such as "10.237.0.16".

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                    |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                   |
| <dl> <dt> E\_POINTER</dt> </dl>        | The parameter *startingIPAddress* was **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>               |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMDHCPVirtualNetworkServer**](ivmdhcpvirtualnetworkserver.md)
</dt> </dl>

 

 





