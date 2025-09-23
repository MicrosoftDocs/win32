---
description: Retrieves the specified connection security rule.
ms.assetid: ffbd2a3c-d84b-41db-99ff-70cbf680802d
title: Find method of the MSFT\_NetConSecRule class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetConSecRule.Find
api_type: 
- COM
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# Find method of the MSFT\_NetConSecRule class

Retrieves the specified connection security rule.

## Syntax


```mof
uint32 Find(
  [in]  string             LocalAddress,
  [in]  string             RemoteAddress,
  [in]  string             Protocol,
  [in]  uint16             LocalPort,
  [in]  uint16             RemotePort,
  [out] MSFT_NetConSecRule CmdletOutput[]
);
```



## Parameters

<dl> <dt>

*LocalAddress* \[in\]
</dt> <dd>

The local address specified in the rule.

</dd> <dt>

*RemoteAddress* \[in\]
</dt> <dd>

The remote address specified in the rule.

</dd> <dt>

*Protocol* \[in\]
</dt> <dd>

The protocol of the rule.

</dd> <dt>

*LocalPort* \[in\]
</dt> <dd>

The local port specified in the rule.

</dd> <dt>

*RemotePort* \[in\]
</dt> <dd>

The remote port specified in the rule.

</dd> <dt>

*CmdletOutput* \[out\]
</dt> <dd>

The [**MSFT\_NetConSecRule**](msft-netconsecrule.md) object that receives the retrieved rule.

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

[**MSFT\_NetConSecRule**](msft-netconsecrule.md)
</dt> </dl>

 

 




