---
title: Accessing Attributes with ADSI
description: The IADs.Get and IADs.GetEx methods are used to retrieve named attribute values.
ms.assetid: 8aa139e1-6b20-4745-92f1-d2f352071f33
ms.tgt_platform: multiple
keywords:
- Attributes, accessing with ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Accessing Attributes with ADSI

The [**IADs.Get**](/windows/desktop/api/Iads/nf-iads-iads-get) and [**IADs.GetEx**](/windows/desktop/api/Iads/nf-iads-iads-getex) methods are used to retrieve named attribute values. Both methods return a [**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant) value. These methods are available only for directories that support a schema. When accessing objects in a directory without a schema, the [**IADsPropertyEntry**](/windows/desktop/api/Iads/nn-iads-iadspropertyentry) and [**IADsPropertyValue**](/windows/desktop/api/Iads/nn-iads-iadspropertyvalue) interfaces must be used to manipulate attribute values.

The [**IADs.Get**](/windows/desktop/api/Iads/nf-iads-iads-get) and [**IADs.GetEx**](/windows/desktop/api/Iads/nf-iads-iads-getex) methods return a [**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant) which may, or may not, be a **VARIANT** array depending on the number of values returned by the server. For example, if only one value is returned from the server, regardless of whether it is a single or multi-valued attribute, the method returns a single **VARIANT**. Conversely, if multiple values are returned, a **VARIANT** array is returned. If a **VARIANT** array is returned, the **vt** member of the **VARIANT** structure contains the **VT\_VARIANT/vbVariant** and **VT\_ARRAY/vbArray** flags.

The [**IADs.Get**](/windows/desktop/api/Iads/nf-iads-iads-get) and [**IADs.GetEx**](/windows/desktop/api/Iads/nf-iads-iads-getex) methods can also return a COM object using the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. In this case, the **vt** member of the [**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant) structure contains the **VT\_DISPATCH/vbObject** flag. To access the COM object, call the [**QueryInterface**](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) method on the **IDispatch** interface to obtain the desired interface.

Another data type returned by the [**IADs.Get**](/windows/desktop/api/Iads/nf-iads-iads-get) and [**IADs.GetEx**](/windows/desktop/api/Iads/nf-iads-iads-getex) methods is binary data. In this case, the data is supplied as a contiguous array of bytes and the **vt** member of the [**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant) structure will contain the **VT\_UI1/vbByte** and **VT\_ARRAY/vbArray** flags.

> [!Note]  
> Microsoft Visual Basic, Scripting Edition only supports [**VARIANT**](/windows/win32/api/oaidl/ns-oaidl-variant) and **VARIANT** arrays. Because of this, VBScript cannot be used to read binary property values.

 

Many ADSI interfaces define interface-specific properties. For example, the [**IADsComputer**](/windows/desktop/api/Iads/nn-iads-iadscomputer) interface defines the [**Location**](iadscomputer-property-methods.md) property. These interface-defined properties may contain data that is identical to one of the named attributes, but the properties are specific to the type of object the interface refers to. In languages that support automation, these interface-defined properties can be accessed using the dot notation as shown in the following code example.

## Examples

The following code example shows how to access the ADsPath property on the IADs interface.


```VB
Dim oUser as IADs
Dim Path as String
 
' Bind to a specific user object.
set oUser = GetObject(
            "LDAP://CN=Jeff Smith,CN=Users,DC=fabrikam,DC=com")
 
' Get property.
Path = MyUser.ADsPath
```



In non-automation languages, the property access methods must be used to access the interface-defined properties. For example, the [**IADsComputer::get\_Location**](iadscomputer-property-methods.md) method is used to retrieve the **IADsComputer.Location** property.

The following C++ code example demonstrates how to use the property access method in C++ to retrieve the ADsPath of a user.


```C++
HRESULT hr;
IADs *pUser; 
 
// Bind to user object.
hr = ADsGetObject(
     L"LDAP://CN=Jeff Smith,CN=Users,DC=fabrikam,DC=com", 
     IID_IADs, 
     (void**)&pUser);
if(SUCCEEDED(hr)) 
{
    BSTR bstrName;

    // Get property.
    hr = pUser->get_Name(&bstrName);
    if(SUCCEEDED(hr)) 
    {
        wprintf(bstrName);
 
        SysFreeString(bstrName);
    }

    pUser->Release();
}
```



For more information about accessing attributes with ADSI, see:

-   [The Get Method](the-get-method.md)
-   [The GetEx Method](the-getex-method.md)
-   [The GetInfo Method](the-getinfo-method.md)
-   [Optimization Using GetInfoEx](optimization-using-getinfoex.md)
-   [Accessing Attributes with the IDirectoryObject Interface](accessing-attributes-with-the-idirectoryobject-interface.md)
-   [Example Code for Reading Attributes](example-code-for-reading-attributes.md)

 

 