---
title: IDistList GetPropList method
description: Retrieves a list of the object property tags.
ms.assetid: 509a7a2e-41a4-49b5-bd16-c747a99932ea
keywords:
- GetPropList method Windows Address Book
- GetPropList method Windows Address Book , IDistList interface
- IDistList interface Windows Address Book , GetPropList method
topic_type:
- apiref
api_name:
- IDistList.GetPropList
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

# IDistList::GetPropList method

Retrieves a list of the object property tags.

## Syntax


```C++
HRESULT GetPropList(
   ULONG         ulFlags,
   SPropTagArray **lppPropTagArray
);
```



## Parameters

<dl> <dt>

*ulFlags* 
</dt> <dd>

Type: **ULONG**

Value of type **ULONG** that specifies MAPI\_UNICODE to return a Unicode-based PROP\_TYPE.

</dd> <dt>

*lppPropTagArray* 
</dt> <dd>

Type: **[**SPropTagArray**](/windows/previous-versions/Wabdefs/ns-wabdefs-_sproptagarray?branch=master)\*\***

Address of a pointer to a returned property tag array. Must be freed by the caller if a non-NULL value is returned.

</dd> </dl>

## Return value

Type: **HRESULT**

This method can return one of these values.



| Return code                                                                                            | Description                                                                                                                                                                  |
|--------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                   | The property tags were retrieved successfully.<br/>                                                                                                                    |
| <dl> <dt>**MAPI\_E\_BAD\_CHARWIDTH**</dt> </dl> | Either the MAPI\_UNICODE flag was set and the implementation does not support Unicode, or MAPI\_UNICODE was not set and the implementation only supports Unicode.<br/> |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Product<br/>                  | Internet Explorer 4.0<br/>                                                     |
| Header<br/>                   | <dl> <dt>Wabtmp.h</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>Wab32.dll</dt> </dl> |



 

 





