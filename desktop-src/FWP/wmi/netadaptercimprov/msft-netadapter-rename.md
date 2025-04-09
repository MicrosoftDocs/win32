---
description: Renames a network adapter.
ms.assetid: 1950746F-9FB1-4333-A702-8A7838132B2D
title: Rename method of the MSFT\_NetAdapter class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapter.Rename
api_type: 
- COM
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# Rename method of the MSFT\_NetAdapter class

Renames a network adapter.

## Syntax


```mof
uint32 Rename(
  [in]  string NewName,
  [out] string CmdletOutput
);
```



## Parameters

<dl> <dt>

*NewName* \[in\]
</dt> <dd>

The new name for the network adapter.

</dd> <dt>

*CmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**MSFT\_NetAdapter**](msft-netadapter.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                   |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_NetAdapter**](msft-netadapter.md)
</dt> </dl>

 

 




