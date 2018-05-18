---
title: IDistList GetIDsFromNames method
description: Retrieves the property identifiers that correspond to one or more property names.
ms.assetid: '9cea7449-8722-4587-b31b-b9563271d831'
keywords: ["GetIDsFromNames method Windows Address Book", "GetIDsFromNames method Windows Address Book , IDistList interface", "IDistList interface Windows Address Book , GetIDsFromNames method"]
topic_type:
- apiref
api_name:
- IDistList.GetIDsFromNames
api_location:
- Wab32.dll
api_type:
- COM
---

# IDistList::GetIDsFromNames method

Retrieves the property identifiers that correspond to one or more property names.

## Syntax


```C++
HRESULT GetIDsFromNames(
   ULONG         cPropNames,
   MAPINAMEID    **lppPropNames,
   ULONG         ulFlags,
   SPropTagArray **lppPropTags
);
```



## Parameters

<dl> <dt>

*cPropNames* 
</dt> <dd>

Type: **ULONG**

Value of type **ULONG** that specifies the count of the names that correspond to property identifiers. If *lppPropNames* is set to **NULL**, the *cPropNames* parameter must be set to 0.

</dd> <dt>

*lppPropNames* 
</dt> <dd>

Type: **[MAPINAMEID](0099fa14-0929-4443-9dff-a8b10b95b1c0)\*\***

Address of a pointer to a variable of type [MAPINAMEID](0099fa14-0929-4443-9dff-a8b10b95b1c0) that specifies the names and their globally unique identifiers (GUIDs).

</dd> <dt>

*ulFlags* 
</dt> <dd>

Type: **ULONG**

Value of type **ULONG** that specifies the bitmask of flags that indicate how the property identifiers should be returned. The following flag may be set:

<dt>

<span id="MAPI_CREATE"></span><span id="mapi_create"></span>

<span id="MAPI_CREATE"></span><span id="mapi_create"></span>**MAPI\_CREATE**


</dt> <dd>

Assigns a property identifier to one or more of the names included in the property name array pointed to by *lppPropNames*, if one has not yet been assigned, and registers the identifier in the name-to-identifier mapping table.

</dd> </dl> </dd> <dt>

*lppPropTags* 
</dt> <dd>

Type: **[**SPropTagArray**](-wab-sproptagarray.md)\*\***

Address of a pointer to a variable of type [**SPropTagArray**](-wab-sproptagarray.md) that receives the property tags.

</dd> </dl>

## Return value

Type: **HRESULT**

This method can return one of these values.



| Return code                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                         |
|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                        | The operation completed successfully.<br/>                                                                                                                                                                                                                                                                                                    |
| <dl> <dt>**MAPI\_E\_NO\_SUPPORT**</dt> </dl>         | The object does not support the requested operation.<br/>                                                                                                                                                                                                                                                                                     |
| <dl> <dt>**MAPI\_E\_NOT\_ENOUGH\_MEMORY**</dt> </dl> | Insufficient memory was available to perform this operation.<br/>                                                                                                                                                                                                                                                                             |
| <dl> <dt>**MAPI\_E\_TOO\_BIG**</dt> </dl>            | The operation cannot be performed because it requires that too many property tags be returned.<br/>                                                                                                                                                                                                                                           |
| <dl> <dt>**MAPI\_W\_ERRORS\_RETURNED**</dt> </dl>    | The call succeeded overall, but the identifiers of one or more properties could not be returned. The corresponding property type for each inaccessible property is set to PT\_ERROR and its identifier to zero. When this warning is returned, the call should be handled as successful. To test for this warning, use the FAILED macro.<br/> |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Product<br/>                  | Internet Explorer 5<br/>                                                       |
| Header<br/>                   | <dl> <dt>Wabtmp.h</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>Wab32.dll</dt> </dl> |



 

 





