---
title: IABContainer OpenEntry method
description: Opens a child container object in the open container.
ms.assetid: 9300d757-8eb9-4160-9e05-9eee3b58b0fb
keywords:
- OpenEntry method Windows Address Book
- OpenEntry method Windows Address Book , IABContainer interface
- IABContainer interface Windows Address Book , OpenEntry method
topic_type:
- apiref
api_name:
- IABContainer.OpenEntry
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

# IABContainer::OpenEntry method

Opens a child container object in the open container.

## Syntax


```C++
HRESULT OpenEntry(
   ULONG     cbEntryID,
   ENTRYID   *lpEntryID,
   IID       *lpInterface,
   ULONG     ulFlags,
   ULONG     *lpulObjType,
   LPUNKNOWN *lppUnk
);
```



## Parameters

<dl> <dt>

*cbEntryID* 
</dt> <dd>

Type: **ULONG**

Value of type **ULONG** that specifies the size of the entry identifier to open.

</dd> <dt>

*lpEntryID* 
</dt> <dd>

Type: **[**ENTRYID**](/windows/previous-versions/Wabdefs/ns-wabdefs-entryid?branch=master)\***

Pointer to a variable of type [**ENTRYID**](/windows/previous-versions/Wabdefs/ns-wabdefs-entryid?branch=master) that specifies the identifier of the object to open.

</dd> <dt>

*lpInterface* 
</dt> <dd>

Type: **IID\***

Pointer to a variable of type **IID** that specifies the IID of the object to open. A user must pass a **NULL** value to specify the standard interface for the object.

</dd> <dt>

*ulFlags* 
</dt> <dd>

Type: **ULONG**

Value of type **ULONG** that specifies the bitmask containing the object access flags. The following flags can be used:

<dt>

<span id="MAPI_BEST_ACCESS"></span><span id="mapi_best_access"></span>

<span id="MAPI_BEST_ACCESS"></span><span id="mapi_best_access"></span>**MAPI\_BEST\_ACCESS**


</dt> <dd>

Opens with the best available access rights.

</dd> <dt>

<span id="MAPI_MODIFY"></span><span id="mapi_modify"></span>

<span id="MAPI_MODIFY"></span><span id="mapi_modify"></span>**MAPI\_MODIFY**


</dt> <dd>

Requests read/write access.

</dd> <dt>

<span id="MAPI_DEFERRED_ERRORS"></span><span id="mapi_deferred_errors"></span>

<span id="MAPI_DEFERRED_ERRORS"></span><span id="mapi_deferred_errors"></span>**MAPI\_DEFERRED\_ERRORS**


</dt> <dd>

Not supported by the WAB.

</dd> </dl> </dd> <dt>

*lpulObjType* 
</dt> <dd>

Type: **ULONG\***

Pointer to a variable of type **ULONG** that receives the address of the object type of the opened entry.

</dd> <dt>

*lppUnk* 
</dt> <dd>

Type: **LPUNKNOWN\***

Pointer to an IUnknown interface that receives the object pointer to the opened entry.

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



 

 





