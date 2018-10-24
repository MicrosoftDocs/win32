---
Description: Defines the prompting behavior of the Protected Store whenever it displays a user interface.
ms.assetid: 413bcb33-5fe9-4ba1-b65f-3e53a7cbf70c
title: PST_PROMPTINFO structure
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- PST_PROMPTINFO
api_type: 
- HeaderDef
api_location: 
- Pstore.h
---

# PST\_PROMPTINFO structure

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](https://msdn.microsoft.com/en-us/library/Aa380261(v=VS.85).aspx) and [**CryptUnprotectData**](https://msdn.microsoft.com/en-us/library/Aa380882(v=VS.85).aspx) functions.\]

Defines the prompting behavior of the Protected Store whenever it displays a user interface.

## Syntax


```C++
typedef struct {
  DWORD      cbSize;
  DWORD      dwPromptFlags;
  DWORD_PTR  hwndApp;
  LPCWSTR    szPrompt;
} PST_PROMPTINFO, *PPST_PROMPTINFO;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

The size of this structure.

</dd> <dt>

**dwPromptFlags**
</dt> <dd>

This flag is ignored.



| Value                                                                                                                                                                                                                                          | Meaning                                                                                                               |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| <span id="PST_PF_ALWAYS_SHOW"></span><span id="pst_pf_always_show"></span><dl> <dt>**PST\_PF\_ALWAYS\_SHOW**</dt> <dt>0x00000001</dt> </dl> | Requests that the provider show the prompt dialog to the user even if it is not required for this access. <br/> |
| <span id="PST_PF_NEVER_SHOW"></span><span id="pst_pf_never_show"></span><dl> <dt>**PST\_PF\_NEVER\_SHOW**</dt> <dt>0x00000002</dt> </dl>    | Do not show the prompt dialog to the user.<br/>                                                                 |



 

</dd> <dt>

**hwndApp**
</dt> <dd>

The handle to the parent window for the user interface. The **hwndApp** member determines where the user interface appears. If **NULL** is passed, the desktop is considered to be the parent window.

</dd> <dt>

**szPrompt**
</dt> <dd>

The prompt string.

</dd> </dl>

## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Pstore.h</dt> </dl> |



## See also

<dl> <dt>

[**DeleteItem**](ipstore-deleteitem.md)
</dt> <dt>

[**OpenItem**](ipstore-openitem.md)
</dt> <dt>

[**ReadItem**](ipstore-readitem.md)
</dt> <dt>

[**WriteItem**](ipstore-writeitem.md)
</dt> </dl>

 

 




