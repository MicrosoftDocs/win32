---
description: VARIANT type variables have a type tag field vt that indicates the data type of the data.
ms.assetid: 3436faf6-2e66-46a1-b1e8-84f513282c16
title: Setting the Type Tag Field
ms.topic: article
ms.date: 05/31/2018
---

# Setting the Type Tag Field

**VARIANT** type variables have a type tag field **vt** that indicates the data type of the data. **VARIANT** type return values are returned by methods with the type tag field set to the data type of the return value. **VARIANT** type input parameters in a method call must have the type tag field set by the application to one of the supported values. The correspondence of parameter types to data types is as follows.



| Parameter type              | Data type                                      |
|-----------------------------|------------------------------------------------|
| PROPTYPE\_LONG<br/>   | VT\_I2 or VT\_I4<br/>                    |
| PROPTYPE\_DATE<br/>   | VT\_DATE<br/>                            |
| PROPTYPE\_BINARY<br/> | VT\_BSTR or (VT\_BSTR \| VT\_BYREF)<br/> |
| PROPTYPE\_STRING<br/> | VT\_BSTR or (VT\_BSTR \| VT\_BYREF)<br/> |



 

The following example shows how to initialize the variant data types listed above.


```C++
HRESULT hr;
VARIANT vEMail;
VARIANT vNotBefore;
VARIANT vCount;
VARIANT vByRef;
BSTR bstr = NULL;
SYSTEMTIME st;

//Set the BSTR variant data type.
VariantInit(&vEMail);
vEMail.vt = VT_BSTR;   
vEMail.bstrVal = SysAllocString(L"someone@example.com");
if (NULL == vEMail.bstrVal)
{
    hr = E_OUTOFMEMORY;
    //Handle error.   
}
//Use the variant.
VariantClear(&vEMail);  //when done


//Set the BSTR|BYREF variant data type.
VariantInit(&vByRef);
vByRef.vt = VT_BSTR | VT_BYREF;   
vByRef.pbstrVal = &bstr;
//Use the variant.
VariantClear(&vByRef);  //when done
SysFreeString(bstr);


//Set the DATE variant data type.
memset(&st, 0, sizeof(SYSTEMTIME));
st.wYear = 2000;
st.wMonth = 1;
st.wDay = 1;
st.wHour = 12;

VariantInit(&vNotBefore);
vNotBefore.vt = VT_DATE;
if (!SystemTimeToVariantTime(&st, &vNotBefore.date))
{
    hr = E_FAIL;
    //Handle error.
}
//Use the variant.
VariantClear(&vNotBefore);  //when done


//Set the LONG variant data type.
VariantInit(&vCount);
vCount.vt = VT_I4;
vCount.long = 123456;
//Use the variant.
VariantClear(&vCount);  //when done
```



 

 




