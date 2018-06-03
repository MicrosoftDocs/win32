---
title: IDistList GetContentsTable method
description: Retrieves the address of the contents table of the distribution list.
ms.assetid: f276c58a-4887-4cde-ba1e-a743a6cb4ea3
keywords:
- GetContentsTable method Windows Address Book
- GetContentsTable method Windows Address Book , IDistList interface
- IDistList interface Windows Address Book , GetContentsTable method
topic_type:
- apiref
api_name:
- IDistList.GetContentsTable
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

# IDistList::GetContentsTable method

Retrieves the address of the contents table of the distribution list.

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

<span id="MAPI_DEFERRED_ERRORS"></span><span id="mapi_deferred_errors"></span>

<span id="MAPI_DEFERRED_ERRORS"></span><span id="mapi_deferred_errors"></span>**MAPI\_DEFERRED\_ERRORS**


</dt> <dd>

Not supported by the WAB.

</dd> <dt>

<span id="MAPI_UNICODE"></span><span id="mapi_unicode"></span>

<span id="MAPI_UNICODE"></span><span id="mapi_unicode"></span>**MAPI\_UNICODE**


</dt> <dd>

Indicates that wide strings are to be retrieved.

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



 

## Remarks

The MAPI\_UNICODE flag is not supported in the first version of the WAB.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Product<br/>                  | Internet Explorer 4.0<br/>                                                     |
| Header<br/>                   | <dl> <dt>Wabtmp.h</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>Wab32.dll</dt> </dl> |



 

 





