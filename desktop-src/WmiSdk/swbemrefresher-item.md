---
Description: The SWbemRefresher.Item method returns the specified SWbemRefreshableItem from the collection.SWbemRefreshableItem from the collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8ae3dea5-0582-422e-9cd8-b6d91b41588a
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: SWbemRefresher.Item method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SWbemRefresher.Item method

The **SWbemRefresher.Item** method returns the specified [**SWbemRefreshableItem**](swbemrefreshableitem.md) from the collection.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objItem = .Item( _
  ByVal lIndex _
)
```



## Parameters

<dl> <dt>

*lIndex* 
</dt> <dd>

Index value of the item in the collection.

</dd> </dl>

## Return value

If the call is successful, the specified [**SWbemRefreshableItem**](swbemrefreshableitem.md) object is returned.

## Error codes

If the refresher has no item with the specified index, **wbemErrNotFound** is generated.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemRefresher<br/>                                                        |
| IID<br/>                      | IID\_ISWbemRefresher<br/>                                                         |



## See also

<dl> <dt>

[**SWbemRefresher**](swbemrefresher.md)
</dt> </dl>

 

 




