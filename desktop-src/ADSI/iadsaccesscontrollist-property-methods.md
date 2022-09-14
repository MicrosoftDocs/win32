---
title: IADsAccessControlList Property Methods (Iads.h)
description: The property methods of the IADsAccessControlList interface get or set the properties described in the following table. For more information, see Interface Property Methods.
ms.assetid: cb68bb61-4216-4f69-bea1-ab7f98937a27
ms.tgt_platform: multiple
keywords:
- IADsAccessControlList Property Methods ADSI
topic_type:
- apiref
api_name:
- IADsAccessControlList Property Methods
- IADsAccessControlList.AclRevision
- IADsAccessControlList.get_AclRevision
- IADsAccessControlList.put_AclRevision
- IADsAccessControlList.AceCount
- IADsAccessControlList.get_AceCount
- IADsAccessControlList.put_AceCount
api_location:
- Activeds.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IADsAccessControlList Property Methods

The property methods of the [**IADsAccessControlList**](/windows/desktop/api/Iads/nn-iads-iadsaccesscontrollist) interface get or set the properties described in the following table. For more information, see [Interface Property Methods](interface-property-methods.md).

## Properties

<dl> <dt>

**AceCount**
</dt> <dd> <dl>

The number of access control entries in the access-control list.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_AceCount(
  [out] LONG* lnAceCount
);
HRESULT put_AceCount(
  [in] LONG lnAceCount
);
```


</dt> </dl> </dd> <dt>

**AclRevision**
</dt> <dd> <dl>

The revision level of an access-control list. This value can be **ACL\_REVISION** or **ACL\_REVISION\_DS**. Use **ACL\_REVISION\_DS** if the ACL contains an object-specific ACE. All ACEs in an ACL must be at the same revision level.

<dt>

Access type: Read/write
</dt> <dt>

Scripting data type: **LONG**
</dt> <dt>



``` syntax
// C++ method syntax
HRESULT get_AclRevision(
  [out] LONG* lnAclRevision
);
HRESULT put_AclRevision(
  [in] LONG lnAclRevision
);
```


</dt> </dl> </dd> </dl>

 

## Examples

The following code example displays the number of ACEs in an ACL.


```VB
Dim x as IADs
Dim sd As IADsSecurityDescriptor
Dim Dacl As IADsAccessControlList

On Error GoTo Cleanup

Set x = GetObject("LDAP://OU=Sales,DC=Fabrikam,DC=com")
Set sd = x.Get("ntSecurityDescriptor")
Set Dacl = sd.DiscretionaryAcl
Debug.Print Dacl.AceCount

Cleanup:
    If (Err.Number <> 0) Then
        MsgBox ("An error has occurred. " & Err.Number)
    End If
    Set x = Nothing
```



The following code example displays the number of ACEs in an ACL.


```C++
HRESULT ShowACEInACL(LPWSTR guestPath,LPWSTR user,LPWSTR passwd)
{
  IADs *pObj = NULL;
  IADsSecurityDescriptor *psd = NULL;
  HRESULT hr = S_OK;
  VARIANT var;

  VariantInit(&var);

  hr = ADsOpenObject(guestPath,user,passwd,ADS_SECURE_AUTHENTICATION,
                     IID_IADs,(void**)&pObj);
  if(FAILED(hr)) {
      printf("hr = %x\n",hr);
      return hr;
  }
  else {
      BSTR bstr = NULL;
      pObj->get_Class(&bstr);
      printf("Object class: %S\n",bstr);
      SysFreeString(bstr);
  }

  hr = pObj->Get(CComBSTR("ntSecurityDescriptor"), &var);
  pObj->Release();

  if(FAILED(hr)) {
      printf("Get ntSD: hr = %x\n",hr);
      return hr;
  }

  hr = V_DISPATCH(&var)->QueryInterface(IID_IADsSecurityDescriptor,
                                        (void**)&psd);

  if(FAILED(hr)) {
      printf("DISP: hr = %x\n",hr);
      VariantClear(&var);
      return hr;
  }

  IDispatch *pDisp = NULL;
  hr = psd->get_DiscretionaryAcl(&pDisp);
  VariantClear(&var);

  if(FAILED(hr)) {
      printf("get_DACL : hr = %x\n",hr);
      return hr;
  }

  IADsAccessControlList *pAcl = NULL;
  hr = pDisp->QueryInterface(IID_IADsAccessControlList,(void**)&pAcl);
  pDisp->Release();

  if(FAILED(hr)) {
      printf("QI ACL: hr = %x\n",hr);
      return hr;
  }

  long count = 0;
  hr = pAcl->get_AceCount(&count);
  pAcl->Release();
  if(FAILED(hr)) {
      printf("Count: hr = %x\n",hr);
      return hr;
  }

  printf("AceCount = %d\n",count);

  return hr;
}
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Header<br/>                   | <dl> <dt>Iads.h</dt> </dl>        |
| DLL<br/>                      | <dl> <dt>Activeds.dll</dt> </dl>  |
| IID<br/>                      | IID\_IADsAccessControlList is defined as B7EE91CC-9BDD-11D0-852C-00C04FD8D503<br/> |



## See also

<dl> <dt>

[**IADsAccessControlList**](/windows/desktop/api/Iads/nn-iads-iadsaccesscontrollist)
</dt> <dt>

[**IEnumVARIANT**](/windows/win32/api/oaidl/nn-oaidl-ienumvariant)
</dt> <dt>

[**IADsAccessControlEntry**](/windows/desktop/api/Iads/nn-iads-iadsaccesscontrolentry)
</dt> <dt>

[**IADsSecurityDescriptor**](/windows/desktop/api/Iads/nn-iads-iadssecuritydescriptor)
</dt> </dl>

 

