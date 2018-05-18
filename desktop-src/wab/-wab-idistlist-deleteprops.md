---
title: IDistList DeleteProps method
description: Deletes property values from a distribution list object.
ms.assetid: 'd794098c-28b3-4e80-8319-54e39aa0199d'
keywords: ["DeleteProps method Windows Address Book", "DeleteProps method Windows Address Book , IDistList interface", "IDistList interface Windows Address Book , DeleteProps method"]
topic_type:
- apiref
api_name:
- IDistList.DeleteProps
api_location:
- Wab32.dll
api_type:
- COM
---

# IDistList::DeleteProps method

Deletes property values from a distribution list object.

## Syntax


```C++
HRESULT DeleteProps(
   SPropTagArray     *lpPropTagArray,
   SPropProblemArray **lppProblems
);
```



## Parameters

<dl> <dt>

*lpPropTagArray* 
</dt> <dd>

Type: **[**SPropTagArray**](-wab-sproptagarray.md)\***

Pointer to a [**SPropTagArray**](-wab-sproptagarray.md) variable receiving the property tag array to be deleted.

</dd> <dt>

*lppProblems* 
</dt> <dd>

Type: **[**SPropProblemArray**](-wab-spropproblemarray.md)\*\***

Address of a pointer to an [**SPropProblemArray**](-wab-spropproblemarray.md) variable receiving the problem array. This must be freed by the caller if a non-NULL value is returned.

</dd> </dl>

## Return value

Type: **HRESULT**

This method can return one of these values.



| Return code                                                                                        | Description                                                                                  |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>               | The properties were successfully deleted.<br/>                                         |
| <dl> <dt>**MAPI\_E\_NO\_ACCESS**</dt> </dl> | The calling method or function has insufficient permissions to delete properties.<br/> |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Product<br/>                  | Internet Explorer 4.0<br/>                                                     |
| Header<br/>                   | <dl> <dt>Wabtmp.h</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>Wab32.dll</dt> </dl> |



 

 





