---
title: Extensions Item method
description: The Item method returns the Extension object at a specified index.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '684cb03a-4e22-457e-9296-49c985776eed'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["Item method MMC", "Item method MMC , Extensions object", "Extensions object MMC , Item method", "Item method MMC , Extensions interface", "Extensions interface MMC , Item method"]
topic_type:
- apiref
api_name:
- Extensions.Item
- Extensions.Item
api_location:
- Mmcndmgr.dll
api_type:
- COM
---

# Extensions::Item method

The **Item** method returns the [**Extension**](extension-object.md) object at a specified index.

## Syntax


```VB
Extensions.Item( _
  ByVal Index As Long _
) As Extension
```



## Parameters

<dl> <dt>

*Index* 
</dt> <dd>

The index of the extension being retrieved. The index is 1-based.

</dd> </dl>

## Examples


```VB
' Retrieve the count of Extension objects.
Dim nCount As Long
nCount = objExts.Count
 
' Iterate the Extensions.
Dim i As Long
Dim objExt As MMC20.Extension
For i = 1 To nCount
    Set objExt = objExts.Item(i)
    ' Use the Extension object.
    ' This code will display the Extension name.
    MsgBox (objExt.Name)
    ' Free the object for the next iteration.
    Set objExt = Nothing
Next i
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Mmcndmgr.dll</dt> </dl> |
| IID<br/>                      | IID\_Extensions is defined as 82DBEA43-8CA4-44bc-A2CA-D18741059EC8<br/>           |



## See also

<dl> <dt>

[**Extensions.Count**](extensions-count.md)
</dt> </dl>

 

 





