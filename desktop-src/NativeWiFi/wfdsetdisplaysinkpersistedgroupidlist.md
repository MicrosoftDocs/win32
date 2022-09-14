---
description: Sets the persisted group id list for all the profiles that are persisted by your app.
ms.assetid: EF83F295-CD53-45A4-B209-560B4069CA7C
title: WFDDisplaySinkSetPersistedGroupIDList function (Wfdsink.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WFDSetDisplaySinkPersistedGroupIDList
api_type: 
- DllExport
api_location: 
- wifidisplay.dll
---

# WFDDisplaySinkSetPersistedGroupIDList function

Sets the persisted group id list for all the profiles that are persisted by your app. Your app should call this method every time it adds or deletes a profile from its storage.

## Syntax


```C++
DWORD WINAPI WFDSetDisplaySinkPersistedGroupIDList(
  _In_ UINT32             cGroupIDList,
  _In_ DOT11_WFD_GROUP_ID *pGroupIDList
);
```



## Parameters

<dl> <dt>

*cGroupIDList* \[in\]
</dt> <dd>

The count of group ids being pointed to by *pGroupIDList*.

</dd> <dt>

*pGroupIDList* \[in\]
</dt> <dd>

Pointer to an array of *cGroupIDList* group ids.

</dd> </dl>

## Return value

If the function succeeds, the return value is ERROR\_SUCCESS.

## Remarks

This method is always expected to be called with the entire list, and not a subset. It is OK to call this method with 0 profiles when the profile store is empty.

A re-invoke for a group id that is not part of the provided list will fail with "Fail; unknown P2P Group"(status 8).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows 10<br/>                                                                      |
| End of server support<br/>    | Windows Server 2016<br/>                                                             |
| Header<br/>                   | <dl> <dt>Wfdsink.h</dt> </dl>       |
| Library<br/>                  | <dl> <dt>Wifidisplay.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wifidisplay.dll</dt> </dl> |



 

 




