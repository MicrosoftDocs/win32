---
title: Example Code for Enumerating Users on a Member Server
description: This topic includes code examples that enumerate users on a member server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: a856281a-7f84-44d0-9123-b27fda56e0ea
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Active Directory examples Active Directory , enumerating users on a member server
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Example Code for Enumerating Users on a Member Server

The following Visual Basic code example enumerates all users on a member server or Windows 2000 Professional.


```VB
Const ADS_SECURE_AUTHENTICATION = 1

'   ListObjectsWithWinNtProvider()
'
'   Uses the WinNT provider to list child objects based on a filter.
'
'   Parameters:
'
'   pwszComputer - Contains the computer to list the objects for.
'   pwszClass - Contains the object class name to filter for.
'   pwszUsername - Contains the user name to be used for 
'                  authentication.
'   pwszPassword - Contains the password to be used for 
'                  authentication.
'
Public Sub ListObjectsWithWinNtProvider(Computer As String, _
                                        Class As String, _
                                        Username As String, _
                                        Password As String)
    Dim BindingString As String
    Dim oComputer As IADsContainer
    Dim oObject As IADs
    Dim oNSP As IADsOpenDSObject
    
    ' Build the binding string.
    BindingString = "WinNT://" + Computer + ",computer"
    
    ' Bind to the computer.
    If Username = "" Then
        Set oComputer = GetObject(BindingString)
    Else
        Set oNSP = GetObject("WinNT:")
        Set oComputer = oNSP.OpenDSObject(BindingString, _
            Username, _
            Password, _
            ADS_SECURE_AUTHENTICATION)
    End If
    
    ' Add the class to the Filter property of the 
    ' IADsContainer object.
    oComputer.Filter = Array(Class)
    
    For Each oObject In oComputer
        Debug.Print ""
        Debug.Print "Name:" + oObject.Name
        Debug.Print "ADsPath:" + oObject.ADsPath
        Debug.Print "-----------------------------------------"
    Next
End Sub
```



The following C++ code example enumerates all objects of a specified class, such as a user, and displays the members contained in each object on a member server or Windows 2000 Professional.


```C++
/********************************************************************

    ListObjectsWithWinNtProvider()

    Uses the WinNT provider to list children based on a filter. 
    Returns S_OK if successful.
 
    Parameters:

    pwszComputer - Contains the computer for which to 
                   list the objects.
    pwszClass - Contains the object class name to filter for.
    pwszUsername - Contains the user name to be used for 
                   authentication.
    pwszPassword - Contains the password to be used for 
                   authentication.
 
*********************************************************************/

HRESULT ListObjectsWithWinNtProvider(
    LPCWSTR pwszComputer, 
    LPCWSTR pwszClass, 
    LPCWSTR pwszUsername, 
    LPCWSTR pwszPassword)
{
    HRESULT hr;
 
    IADsContainer * pIADsCont = NULL;
 
    // Build the binding string.
    CComBSTR sbstrBindingString;
    sbstrBindingString = "WinNT://";
    sbstrBindingString += pwszComputer;
    sbstrBindingString += ",computer";
    
    // Bind to the container.
    hr = ADsOpenObject( sbstrBindingString,
                        pwszUsername, 
                        pwszPassword, 
                        ADS_SECURE_AUTHENTICATION,
                        IID_IADsContainer, 
                        (void**) &amp;pIADsCont);

    if (SUCCEEDED(hr))
    {
        VARIANT vFilter;
        VariantInit(&amp;vFilter);
        LPWSTR rgpwszFilter[] = {(LPWSTR)pwszClass};
 
        // Build a Variant of array type, using the filter passed.
        hr = ADsBuildVarArrayStr(rgpwszFilter, 1, &amp;vFilter);
        if (SUCCEEDED(hr))
        {
            // Set the filter for the results of the enumeration.
            hr = pIADsCont->put_Filter(vFilter);
            if (SUCCEEDED(hr))
            {
                IEnumVARIANT *pEnumVariant = NULL;
 
                // Build an enumerator interface. This is used 
                // to enumerate the objects contained in 
                // the IADsContainer.
                hr = ADsBuildEnumerator(pIADsCont, &amp;pEnumVariant);

                if(SUCCEEDED(hr))
                {
                    VARIANT Variant;
                    ULONG ulElementsFetched;

                    // Loop through and print the data.
                    while(SUCCEEDED(ADsEnumerateNext(pEnumVariant, 
                                                     1,
                                                     &amp;Variant, 
                                                     &amp;ulElementsFetched))
                          &amp;&amp; (ulElementsFetched > 0))
                    {
                        if(VT_DISPATCH == Variant.vt)
                        {
                            IADs *pIADs= NULL;

                            // Query the variant IDispatch *
                            // for the IADs interface
                            hr = Variant.pdispVal->QueryInterface(IID_IADs,
                                                                  (VOID**)&amp;pIADs);
     
                            if (SUCCEEDED(hr))
                            {
                                // Print the object data.
                                CComBSTR sbstrResult;
                                hr = pIADs->get_Name(&amp;sbstrResult); 
                                if(SUCCEEDED(hr))
                                {
                                    wprintf(L"Name : %s\n", 
                                            sbstrResult);
                                }

                                hr = pIADs->get_ADsPath(&amp;sbstrResult); 
                                if(SUCCEEDED(hr))
                                {
                                    wprintf(L"ADsPath : %s\n", 
                                            sbstrResult);
                                }
     
                                wprintf(L"-------------------\n\n");
                                
                                pIADs->Release();
                            }
                        }
                    
                        VariantClear(&amp;Variant);
                    }
                    
                    pEnumVariant->Release();
                }

            }
        }
        VariantClear(&amp;vFilter);
    }
 
    return hr;
}
```



 

 




