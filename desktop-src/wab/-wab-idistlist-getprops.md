---
title: IDistList GetProps method
description: Retrieves the property tag information for the distribution list items.
ms.assetid: 1e694aa2-2954-4554-9d99-1b3cc8510513
keywords:
- GetProps method Windows Address Book
- GetProps method Windows Address Book , IDistList interface
- IDistList interface Windows Address Book , GetProps method
topic_type:
- apiref
api_name:
- IDistList.GetProps
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

# IDistList::GetProps method

Retrieves the property tag information for the distribution list items.

## Syntax


```C++
HRESULT GetProps(
   SPropTagArray *lpPropTagArray,
   ULONG         ulFlags,
   ULONG         *lpcValues,
   SPropValue    **lppPropArray
);
```



## Parameters

<dl> <dt>

*lpPropTagArray* 
</dt> <dd>

Type: **[**SPropTagArray**](/windows/previous-versions/Wabdefs/ns-wabdefs-_sproptagarray?branch=master)\***

Pointer to an [**SPropTagArray**](/windows/previous-versions/Wabdefs/ns-wabdefs-_sproptagarray?branch=master) structure of properties whose values are to be retrieved. A **NULL** value specifies that all properties should be retrieved.

</dd> <dt>

*ulFlags* 
</dt> <dd>

Type: **ULONG**

The following flag is required.

<dt>

<span id="MAPI_UNICODE"></span><span id="mapi_unicode"></span>

<span id="MAPI_UNICODE"></span><span id="mapi_unicode"></span>**MAPI\_UNICODE**


</dt> <dd>

Indicates that wide strings are to be retrieved.

</dd> </dl> </dd> <dt>

*lpcValues* 
</dt> <dd>

Type: **ULONG\***

Pointer to a variable of type **ULONG** that retrieves the number of returned property values. The value of *lpcValues* is zero if *lppPropArray* is **NULL**.

</dd> <dt>

*lppPropArray* 
</dt> <dd>

Type: **[**SPropValue**](/windows/previous-versions/Wabdefs/ns-wabdefs-_spropvalue?branch=master)\*\***

Address of a pointer to an `SPropValue` variable type that retrieves the [**SPropValue**](/windows/previous-versions/Wabdefs/ns-wabdefs-_spropvalue?branch=master) array. It must be freed by the caller.

</dd> </dl>

## Return value

Type: **HRESULT**

This method can return one of these values.



| Return code                                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                               |
|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                       | The property values were retrieved successfully.<br/>                                                                                                                                                                                                                                                                                                                               |
| <dl> <dt>**MAPI\_W\_ERRORS\_RETURNED**</dt> </dl>   | The call succeeded overall, but one or more properties could not be accessed. The *ulPropTag* member of the property value for each inaccessible property in the *lppPropArray* parameter has a property type of PT\_ERROR and an identifier of zero. When this warning is returned, the call should be handled as successful. To test for this warning, use the FAILED macro.<br/> |
| <dl> <dt>**MAPI\_E\_INVALID\_PARAMETER**</dt> </dl> | Zero was passed in the *cValues* member of the [**SPropTagArray**](/windows/previous-versions/Wabdefs/ns-wabdefs-_sproptagarray?branch=master) structure to which *lpPropTagArray* points. <br/>                                                                                                                                                                                                                                        |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Product<br/>                  | Internet Explorer 4.0<br/>                                                     |
| Header<br/>                   | <dl> <dt>Wabtmp.h</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>Wab32.dll</dt> </dl> |



 

 





