---
description: The SWbemRefreshableItem.Object property represents a single SWbemObject instance that is refreshed. The item is contained in an SWbemRefresher object.SWbemObject instance that is refreshed. The item is contained in an SWbemRefresher object.
ms.assetid: 91a693c0-cde4-4cf6-b85a-662cfd0333e9
ms.tgt_platform: multiple
title: SWbemRefreshableItem.Object property (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemRefreshableItem.Object
- ISWbemRefreshableItem.Object
- ISWbemRefreshableItem.get_Object
- ISWbemRefreshableItem.put_Object
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemRefreshableItem.Object property

The **SWbemRefreshableItem.Object** property represents a single [**SWbemObject**](swbemobject.md) instance that is refreshed. The item is contained in an [**SWbemRefresher**](swbemrefresher.md) object.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

This property is read/write.

## Syntax


```VB
SWbemRefreshableItem.Object As Object
```



## Property value

## Remarks

This property is **NULL** unless [**SWbemRefreshableItem.IsSet**](swbemrefreshableitem-isset.md) is **FALSE**.

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

 

 




