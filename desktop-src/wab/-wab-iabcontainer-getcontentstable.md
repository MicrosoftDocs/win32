---
title: IABContainer GetContentsTable method
description: Retrieves the address of the contents table of the container.
ms.assetid: 644dd9c8-7e30-4820-aba1-46d7658e43c9
keywords:
- GetContentsTable method Windows Address Book
- GetContentsTable method Windows Address Book , IABContainer interface
- IABContainer interface Windows Address Book , GetContentsTable method
topic_type:
- apiref
api_name:
- IABContainer.GetContentsTable
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

# IABContainer::GetContentsTable method

Retrieves the address of the contents table of the container.

## Syntax


```C++
HRESULT GetContentsTable(
   ULONG      ulFlags,
   IMAPITable **lppTable
);
```



## Parameters

<dl> <dt>

*ulFlags* 
</dt> <dd>

Type: **ULONG**

Value of type **ULONG** that specifies the bitmask of flags that control how the contents table is retrieved. The following flags can be set:

<dt>

<span id="WAB_LOCAL_CONTAINERS"></span><span id="wab_local_containers"></span>

<span id="WAB_LOCAL_CONTAINERS"></span><span id="wab_local_containers"></span>**WAB\_LOCAL\_CONTAINERS**


</dt> <dd>

Retrieves a list of containers that is limited to containers from the local WAB.

</dd> <dt>

<span id="WAB_PROFILE_CONTENTS"></span><span id="wab_profile_contents"></span>

<span id="WAB_PROFILE_CONTENTS"></span><span id="wab_profile_contents"></span>**WAB\_PROFILE\_CONTENTS**


</dt> <dd>

Retrieves a contents table for all of the containers for the current profile.

</dd> </dl> </dd> <dt>

*lppTable* 
</dt> <dd>

Type: **[**IMAPITable**](/previous-versions/windows/desktop/api/Wabdefs/)\*\***

Address of a pointer to a variable of type IMAPITable that receives the table object containing the contents table.

</dd> </dl>

## Return value

Type: **HRESULT**

This method can return one of these values.



| Return code                                                                                            | Description                                                                                                                                                                  |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                   | The contents table was successfully retrieved.<br/>                                                                                                                    |
| <dl> <dt>**MAPI\_E\_BAD\_CHARWIDTH**</dt> </dl> | Either the MAPI\_UNICODE flag was set and the implementation does not support Unicode, or MAPI\_UNICODE was not set and the implementation only supports Unicode.<br/> |
| <dl> <dt>**MAPI\_E\_NO\_SUPPORT**</dt> </dl>    | The object does not support the requested operation.<br/>                                                                                                              |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Product<br/>                  | Internet Explorer 4.0<br/>                                                     |
| Header<br/>                   | <dl> <dt>Wabtmp.h</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>Wab32.dll</dt> </dl> |



 

 





