---
title: Reading an Object's Security Descriptor
description: The following code example uses the IADs interfaces to enumerate the properties of a directory object's security descriptor, DACL, and the ACEs of the DACL.
ms.assetid: a8d0a6aa-9fbd-4392-b28b-f2eadef3935c
ms.tgt_platform: multiple
keywords:
- Reading an Object's Security Descriptor AD
- Active Directory, example code Visual Basic , reading an object's security descriptor
ms.topic: article
ms.date: 05/31/2018
---

# Reading an Object's Security Descriptor

The following code example uses the [**IADs**](/windows/desktop/api/iads/nn-iads-iads) interfaces to enumerate the properties of a directory object's security descriptor, DACL, and the ACEs of the DACL.

The following code example uses the [**IADs.Get**](/windows/desktop/api/iads/nf-iads-iads-get) method to retrieve the **nTSecurityDescriptor** property of the directory object. The C++ version of this method returns a **VARIANT** that contains an [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) pointer. The code example then calls **QueryInterface** on that **IDispatch** pointer to get an [**IADsSecurityDescriptor**](/windows/desktop/api/iads/nn-iads-iadssecuritydescriptor) interface to the object's security descriptor.

The code example then uses [**IADsSecurityDescriptor**](/windows/desktop/api/iads/nn-iads-iadssecuritydescriptor) methods to retrieve data from the security descriptor. Be aware that the data, available through **IADsSecurityDescriptor**, depends on the access rights of the caller. The [**IADsSecurityDescriptor.DiscretionaryAcl**](/windows/desktop/ADSI/iadssecuritydescriptor-property-methods) and **IADsSecurityDescriptor.Owner** properties will fail if the caller does not have **READ\_CONTROL** access to the object. Similarly, a call to the **get\_SystemAcl** method would fail if the caller does not have the **SE\_SECURITY\_NAME** privilege enabled.


```VB
Dim rootDSE As IADs
Dim dsobject As IADs
Dim sd As IADsSecurityDescriptor
Dim dacl As IADsAccessControlList
Dim ace As IADsAccessControlEntry
 
Private Sub Form_Load()

On Error GoTo Cleanup

' Bind to the Users container in the local domain.
Set rootDSE = GetObject("LDAP://rootDSE")
Set dsobject = GetObject("LDAP://cn=users," & rootDSE.Get("defaultNamingContext"))
 
' Read the security descriptor on the Users container.
Set sd = dsobject.Get("ntSecurityDescriptor")
Debug.Print "****SECURITY DESCRIPTOR PROPERTIES****"
Debug.Print "Revision: " & sd.Revision

SDParseControlMasks (sd.Control)
Debug.Print "Owner: " & sd.Owner
Debug.Print "Owner Defaulted: " & sd.OwnerDefaulted
Debug.Print "Group: " & sd.Group
Debug.Print "Group Defaulted: " & sd.GroupDefaulted
Debug.Print "System ACL Defaulted: " & sd.SaclDefaulted
Debug.Print "Discretionary ACL Defaulted: " & sd.DaclDefaulted
Debug.Print "****DACL PROPERTIES****"

Set dacl = sd.DiscretionaryAcl
AceCount = 0
For Each ace In dacl
    AceCount = AceCount + 1
    Debug.Print "**** Properties of ACE " & AceCount & " ****"
    Debug.Print "Trustee: " & ace.Trustee

    SDParseAccessMask (ace.AccessMask)

    AceType = ace.AceType
    If (AceType = &H5) Then
        Debug.Print "ACE Type: ADS_ACETYPE_ACCESS_ALLOWED_OBJECT"
    ElseIf (AceType = &H6) Then
        Debug.Print "ACE Type: ADS_ACETYPE_ACCESS_DENIED_OBJECT"
    ElseIf (AceType = &H0) Then
        Debug.Print "ACE Type: ADS_ACETYPE_ACCESS_ALLOWED"
    ElseIf (AceType = &H1) Then
        Debug.Print "ACE Type: ADS_ACETYPE_ACCESS_DENIED"
    Else
        Debug.Print "ACE Type: UNKNOWN TYPE: " & Hex(AceType)
    End If

    AceFlags = ace.Flags
    If (AceFlags And &H1) Then
        Debug.Print "Flags: ADS_FLAG_OBJECT_TYPE_PRESENT"
        Debug.Print "ObjectType: " & ace.ObjectType
    End If

    If (AceFlags And &H2) Then
        Debug.Print "Flags: ADS_FLAG_INHERITED_OBJECT_TYPE_PRESENT"
        Debug.Print "InheritedObjectType: " & ace.InheritedObjectType
    End If
Next ace

Cleanup:
    Set rootDSE = Nothing
    Set dsobject = Nothing
    Set sd = Nothing
    Set dacl = Nothing
    Set ace = Nothing

End Sub
 
' SDParseControlMasks
' Print flags set in the security descriptor Control.
Sub SDParseControlMasks(lCtrl As Long)
    Debug.Print "Control Mask: "
    If (lCtrl And &H1) Then Debug.Print "  SE_OWNER_DEFAULTED"
    If (lCtrl And &H2) Then Debug.Print "  SE_GROUP_DEFAULTED"
    If (lCtrl And &H4) Then Debug.Print "  SE_DACL_PRESENT"
    If (lCtrl And &H8) Then Debug.Print "  SE_DACL_DEFAULTED"
    If (lCtrl And &H10) Then Debug.Print "  SE_SACL_PRESENT"
    If (lCtrl And &H20) Then Debug.Print "  SE_SACL_DEFAULTED"
    If (lCtrl And &H400) Then Debug.Print "  SE_DACL_AUTO_INHERITED"
    If (lCtrl And &H800) Then Debug.Print "  SE_SACL_AUTO_INHERITED"
    If (lCtrl And &H1000) Then Debug.Print "  SE_DACL_PROTECTED"
    If (lCtrl And &H2000) Then Debug.Print "  SE_SACL_PROTECTED"
    If (lCtrl And &H8000) Then Debug.Print "  SE_SELF_RELATIVE"
End Sub
 
' SDParseControlMasks
' Print the access rights in an access mask.
Sub SDParseAccessMask(lMask As Long)
    Debug.Print "AccessMask: "
    If (lMask And &H10000) Then Debug.Print "  ADS_RIGHT_DELETE"
    If (lMask And &H20000) Then Debug.Print "  ADS_RIGHT_READ_CONTROL"
    If (lMask And &H40000) Then Debug.Print "  ADS_RIGHT_WRITE_DAC"
    If (lMask And &H80000) Then Debug.Print "  ADS_RIGHT_WRITE_OWNER"
    If (lMask And &H80000000) Then Debug.Print "  ADS_RIGHT_GENERIC_READ"
    If (lMask And &H40000000) Then Debug.Print "  ADS_RIGHT_GENERIC_WRITE"
    If (lMask And &H20000000) Then Debug.Print "  ADS_RIGHT_GENERIC_EXECUTE"
    If (lMask And &H10000000) Then Debug.Print "  ADS_RIGHT_GENERIC_ALL"
    If (lMask And &H1) Then Debug.Print "  ADS_RIGHT_DS_CREATE_CHILD"
    If (lMask And &H2) Then Debug.Print "  ADS_RIGHT_DS_DELETE_CHILD"
    If (lMask And &H4) Then Debug.Print "  ADS_RIGHT_ACTRL_DS_LIST"
    If (lMask And &H8) Then Debug.Print "  ADS_RIGHT_DS_SELF"
    If (lMask And &H10) Then Debug.Print "  ADS_RIGHT_DS_READ_PROP"
    If (lMask And &H20) Then Debug.Print "  ADS_RIGHT_DS_WRITE_PROP"
    If (lMask And &H40) Then Debug.Print "  ADS_RIGHT_DS_DELETE_TREE"
    If (lMask And &H80) Then Debug.Print "  ADS_RIGHT_DS_LIST_OBJECT"
    If (lMask And &H100) Then Debug.Print "  ADS_RIGHT_DS_CONTROL_ACCESS"
End Sub
```




```C++
HRESULT ReadSecurityDescriptor( IADs *pObject ) 
{
HRESULT hr = E_FAIL;
VARIANT var,varACE;
VARIANT_BOOL boolVal;
IADsSecurityDescriptor *pSD = NULL;
IADsAccessControlList *pACL = NULL;
IADsAccessControlEntry *pACE = NULL;
IEnumVARIANT *pEnum = NULL;
IDispatch *pDisp = NULL;
LPUNKNOWN pUnk = NULL;
ULONG lFetch;
BSTR szObjectType = NULL;
BSTR szTrustee = NULL;
BSTR szProp = NULL;
long lRev,lControl;
long lAceType, lAccessMask, lTypeFlag;
DWORD dwAces = 0;
 
if (NULL == pObject)
    return hr;
 
VariantClear(&var);
 
// Get the nTSecurityDescriptor.
// Type should be VT_DISPATCH - an IDispatch pointer to the security descriptor object.
hr = pObject->Get(CComBSTR("nTSecurityDescriptor"), &var);
if ( FAILED(hr) || var.vt != VT_DISPATCH ) {
    wprintf(L"get nTSecurityDescriptor failed: 0x%x\n", hr);
    goto Cleanup;
}
 
hr = V_DISPATCH( &var )->QueryInterface(IID_IADsSecurityDescriptor,(void**)&pSD);
if ( FAILED(hr) ) {
    wprintf(L"QueryInterface for IADsSecurityDescriptor failed: 0x%x\n", hr);
    goto Cleanup;
}
 
wprintf(L"****SECURITY DESCRIPTOR PROPERTIES****\n");
          
// Get properties using IADsSecurityDescriptor property methods.
hr = pSD->get_Revision(&lRev);
wprintf(L"Revision: %d\n", lRev);
          
// Print the control mask bits.
hr = pSD->get_Control(&lControl);
wprintf(L"Control Mask: \n");
SDParseControlMasks(lControl);
 
hr = pSD->get_Owner(&szProp);
wprintf(L"Owner: %s\n", szProp);
if (szProp)
    SysFreeString(szProp);
 
hr = pSD->get_OwnerDefaulted(&boolVal);
wprintf(L"Owner Defaulted: %s\n", boolVal ? L"True" : L"False");
 
hr = pSD->get_Group(&szProp);
wprintf(L"Group: %s\n", szProp);
if (szProp)
    SysFreeString(szProp);
 
hr = pSD->get_GroupDefaulted(&boolVal);
wprintf(L"Group Defaulted: %s\n", boolVal ? L"True" : L"False");
 
hr = pSD->get_SaclDefaulted(&boolVal);
wprintf(L"System ACL Defaulted: %s\n", boolVal ? L"True" : L"False");
 
hr = pSD->get_DaclDefaulted(&boolVal);
wprintf(L"Discretionary ACL Defaulted: %s\n", boolVal ? L"True" : L"False");
 
// Get the DACL.
wprintf(L"****DACL PROPERTIES****\n");
hr = pSD->get_DiscretionaryAcl(&pDisp);
if (SUCCEEDED(hr)) 
{
    hr = pDisp->QueryInterface(IID_IADsAccessControlList, (void**)&pACL);
    if (SUCCEEDED(hr)) 
    {
        hr = pACL->get__NewEnum( &pUnk );
        if (SUCCEEDED(hr)) 
        {
            hr = pUnk->QueryInterface( IID_IEnumVARIANT, (void**) &pEnum );
        }
    }
}
if ( FAILED(hr) ) {
    wprintf(L"Could not get DACL: 0x%x\n", hr);
    goto Cleanup;
}
 
// Loop to read all ACEs on the object.
hr = pEnum->Next( 1, &varACE, &lFetch );
while ( (hr == S_OK) && (lFetch == 1) && (varACE.vt==VT_DISPATCH))
{
    // QueryInterface for an IADsAccessControlEntry to use to read the ACE.
    hr = V_DISPATCH(&varACE)->QueryInterface( 
                           IID_IADsAccessControlEntry, (void**)&pACE );
    if ( FAILED(hr) ) {
        wprintf(L"QI for IADsAccessControlEntry failed: 0x%x\n", hr);
        break;
    }
 
    wprintf(L"**** Properties of ACE %u ****\n", ++dwAces);
 
    // Get the trustee that the ACE applies to and print it.
    hr = pACE->get_Trustee(&szTrustee);
    if (SUCCEEDED(hr))
    {
        wprintf(L"Trustee: %s\n", szTrustee);
        if (szTrustee)
            SysFreeString(szTrustee);
    }
 
    // Get the AceMask.
    hr = pACE->get_AccessMask(&lAccessMask);
    if (SUCCEEDED(hr))
    {
        wprintf(L"AccessMask: \n");
        SDParseAccessMask(lAccessMask);
    }
 
    // Get the AceType.
    hr = pACE->get_AceType(&lAceType);
    if (SUCCEEDED(hr))
    {
        if (lAceType == ADS_ACETYPE_ACCESS_ALLOWED_OBJECT)
            wprintf(L"ACE Type: ADS_ACETYPE_ACCESS_ALLOWED_OBJECT\n");
        else if (lAceType == ADS_ACETYPE_ACCESS_DENIED_OBJECT)
            wprintf(L"ACE Type: ADS_ACETYPE_ACCESS_DENIED_OBJECT\n");
        else if (lAceType == ADS_ACETYPE_ACCESS_ALLOWED)
            wprintf(L"ACE Type: ADS_ACETYPE_ACCESS_ALLOWED\n");
        else if (lAceType == ADS_ACETYPE_ACCESS_DENIED)
            wprintf(L"ACE Type: ADS_ACETYPE_ACCESS_DENIED\n");
        else
            wprintf(L"ACE Type: UNKNOWN TYPE: %x\n", lAceType);
    }
 
    // Get the flags. Based on flags, get objecttype and inheritedobjecttype.
    hr = pACE->get_Flags(&lTypeFlag);
    if (SUCCEEDED(hr))
    {
        // If the object type GUID is present, print it.
        if (lTypeFlag & ADS_FLAG_OBJECT_TYPE_PRESENT)
        {
            wprintf(L"Flags: ADS_FLAG_OBJECT_TYPE_PRESENT\n");
            hr = pACE->get_ObjectType(&szObjectType);
            if (SUCCEEDED(hr))
            {
                wprintf(L"ObjectType: %s\n", szObjectType);
                if (szObjectType)
                    SysFreeString(szObjectType);
            }
        }
 
        // If the inherited object type GUID is present, print it.
        if (lTypeFlag & ADS_FLAG_INHERITED_OBJECT_TYPE_PRESENT)
        {
            wprintf(L"Flags: ADS_FLAG_INHERITED_OBJECT_TYPE_PRESENT\n");
            hr = pACE->get_InheritedObjectType(&szObjectType);
            if (SUCCEEDED(hr))
            {
                wprintf(L"InheritedObjectType: %s\n", szObjectType);
                if (szObjectType)
                    SysFreeString(szObjectType);
            }
        }
    }
 
    // Cleanup the enumerated ACE item.
    if (pACE)
        pACE->Release();
 
    // Cleanup the VARIANT for the ACE item.
    VariantClear(&varACE);
 
    // Get the next ACE.
    hr = pEnum->Next( 1, &varACE, &lFetch );
 
} // End of While loop
 
Cleanup:
if (pEnum)
    pEnum->Release();
if (pUnk)
    pUnk->Release();
if (pACL)
    pACL->Release();
if (pDisp)
    pDisp->Release();
if (pSD)
    pSD->Release();
VariantClear(&var);
return hr;
}
 
// ******************************************************************
//  SDParseControlMasks
//  Function to print Control flags.
// ******************************************************************
int SDParseControlMasks( long lCtrl )
{
int iReturn = TRUE;
 
if (lCtrl & SE_OWNER_DEFAULTED)
    wprintf(L"  SE_OWNER_DEFAULTED\n");
 
if (lCtrl & SE_GROUP_DEFAULTED)
    wprintf(L"  SE_GROUP_DEFAULTED\n");
 
if (lCtrl & SE_DACL_PRESENT)
    wprintf(L"  SE_DACL_PRESENT\n");
 
if (lCtrl & SE_DACL_DEFAULTED)
    wprintf(L"  SE_DACL_DEFAULTED\n");
 
if (lCtrl & SE_SACL_PRESENT)
    wprintf(L"  SE_SACL_PRESENT\n");
 
if (lCtrl & SE_SACL_DEFAULTED)
    wprintf(L"  SE_SACL_DEFAULTED\n");
 
if (lCtrl & SE_DACL_AUTO_INHERIT_REQ)
    wprintf(L"  SE_DACL_AUTO_INHERIT_REQ\n");
 
if (lCtrl & SE_SACL_AUTO_INHERIT_REQ)
    wprintf(L"  SE_SACL_AUTO_INHERIT_REQ\n");
 
if (lCtrl & SE_DACL_AUTO_INHERITED)
    wprintf(L"  SE_DACL_AUTO_INHERITED\n");
 
if (lCtrl & SE_SACL_AUTO_INHERITED)
    wprintf(L"  SE_SACL_AUTO_INHERITED\n");
 
if (lCtrl & SE_DACL_PROTECTED)
    wprintf(L"  SE_DACL_PROTECTED\n");
 
if (lCtrl & SE_SACL_PROTECTED)
    wprintf(L"  SE_SACL_PROTECTED\n");
 
if (lCtrl & SE_SELF_RELATIVE)
    wprintf(L"  SE_OWNER_DEFAULTED\n");
 
return iReturn;
 
}
 
// ******************************************************************
//  SDParseAccessMask
//  Function to print AccessMask flags.
// ******************************************************************
int SDParseAccessMask( long lCtrl )
{
    int iReturn = TRUE;
 
if (lCtrl & ADS_RIGHT_DELETE)
    wprintf(L"  ADS_RIGHT_DELETE\n");
 
if (lCtrl & ADS_RIGHT_READ_CONTROL)
    wprintf(L"  ADS_RIGHT_READ_CONTROL\n");
 
if (lCtrl & ADS_RIGHT_WRITE_DAC)
    wprintf(L"  ADS_RIGHT_WRITE_DAC\n");
 
if (lCtrl & ADS_RIGHT_WRITE_OWNER)
    wprintf(L"  ADS_RIGHT_WRITE_OWNER\n");
 
if (lCtrl & ADS_RIGHT_GENERIC_READ)
    wprintf(L"  ADS_RIGHT_GENERIC_READ\n");
 
if (lCtrl & ADS_RIGHT_GENERIC_WRITE)
    wprintf(L"  ADS_RIGHT_GENERIC_WRITE\n");
 
if (lCtrl & ADS_RIGHT_GENERIC_EXECUTE)
    wprintf(L"  ADS_RIGHT_GENERIC_EXECUTE\n");
 
if (lCtrl & ADS_RIGHT_GENERIC_ALL)
    wprintf(L"  ADS_RIGHT_GENERIC_ALL\n");
 
if (lCtrl & ADS_RIGHT_DS_CREATE_CHILD)
    wprintf(L"  ADS_RIGHT_DS_CREATE_CHILD\n");
 
if (lCtrl & ADS_RIGHT_DS_DELETE_CHILD)
    wprintf(L"  ADS_RIGHT_DS_DELETE_CHILD\n");
 
if (lCtrl & ADS_RIGHT_ACTRL_DS_LIST)
    wprintf(L"  ADS_RIGHT_ACTRL_DS_LIST\n");
 
if (lCtrl & ADS_RIGHT_DS_SELF)
    wprintf(L"  ADS_RIGHT_DS_SELF\n");
 
if (lCtrl & ADS_RIGHT_DS_READ_PROP)
    wprintf(L"  ADS_RIGHT_DS_READ_PROP\n");
 
if (lCtrl & ADS_RIGHT_DS_WRITE_PROP)
    wprintf(L"  ADS_RIGHT_DS_WRITE_PROP\n");
 
if (lCtrl & ADS_RIGHT_DS_DELETE_TREE)
    wprintf(L"  ADS_RIGHT_DS_DELETE_TREE\n");
 
if (lCtrl & ADS_RIGHT_DS_LIST_OBJECT)
    wprintf(L"  ADS_RIGHT_DS_LIST_OBJECT\n");
 
if (lCtrl & ADS_RIGHT_DS_CONTROL_ACCESS)
    wprintf(L"  ADS_RIGHT_DS_CONTROL_ACCESS\n");
 
return iReturn;
 
}
```



 

 