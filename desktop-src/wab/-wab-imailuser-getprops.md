---
title: IMailUser GetProps method
description: Retrieves property values from a mail user object.
ms.assetid: '40b09d3a-693d-4760-ae51-0d9f3ee28947'
keywords: ["GetProps method Windows Address Book", "GetProps method Windows Address Book , IMailUser interface", "IMailUser interface Windows Address Book , GetProps method"]
topic_type:
- apiref
api_name:
- IMailUser.GetProps
api_location:
- Wab32.dll
api_type:
- COM
---

# IMailUser::GetProps method

Retrieves property values from a mail user object.

## Syntax


```C++
HRESULT GetProps(
   SPropTagArray *lpPropTagArray,
   ULONG         ulFlags,
   ULONG         *lpcValues,
   SPropValue    **lppPropArray
);
```



## Parameters

<dl> <dt>

*lpPropTagArray* 
</dt> <dd>

Type: **[**SPropTagArray**](-wab-sproptagarray.md)\***

Pointer to a variable of type [**SPropTagArray**](-wab-sproptagarray.md) that specifies the properties to be retrieved.

<dt>



 (NULL)


</dt> <dd>

Specifies that all properties are to be retrieved.

</dd> </dl> </dd> <dt>

*ulFlags* 
</dt> <dd>

Type: **ULONG**

Value of type **ULONG** that specifies the bitmask of flags that determine the kind of strings that the *lppPropArray* parameter is to retrieve.

<dt>

<span id="MAPI_UNICODE"></span><span id="mapi_unicode"></span>

<span id="MAPI_UNICODE"></span><span id="mapi_unicode"></span>**MAPI\_UNICODE**


</dt> <dd>

Indicates that wide strings are to be retrieved.

</dd> </dl> </dd> <dt>

*lpcValues* 
</dt> <dd>

Type: **ULONG\***

Pointer to a variable of type **ULONG** that receives the count of property values retrieved by the *lppPropArray* parameter.

<dt>



 (NULL)


</dt> <dd>

May be passed if no count is desired.

</dd> </dl> </dd> <dt>

*lppPropArray* 
</dt> <dd>

Type: **[**SPropValue**](-wab-spropvalue.md)\*\***

Address of a pointer to a variable of type [**SPropValue**](-wab-spropvalue.md) that receives the property values. The variable must be freed by the client.

</dd> </dl>

## Return value

Type: **HRESULT**

This method can return one of these values.



| Return code                                                                                                | Description                                        |
|------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                       | The operation completed successfully.<br/>   |
| <dl> <dt>**MAPI\_E\_INVALID\_PARAMETER**</dt> </dl> | The IRowCount parameter is set to zero.<br/> |



 

## Remarks

If zero was passed in the cValues member of the [**SPropTagArray**](-wab-sproptagarray.md) structure to which *lpPropTagArray* points, the method returns MAPI\_E\_INVALID\_PARAMETER.

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

[**SetProps**](-wab-idistlist-setprops.md)
</dt> </dl>

 

 





