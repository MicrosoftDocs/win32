---
title: IMailUser SetProps method
description: Sets property values on a mail user object.
ms.assetid: '51b5c12c-2a38-4264-9435-f04f5a5de962'
keywords: ["SetProps method Windows Address Book", "SetProps method Windows Address Book , IMailUser interface", "IMailUser interface Windows Address Book , SetProps method"]
topic_type:
- apiref
api_name:
- IMailUser.SetProps
api_location:
- Wab32.dll
api_type:
- COM
---

# IMailUser::SetProps method

Sets property values on a mail user object.

## Syntax


```C++
HRESULT SetProps(
   ULONG             cValues,
   SPropValue        *lpPropArray,
   SPropProblemArray **lppProblems
);
```



## Parameters

<dl> <dt>

*cValues* 
</dt> <dd>

Type: **ULONG**

A value of type **ULONG** that specifies the count of the property values to be set.

</dd> <dt>

*lpPropArray* 
</dt> <dd>

Type: **[**SPropValue**](-wab-spropvalue.md)\***

Pointer to a variable of type [**SPropValue**](-wab-spropvalue.md) that specifies the properties to be set.

</dd> <dt>

*lppProblems* 
</dt> <dd>

Type: **[**SPropProblemArray**](-wab-spropproblemarray.md)\*\***

Address of a pointer to a variable of type [**SPropProblemArray**](-wab-spropproblemarray.md) that receives any problems that occurred. The variable must be freed by the client if a non-null value is returned.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Product<br/>                  | Internet Explorer 4.0<br/>                                                     |
| Header<br/>                   | <dl> <dt>Wabtmp.h</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>Wab32.dll</dt> </dl> |



## See also

<dl> <dt>

[**IMailUser**](-wab-imailuser.md)
</dt> <dt>

[**IMailUser::GetProps**](-wab-imailuser-getprops.md)
</dt> </dl>

 

 





