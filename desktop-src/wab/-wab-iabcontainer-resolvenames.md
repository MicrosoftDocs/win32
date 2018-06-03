---
title: IABContainer ResolveNames method
description: Resolves entries against the address book container.
ms.assetid: 74991ff8-0ec4-413f-ba73-c60c9d0c8065
keywords:
- ResolveNames method Windows Address Book
- ResolveNames method Windows Address Book , IABContainer interface
- IABContainer interface Windows Address Book , ResolveNames method
topic_type:
- apiref
api_name:
- IABContainer.ResolveNames
api_location:
- Wab32.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IABContainer::ResolveNames method

Resolves entries against the address book container.

## Syntax


```C++
HRESULT ResolveNames(
   SPropTagArray *lpPropTagArray,
   ULONG         ulFlags = ,
   ADRLIST       *lpAdrList,
   FlagList      *lpFlagList
);
```



## Parameters

<dl> <dt>

*lpPropTagArray* 
</dt> <dd>

Type: **[**SPropTagArray**](/previous-versions/windows/desktop/api/Wabdefs/ns-wabdefs-_sproptagarray)\***

Pointer to a variable of type [**SPropTagArray**](/previous-versions/windows/desktop/api/Wabdefs/ns-wabdefs-_sproptagarray) that specifies the set of properties to be included in the returned [**ADRLIST**](/previous-versions/windows/desktop/api/Wabdefs/ns-wabdefs-_adrlist). Pass **NULL** to return the default columns.

</dd> <dt>

*ulFlags* 
</dt> <dd>

Type: **ULONG**

Value of type **ULONG** that specifies flags affecting functionality.

<dt>



 (0)


</dt> <dd>

Default.

</dd> <dt>

<span id="WAB_IGNORE_PROFILES"></span><span id="wab_ignore_profiles"></span>

<span id="WAB_IGNORE_PROFILES"></span><span id="wab_ignore_profiles"></span>**WAB\_IGNORE\_PROFILES**


</dt> <dd>

Enables the caller to resolve names against the whole WAB, not just against the current container, during profile-enabled sessions. The flag can be useful when you need to bypass profiles and containers.

</dd> </dl> </dd> <dt>

*lpAdrList* 
</dt> <dd>

Type: **[**ADRLIST**](/previous-versions/windows/desktop/api/Wabdefs/ns-wabdefs-_adrlist)\***

Pointer to a variable of type [**ADRLIST**](/previous-versions/windows/desktop/api/Wabdefs/ns-wabdefs-_adrlist) that specifies the address list of entries whose names need to be resolved. On output, *lpFlagList* receives the list of resolved names.

</dd> <dt>

*lpFlagList* 
</dt> <dd>

Type: **FlagList\***

Pointer to a variable of type [FLAGLIST](https://msdn.microsoft.com/windows/desktop/fdc53a19-38be-4ee9-a092-a085196bdde5) that receives an array of input-output flags. Each flag corresponds to an entry in *lpAdrList* and provides the name resolution status for that particular entry. The flags in the *lpFlagList* parameter are in the same order as the entries in *lpAdrList*. The following flags can be set:

<dt>

<span id="MAPI_AMBIGUOUS"></span><span id="mapi_ambiguous"></span>

<span id="MAPI_AMBIGUOUS"></span><span id="mapi_ambiguous"></span>**MAPI\_AMBIGUOUS**


</dt> <dd>

Indicates that the corresponding entry was resolved, but was not resolved to a unique entry identifier. If this flag is returned, other containers must ignore this entry in further resolution.

</dd> <dt>

<span id="MAPI_RESOLVED"></span><span id="mapi_resolved"></span>

<span id="MAPI_RESOLVED"></span><span id="mapi_resolved"></span>**MAPI\_RESOLVED**


</dt> <dd>

Indicates that the corresponding entry has been resolved to a unique entry identifier. If this flag is returned, other containers must ignore this entry in further resolution.

</dd> <dt>

<span id="MAPI_UNRESOLVED"></span><span id="mapi_unresolved"></span>

<span id="MAPI_UNRESOLVED"></span><span id="mapi_unresolved"></span>**MAPI\_UNRESOLVED**


</dt> <dd>

Indicates that the corresponding entry is unresolved. Another container can attempt to resolve this entry.

</dd> </dl> </dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

**IABContainer::ResolveNames** uses the address list passed in *lpAdrList* in attempting to resolve all the entries that have their corresponding **MAPI\_UNRESOLVED** flag set in *lpFlagList*. Entries in *lpAdrList* that lack the PR\_ENTRYID property are considered unresolved.

The client uses the array of flags retrieved by **IABContainer::ResolveNames** in *lpFlagList* to track the results of the name resolution operation. The array indicates whether each entry name is resolved, unresolved, or matches more than one entry. If the container can uniquely match any unresolved entry, **IABContainer::ResolveNames** sets the flag for that entry in *lpFlagList* to **MAPI\_RESOLVED**. **IABContainer::ResolveNames** also adds the PR\_ENTRYID property for that entry to the entry's [**ADRENTRY**](/previous-versions/windows/desktop/api/Wabdefs/ns-wabdefs-_adrentry) structure in the address list in *lpAdrList*. If a container holds more than one entry that matches a given unresolved entry, **IABContainer::ResolveNames** sets the flag for the unresolved entry in *lpFlagList* to **MAPI\_AMBIGUOUS** and leaves that entry's **ADRENTRY** unchanged.

If **IABContainer::ResolveNames** cannot retrieve all of the properties requested for an unresolved entry, and these properties do not exist in the [**ADRENTRY**](/previous-versions/windows/desktop/api/Wabdefs/ns-wabdefs-_adrentry) structure passed in, **IABContainer::ResolveNames** sets the property type of each property not retrieved to PT\_ERROR. Any property columns that are already included for an entry are retained if that entry is resolved.

> [!Note]  
> The [**ADRENTRY**](/previous-versions/windows/desktop/api/Wabdefs/ns-wabdefs-_adrentry) items in the [**ADRLIST**](/previous-versions/windows/desktop/api/Wabdefs/ns-wabdefs-_adrlist) must be allocated separately, NOT allocated with [**AllocateMore**](/previous-versions/windows/desktop/api/Wabapi/). When **IABContainer::ResolveNames** replaces an entry, it uses [**FreeBuffer**](/previous-versions/windows/desktop/api/Wabapi/) to eliminate the **ADRENTRY** and [**AllocateBuffer**](/previous-versions/windows/desktop/api/Wabapi/) to create a new one.

 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Product<br/>                  | Internet Explorer 4.0<br/>                                                     |
| Header<br/>                   | <dl> <dt>Wabtmp.h</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>Wab32.dll</dt> </dl> |



 

 





