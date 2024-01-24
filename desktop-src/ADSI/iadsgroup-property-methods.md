---
title: IADsGroup Property Methods (Iads.h)
description: Property methods of the IADsGroup interface.
ms.assetid: a8aa88d4-4695-47bc-bf7f-a17236a5671c
ms.tgt_platform: multiple
keywords:
- IADsGroup Property Methods ADSI
topic_type:
- apiref
api_name:
- IADsGroup Property Methods
- IADsGroup.Description
- IADsGroup.get_Description
- IADsGroup.put_Description
api_location:
- Activeds.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IADsGroup Property Methods

The property methods of the [**IADsGroup**](/windows/desktop/api/Iads/nn-iads-iadsgroup) interface read and write the following properties. For more information, see [Interface Property Methods](interface-property-methods.md).

## Properties

<dl> <dt>

**Description**
</dt> <dd> <dl>

Indicates the textual description of the group membership.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **BSTR**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_Description(
  [out] BSTR* pbstrDescription
);
HRESULT put_Description(
  [in] BSTR bstrDescription
);
```


</dt> </dl> </dd> </dl>

 

## Remarks

### Using IADsGroup to Retrieve Descriptions of Built-in Groups

The following examples show how to retrieve information about Windows group objects by name. In a multilingual environment, built-in groups are sometimes known by different localized names, which means that they cannot be retrieved directly by using string identifiers such as "WinNT://Microsoft/Administrators". In that case, the user can bind to the well-known SID object for the group, retrieve the localized group name, and supply that to the GetObject method. For more information, see [Well-known SIDs](/windows/desktop/SecAuthZ/well-known-sids).

## Examples

The following Visual Basic example shows how to bind to a group object and display the description of the group.


```VB
Dim grp As IADsGroup
On Error GoTo Cleanup

Set grp = GetObject("WinNT://Microsoft/Administrators")
Debug.Print grp.Description

Cleanup
    If (Err.Number<>0) Then
        MsgBox("An error has occurred. " & Err.Number)
    End If
    Set grp = Nothing
```



The following C++ example shows how to bind to a group object and display the description of the group.


```C++
IADsGroup *pGroup = NULL;
HRESULT hr = S_OK;
LPWSTR adsPath = L"WinNT://localHost/Administrators";
BSTR bstr;

hr = ADsGetObject(adsPath,IID_IADsGroup,(void**)&pGroup);

if(FAILED(hr)) {goto Cleanup;}

hr = pGroup->get_Description(&bstr);
if(FAILED(hr)) {goto Cleanup;}

printf("Description: %S\n",bstr);

Cleanup:
    SysFreeString(bstr);
    if(pGroup) 
        pGroup->Release();

    return hr;
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Iads.h</dt> </dl>       |
| DLL<br/>                      | <dl> <dt>Activeds.dll</dt> </dl> |
| IID<br/>                      | IID\_IADsGroup is defined as 27636B00-410F-11CF-B1FF-02608C9E7553<br/>            |



## See also

<dl> <dt>

[**IADs**](/windows/desktop/api/Iads/nn-iads-iads)
</dt> <dt>

[**IADsGroup**](/windows/desktop/api/Iads/nn-iads-iadsgroup)
</dt> <dt>

[Interface Property Methods](interface-property-methods.md)
</dt> </dl>

 

