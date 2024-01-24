---
description: Gets the properties of the view.
title: IShellFolderViewType::GetViewTypeProperties method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IShellFolderViewType.GetViewTypeProperties
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: 82be6bd5-a46c-48b3-a1f0-a92b9454c35e

---

# IShellFolderViewType::GetViewTypeProperties method

Gets the properties of the view.

## Syntax


```C++
HRESULT GetViewTypeProperties(
  [in]  PCUITEMID_CHILD pidl,
  [out] DWORD           *pdwFlags
);
```



## Parameters

<dl> <dt>

*pidl* \[in\]
</dt> <dd>

Type: **PCUITEMID\_CHILD**

A PIDL.

</dd> <dt>

*pdwFlags* \[out\]
</dt> <dd>

Type: **DWORD\***

A pointer to an unsigned integer variable that receives the view properties, which indicate what to do when the view is selected. Flags may be any combination of the following values.

<dt>

<span id="SFVTFLAG_NOTIFY_CREATE"></span><span id="sfvtflag_notify_create"></span>

<span id="SFVTFLAG_NOTIFY_CREATE"></span><span id="sfvtflag_notify_create"></span>**SFVTFLAG\_NOTIFY\_CREATE** (0x00000001)


</dt> <dd>

Create view item if not there.

</dd> <dt>

<span id="SFVTFLAG_NOTIFY_RESORT"></span><span id="sfvtflag_notify_resort"></span>

<span id="SFVTFLAG_NOTIFY_RESORT"></span><span id="sfvtflag_notify_resort"></span>**SFVTFLAG\_NOTIFY\_RESORT** (0x00000002)


</dt> <dd>

Reinsert PIDL and re-sort.

</dd> </dl> </dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                             |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| DLL<br/>                      | <dl> <dt>Shell32.dll</dt> </dl> |



 

 




