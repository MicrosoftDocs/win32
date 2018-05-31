---
error-parsing-yaml: 
---

# IVMDHCPVirtualNetworkServer::DefaultGatewayAddress property

The **DefaultGatewayAddress** property specifies the TCP/IP address of the default gateway.

This property is read/write.

## Syntax


```C++
HRESULT put_DefaultGatewayAddress(
  [in]  BSTR defaultGatewayAddress
);

HRESULT get_DefaultGatewayAddress(
  [out] BSTR *defaultGatewayAddress
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
<td><pre><code>VMDHCPVirtualNetworkServer.DefaultGatewayAddress( _
  ByRef defaultGatewayAddress, _
  ByVal defaultGatewayAddress _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The TCP/IP address formatted as a string in dotted-decimal notation. For example, 10.237.0.1.

This property value is read/write. If an empty value is written then the current default gateway is deleted.

## Error codes



| Name                                                                                                   | Meaning                                                                                     |
|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                       | The operation was successful.<br/>                                                    |
| <dl> <dt>E\_POINTER</dt> </dl>                  | The *defaultGatewayAddress* parameter was **NULL**.<br/>                              |
| <dl> <dt>VM\_E\_INVALID\_IP\_ADDRESS</dt> </dl> | The *defaultGatewayAddress* parameter was not a valid dotted-decimal IP address.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>          | An unexpected error has occurred.<br/>                                                |



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

 

 





