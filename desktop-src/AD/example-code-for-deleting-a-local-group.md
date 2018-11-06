---
title: Example Code for Deleting a Local Group
description: Code examples to delete a local group on a member server or a computer running Windows NT Workstation or Windows 2000 Professional.
ms.assetid: ff4fd148-2fa2-4355-bfaa-1f093d61aa00
ms.tgt_platform: multiple
keywords:
- Active Directory examples Active Directory ,deleting a local group
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Deleting a Local Group

The following C++ code example deletes a local group on a member server or a computer running Windows 2000 Professional or Windows NT Workstation.


```C++
/********************************************************************

    DeleteADObject()

********************************************************************/

HRESULT DeleteADObject(LPOLESTR pwszAdsPath, 
                       LPWSTR pwszUsername, 
                       LPWSTR pwszPassword)
{
    HRESULT hr;
    IADs *pIADsToDelete = NULL;
 
    // Bind to the object to be deleted.
 
    // If a username and password are passed, use ADsOpenObject(), 
    // otherwise use ADsGetObject()
    if (!pwszUsername || 0 == *pwszUsername) // No user password --
                                             // use ADsOpenObject.
    {
        hr = ADsGetObject(  pwszAdsPath, 
                            IID_IADs,
                            (void **)& pIADsToDelete);
    }
    else
    {
        hr = ADsOpenObject( pwszAdsPath, 
                            pwszUsername, 
                            pwszPassword, 
                            ADS_SECURE_AUTHENTICATION,
                            IID_IADs, 
                            (void**) & pIADsToDelete);
    }
 
    if (SUCCEEDED(hr))
    {
        BSTR bsParentPath;
        
        // Get the parent path.
        hr = pIADsToDelete->get_Parent(&bsParentPath); 
        if(SUCCEEDED(hr))
        {
            VARIANT vCNToDelete;
     
            VariantInit(&vCNToDelete);

            // Get the CN property for the object to delete.
            hr = pIADsToDelete->Get(CComBSTR("cn"), &vCNToDelete);
            if (SUCCEEDED(hr))
            {
                IDirectoryObject *pIDirObjectParent = NULL;

                // ***********************************************
                // Bind to the parent.
                // If a username and password are passed,
                // use ADsOpenObject()
                // otherwise use ADsGetObject()
                if (!pwszUsername || 0 == *pwszUsername) 
                 // No user password passed - use ADsOpenObject.
                {
                    hr = ADsGetObject(bsParentPath, 
                                      IID_IDirectoryObject,
                                      (void **)&pIDirObjectParent);
                }
                else
                {
                    hr = ADsOpenObject(bsParentPath, 
                                       pwszUsername, 
                                       pwszPassword, 
                                       ADS_SECURE_AUTHENTICATION,
                                       IID_IDirectoryObject, 
                                       (void**)&pIDirObjectParent);
                }
                if (SUCCEEDED(hr))
                {
                    // Release the object to delete.
                    pIADsToDelete->Release();
                    pIADsToDelete = NULL;
     
                    LPWSTR pwszPrefix = L"CN=";
                    LPWSTR pwszRDN = 
                      new WCHAR[lstrlenW(pwszPrefix) + 
                      lstrlenW(vCNToDelete.bstrVal) + 1];
                    if(pwszRDN)
                    {
                        wcscpy_s(pwszRDN, pwszPrefix);
                        wcscat_s(pwszRDN, vCNToDelete.bstrVal);

                        // Instruct the parent to 
                        // delete the child object.
                        hr = pIDirObjectParent->DeleteDSObject(pwszRDN);
                        
                        delete pwszRDN;
                    }
                    else
                    {
                        hr = E_OUTOFMEMORY;
                    }

                    // Release the Parent Object.
                    pIDirObjectParent->Release();
                    pIDirObjectParent = NULL;
                }

                VariantClear(&vCNToDelete);
            }
            
            SysFreeString(bsParentPath);
        }
    }
    
    // If a IADsObject is held, release it.
    if ( pIADsToDelete)
    {
        // Release the object to delete.
        pIADsToDelete->Release();
        pIADsToDelete = NULL;
    }
 
    return hr;
}
```



The following Visual Basic Scripting Edition code example deletes a local group on a member server or a computer running Windows 2000 Professional or Windows NT Workstation.


```VB
' Example: Deleting a local group on a member server or Windows NT
'          Workstation or Windows 2000 Professional
 
''''''''''''''''''''
' Parse the arguments.
''''''''''''''''''''
On Error Resume Next
 
Set oArgs = WScript.Arguments
If oArgs.Count < 2 Then
    sComputer = InputBox("This script deletes a group from a member server or workstation." & vbCrLf & vbCrLf &"Specify 
 
the computer name:")
    sGroup = InputBox("Specify the group name:")
Else
    sComputer = oArgs.item(0)
    sGroup = oArgs.item(1)
End If
 
If sComputer = "" Then
    WScript.Echo "No computer name was specified. You must specify a computer name."
    WScript.Quit(1)
End If
If sGroup = "" Then
    WScript.Echo "No group name was specified. You must specify a group name."
    WScript.Quit(1)
End If
 
''''''''''''''''''''
' Bind to the computer.
''''''''''''''''''''
Set cont= GetObject("WinNT://" & sComputer & ",computer")
If (Err.Number <> 0) Then
    BailOnFailure Err.Number, "on GetObject method"
End If
 
''''''''''''''''''''
' Delete the group.
''''''''''''''''''''
' It is not necessary to specify localGroup. 
' To specify the group is acceptable.
Set oGroup = cont.Delete("group", sGroup)
If (Err.Number <> 0) Then
    BailOnFailure Err.Number, "on IADsContainer::Delete method"
End If
 
strText = "The group " & sGroup & " was deleted on computer " & sComputer & "."
 
Call show_groups(strText, sComputer)
 

''''''''''''''''''''
' Display subroutines.
''''''''''''''''''''
Sub show_groups(strText, strName)
    MsgBox strText, vbInformation, "Create group on " & strName
End Sub
```



 

 




