---
title: IADs Property Methods (Iads.h)
description: The property methods of the IADs interface get or set the properties described in the following table. For more information about property methods, see Interface Property Methods.
ms.assetid: d2f6f686-a35a-4a9a-9b57-2ceb2f26ef12
ms.tgt_platform: multiple
keywords:
- IADs Property Methods ADSI
topic_type:
- apiref
api_name:
- IADs Property Methods
- IADs.ADsPath
- IADs.get_ADsPath
- IADs.Class
- IADs.get_Class
- IADs.GUID
- IADs.get_GUID
- IADs.Name
- IADs.get_Name
- IADs.Parent
- IADs.get_Parent
- IADs.Schema
- IADs.get_Schema
api_location:
- Activeds.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IADs Property Methods

The property methods of the [**IADs**](/windows/desktop/api/Iads/nn-iads-iads) interface get or set the properties described in the following table. For more information about property methods, see [Interface Property Methods](interface-property-methods.md).

## Properties

<dl> <dt>

**ADsPath**
</dt> <dd> <dl>

The ADsPath string of this object. The string uniquely identifies this object in a network environment. The object can always be retrieved using this path.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_ADsPath(
  [out] BSTR* pbstrADsPath
);
```


</dt> </dl> </dd> <dt>

**Class**
</dt> <dd> <dl>

The name of the object Schema class.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Class(
  [out] BSTR* pbstrClass
);
```


</dt> </dl> </dd> <dt>

**GUID**
</dt> <dd> <dl>

The globally unique identifier of the directory object. The [**IADs**](/windows/desktop/api/Iads/nn-iads-iads) interface converts the **GUID** from an octet string, as stored on a directory server, into a string format.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_GUID(
  [out] BSTR* pbstrGUID
);
```


</dt> </dl> </dd> <dt>

**Name**
</dt> <dd> <dl>

The relative name of the object as named within the underlying directory service. This name distinguishes this object from its siblings.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Name(
  [out] BSTR* pbstrName
);
```


</dt> </dl> </dd> <dt>

**Parent**
</dt> <dd> <dl>

The ADsPath string of the parent container. Active Directory does not permit the formation of the ADsPath of a given object by concatenating the **Parent** and **Name** properties. While this operation might work in some providers, it is not guaranteed to work for all implementations. The ADsPath is guaranteed to be valid and should always be used to retrieve an object's interface pointer.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Parent(
  [out] BSTR* pbstrParent
);
```


</dt> </dl> </dd> <dt>

**Schema**
</dt> <dd> <dl>

The ADsPath string of the Schema class object of this object.

<dt>

Access type: Read-only
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Schema(
  [out] BSTR* pbstrSchema
);
```


</dt> </dl> </dd> </dl>

 

## Remarks

In Active Directory, the **GUID** returned from GUID is a string of hexadecimals. Use the resultant **GUID** to bind to the object directly.


```VB
Dim x As IADs
Set x = GetObject("LDAP://servername/<GUID=xxx>")
```



where xxx is the value returned from the GUID property. For more information, see [Using objectGUID to Bind to an Object](/windows/desktop/AD/using-objectguid-to-bind-to-an-object). Be aware that if you use a GUID to bind to an object, the **ADsPath** property method returns values that are different from the normal values that would be returned if you used a distinguished name (DN) to bind to the same object. For example, the following table lists the values returned when using the two different binding methods to bind to the same user object.



|             | Bind using DN                                           | Bind using GUID                                             |
|-------------|---------------------------------------------------------|-------------------------------------------------------------|
| **Name**    | CN=Jeff Smith                                           | CN=Jeff Smith                                               |
| **Parent**  | LDAP://server/CN=Users,DC=Fabrikam,DC=com               | LDAP://server/CN=Users,DC=Fabrikam,DC=com                   |
| **ADsPath** | LDAP://server/CN=Jeff Smith,CN=Users,DC=Fabrikam,DC=com | LDAP://server/<GUID=c0f59dfcf507d311a99e0000f879f7c7> |



 

> [!Note]  
> The WinNT provider does not support binding using the object **GUID**, and returns the **GUID** property in a slightly different string format.

 

## Examples

The following code example shows how to retrieve object data using property methods of the [**IADs**](/windows/desktop/api/Iads/nn-iads-iads) interface.


```VB
Dim x As IADs
Dim parent As IADsContainer
Dim cls As IADsClass
Dim op As Variant

On Error GoTo Cleanup

Set x = GetObject("WinNT://Fabrikam/Administrator")
Debug.Print "Object Name: " & x.Name
Debug.Print "Object Path: " & x.ADsPath
Debug.Print "Object Class: " & x.Class
 
' Get more data about the object schema.
Set cls = GetObject(x.Schema)
Debug.Print "Class Name is: " & cls.Name
For Each op In cls.OptionalProperties
    Debug.Print "Optional Property: " & op
Next op

Cleanup:
    If (Err.Number<>0) Then
        MsgBox("An error has occurred. " & Err.Number)
    End If
    Set x = Nothing
    Set parent = Nothing
    Set cls = Nothing
```



The following code example shows how to retrieve object data using property methods of the [**IADs**](/windows/desktop/api/Iads/nn-iads-iads) interface.


```VB
<HTML>
<head><title></title></head>

<body>
<%
Dim x 
On Error Resume Next
 
Set x = GetObject("WinNT://Fabrikam/Administrator")
Response.Write "Object Name: " & x.Name & "<br>"
Response.Write "Object Path: " & x.ADsPath & "<br>"
Response.Write "Object Class: " & x.Class & "<br>"
 
' Get more data about the object schema.
Set cls = GetObject(x.Schema)
Response.Write "Class Name is: " & cls.Name & "<br>"
For Each op In cls.OptionalProperties
    Response.Write "Optional Property: " & op & "<br>"
Next op
%>

</body>
</html>
```



The following code example shows how to work with the property methods of the [**IADs**](/windows/desktop/api/Iads/nn-iads-iads) interface.


```C++
#include <stdio.h>
#include <activeds.h>
 
int main(int argc, char* argv[])
{
    IADs *pADs = NULL;
    IADsUser *pADsUser = NULL;
    IADsClass *pCls = NULL;
    CComBSTR sbstr;
 
    HRESULT hr = CoInitialize(NULL);
    if (hr != S_OK) { return 0; }
 
    hr=ADsGetObject(L"WinNT://Fabrikam/Administrator",
                IID_IADsUser,
                (void**) &pADsUser);
    if (hr != S_OK) { goto Cleanup; }
 
    hr = pADsUser->QueryInterface(IID_IADs, (void**) &pADs);
    if( hr !=S_OK) { goto Cleanup;}
 
    pADsUser->Release();
 
    if( S_OK == pADs->get_Name(&sbstr) ) {
        printf("Object Name: %S\n",sbstr);
    }
 
    if( S_OK == pADs->get_ADsPath(&sbstr) ) {
        printf("Object path: %S\n",sbstr);
    }
 
    if( S_OK == pADs->get_Class(&sbstr) ) {
        printf("Object class: %S\n",sbstr);
    }
 
    hr = pADs->get_Schema(&sbstr);
    if ( hr != S_OK) {goto Cleanup;}
 
    hr = ADsGetObject(sbstr,IID_IADsClass, (void**)&pCls);
    if ( hr != S_OK) {goto Cleanup;}
    if( S_OK == pCls->get_Name(&sbstr) ) {
        printf("Class name is %S\n", sbstr);
    }
 
 Cleanup:
    if(pADs)
        pADs->Release();

    if(pIADsUser)
        pADsUser->Release();

    if(IADsClass)
        pADsClass->Release();

    CoUninitialize();

    if(hr==S_OK)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Iads.h</dt> </dl>       |
| DLL<br/>                      | <dl> <dt>Activeds.dll</dt> </dl> |
| IID<br/>                      | IID\_IADs is defined as FD8256D0-FD15-11CE-ABC4-02608C9E7553<br/>                 |



## See also

<dl> <dt>

[**IADs**](/windows/desktop/api/Iads/nn-iads-iads)
</dt> <dt>

[**IADsContainer**](/windows/desktop/api/Iads/nn-iads-iadscontainer)
</dt> </dl>

 

