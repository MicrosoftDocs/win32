---
title: View ExportList method
description: The ExportList method exports the selected list to the specified file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ff552b80-2f5f-4425-9157-71f7c7fb5a44
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- ExportList method MMC
- ExportList method MMC , View object
- View object MMC , ExportList method
- ExportList method MMC , View interface
- View interface MMC , ExportList method
topic_type:
- apiref
api_name:
- View.ExportList
- View.ExportList
api_location:
- Mmc.exe
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# View::ExportList method

The **ExportList** method exports the selected list to the specified file.

## Syntax


```VB
View.ExportList( _
  ByVal File As String, _
  ByVal exportoptions As ExportListOptions _
)
```



## Parameters

<dl> <dt>

*File* 
</dt> <dd>

The name of the export file.

</dd> <dt>

*exportoptions* 
</dt> <dd>

This parameter can be one or more of the following [**ExportListOptions**](/windows/win32/MmcObj/ne-mmcobj-exportlistoptions?branch=master) values. These flags can be combined using a bitwise OR operation.

<dt>

<span id="ExportListOptions_Default"></span><span id="exportlistoptions_default"></span><span id="EXPORTLISTOPTIONS_DEFAULT"></span>

<span id="ExportListOptions_Default"></span><span id="exportlistoptions_default"></span><span id="EXPORTLISTOPTIONS_DEFAULT"></span>**ExportListOptions\_Default**


</dt> <dd>

Default list export option. If this is the only flag specified in the call to **View.ExportList**, then the list view contents are exported as comma-delimited ANSI text.

</dd> <dt>

<span id="ExportListOptions_Unicode"></span><span id="exportlistoptions_unicode"></span><span id="EXPORTLISTOPTIONS_UNICODE"></span>

<span id="ExportListOptions_Unicode"></span><span id="exportlistoptions_unicode"></span><span id="EXPORTLISTOPTIONS_UNICODE"></span>**ExportListOptions\_Unicode**


</dt> <dd>

The list is exported as Unicode text.

</dd> <dt>

<span id="ExportListOptions_TabDelimited"></span><span id="exportlistoptions_tabdelimited"></span><span id="EXPORTLISTOPTIONS_TABDELIMITED"></span>

<span id="ExportListOptions_TabDelimited"></span><span id="exportlistoptions_tabdelimited"></span><span id="EXPORTLISTOPTIONS_TABDELIMITED"></span>**ExportListOptions\_TabDelimited**


</dt> <dd>

The list is exported as tab-delimited text.

</dd> <dt>

<span id="ExportListOptions_SelectedItemsOnly"></span><span id="exportlistoptions_selecteditemsonly"></span><span id="EXPORTLISTOPTIONS_SELECTEDITEMSONLY"></span>

<span id="ExportListOptions_SelectedItemsOnly"></span><span id="exportlistoptions_selecteditemsonly"></span><span id="EXPORTLISTOPTIONS_SELECTEDITEMSONLY"></span>**ExportListOptions\_SelectedItemsOnly**


</dt> <dd>

The exported list contains only selected items.

</dd> </dl> </dd> </dl>

## Return value

This method does not return a value.

## Examples


```VB
' Export the list view contents.
objView.ExportList "D:\output.txt", _
            ExportListOptions_TabDelimited Or _
            ExportListOptions_SelectedItemsOnly
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mmc.exe</dt> </dl>    |
| IID<br/>                      | IID\_View is defined as 6EFC2DA2-B38C-457E-9ABB-ED2D189B8C38<br/>               |



## See also

<dl> <dt>

[**ExportListOptions**](/windows/win32/MmcObj/ne-mmcobj-exportlistoptions?branch=master)
</dt> </dl>

 

 





