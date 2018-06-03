---
Description: Renames an entry in the DirectAccess site table.
ms.assetid: c1f98b50-b4f6-45ce-8e3d-da625f2b47f7
title: Rename method of the MSFT\_DASiteTableEntry class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Rename method of the MSFT\_DASiteTableEntry class

Renames an entry in the DirectAccess site table.

## Syntax


```mof
uint32 Rename(
  [in]  string                NewName,
  [in]  boolean               PassThru,
  [out] MSFT_DASiteTableEntry OutputObject
);
```



## Parameters

<dl> <dt>

*NewName* \[in\]
</dt> <dd>

Specifies the new name for the entry.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifies whether the method should output an object that represents the renamed entry in the *OutputObject* parameter.

</dd> <dt>

*OutputObject* \[out\]
</dt> <dd>

Receives a [**MSFT\_DASiteTableEntry**](msft-dasitetableentry.md) object for the renamed entry.

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

 

 




