---
error-parsing-yaml: 
---

# IVMDHCPVirtualNetworkServer::ServerIPAddress property

The **ServerIPAddress** property contains the TCP/IP address of the virtual DHCP server.

This property is read-only.

## Syntax


```C++
HRESULT get_ServerIPAddress(
  [out] BSTR *serverIPAddress
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
<td><pre><code>VMDHCPVirtualNetworkServer.ServerIPAddress( _
  ByRef serverIPAddress _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Retrieves the TCP/IP address of the virtual DHCP server formatted as a string in dotted-decimal notation, such as "10.237.0.16".

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                  |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                 |
| <dl> <dt> E\_POINTER</dt> </dl>        | The parameter *serverIPAddress* was **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>             |



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

 

 





