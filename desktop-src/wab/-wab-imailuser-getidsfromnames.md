---
title: IMailUser GetIDsFromNames method
description: Registers named properties with the mail user object.
ms.assetid: 6a36e0f4-21be-4383-9618-48c26b622558
keywords:
- GetIDsFromNames method Windows Address Book
- GetIDsFromNames method Windows Address Book , IMailUser interface
- IMailUser interface Windows Address Book , GetIDsFromNames method
topic_type:
- apiref
api_name:
- IMailUser.GetIDsFromNames
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

# IMailUser::GetIDsFromNames method

Registers named properties with the mail user object.

## Syntax


```C++
HRESULT GetIDsFromNames(
   ULONG         cPropNames,
   MAPINAMEID    **lppPropNames,
   ULONG         ulFlags,
   SPropTagArray **lppPropTags
);
```



## Parameters

<dl> <dt>

*cPropNames* 
</dt> <dd>

Type: **ULONG**

Value of type **ULONG** that specifies the count of the names to be registered. If *lppPropNames* is set to **NULL**, the *cPropNames* parameter must be set to 0.

</dd> <dt>

*lppPropNames* 
</dt> <dd>

Type: **[MAPINAMEID](0099fa14-0929-4443-9dff-a8b10b95b1c0)\*\***

Address of a pointer to a variable of type [MAPINAMEID](0099fa14-0929-4443-9dff-a8b10b95b1c0) that specifies the names and their globally unique identifiers (GUIDs).

</dd> <dt>

*ulFlags* 
</dt> <dd>

Type: **ULONG**

Value of type **ULONG** that specifies the bitmask of flags that indicate how the property identifiers should be returned. The default is to fail non-existent property names. The following flag may be set:

<dt>

<span id="MAPI_CREATE"></span><span id="mapi_create"></span>

<span id="MAPI_CREATE"></span><span id="mapi_create"></span>**MAPI\_CREATE**


</dt> <dd>

Creates a property identifier for any name not already mapped.

</dd> </dl> </dd> <dt>

*lppPropTags* 
</dt> <dd>

Type: **[**SPropTagArray**](/windows/previous-versions/Wabdefs/ns-wabdefs-_sproptagarray?branch=master)\*\***

Address of a pointer to a variable of type [**SPropTagArray**](/windows/previous-versions/Wabdefs/ns-wabdefs-_sproptagarray?branch=master) that receives the property tags. Must be freed by the client.

</dd> </dl>

## Return value

Type: **HRESULT**

This method can return one of these values.



| Return code                                                                                                 | Description                                                                                               |
|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                        | The operation completed successfully.<br/>                                                          |
| <dl> <dt>**MAPI\_E\_NO\_SUPPORT**</dt> </dl>         | The object does not support the requested operation.<br/>                                           |
| <dl> <dt>**MAPI\_E\_NOT\_ENOUGH\_MEMORY**</dt> </dl> | Insufficient memory was available to perform this operation.<br/>                                   |
| <dl> <dt>**MAPI\_E\_TOO\_BIG**</dt> </dl>            | The operation cannot be performed because it requires that too many property tags be returned.<br/> |



 

## Remarks

If the identifiers for the specified property names were successfully retrieved, the method returns S\_OK. If the object does not support named properties, the method returns MAPI\_E\_NO\_SUPPORT. If insufficient memory was available to retrieve the identifiers, the method returns MAPI\_E\_NOT\_ENOUGH\_MEMORY.

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

[**IMailUser::GetNamesFromIDs**](-wab-imailuser-getnamesfromids.md)
</dt> </dl>

 

 





