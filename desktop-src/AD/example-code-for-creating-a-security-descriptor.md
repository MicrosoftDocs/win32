---
title: Example Code for Creating a Security Descriptor
description: This topic includes PowerShell, C++, and legacy Visual Basic 6.0 code examples that show how to create a security descriptor for a new Active Directory object using ADSI.
ms.assetid: 7c6dcdaf-0bef-4f72-bd9d-dc3ab4295008
ms.tgt_platform: multiple
keywords:
- Example Code for Creating a Security Descriptor
ms.topic: reference
ms.date: 09/20/2026
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Example Code for Creating a Security Descriptor

The following examples use Active Directory Service Interfaces (ADSI) to create a new organizational unit, build a security descriptor whose discretionary access-control list (DACL) contains one access-control entry (ACE), and assign that security descriptor before the object is committed to Active Directory. The caller must have permission to create objects in the parent container.

## PowerShell

> [!NOTE]
> For routine Active Directory administration, the [ActiveDirectory PowerShell module](/powershell/module/activedirectory/about/about_activedirectory) is usually simpler. This example calls the ADSI COM interfaces directly so that it mirrors the C++ example.

```powershell
# ADSI constants.
$ADS_RIGHT_DS_READ_PROP             = 0x10
$ADS_ACETYPE_ACCESS_ALLOWED         = 0x00
$ADS_ACEFLAG_NONE                   = 0x00
$ADS_SD_CONTROL_SE_DACL_PRESENT     = 0x04
$ACL_REVISION_DS                    = 0x04

# Parent container and new object.
$parentPath   = 'LDAP://DC=Fabrikam,DC=com'
$relativeName = 'OU=Sales'

# Trustee that receives the ACE.
$trustee = 'FABRIKAM\Security Readers'

$container          = $null
$newObject          = $null
$securityDescriptor = $null
$dacl               = $null
$ace                = $null

try {
    # Bind to the parent container.
    $container =
        [System.Runtime.InteropServices.Marshal]::BindToMoniker($parentPath)

    # Create the directory object in the ADSI property cache.
    # The object is not committed until SetInfo is called.
    $newObject =
        $container.Create('organizationalUnit', $relativeName)

    # Create a new ADSI security descriptor.
    $securityDescriptor =
        New-Object -ComObject 'SecurityDescriptor'

    # Create a new DACL.
    $dacl =
        New-Object -ComObject 'AccessControlList'

    $dacl.AclRevision = $ACL_REVISION_DS

    # Create an ACE for the DACL.
    $ace =
        New-Object -ComObject 'AccessControlEntry'

    # Grant Read Property permission for all properties on this object.
    $ace.Trustee    = $trustee
    $ace.AccessMask = $ADS_RIGHT_DS_READ_PROP
    $ace.AceType    = $ADS_ACETYPE_ACCESS_ALLOWED
    $ace.AceFlags   = $ADS_ACEFLAG_NONE

    $dacl.AddAce($ace)

    # Configure the new security descriptor. The owner is not set,
    # so Active Directory assigns the default owner.
    $securityDescriptor.Revision = 1
    $securityDescriptor.Control =
        $ADS_SD_CONTROL_SE_DACL_PRESENT
    $securityDescriptor.DiscretionaryAcl = $dacl

    # Attach the security descriptor to the new object.
    $newObject.Put(
        'nTSecurityDescriptor',
        $securityDescriptor
    )

    # Create the object and commit the security descriptor.
    $newObject.SetInfo()
}
catch {
    throw [System.InvalidOperationException]::new(
        "Unable to create '$relativeName'.",
        $_.Exception
    )
}
finally {
    foreach ($comObject in @(
        $ace,
        $dacl,
        $securityDescriptor,
        $newObject,
        $container
    )) {
        if (
            $null -ne $comObject -and
            [System.Runtime.InteropServices.Marshal]::IsComObject($comObject)
        ) {
            [void][System.Runtime.InteropServices.Marshal]::ReleaseComObject(
                $comObject
            )
        }
    }
}
```

## C++

The following example performs the same operation by calling the ADSI interfaces directly from C++.

```cpp
#include <windows.h>

#include <activeds.h>
#include <adshlp.h>
#include <atlbase.h>
#include <atlcomcli.h>
#include <stdio.h>

#pragma comment(lib, "Activeds.lib")
#pragma comment(lib, "Adsiid.lib")

HRESULT CreateOuWithSecurityDescriptor(
    const wchar_t* parent_path,
    const wchar_t* relative_name,
    const wchar_t* trustee) {
  if (parent_path == nullptr ||
      relative_name == nullptr ||
      trustee == nullptr) {
    return E_INVALIDARG;
  }

  // Bind to the parent container using the caller's security context.
  CComPtr<IADsContainer> container;

  HRESULT hr = ADsOpenObject(
      parent_path,
      nullptr,
      nullptr,
      ADS_SECURE_AUTHENTICATION,
      IID_IADsContainer,
      reinterpret_cast<void**>(&container));

  if (FAILED(hr)) {
    return hr;
  }

  // Create the directory object in the ADSI property cache.
  CComPtr<IDispatch> object_dispatch;

  hr = container->Create(
      CComBSTR(L"organizationalUnit"),
      CComBSTR(relative_name),
      &object_dispatch);

  if (FAILED(hr)) {
    return hr;
  }

  CComQIPtr<IADs> new_object(object_dispatch);

  if (!new_object) {
    return E_NOINTERFACE;
  }

  // Create a new ADSI security descriptor.
  CComPtr<IADsSecurityDescriptor> security_descriptor;

  hr = CoCreateInstance(
      CLSID_SecurityDescriptor,
      nullptr,
      CLSCTX_INPROC_SERVER,
      IID_IADsSecurityDescriptor,
      reinterpret_cast<void**>(&security_descriptor));

  if (FAILED(hr)) {
    return hr;
  }

  // Create a new DACL.
  CComPtr<IADsAccessControlList> dacl;

  hr = CoCreateInstance(
      CLSID_AccessControlList,
      nullptr,
      CLSCTX_INPROC_SERVER,
      IID_IADsAccessControlList,
      reinterpret_cast<void**>(&dacl));

  if (FAILED(hr)) {
    return hr;
  }

  hr = dacl->put_AclRevision(ACL_REVISION_DS);

  if (FAILED(hr)) {
    return hr;
  }

  // Create a new ACE.
  CComPtr<IADsAccessControlEntry> ace;

  hr = CoCreateInstance(
      CLSID_AccessControlEntry,
      nullptr,
      CLSCTX_INPROC_SERVER,
      IID_IADsAccessControlEntry,
      reinterpret_cast<void**>(&ace));

  if (FAILED(hr)) {
    return hr;
  }

  // Grant Read Property permission for all properties on this object.
  hr = ace->put_Trustee(CComBSTR(trustee));

  if (FAILED(hr)) {
    return hr;
  }

  hr = ace->put_AccessMask(ADS_RIGHT_DS_READ_PROP);

  if (FAILED(hr)) {
    return hr;
  }

  hr = ace->put_AceType(ADS_ACETYPE_ACCESS_ALLOWED);

  if (FAILED(hr)) {
    return hr;
  }

  // Apply the ACE only to the new object.
  hr = ace->put_AceFlags(0);

  if (FAILED(hr)) {
    return hr;
  }

  CComQIPtr<IDispatch> ace_dispatch(ace);

  if (!ace_dispatch) {
    return E_NOINTERFACE;
  }

  hr = dacl->AddAce(ace_dispatch);

  if (FAILED(hr)) {
    return hr;
  }

  CComQIPtr<IDispatch> dacl_dispatch(dacl);

  if (!dacl_dispatch) {
    return E_NOINTERFACE;
  }

  // Configure the new security descriptor. The owner is not set,
  // so Active Directory assigns the default owner.
  hr = security_descriptor->put_Revision(1);

  if (FAILED(hr)) {
    return hr;
  }

  hr = security_descriptor->put_Control(
      ADS_SD_CONTROL_SE_DACL_PRESENT);

  if (FAILED(hr)) {
    return hr;
  }

  hr = security_descriptor->put_DiscretionaryAcl(
      dacl_dispatch);

  if (FAILED(hr)) {
    return hr;
  }

  // Put requires the security descriptor as an IDispatch VARIANT.
  CComQIPtr<IDispatch> security_descriptor_dispatch(
      security_descriptor);

  if (!security_descriptor_dispatch) {
    return E_NOINTERFACE;
  }

  CComVariant security_descriptor_value(
      security_descriptor_dispatch);

  hr = new_object->Put(
      CComBSTR(L"nTSecurityDescriptor"),
      security_descriptor_value);

  if (FAILED(hr)) {
    return hr;
  }

  // Create the object and commit the security descriptor.
  return new_object->SetInfo();
}

int wmain() {
  HRESULT hr = CoInitializeEx(
      nullptr,
      COINIT_APARTMENTTHREADED);

  if (FAILED(hr)) {
    fwprintf(
        stderr,
        L"COM initialization failed: 0x%08lX\n",
        static_cast<unsigned long>(hr));

    return 1;
  }

  hr = CreateOuWithSecurityDescriptor(
      L"LDAP://DC=Fabrikam,DC=com",
      L"OU=Sales",
      L"FABRIKAM\\Security Readers");

  CoUninitialize();

  if (FAILED(hr)) {
    fwprintf(
        stderr,
        L"Unable to create the directory object: 0x%08lX\n",
        static_cast<unsigned long>(hr));

    return 1;
  }

  return 0;
}
```

The example uses [IADsContainer::Create](/windows/win32/api/iads/nf-iads-iadscontainer-create) to prepare the new object in the ADSI property cache, builds the security descriptor from `CLSID_SecurityDescriptor`, `CLSID_AccessControlList`, and `CLSID_AccessControlEntry` objects, and assigns it before calling `IADs::SetInfo`. For more information, see [Creating Security Descriptors for New Directory Objects](creating-a-security-descriptor-for-a-new-directory-object.md), [IADsSecurityDescriptor](/windows/win32/api/iads/nn-iads-iadssecuritydescriptor), and [IADsAccessControlEntry](/windows/win32/api/iads/nn-iads-iadsaccesscontrolentry).

## Visual Basic 6.0

> [!NOTE]
> This example is provided for developers who maintain existing Visual Basic 6.0 applications. Visual Basic 6.0 development and the Visual Basic 6.0 IDE are no longer supported, although the Visual Basic 6.0 runtime remains supported for existing applications for the support lifetime of the Windows versions in which it ships. For new development, use a supported language. For more information, see [Support Statement for Visual Basic 6.0 on Windows](/previous-versions/visualstudio/visual-basic-6/visual-basic-6-support-policy).

The following example performs the same operation as the PowerShell and C++ examples. It requires a project reference to the Active DS Type Library.

```VB
Dim Container As IADsContainer
Dim NewObject As IADs
Dim SecDes As New SecurityDescriptor
Dim Dacl As New AccessControlList
Dim Ace As New AccessControlEntry

On Error GoTo Cleanup

' Bind to the parent container and create the new object
' in the ADSI property cache.
Set Container = GetObject("LDAP://DC=Fabrikam,DC=com")
Set NewObject = Container.Create("organizationalUnit", "OU=Sales")

' Grant Read Property permission for all properties on this object.
Ace.Trustee = "FABRIKAM\Security Readers"
Ace.AccessMask = ADS_RIGHT_DS_READ_PROP
Ace.AceType = ADS_ACETYPE_ACCESS_ALLOWED
Ace.AceFlags = 0

Dacl.AclRevision = ADS_SD_REVISION_DS
Dacl.AddAce Ace

' Configure the new security descriptor. The owner is not set,
' so Active Directory assigns the default owner.
SecDes.Revision = 1
SecDes.Control = ADS_SD_CONTROL_SE_DACL_PRESENT
SecDes.DiscretionaryAcl = Dacl

' Attach the security descriptor, then create the object
' and commit the security descriptor.
NewObject.Put "nTSecurityDescriptor", SecDes
NewObject.SetInfo

Cleanup:
    If Err.Number <> 0 Then
        MsgBox "An error has occurred: 0x" & Hex(Err.Number)
    End If
    Set Ace = Nothing
    Set Dacl = Nothing
    Set SecDes = Nothing
    Set NewObject = Nothing
    Set Container = Nothing
```

## Resulting security descriptor

The supplied DACL contains one explicit allow ACE that grants `ADS_RIGHT_DS_READ_PROP` to the trustee, and because no object type GUID is specified, the permission applies to all properties of the new object. The examples set neither an owner nor a system access-control list (SACL), so Active Directory assigns the default owner from the creator's security context. The supplied DACL contains one ACE, which differs from an empty DACL (which grants no access) and from a NULL DACL (which grants unrestricted access). Code that builds security descriptors must keep these cases distinct.

Because the examples supply a DACL without setting `ADS_SD_CONTROL_SE_DACL_PROTECTED`, the new object's DACL consists of the explicit ACE followed by inheritable ACEs from the parent container. The default DACL from the `defaultSecurityDescriptor` attribute of the object's class is applied only when the creator does not supply a DACL, so the new organizational unit does not receive those default ACEs. Applications that add several explicit ACEs should add them in canonical order. For more information, see [How Security Descriptors are Set on New Directory Objects](how-security-descriptors-are-set-on-new-directory-objects.md) and [Order of ACEs in a DACL](../SecAuthZ/order-of-aces-in-a-dacl.md).

## Modifying existing objects

A new security descriptor can also be assigned to the `nTSecurityDescriptor` property of an existing object. However, doing so replaces the security descriptor components that ADSI writes, including the entire DACL. For routine permission changes, retrieve the object's current security descriptor, add or remove ACEs in its DACL, and write it back so that unrelated access-control information is preserved. For more information, see [Setting Access Rights on an Object](setting-access-rights-on-an-object.md).
