---
description: The SWbemRefresher.DeleteAll method removes all the items from the collection in the SWbemRefresher object.SWbemRefresher object.
ms.assetid: c6e462d3-52b3-40c0-9a9c-fa268415a5f0
ms.tgt_platform: multiple
title: SWbemRefresher.DeleteAll method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemRefresher.DeleteAll
- ISWbemRefresher.DeleteAll
- ISWbemRefresher.DeleteAll
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemRefresher.DeleteAll method

The **SWbemRefresher.DeleteAll** method removes all the items from the collection in the [**SWbemRefresher**](swbemrefresher.md) object.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
SWbemRefresher.DeleteAll()
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

The corresponding [**SWbemRefreshableItem**](swbemrefreshableitem.md) for each removed item has its [**Refresher**](swbemrefreshableitem-refresher.md) property set to **NULL**, which indicates that it no longer has a parent refresher.

## Requirements



| Requirement | Value |
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

 

 




