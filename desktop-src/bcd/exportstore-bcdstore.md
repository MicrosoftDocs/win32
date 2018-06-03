---
title: ExportStore method of the BcdStore class
description: Exports the BCD store to the specified file. The resulting file can be used with ImportStore or BcdEdit /import.
ms.assetid: 4212ce1b-bcf1-40d6-b590-9f963c6b1723
keywords:
- ExportStore method Boot Config
- ExportStore method Boot Config , BcdStore class
- BcdStore class Boot Config , ExportStore method
topic_type:
- apiref
api_name:
- BcdStore.ExportStore
api_location:
- Root\WMI
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ExportStore method of the BcdStore class

Exports the BCD store to the specified file. The resulting file can be used with [**ImportStore**](importstore-bcdstore.md) or **BcdEdit /import**.

## Syntax


```mof
boolean ExportStore(
  [in] string File
);
```



## Parameters

<dl> <dt>

*File* \[in\]
</dt> <dd>

Path to the file where the exported BCD store will be copied.

</dd> </dl>

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Namespace<br/>                | Root\\WMI<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Bcd.mof</dt> </dl> |



## See also

<dl> <dt>

[**BcdStore**](bcdstore.md)
</dt> <dt>

[**ImportStore**](importstore-bcdstore.md)
</dt> </dl>

 

 





