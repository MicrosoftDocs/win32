---
title: IDistList CreateEntry method
description: Creates a new entry in the distribution list container.
ms.assetid: 'b159ccd3-5825-4e1b-acd0-9287b46ea69e'
keywords: ["CreateEntry method Windows Address Book", "CreateEntry method Windows Address Book , IDistList interface", "IDistList interface Windows Address Book , CreateEntry method"]
topic_type:
- apiref
api_name:
- IDistList.CreateEntry
api_location:
- Wab32.dll
api_type:
- COM
---

# IDistList::CreateEntry method

Creates a new entry in the distribution list container.

## Syntax


```C++
HRESULT CreateEntry(
   ULONG     cbEntryID,
   ENTRYID   *lpEntryID,
   ULONG     ulCreateFlags,
   IDistList **lppMAPIPropEntry
);
```



## Parameters

<dl> <dt>

*cbEntryID* 
</dt> <dd>

Type: **ULONG**

Value of type **ULONG** that specifies the size of the existing EntryID to copy from.

</dd> <dt>

*lpEntryID* 
</dt> <dd>

Type: **[**ENTRYID**](-wab-entryid.md)\***

Pointer to a variable of type [**ENTRYID**](-wab-entryid.md) specifying the entry identifier of the object to copy from.

</dd> <dt>

*ulCreateFlags* 
</dt> <dd>

Type: **ULONG**

Value of type **ULONG** specifying the bitmask that controls the level of duplicate entries. The following flags may be set:

<dt>

<span id="CREATE_CHECK_DUP_LOOSE"></span><span id="create_check_dup_loose"></span>

<span id="CREATE_CHECK_DUP_LOOSE"></span><span id="create_check_dup_loose"></span>**CREATE\_CHECK\_DUP\_LOOSE**


</dt> <dd>

Indicates a loose level should be used for duplicate entry checking, which returns more matches than setting a strict level with the CREATE\_CHECK\_DUP\_STRICT flag. For example, a provider can define a loose match as any two entries having the same display name, while defining a strict match as any two entries having the same display name and messaging address.

</dd> <dt>

<span id="CREATE_CHECK_DUP_STRICT"></span><span id="create_check_dup_strict"></span>

<span id="CREATE_CHECK_DUP_STRICT"></span><span id="create_check_dup_strict"></span>**CREATE\_CHECK\_DUP\_STRICT**


</dt> <dd>

Indicates a strict level should be used for duplicate entry checking, which returns fewer matches than setting a loose level with the CREATE\_CHECK\_DUP\_LOOSE flag.

</dd> <dt>

<span id="CREATE_REPLACE"></span><span id="create_replace"></span>

<span id="CREATE_REPLACE"></span><span id="create_replace"></span>**CREATE\_REPLACE**


</dt> <dd>

Indicates that duplicate entries replace existing entries within a container.

</dd> </dl> </dd> <dt>

*lppMAPIPropEntry* 
</dt> <dd>

Type: **[**IDistList**](-wab-idistlist.md)\*\***

Address of a pointer to a variable of type [**IDistList**](-wab-idistlist.md) receiving the property interface to the new object.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Windows Address Book supports creation of mail users and distribution lists.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Product<br/>                  | Internet Explorer 4.0<br/>                                                     |
| Header<br/>                   | <dl> <dt>Wabtmp.h</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>Wab32.dll</dt> </dl> |



 

 





