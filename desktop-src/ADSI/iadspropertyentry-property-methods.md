---
title: IADsPropertyEntry Property Methods (Iads.h)
description: Provide access to the following properties.
ms.assetid: 73b0f6d4-55db-46cf-a781-e10bc4fcf2db
ms.tgt_platform: multiple
keywords:
- IADsPropertyEntry Property Methods ADSI
topic_type:
- apiref
api_name:
- IADsPropertyEntry Property Methods
- IADsPropertyEntry.Name
- IADsPropertyEntry.get_Name
- IADsPropertyEntry.put_Name
- IADsPropertyEntry.ADsType
- IADsPropertyEntry.get_ADsType
- IADsPropertyEntry.put_ADsType
- IADsPropertyEntry.ControlCode
- IADsPropertyEntry.get_ControlCode
- IADsPropertyEntry.put_ControlCode
- IADsPropertyEntry.Values
- IADsPropertyEntry.get_Values
- IADsPropertyEntry.put_Values
api_location:
- Activeds.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IADsPropertyEntry Property Methods

The property methods of the [**IADsPropertyEntry**](/windows/desktop/api/Iads/nn-iads-iadspropertyentry) interface provide access to the following properties. For more information about property methods, see [Interface Property Methods](interface-property-methods.md).

## Properties

<dl> <dt>

**ADsType**
</dt> <dd> <dl>

The data type of the **Name** property. The values of the data type is defined in the [**ADSTYPEENUM**](/windows/win32/api/iads/ne-iads-adstypeenum) enumeration.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_ADsType(
  [out] LONG* plADsType
);
HRESULT put_ADsType(
  [in] LONG lADsType
);
```


</dt> </dl> </dd> <dt>

**ControlCode**
</dt> <dd> <dl>

A constant that specifies the operation to be performed on the named property. The value is defined in the [**ADS\_PROPERTY\_OPERATION\_ENUM**](/windows/win32/api/iads/ne-iads-ads_property_operation_enum) enumeration.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_ControlCode(
  [out] LONG* pControlCode
);
HRESULT put_ControlCode(
  [in] LONG lnControlCode
);
```


</dt> </dl> </dd> <dt>

**Name**
</dt> <dd> <dl>

Name of the property entry. This name should correspond to the name of an attribute as defined in the schema.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Name(
  [out] BSTR* pbstrName
);
HRESULT put_Name(
  [in] BSTR bstrName
);
```


</dt> </dl> </dd> <dt>

**Values**
</dt> <dd> <dl>

A **VARIANT** array. Each element in this array represents a value of the named property. Such property values are represented by ADSI objects implementing the [**IADsPropertyValue**](/windows/desktop/api/Iads/nn-iads-iadspropertyvalue) and [**IADsPropertyValue2**](/windows/desktop/api/Iads/nn-iads-iadspropertyvalue2) interfaces. Therefore, the **VARIANT** array holds an array of pointers to the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface on the ADSI objects implementing the **IADsPropertyValue** and **IADsPropertyValue2** interfaces.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **VARIANT**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Values(
  [out] VARIANT* pvValues
);
HRESULT put_Values(
  [in] VARIANT vValues
);
```


</dt> </dl> </dd> </dl>

 

## Remarks

Each property method supports the standard **HRESULT** return values, including S\_OK. For more information about other return values, see [ADSI Error Codes](adsi-error-codes.md).

## Examples

The following code example shows how to retrieve a named property from the cache and create a new property entry.


```VB
 
Dim propList As IADsPropertyList
Dim propEntry As IADsPropertyEntry
Dim propVal As IADsPropertyValue

On Error GoTo Cleanup

'------------------------------------------------------------
'----- Getting IADsPropertyEntry ----------------------------
'------------------------------------------------------------
 
' Create the property list object.
Set propList = GetObject("LDAP://dc01/DC=Fabrikam,DC=com")
propList.GetInfo
 
' Get a named property entry object.
Set propEntry = propList.GetPropertyItem("dc", ADSTYPE_CASE_IGNORE_STRING)

' Insert code to do something with propEntry
Set propEntry = Nothing
 
'------------------------------------------------------------
'---- Setting IADsPropertyEntry -----------------------------
'------------------------------------------------------------
 
' Create a property value object.
Set propVal = New PropertyValue
 
'---- Property Value -----
propVal.CaseIgnoreString = "Fabrikam, Inc - Seattle, WA"
propVal.ADsType = ADSTYPE_CASE_IGNORE_STRING
 
'---- Create a new Property Entry ----
Set propEntry = New PropertyEntry
propEntry.Name = "adminDescription"
propEntry.Values = Array(propVal)
propEntry.ControlCode = ADS_PROPERTY_UPDATE
propEntry.ADsType = ADS_CASE_IGNORE_STRING
 
' ---- Put the newly created property entry to the cache ----
propList.PutPropertyItem (propEntry)
 
' Commit the entry to the directory store.
propList.SetInfo

Cleanup:
    If (Err.Number<>0) Then
        MsgBox("An error has occurred. " & Err.Number)
    End If
    Set propList = Nothing
    Set propEntry = Nothing
    Set propVal = Nothing
```



The following code example shows how to get a named property from a cache.


```C++
#include <activeds.h>
#include <stdio.h>
 
IADsPropertyList *pList = NULL;
IADsPropertyEntry *pEntry = NULL;
IADs *pObj = NULL;
VARIANT var;
long valType = ADSTYPE_CASE_IGNORE_STRING;
 
VariantInit(&var);
 
// Bind to directory object.
HRESULT hr = ADsGetObject(L"LDAP://dc01/DC=Fabrikam,DC=com",
                          IID_IADsPropertyList,
                          (void**)&pList);
if(FAILED(hr)){return;}
 
// Initialize the property cache.
hr = pList->QueryInterface(IID_IADs,(void**)&pObj);
if(FAILED(hr)){goto Cleanup;}
pObj->GetInfo();
pObj->Release();
 
// Get a property entry.
hr = pList->GetPropertyItem(CComBSTR("description"), valType, &var);
pList->Release();
if(FAILED(hr)){goto Cleanup;}
hr = V_DISPATCH(&var)->QueryInterface(IID_IADsPropertyEntry,
                                      (void**)&pEntry);
VariantClear(&var);
if(FAILED(hr)){goto Cleanup;}
 
// Get the name and the type of the property entry.
BSTR nm = NULL;
hr = pEntry->get_Name(&nm);
printf("Property name = %S\n",nm);
VariantClear(&var);
long at;
hr = pEntry->get_ADsType(&at);
printf("Property type = %d\n",a);

Cleanup:
    if(nm)
        SysFreeString(nm);

    if(pList)
        pList->Release();

    if(pEntry)
        pEntry->Release();

    if(pObj)
        pObj->Release();

    VariantClear(&var);
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Iads.h</dt> </dl>       |
| DLL<br/>                      | <dl> <dt>Activeds.dll</dt> </dl> |
| IID<br/>                      | IID\_IADsPropertyEntry is defined as 05792C8E-941F-11D0-8529-00C04FD8D503<br/>    |



## See also

<dl> <dt>

[**ADS\_PROPERTY\_OPERATION\_ENUM**](/windows/win32/api/iads/ne-iads-ads_property_operation_enum)
</dt> <dt>

[ADSI Error Codes](adsi-error-codes.md)
</dt> <dt>

[**ADSTYPEENUM**](/windows/win32/api/iads/ne-iads-adstypeenum)
</dt> <dt>

[**IADsPropertyEntry**](/windows/desktop/api/Iads/nn-iads-iadspropertyentry)
</dt> <dt>

[**IADsPropertyValue**](/windows/desktop/api/Iads/nn-iads-iadspropertyvalue)
</dt> <dt>

[**IADsPropertyValue2**](/windows/desktop/api/Iads/nn-iads-iadspropertyvalue2)
</dt> <dt>

[**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch)
</dt> </dl>

 

