---
title: IMailUser DeleteProps method
description: Deletes property values from a mail user object.
ms.assetid: 453bd815-091c-40be-8074-57ab6377e711
keywords:
- DeleteProps method Windows Address Book
- DeleteProps method Windows Address Book , IMailUser interface
- IMailUser interface Windows Address Book , DeleteProps method
topic_type:
- apiref
api_name:
- IMailUser.DeleteProps
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

# IMailUser::DeleteProps method

Deletes property values from a mail user object.

## Syntax


```C++
HRESULT DeleteProps(
   SPropTagArray     *lpPropTagArray,
   SPropProblemArray **lppProblems
);
```



## Parameters

<dl> <dt>

*lpPropTagArray* 
</dt> <dd>

Type: **[**SPropTagArray**](/windows/previous-versions/Wabdefs/ns-wabdefs-_sproptagarray?branch=master)\***

Pointer to a variable of type [**SPropTagArray**](/windows/previous-versions/Wabdefs/ns-wabdefs-_sproptagarray?branch=master) that specifies the properties to be deleted. The cValues member of the **SPropTagArray** structure to which *lpPropTagArray* points must not be zero, and the *lpPropTagArray* parameter itself must not be **NULL**.

</dd> <dt>

*lppProblems* 
</dt> <dd>

Type: **[**SPropProblemArray**](/windows/previous-versions/Wabdefs/ns-wabdefs-_spropproblemarray?branch=master)\*\***

Address of a pointer to a variable of type [**SPropProblemArray**](/windows/previous-versions/Wabdefs/ns-wabdefs-_spropproblemarray?branch=master) that receives any problems that occur. Must be freed by the client if a non-**null** value is returned.

</dd> </dl>

## Return value

Type: **HRESULT**

This method can return one of these values.



| Return code                                                                                        | Description                                                                                          |
|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>               | The operation completed successfully.<br/>                                                     |
| <dl> <dt>**MAPI\_E\_NO\_ACCESS**</dt> </dl> | An attempt was made to perform an operation for which the user does not have permission. <br/> |



 

## Remarks

If the client does not have permission to delete values, the method returns MAPI\_E\_NO\_ACCESS.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Product<br/>                  | Internet Explorer 4.0<br/>                                                     |
| Header<br/>                   | <dl> <dt>Wabtmp.h</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>Wab32.dll</dt> </dl> |



 

 





