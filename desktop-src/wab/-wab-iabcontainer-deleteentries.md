---
title: IABContainer DeleteEntries method
description: Removes one or more entries from the address book container.
ms.assetid: 3576116f-cb53-46f5-b8e0-f7d97dbae5e0
keywords:
- DeleteEntries method Windows Address Book
- DeleteEntries method Windows Address Book , IABContainer interface
- IABContainer interface Windows Address Book , DeleteEntries method
topic_type:
- apiref
api_name:
- IABContainer.DeleteEntries
api_location:
- Wab32.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IABContainer::DeleteEntries method

Removes one or more entries from the address book container.

## Syntax


```C++
HRESULT DeleteEntries(
   ENTRYLIST *lpEntries,
   ULONG     ulFlags
);
```



## Parameters

<dl> <dt>

*lpEntries* 
</dt> <dd>

Type: **[**ENTRYLIST**](/windows/previous-versions/Wabdefs/ns-wabdefs-_sbinaryarray?branch=master)\***

Pointer to a variable of type [**ENTRYLIST**](/windows/previous-versions/Wabdefs/ns-wabdefs-_sbinaryarray?branch=master) that specifies the identifiers of entries to be deleted.

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
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Product<br/>                  | Internet Explorer 4.0<br/>                                                     |
| Header<br/>                   | <dl> <dt>Wabtmp.h</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>Wab32.dll</dt> </dl> |



 

 





