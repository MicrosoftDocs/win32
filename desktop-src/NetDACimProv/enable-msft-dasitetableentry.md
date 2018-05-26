---
Description: Turns on manual site selection for DirectAccess.
ms.assetid: 1198c3eb-4b0a-4764-ba21-fb139b6260fd
title: Enable method of the MSFT\_DASiteTableEntry class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enable method of the MSFT\_DASiteTableEntry class

Turns on manual site selection for DirectAccess.

## Syntax


```mof
uint32 Enable(
  [in] string EntryPointName
);
```



## Parameters

<dl> <dt>

*EntryPointName* \[in\]
</dt> <dd>

Specifies the address of the DirectAccess server.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetDACim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetDACim.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DASiteTableEntry**](msft-dasitetableentry.md)
</dt> </dl>

 

 




