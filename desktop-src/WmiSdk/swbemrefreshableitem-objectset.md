---
description: The SWbemRefreshableItem.ObjectSet property represents the object set to be refreshed.
ms.assetid: f52101b1-bb6e-4798-b20f-d6efd31cf7c1
ms.tgt_platform: multiple
title: SWbemRefreshableItem.ObjectSet property (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemRefreshableItem.ObjectSet
- ISWbemRefreshableItem.ObjectSet
- ISWbemRefreshableItem.get_ObjectSet
- ISWbemRefreshableItem.put_ObjectSet
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemRefreshableItem.ObjectSet property

The **SWbemRefreshableItem.ObjectSet** property represents the object set to be refreshed. The **ObjectSet** property is either an enumerator or a collection item that is contained in an [**SWbemRefresher**](swbemrefresher.md) object.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

This property is read/write.

## Syntax


```VB
SWbemRefreshableItem.ObjectSet As Object
```



## Property value

## Remarks

This property is **NULL** unless [**SWbemRefreshableItem.IsSet**](swbemrefreshableitem-isset.md) is **TRUE**.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemRefreshableItem<br/>                                                  |
| IID<br/>                      | IID\_ISWbemRefreshableItem<br/>                                                   |



## See also

<dl> <dt>

[**SWbemRefreshableItem**](swbemrefreshableitem.md)
</dt> <dt>

[**SWbemRefreshableItem**](swbemrefresher.md)
</dt> </dl>

 

 




