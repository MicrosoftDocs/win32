---
title: IDistList OpenEntry method
description: Opens an entry from the distribution list and returns a pointer to the object to provide further access.
ms.assetid: '02d46f4b-d511-4fe9-b995-bcd985b711e2'
keywords: ["OpenEntry method Windows Address Book", "OpenEntry method Windows Address Book , IDistList interface", "IDistList interface Windows Address Book , OpenEntry method"]
topic_type:
- apiref
api_name:
- IDistList.OpenEntry
api_location:
- Wab32.dll
api_type:
- COM
---

# IDistList::OpenEntry method

Opens an entry from the distribution list and returns a pointer to the object to provide further access.

## Syntax


```C++
HRESULT OpenEntry(
   ULONG     cbEntryID,
   ENTRYID   *lpEntryID,
   IID       *lpInterface,
   ULONG     ulFlags,
   ULONG     *lpulObjType,
   LPUNKNOWN *lppUnk
);
```



## Parameters

<dl> <dt>

*cbEntryID* 
</dt> <dd>

Type: **ULONG**

Value of type **ULONG** specifying the size of the entry identifier to open.

</dd> <dt>

*lpEntryID* 
</dt> <dd>

Type: **[**ENTRYID**](-wab-entryid.md)\***

Pointer to a variable of type [**ENTRYID**](-wab-entryid.md) specifying the address to open for the entry identifier of the object.

</dd> <dt>

*lpInterface* 
</dt> <dd>

Type: **IID\***

Pointer to a variable of type **IID** that specifies the address of an interface identifier (IID) for the object to open. User must pass a **NULL** value to specify the standard interface for the object.

</dd> <dt>

*ulFlags* 
</dt> <dd>

Type: **ULONG**

Value of type **ULONG** specifying the bitmask containing object access flags. The default is "read access only." The following flags can be used for modifications:

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

Not supported by Windows Address Book.

</dd> </dl> </dd> <dt>

*lpulObjType* 
</dt> <dd>

Type: **ULONG\***

Pointer to a variable of type **ULONG** receiving the address of the object type of the opened entry.

</dd> <dt>

*lppUnk* 
</dt> <dd>

Type: **LPUNKNOWN\***

Pointer to an IUnknown interface receiving the object pointer to the opened entry.

</dd> </dl>

## Return value

Type: **HRESULT**

This method can return one of these values.



| Return code                                                                                              | Description                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                     | The entry was successfully opened.<br/>                                                                                                                                                   |
| <dl> <dt>**MAPI\_E\_NO\_ACCESS**</dt> </dl>       | An attempt was made to open an entry for which the user has insufficient permissions.<br/>                                                                                                |
| <dl> <dt>**MAPI\_E\_NOT\_FOUND**</dt> </dl>       | The entry represented by *lpEntryID* does not exist.<br/>                                                                                                                                 |
| <dl> <dt>**MAPI\_E\_UNKNOWN\_ENTRYID**</dt> </dl> | The entry identifier specified in *lpEntryID* is not recognized. This value is typically returned if the address book provider responsible for the corresponding entry is not open. <br/> |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Product<br/>                  | Internet Explorer 4.0<br/>                                                     |
| Header<br/>                   | <dl> <dt>Wabtmp.h</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>Wab32.dll</dt> </dl> |



 

 





