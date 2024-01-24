---
description: The SWbemRefreshableItem.Remove method removes the SWbemRefreshableItem object from the parent SWbemRefresher object.SWbemRefreshableItem object from the parent SWbemRefresher object.
ms.assetid: 8d3f5e22-c343-4191-a20a-6bca2ec9b01a
ms.tgt_platform: multiple
title: SWbemRefreshableItem.Remove method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemRefreshableItem.Remove
- ISWbemRefreshableItem.Remove
- ISWbemRefreshableItem.Remove
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemRefreshableItem.Remove method

The **SWbemRefreshableItem.Remove** method removes the [**SWbemRefreshableItem**](swbemrefreshableitem.md) object from the parent [**SWbemRefresher**](swbemrefresher.md) object.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
SWbemRefreshableItem.Remove( _
  [ ByVal lFlags ] _
)
```



## Parameters

<dl> <dt>

*lFlags* \[in, optional\]
</dt> <dd>

This parameter must be set to 0 (zero).

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

**Error Codes** If the refresher has no item with the specified index, **wbemErrNotFound** is generated.

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

[**SWbemRefresher**](swbemrefresher.md)
</dt> </dl>

 

 




