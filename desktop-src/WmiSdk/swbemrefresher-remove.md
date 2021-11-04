---
description: The SWbemRefresher.Remove method removes the SWbemRefreshableItem object with the specified index from the refresher.
ms.assetid: db5ac740-e2b3-4667-b511-d750cb092e0f
ms.tgt_platform: multiple
title: SWbemRefresher.Remove method (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemRefresher.Remove
- ISWbemRefresher.Remove
- ISWbemRefresher.Remove
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemRefresher.Remove method

The **SWbemRefresher.Remove** method removes the [**SWbemRefreshableItem**](swbemrefreshableitem.md) object with the specified index from the refresher. The **SWbemRefreshableItem** object can represent either a single object or an object set.

For an explanation of this syntax, see [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md).

## Syntax


```VB
objRefresher = .Remove( _
  ByVal LIndex, _
  [ ByVal iFlags ], _
  [ ByVal objWbemNamedvalueSet ] _
)
```



## Parameters

<dl> <dt>

*LIndex* 
</dt> <dd>

Index of the item in the [**SWbemRefresher**](swbemrefresher.md) object.

</dd> <dt>

*iFlags* \[optional\]
</dt> <dd>

Flags must be set t0 (zero).

</dd> <dt>

*objWbemNamedvalueSet* \[optional\]
</dt> <dd>

Null.

</dd> </dl>

## Return value

This method has no return values.

## Remarks

**Error codes** If the refresher has no item with the specified index, **wbemErrNotFound** is generated.

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

 

 




