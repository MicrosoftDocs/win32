---
title: IDistList DeleteEntries method
description: Removes one or more entries from the distribution list.
ms.assetid: '0d268a7c-7a93-4155-b2cb-a1b1067a8ec6'
keywords: ["DeleteEntries method Windows Address Book", "DeleteEntries method Windows Address Book , IDistList interface", "IDistList interface Windows Address Book , DeleteEntries method"]
topic_type:
- apiref
api_name:
- IDistList.DeleteEntries
api_location:
- Wab32.dll
api_type:
- COM
---

# IDistList::DeleteEntries method

Removes one or more entries from the distribution list.

## Syntax


```C++
HRESULT DeleteEntries(
   ENTRYLIST *lpEntries,
   ULONG     ulFlags
);
```



## Parameters

<dl> <dt>

*lpEntries* 
</dt> <dd>

Type: **[**ENTRYLIST**](-wab-entrylist.md)\***

Pointer to a variable of type [**ENTRYLIST**](-wab-entrylist.md) that specifies the address of an array of entry identifier structures that are being deleted from the distribution list.

</dd> <dt>

*ulFlags* 
</dt> <dd>

Type: **ULONG**

Reserved. Must be set to 0.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Product<br/>                  | Internet Explorer 4.0<br/>                                                     |
| Header<br/>                   | <dl> <dt>Wabtmp.h</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>Wab32.dll</dt> </dl> |



 

 





