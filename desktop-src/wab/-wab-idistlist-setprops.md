---
title: IDistList SetProps method
description: Sets property values for a distribution list object.
ms.assetid: 5cfd22b1-19cb-48e3-a51f-b1a1437e61a3
keywords:
- SetProps method Windows Address Book
- SetProps method Windows Address Book , IDistList interface
- IDistList interface Windows Address Book , SetProps method
topic_type:
- apiref
api_name:
- IDistList.SetProps
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

# IDistList::SetProps method

Sets property values for a distribution list object.

## Syntax


```C++
HRESULT SetProps(
   ULONG             cValues,
   SPropValue        *lpPropArray,
   SPropProblemArray **lppProblems
);
```



## Parameters

<dl> <dt>

*cValues* 
</dt> <dd>

Type: **ULONG**

Value of type **ULONG** that specifies the count of the property values to be set.

</dd> <dt>

*lpPropArray* 
</dt> <dd>

Type: **[**SPropValue**](/previous-versions/windows/desktop/api/Wabdefs/ns-wabdefs-_spropvalue)\***

Pointer to an [**SPropValue**](/previous-versions/windows/desktop/api/Wabdefs/ns-wabdefs-_spropvalue) array containing the properties to be set.

</dd> <dt>

*lppProblems* 
</dt> <dd>

Type: **[**SPropProblemArray**](/previous-versions/windows/desktop/api/Wabdefs/ns-wabdefs-_spropproblemarray)\*\***

Address of a pointer to a [**SPropProblemArray**](/previous-versions/windows/desktop/api/Wabdefs/ns-wabdefs-_spropproblemarray). This must be freed by the caller if a non-NULL value is retrieved.

</dd> </dl>

## Return value

Type: **HRESULT**

This method can return one of these values.



| Return code                                                                                                 | Description                                                                                                                                                                  |
|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                        | The properties were updated successfully.<br/>                                                                                                                         |
| <dl> <dt>**MAPI\_E\_BAD\_CHARWIDTH**</dt> </dl>      | Either the MAPI\_UNICODE flag was set and the implementation does not support Unicode, or MAPI\_UNICODE was not set and the implementation only supports Unicode.<br/> |
| <dl> <dt>**MAPI\_E\_COMPUTED**</dt> </dl>            | The property cannot be updated because it is read-only, computed by the service provider responsible for the object.<br/>                                              |
| <dl> <dt>**MAPI\_E\_INVALID\_TYPE**</dt> </dl>       | The property type is invalid.<br/>                                                                                                                                     |
| <dl> <dt>**MAPI\_E\_NO\_ACCESS**</dt> </dl>          | An attempt was made to perform an operation for which the user does not have permission. <br/>                                                                         |
| <dl> <dt>**MAPI\_E\_NOT\_ENOUGH\_MEMORY**</dt> </dl> | Insufficient memory was available to perform this operation.<br/>                                                                                                      |
| <dl> <dt>**MAPI\_E\_UNEXPECTED\_TYPE**</dt> </dl>    | The property type is not the type expected by the calling implementation.<br/>                                                                                         |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Product<br/>                  | Internet Explorer 4.0<br/>                                                     |
| Header<br/>                   | <dl> <dt>Wabtmp.h</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>Wab32.dll</dt> </dl> |



 

 





