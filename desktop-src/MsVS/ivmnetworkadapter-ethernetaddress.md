---
title: IVMNetworkAdapter EthernetAddress property
description: The EthernetAddress property contains the Ethernet (MAC/Physical/Network) address of the virtual NIC.
ms.assetid: 62764939-8408-4b52-970b-f487c450bf7d
keywords:
- EthernetAddress property Virtual Server
- EthernetAddress property Virtual Server , IVMNetworkAdapter interface
- IVMNetworkAdapter interface Virtual Server , EthernetAddress property
- EthernetAddress property Virtual Server , VMNetworkAdapter interface
- VMNetworkAdapter interface Virtual Server , EthernetAddress property
topic_type:
- apiref
api_name:
- IVMNetworkAdapter.EthernetAddress
- IVMNetworkAdapter.get_EthernetAddress
- IVMNetworkAdapter.put_EthernetAddress
- VMNetworkAdapter.EthernetAddress
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVMNetworkAdapter::EthernetAddress property

The **EthernetAddress** property contains the Ethernet (MAC/Physical/Network) address of the virtual NIC.

This property is read/write.

## Syntax


```C++
HRESULT put_EthernetAddress(
  [in]  BSTR ethernetAddress
);

HRESULT get_EthernetAddress(
  [out] BSTR *ethernetAddress
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
<td><pre><code>VMNetworkAdapter.EthernetAddress( _
  ByRef ethernetAddress, _
  ByVal ethernetAddress _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The Ethernet address of the virtual NIC. It is in MAC address form of XX-XX-XX-XX-XX-XX where X is a hexadecimal digit with a value in the range of 0-9 or a-f.

This property value is read/write.

## Error codes



| Name                                                                                                               | Meaning                                                                                                                                                                                                                                                                                                                                                                                                       |
|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt> S\_OK</dt> </dl>                                  | The operation was successful.<br/>                                                                                                                                                                                                                                                                                                                                                                      |
| <dl> <dt>E\_POINTER</dt> </dl>                              | The *ethernetAddress* parameter was **NULL**.<br/>                                                                                                                                                                                                                                                                                                                                                      |
| <dl> <dt>E\_INVALIDARG</dt> </dl>                           | The *ethernetAddress* parameter is not in the correct format.<br/>                                                                                                                                                                                                                                                                                                                                      |
| <dl> <dt>VM\_E\_CANT\_SET\_DYNAMIC\_MAC\_ADDRESS</dt> </dl> | The Ethernet address for a network interface can either be generated dynamically by virtual server or can be set to a static address by the user. This method cannot be called when the address is set to be generated dynamically. The [**IsEthernetAddressDynamic**](ivmnetworkadapter-isethernetaddressdynamic.md) property is used to change the generation behavior of the Ethernet address.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl>                      | The virtual machine was not found. This may occur if the machine was removed after the [**IVMNetworkAdapter**](ivmnetworkadapter.md) object was created.<br/>                                                                                                                                                                                                                                          |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>                      | An unexpected error has occurred.<br/>                                                                                                                                                                                                                                                                                                                                                                  |



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

 

 





