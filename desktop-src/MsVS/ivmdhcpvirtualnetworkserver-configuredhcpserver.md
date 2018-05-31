---
error-parsing-yaml: 
---

# IVMDHCPVirtualNetworkServer::ConfigureDHCPServer method

The **ConfigureDHCPServer** method sets the parameters for the virtual network DHCP server.

## Syntax


```C++
HRESULT ConfigureDHCPServer(
  [in] BSTR network,
  [in] BSTR networkMask,
  [in] BSTR startingIPAddress,
  [in] BSTR endingIPAddress,
  [in] BSTR serverIPAddress
);
```



## Parameters

<dl> <dt>

*network* \[in\]
</dt> <dd>

This parameter and the *networkMask* parameter define the range of TCP/IP addresses managed by the DHCP server. This parameter defines the base TCP/IP address of the range.

For example, a *network* of "192.168.0.0" and a *networkMask* of "255.255.255.0" defines the address range "192.168.0.1" to "192.168.0.254". ("192.168.0.0" is invalid and "192.168.0.255" is a special address used to broadcast to all nodes in this network range.)

This parameter must contain a TCP/IP address formatted as a string in dotted-decimal notation, such as "10.237.0.0".

</dd> <dt>

*networkMask* \[in\]
</dt> <dd>

This parameter and the *network* parameter define the range of TCP/IP addresses managed by the DHCP server. This parameter is a mask used to calculate the base TCP/IP address for the given network.

This parameter must contain a TCP/IP address formatted as a string in dotted-decimal notation, such as "255.255.0.0".

</dd> <dt>

*startingIPAddress* \[in\]
</dt> <dd>

This parameter specifies the first TCP/IP address that the server can dynamically assign to a client on the Virtual Network. Virtual Server reserves the first fifteen TCP/IP valid *network* and *networkMask* for internal use. Therefore, this parameter must have a value between the sixteenth and the last valid TCP/IP address.

For example, if the *network* parameter is "192.168.0.0", *startingIPAddress* must be between "192.168.0.16" and "192.168.0.254".

This parameter must contain a TCP/IP address formatted as a string in dotted-decimal notation, such as "10.237.0.16".

</dd> <dt>

*endingIPAddress* \[in\]
</dt> <dd>

This parameter specifies the last TCP/IP address that the DHCP server can dynamically assign to a client on the Virtual Network. The value must be between the *startingIPAddress* parameter and the last valid TCP/IP address.

This parameter must contain a TCP/IP address formatted as a string in dotted-decimal notation, such as "10.237.255.254".

</dd> <dt>

*serverIPAddress* \[in\]
</dt> <dd>

This parameter specifies the TCP/IP address to be used by the DHCP server. The value must be between the first valid TCP/IP address defined by the *network* and *networkMask* parameters and the *startingIPAddress* parameter.

This parameter must contain a TCP/IP address formatted as a string in dotted-decimal notation, such as "10.237.255.131".

</dd> </dl>

## Return value

This method can return one of these values.

This method supports standard return values, as well as the following. For information on Virtual Server specific return values not listed below, see [**HRESULT Codes Specific to the Virtual Server**](hresult-codes-specific-to-the-virtual-server.md).



| Return code                                                                                                        | Description                                                                             |
|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| <dl> <dt> **S\_OK** </dt> </dl>                             | The operation was successful.<br/>                                                |
| <dl> <dt> **E\_INVALIDARG**</dt> </dl>                      | A parameter contained no data (the string was empty).<br/>                        |
| <dl> <dt> **VM\_E\_INVALID\_IP\_ADDRESS** </dt> </dl>       | A parameter was not a valid IP address.<br/>                                      |
| <dl> <dt> **VM\_E\_INVALID\_NETWORK\_ADDRESS** </dt> </dl>  | The IP address string must be a class A, class B, or class C address.<br/>        |
| <dl> <dt> **VM\_E\_INVALID\_NETWORK\_MASK** </dt> </dl>     | The network mask is not valid for the class of network address.<br/>              |
| <dl> <dt> **VM\_E\_INVALID\_ENDING\_ADDRESS** </dt> </dl>   | The ending IP address is not in a valid range.<br/>                               |
| <dl> <dt> **VM\_E\_INVALID\_STARTING\_ADDRESS** </dt> </dl> | The starting IP address is not in a valid range.<br/>                             |
| <dl> <dt> **VM\_E\_INVALID\_ADDRESS\_RANGE** </dt> </dl>    | The starting IP address must be less than or equal to the ending IP address.<br/> |
| <dl> <dt> **DISP\_E\_EXCEPTION** </dt> </dl>                | An unexpected error has occurred.<br/>                                            |



 

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

 

 





