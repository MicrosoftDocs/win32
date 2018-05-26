---
title: IMailUser GetPropList method
description: Gets a list of property tags on the object.
ms.assetid: a303b10f-d25b-4a25-a676-61ca0de6b64a
keywords:
- GetPropList method Windows Address Book
- GetPropList method Windows Address Book , IMailUser interface
- IMailUser interface Windows Address Book , GetPropList method
topic_type:
- apiref
api_name:
- IMailUser.GetPropList
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

# IMailUser::GetPropList method

Gets a list of property tags on the object.

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

Value of type **ULONG** that specifies the bitmask of flags that determine the kind of strings that the *lppPropTagArray* parameter is to retrieve.

<dt>

<span id="MAPI_UNICODE"></span><span id="mapi_unicode"></span>

<span id="MAPI_UNICODE"></span><span id="mapi_unicode"></span>**MAPI\_UNICODE**


</dt> <dd>

Indicates that wide strings are to be retrieved.

</dd> </dl> </dd> <dt>

*lppPropTagArray* 
</dt> <dd>

Type: **[**SPropTagArray**](/windows/previous-versions/Wabdefs/ns-wabdefs-_sproptagarray?branch=master)\*\***

Address of a pointer to a variable of type [**SPropTagArray**](/windows/previous-versions/Wabdefs/ns-wabdefs-_sproptagarray?branch=master) that receives the property tags. Must be freed by the client if a non-null value is retrieved.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

If *ulFlags* is set to MAPI\_UNICODE, PT\_UNICODE and PT\_MV\_UNICODE tags are retrieved instead of PT\_STRING8 and PT\_MV\_STRING8.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Product<br/>                  | Internet Explorer 4.0<br/>                                                     |
| Header<br/>                   | <dl> <dt>Wabtmp.h</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>Wab32.dll</dt> </dl> |



## See also

<dl> <dt>

[**IMailUser**](/windows/previous-versions/wabdefs/?branch=master)
</dt> <dt>

[**IMailUser::GetProps**](-wab-imailuser-getprops.md)
</dt> </dl>

 

 





