---
description: Determines whether the specified network address points to an intranet or Internet network.
ms.assetid: 5479bf61-9539-4c62-be06-2597193cacf2
title: QueryIsolationType method of the MSFT\_NetAddressFilter class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAddressFilter.QueryIsolationType
api_type: 
- COM
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# QueryIsolationType method of the MSFT\_NetAddressFilter class

Determines whether the specified network address points to an intranet or Internet network.

## Syntax


```mof
uint32 QueryIsolationType(
  [in]  uint32 InterfaceIndex,
  [in]  string RemoteAddress,
  [out] uint32 IsolationType
);
```



## Parameters

<dl> <dt>

*InterfaceIndex* \[in\]
</dt> <dd>

The index of the network interface for the network address.

</dd> <dt>

*RemoteAddress* \[in\]
</dt> <dd>

The remote network address.

</dd> <dt>

*IsolationType* \[out\]
</dt> <dd>

Receives a value that indicates whether the network address points to an intranet or Internet network. This parameter returns one of the following values.



| Value                                                                        | Meaning                                                       |
|------------------------------------------------------------------------------|---------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | The network address points to an intranet network.<br/> |
| <dl> <dt>1</dt> </dl> | The network address points to an Internet network.<br/> |



 

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                      |
| Namespace<br/>                | Root\\standardcimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_NetAddressFilter**](msft-netaddressfilter.md)
</dt> </dl>

 

 




