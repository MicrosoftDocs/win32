---
title: IADsClass Property Methods (Iads.h)
description: The property methods of the IADsClass interface get or set the following properties. For more information, see Interface Property Methods.
ms.assetid: 191f6873-c4bd-4e71-9d23-478454b7cec2
ms.tgt_platform: multiple
keywords:
- IADsClass Property Methods ADSI
topic_type:
- apiref
api_name:
- IADsClass Property Methods
- IADsClass.Abstract
- IADsClass.get_Abstract
- IADsClass.put_Abstract
- IADsClass.AuxDerivedFrom
- IADsClass.get_AuxDerivedFrom
- IADsClass.put_AuxDerivedFrom
- IADsClass.Auxiliary
- IADsClass.get_Auxiliary
- IADsClass.put_Auxiliary
- IADsClass.CLSID
- IADsClass.get_CLSID
- IADsClass.put_CLSID
- IADsClass.Container
- IADsClass.get_Container
- IADsClass.put_Container
- IADsClass.Containment
- IADsClass.get_Containment
- IADsClass.put_Containment
- IADsClass.DerivedFrom
- IADsClass.get_DerivedFrom
- IADsClass.put_DerivedFrom
- IADsClass.HelpFileContext
- IADsClass.get_HelpFileContext
- IADsClass.put_HelpFileContext
- IADsClass.HelpFileName
- IADsClass.get_HelpFileName
- IADsClass.put_HelpFileName
- IADsClass.MandatoryProperties
- IADsClass.get_MandatoryProperties
- IADsClass.put_MandatoryProperties
- IADsClass.NamingProperties
- IADsClass.get_NamingProperties
- IADsClass.put_NamingProperties
- IADsClass.OID
- IADsClass.get_OID
- IADsClass.put_OID
- IADsClass.OptionalProperties
- IADsClass.get_OptionalProperties
- IADsClass.put_OptionalProperties
- IADsClass.PossibleSuperiors
- IADsClass.get_PossibleSuperiors
- IADsClass.put_PossibleSuperiors
- IADsClass.PrimaryInterface
- IADsClass.get_PrimaryInterface
api_location:
- Activeds.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IADsClass Property Methods

The property methods of the [**IADsClass**](/windows/desktop/api/Iads/nn-iads-iadsclass) interface get or set the following properties. For more information, see [Interface Property Methods](interface-property-methods.md).

## Properties

<dl> <dt>

**Abstract**
</dt> <dd> <dl>

Boolean value that indicates if this class is Abstract or non-abstract. When **TRUE**, this class is an Abstract class and cannot be directly instantiated in the directory service. Abstract classes can only be used as super classes.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BOOLEAN**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Abstract(
  [out] BOOLEAN* pbAbstract
);
HRESULT put_Abstract(
  [in] BOOLEAN bAbstract
);
```


</dt> </dl> </dd> <dt>

**AuxDerivedFrom**
</dt> <dd> <dl>

Array of ADsPath strings that indicate the super Auxiliary classes this class derives from.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **VARIANT**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_AuxDerivedFrom(
  [out] VARIANT* pvAuxDerivedFrom
);
HRESULT put_AuxDerivedFrom(
  [in] VARIANT vAuxDerivedFrom
);
```


</dt> </dl> </dd> <dt>

**Auxiliary**
</dt> <dd> <dl>

Boolean value that indicates whether or not this class is Auxiliary. When **TRUE**, this class is an Auxiliary class and cannot be directly instantiated in the directory service. Auxiliary classes can only be used as super classes of other Auxiliary classes or as a source of additional properties on structural classes.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BOOLEAN**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Auxiliary(
  [out] BOOLEAN* pbAuxiliary
);
HRESULT put_Auxiliary(
  [in] BOOLEAN bAuxiliary
);
```


</dt> </dl> </dd> <dt>

**CLSID**
</dt> <dd> <dl>

Optional provider-specific CLSID identifying the COM object that implements this class.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_CLSID(
  [out] BSTR* pbstrCLSID
);
HRESULT put_CLSID(
  [in] BSTR bstrCLSID
);
```


</dt> </dl> </dd> <dt>

**Container**
</dt> <dd> <dl>

Boolean value that indicates if this class can be a container of other object classes. If this value is **TRUE**, you can call the **get\_Container** method to get an array of the object classes that this class can contain.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BOOLEAN**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Container(
  [out] BOOLEAN* pbContainer
);
HRESULT put_Container(
  [in] BOOLEAN bContainer
);
```


</dt> </dl> </dd> <dt>

**Containment**
</dt> <dd> <dl>

A **BSTR** array in which each element is the name of an object class that this class can contain.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **VARIANT**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Containment(
  [out] VARIANT* pvContainment
);
HRESULT put_Containment(
  [in] VARIANT vContainment
);
```


</dt> </dl> </dd> <dt>

**DerivedFrom**
</dt> <dd> <dl>

Array of ADsPath strings that indicate which classes this class was derived from.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **VARIANT**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_DerivedFrom(
  [out] VARIANT* pvDerivedFrom
);
HRESULT put_DerivedFrom(
  [in] VARIANT vDerivedFrom
);
```


</dt> </dl> </dd> <dt>

**HelpFileContext**
</dt> <dd> <dl>

Context ID inside **HelpFileName** where specific information for this class can be found.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **long**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_HelpFileContext(
  [out] long* plHelpContext
);
HRESULT put_HelpFileContext(
  [in] long lHelpContext
);
```


</dt> </dl> </dd> <dt>

**HelpFileName**
</dt> <dd> <dl>

Name of a help file that contains more information about objects of this class.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_HelpFileName(
  [out] BSTR* pbstrHelpFileName
);
HRESULT put_HelpFileName(
  [in] BSTR bstrHelpFileName
);
```


</dt> </dl> </dd> <dt>

**MandatoryProperties**
</dt> <dd> <dl>

**SAFEARRAY** of **VARIANT**s that lists the properties that must be set for this class to be written to storage. If the class only contains one property, then **get\_MandatoryProperties** will return a **BSTR**.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **VARIANT**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_MandatoryProperties(
  [out] VARIANT* pvarMandatoryProperties
);
HRESULT put_MandatoryProperties(
  [in] VARIANT varMandatoryProperties
);
```


</dt> </dl> </dd> <dt>

**NamingProperties**
</dt> <dd> <dl>

**SAFEARRAY** of **BSTR**s that lists the properties used to name attributes of this schema class.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **VARIANT**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_NamingProperties(
  [out] VARIANT* pvarNamingProperties
);
HRESULT put_NamingProperties(
  [in] VARIANT varNamingProperties
);
```


</dt> </dl> </dd> <dt>

**OID**
</dt> <dd> <dl>

Provider-specific Object Identifier that defines this class. This is provided to allow schema extension, using Active Directory, in directory services that require provider-specific OIDs for classes.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_OID(
  [out] BSTR* pbstrOID
);
HRESULT put_OID(
  [in] BSTR bstrOID
);
```


</dt> </dl> </dd> <dt>

**OptionalProperties**
</dt> <dd> <dl>

**SAFEARRAY** of **VARIANT**s that lists the optional properties for this schema class. If the class only contains one property, then **get\_OptionalProperties** will return a **BSTR**.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **VARIANT**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_OptionalProperties(
  [out] VARIANT* pvarOptionalProperties
);
HRESULT put_OptionalProperties(
  [in] VARIANT varOptionalProperties
);
```


</dt> </dl> </dd> <dt>

**PossibleSuperiors**
</dt> <dd> <dl>

Array of ADsPath strings that indicate the schema classes that can contain instances of this class.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **VARIANT**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PossibleSuperiors(
  [out] VARIANT* pvSuperiors
);
HRESULT put_PossibleSuperiors(
  [in] VARIANT vSuperiors
);
```


</dt> </dl> </dd> <dt>

**PrimaryInterface**
</dt> <dd> <dl>

Optional provider-specific identifier GUID that associates an interface to objects of this schema class. For example, the "User" class that supports [**IADsUser**](/windows/desktop/api/Iads/nn-iads-iadsuser) and **PrimaryInterface** is identified by **IID\_IADsUser**. This must be in the standard string format of a GUID, as defined by COM. This GUID is the value that appears in the [**IADs::get\_GUID**](/windows/desktop/api/Iads/nn-iads-iads) property in instances of this class for providers that implement this property. Identifying a schema class by IID of the class code's primary interface enables the use of **QueryInterface** at run time to determine whether an object is of the desired class.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_PrimaryInterface(
  [out] BSTR* pbstrGUID
);
```


</dt> </dl> </dd> </dl>

 

## Examples

The following code example shows how to use the [**IADsClass**](/windows/desktop/api/Iads/nn-iads-iadsclass) interface to determine if an object can be a container and, if so, lists the names of any contained objects.


```VB
Dim ads As IADs
Dim cls As IADsClass

On Error GoTo Cleanup

Set ads = GetObject("WinNT://myComputer,computer")
Set cls = GetObject(ads.Schema)
if cls.Container = True Then
    MsgBox "This object contains the following children:"
    For Each o In cls.Containment
        MsgBox o
    Next
End If

Cleanup:
    If (Err.Number<>0) Then
        MsgBox("An error has occurred. " & Err.Number)
    End If
    Set ads = Nothing
    Set cls = Nothing
```



The following code example shows how to use the [**IADsClass**](/windows/desktop/api/Iads/nn-iads-iadsclass) interface to determine if an object can be a container and, if so, lists the names of any contained objects.


```C++
HRESULT hr = S_OK;
IADsClass *pCls = NULL;
IADs *pADs = NULL;
BSTR bstrSchema;
VARIANT var;
 
hr = CoInitialize(NULL);
hr = ADsGetObject(L"WinNT://myComputer,computer",
                  IID_IADs,
                  (void**)&pADs);
if (FAILED(hr)) {goto Cleanup;}
 
hr = pADs->get_Schema(&bstrSchema);
pADs->Release();
if(FAILED(hr)) {goto Cleanup;}
 
hr = ADsGetObject(bstrSchema, IID_IADsClass, (void**)&pCls);
if(FAILED(hr)) {goto Cleanup;}
 
VariantInit(&var);
VARIANT_BOOL bCont;
pCls->get_Container(&bCont);
if(bCont != false) {
    VariantClear(&var);
    pCls->get_Containment(&var);
    hr = printVarArray(var);
}

Cleanup:
    if(pADs)
        pADs->Release();

    if(pCls)
        pCls->Release();

    SysFreeString(bstrSchema);
    CoUninitialize();
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Iads.h</dt> </dl>       |
| DLL<br/>                      | <dl> <dt>Activeds.dll</dt> </dl> |
| IID<br/>                      | IID\_IADsClass is defined as C8F93DD0-4AE0-11CF-9E73-00AA004A5691<br/>            |



## See also

<dl> <dt>

[**IADsClass**](/windows/desktop/api/Iads/nn-iads-iadsclass)
</dt> <dt>

[**IADsClass::Qualifiers**](/windows/desktop/api/Iads/nf-iads-iadsclass-qualifiers)
</dt> </dl>

 

 





