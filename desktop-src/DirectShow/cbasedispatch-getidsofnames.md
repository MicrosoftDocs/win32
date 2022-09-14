---
description: CBaseDispatch.GetIDsOfNames method - The GetIDsOfNames method maps a set of names to a corresponding set of DISPIDs.
ms.assetid: 0c0a2726-e89a-4eaf-aab0-e7e9e82e3c34
title: CBaseDispatch.GetIDsOfNames method (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseDispatch.GetIDsOfNames
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseDispatch.GetIDsOfNames method

The `GetIDsOfNames` method maps a set of names to a corresponding set of DISPIDs.

## Syntax


```C++
HRESULT GetIDsOfNames(
   REFIID  riid,
   OLECHAR **rgszNames,
   UINT    cNames,
   LCID    lcid,
   DISPID  *rgdispid
);
```



## Parameters

<dl> <dt>

*riid* 
</dt> <dd>

Reference to an interface identifier (IID) that specifies the interface.

</dd> <dt>

*rgszNames* 
</dt> <dd>

Address of an array of wide-character strings that contain the names to be mapped.

</dd> <dt>

*cNames* 
</dt> <dd>

Size of the array given by the *rgszNames* parameter.

</dd> <dt>

*lcid* 
</dt> <dd>

Locale context in which to interpret the names. Can be **NULL**.

</dd> <dt>

*rgdispid* 
</dt> <dd>

Pointer to an array that receives the DISPIDs. Each element of receives an identifier that corresponds to one of the names passed in the *rgszNames* parameter.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include the following.



| Return code                                                                                         | Description                                         |
|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                | Success.<br/>                                 |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>       | Insufficient memory.<br/>                     |
| <dl> <dt>**DISP\_E\_UNKNOWNNAME**</dt> </dl> | One or more of the names were not known.<br/> |



 

## Remarks

This method behaves like the **IDispatch::GetIDsOfNames** method, but the *riid* parameter specifies the interface on which to retrieve DISPIDs. (In the **IDispatch** version, the *riid* parameter is reserved.)

If the method returns DISP\_E\_UNKNOWNNAME, the returned DISPIDs contain DISPID\_UNKNOWN for each entry that corresponds to an unknown name.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseDispatch Class**](cbasedispatch.md)
</dt> </dl>

 

 




