---
title: Creating Organizational Units
description: To create an organizational unit, bind to the object that will contain the organizational unit, create an organizationalUnit object, set its properties, and save the object to the directory store.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 35fa566c-9742-4d63-bc97-8d2631256245
ms.prod: windows-server-dev
ms.technology: active-directory-application-mode
ms.tgt_platform: multiple
keywords:
- AD LDS examples ADAM , creating organizational units
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating Organizational Units

To create an organizational unit, bind to the object that will contain the organizational unit, create an **organizationalUnit** object, set its properties, and save the object to the directory store.

Delete a created object with the following code example by [Deleting Organizational Units](deleting-organizational-units.md).

The following Visual Basic Scripting Edition code example uses the **GetObject** function to bind to an **organization** object and uses the **Create** method to create an **organizationalUnit** object in that **organization**.


```VB
' Create AD LDS Organizational Unit.

Option Explicit

Dim objADAM         ' Binding object.
Dim objOU           ' Organizational unit.
Dim strDescription  ' Description of OU.
Dim strOU           ' Organizational unit.
Dim strPath         ' Binding path.

' Construct the binding string.
strPath = "LDAP://localhost:389/O=Fabrikam,C=US"

WScript.Echo "Bind to: " & strPath

' Specify Organizational Unit.
strOU = "OU=TestOU"
strDescription = "AD LDS Test Organizational Unit"

On Error Resume Next

' Bind to object.
Set objADAM = GetObject(strPath)

' Output error if bind fails.
If Err.Number <> vbEmpty Then
    WScript.Echo "Error:   Bind failed."
    WScript.Quit
End If

WScript.Echo "Create:  " & strOU

' Create Organizational Unit.
Set objOU = objADAM.Create("organizationalUnit", strOU)
objOU.Put "description", strDescription
objOU.SetInfo

' Output success or error.
If Err.Number <> vbEmpty Then
    WScript.Echo "Error:   Create failed."
Else
    WScript.Echo "Success: Organizational Unit created."
End If
```



The following Visual Basic .NET code example uses the **DirectoryEntry** constructor to bind to an **organization** object and uses the **Add** method to create an **organizationalUnit** object in that **organization**.


```VB
Imports System
Imports System.DirectoryServices

Namespace ADAM_Examples

    Class CreateOU

        '/ <summary>
        '/ Create AD LDS Organizational Unit.
        '/ </summary>

        <STAThread()>  Shared Sub Main()

            Dim objADAM As DirectoryEntry  ' Binding object.
            Dim objOU As DirectoryEntry    ' Organizational unit.
            Dim strDescription As String   ' Description of OU.
            Dim strOU As String            ' Organiztional unit.
            Dim strPath As String          ' Binding path.

            ' Construct the binding string.
            strPath = "LDAP://localhost:389/O=Fabrikam,C=US"

            Console.WriteLine("Bind to: {0}", strPath)

            ' Get AD LDS object.
            Try
                objADAM = New DirectoryEntry(strPath)
                objADAM.RefreshCache()
            Catch e As Exception
                Console.WriteLine("Error:   Bind failed.")
                Console.WriteLine("         {0}", e.Message)
                Return
            End Try

            ' Specify Organizational Unit.
            strOU = "OU=TestOU"
            strDescription = "AD LDS Test Organizational Unit"
            Console.WriteLine("Create:  {0}", strOU)

            ' Create Organizational Unit.
            Try
                objOU = objADAM.Children.Add(strOU, "OrganizationalUnit")
                objOU.Properties("description").Add(strDescription)
                objOU.CommitChanges()
            Catch e As Exception
                Console.WriteLine("Error:   Create failed.")
                Console.WriteLine("         {0}", e.Message)
                Return
            End Try

            ' Output Organizational Unit attributes.
            Console.WriteLine("Success: Create succeeded.")
            Console.WriteLine("Name:    {0}", objOU.Name)
            Console.WriteLine("         {0}", _
                objOU.Properties("description").Value)
            Return

        End Sub 'Main
    End Class 'CreateOU
End Namespace 'ADAM_Examples
```



The following C# code example in uses the **DirectoryEntry** constructor to bind to an **organization** object and uses the **Add** method to create an **organizationalUnit** object in that **organization**.


```CSharp
using System;
using System.DirectoryServices;

namespace ADAM_Examples
{
    class CreateOU
    {
        /// <summary>
        /// Create AD LDS Organizational Unit.
        /// </summary>
        [STAThread]
        static void Main()
        {
            DirectoryEntry objADAM;  // Binding object.
            DirectoryEntry objOU;    // Organizational unit.
            string strDescription;   // Description of OU.
            string strOU;            // Organiztional unit.
            string strPath;          // Binding path.

            // Construct the binding string.
            strPath = "LDAP://localhost:389/O=Fabrikam,C=US";

            Console.WriteLine("Bind to: {0}", strPath);

            // Get AD LDS object.
            try
            {
                objADAM = new DirectoryEntry(strPath);
                objADAM.RefreshCache();
            }
            catch (Exception e)
            {
                Console.WriteLine("Error:   Bind failed.");
                Console.WriteLine("         {0}", e.Message);
                return;
            }

            // Specify Organizational Unit.
            strOU = "OU=TestOU";
            strDescription = "AD LDS Test Organizational Unit";
            Console.WriteLine("Create:  {0}", strOU);

            // Create Organizational Unit.
            try
            {
                objOU = objADAM.Children.Add(strOU,
                    "OrganizationalUnit");
                objOU.Properties["description"].Add(strDescription);
                objOU.CommitChanges();
            }
            catch (Exception e)
            {
                Console.WriteLine("Error:   Create failed.");
                Console.WriteLine("         {0}", e.Message);
                return;
            }

            // Output Organizational Unit attributes.
            Console.WriteLine("Success: Create succeeded.");
            Console.WriteLine("Name:    {0}", objOU.Name);
            Console.WriteLine("         {0}",
                objOU.Properties["description"].Value);
            return;
        }
    }
}
```



The following C++ code example in shows how to add an organizational unit to an application partition directory using [Active Directory Service Interfaces (ADSI)](https://msdn.microsoft.com/library/aa772170). The example uses the [**IADsContainer::Create**](https://msdn.microsoft.com/library/aa705987) and the [**IADs::SetInfo**](https://msdn.microsoft.com/library/aa746354) methods. For more information about adding objects using ADSI, see [Creating and Deleting Objects](https://msdn.microsoft.com/library/aa772364).

The function takes a binary string that contains the binding data and another binary string contains the relative name of the organizational unit. For example, the function accepts:

-   "bstrADsPath = "LDAP://localhost:389/O=fabrikam,c=US"
-   "bstrRelativeName = "OU=Accounting""

This examples assumes that you have set up your development environment for ADSI. For more information, see [Setting Up Visual C++ 6.0 for ADSI Development](https://msdn.microsoft.com/library/aa746483).


```C++
HRESULT CreateOU( BSTR bstrADsPath, BSTR bstrRelativeName)
{
    
    HRESULT hr = NULL;
    
    IADsContainer* pContainer = NULL;
    
    // Initialize COM.
    CoInitialize(NULL);  
    
    // Bind to the container.
    hr = ADsGetObject ( 
    
                        bstrADsPath, 
                        
                        IID_IADsContainer, 
                        
                        (void**) &amp;pContainer;
                        
                      );
    
    if ( SUCCEEDED(hr) )
    {
        
        IDispatch* pDisp = NULL;
        
        IADs* pOrganizationalUnit = NULL;
        
        // Create the new organizational unit.
        hr = pContainer->Create( 
        
                                 CComBSTR("organizationalUnit"), 
                                 
                                 bstrRelativeName, 
                                 
                                 &amp;pDisp;
                                 
                               );
        
        if ( SUCCEEDED(hr) )
        
        {
        
           hr = pDisp->QueryInterface( 
                                
                                        IID_IADs, 
                                        
                                        (void**) &amp;pOrganizationalUnit;
   
                                     );
           
           if ( SUCCEEDED(hr) )
           
           {
            
                // Commit newly created organizational unit to the
                // directory.
                hr = pOrganizationalUnit->SetInfo();
                
                if ( !SUCCEEDED(hr) )
                
                {
                
                    wprintf(L"Error 0x%x occurred. Container not created.\n", hr);
                                        
                    return hr;
                
                }        
                
            }
            
            
            // Release the IDispatch object.
            pDisp->Release();
            
        }
        
        // Release the organizational unit object.
        pOrganizationalUnit->Release();
    
    }
    
    // Release the container object.
    pContainer->Release();
    
    CoUninitialize();

}
```



 

 




