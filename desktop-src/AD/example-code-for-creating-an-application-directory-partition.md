---
title: Example Code for Creating an Application Directory Partition
description: This topic includes code examples create an application directory partition.
ms.assetid: dc538afc-8529-42cf-a276-a4579d555557
ms.tgt_platform: multiple
keywords:
- example code for creating an application directory partition Active Directory
- application directory partitions Active Directory , example code for creating
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Creating an Application Directory Partition

The following C++ code example creates a new application directory partition using ADSI.


```C++
/********************************************************************

    CreateApplicationPartitionIADs()

    Description: Creates an application directory partition.

    Parameters:

    pwszDCADsPath - Contains the ADsPath of the partition. This must
    also contain the DNS name of the domain controller on which the
    partition will be created. For example, the ADsPath 
    "LDAP://DC01.fabrikam.com/DC=test,DC=com" would cause the 
    partition to be created on DC01.fabrikam.com. The distinguished
    name of the partition will be "<pwszPartitionPath>,DC=test,DC=com".

    pwszUsername - Contains the user name to be used for 
    authentication.

    pwszPassword - Contains the password to be used for
    authentication.

    pwszPartitionPath - Contains the relative distinguished name of
    the partition. This must be in the form of "DC=dynamicdata".

    pwszDescription - Contains a string that will be used for the 
    description property for the domainDNS object.

********************************************************************/

HRESULT CreateApplicationPartitionIADs(LPCWSTR pwszDCADsPath, 
                                       LPCWSTR pwszUsername, 
                                       LPCWSTR pwszPassword,
                                       LPCWSTR pwszPartitionPath,
                                       LPCWSTR pwszDescription)
{
    HRESULT hr = E_FAIL;

    IADsContainer *padsDC;

    /* 
    Bind to the specified domain controller. The path must be in the 
    form "LDAP://<server DNS name>/<partition path>", in most cases,
    the <partition path> will not be a valid path, so ADS_FAST_BIND 
    is used to allow the bind to succeed even if the path is invalid. 
    ADS_USE_DELEGATION is used to enable the LDAP provider to use the 
    credentials to contact the Domain Naming FSMO role holder to
    create or modify the crossRef object.
    */
    hr = ADsOpenObject( pwszDCADsPath,
                        pwszUsername,
                        pwszPassword,
                          ADS_SECURE_AUTHENTICATION | 
                          ADS_FAST_BIND | 
                          ADS_USE_DELEGATION,
                        IID_IADsContainer, 
                        (LPVOID*)&padsDC);

    if(SUCCEEDED(hr))
    {
        CComBSTR sbstrPath = pwszPartitionPath;
        IDispatch *pDisp;
        
        // Create the domainDNS object.
        hr = padsDC->Create(CComBSTR("domainDNS"), 
                            sbstrPath, 
                            &pDisp);

        if(SUCCEEDED(hr))
        {
            IADs *padsPartition;

            // Get the IADs interface.
            hr = pDisp->QueryInterface(IID_IADs, 
                                       (LPVOID*)&padsPartition);
            if(SUCCEEDED(hr))
            {
                CComVariant svar;

                // Set the instanceType property.
                svar = DS_INSTANCETYPE_IS_NC_HEAD | 
                       DS_INSTANCETYPE_NC_IS_WRITEABLE;
                hr = padsPartition->Put(CComBSTR("instanceType"), 
                                        svar);

                // Set the description property.
                svar = pwszDescription;
                hr = padsPartition->Put(CComBSTR("description"), 
                                        svar);

                // Commit the new object to the server.
                hr = padsPartition->SetInfo();

                padsPartition->Release();
            }
            
            pDisp->Release();
        }
        
        padsDC->Release();
    }

    return hr;
}
```



The following Visual Basic Scripting Edition code example shows how to create a new application directory partition using ADSI.


```VB
' CreateApplicationPartitionVBS()
' 
' Description: Creates an application directory partition.
' 
' Parameters:
' 
' DCADsPath - Contains the ADsPath of the partition. This must also 
' contain the DNS name of the domain controller on which the
' partition will be created. For example, the ADsPath 
' "LDAP://DC01.fabrikam.com/DC=test,DC=com" would cause the partition
' to be created on DC01.fabrikam.com. The distinguished name of the
' partition will be "<pwszPartitionPath>,DC=test,DC=com".
' 
' Username - Contains the user name to be used for authentication.
' 
' Password - Contains the password to be used for authentication.
' 
' PartitionPath - Contains the relative distinguished name of the 
' partition. This must be in the form of "DC=dynamicdata".
' 
' Description - Contains a string that will be used for the 
' description property for the domainDNS object.

Const ADS_SECURE_AUTHENTICATION =   1
Const ADS_FAST_BIND             =  32
Const ADS_USE_DELEGATION        = 256

Const DS_INSTANCETYPE_IS_NC_HEAD      = 1
Const DS_INSTANCETYPE_NC_IS_WRITEABLE = 4

Sub CreateApplicationPartitionVBS(  DCADsPath, _
                                    Username, _
                                    Password, _
                                    PartitionPath, _
                                    Description)
    set oNSP = GetObject("LDAP:")

    ' Bind to the specified domain controller. The path must be in the
    ' form "LDAP://<server DNS name>/<partition path>", in most cases, 
    ' the <partition path> will be an invalid path, so ADS_FAST_BIND 
    ' is used to allow the bind to succeed even if the path is 
    ' invalid. ADS_USE_DELEGATION is used to enable the LDAP provider
    ' to use the credentials to contact the Domain Naming FSMO role
    ' holder to create or modify the crossRef object.
    If Username = "" or Username = vbNullString Then
        set oParent = oNSP.OpenDSObject(DCADsPath, _
            vbNullString, _
            vbNullString, _
            ADS_SECURE_AUTHENTICATION Or _
                ADS_FAST_BIND Or _
                ADS_USE_DELEGATION)
    Else
        set oParent = oNSP.OpenDSObject(DCADsPath, _
            Username, _
            Password, _
            ADS_SECURE_AUTHENTICATION Or _
                ADS_FAST_BIND Or _
                ADS_USE_DELEGATION)
    End If
    

    ' Create the domainDNS object.
    set oNewPartition = oParent.Create("domainDNS", PartitionPath)

    ' Set the instanceType property.
    oNewPartition.Put "instanceType", DS_INSTANCETYPE_IS_NC_HEAD Or _
        DS_INSTANCETYPE_NC_IS_WRITEABLE 

    ' Set the description property.
    oNewPartition.Put "description", Description

    ' Commit the new object to the server.
    oNewPartition.SetInfo

    set oNewPartition = Nothing
    set oFalseParent = Nothing
    set oNSP = Nothing
    set oPathName = Nothing
End Sub
```



The following Visual Basic .NET code example shows how to create a new application directory partition using [System.DirectoryServices](/dotnet/api/system.directoryservices).


```VB
Imports System.DirectoryServices

' CreateApplicationPartitionVBNet()
' 
' Description: Creates an application directory partition.
' 
' Parameters:
' 
' DCADsPath - Contains the ADsPath of the partition. This must also 
' contain the DNS name of the domain controller that the partition  
' will be created on. For example, the ADsPath  
' "LDAP://DC01.fabrikam.com/DC=test,DC=com" would cause the partition
' to be created on DC01.fabrikam.com. The distinguished name of the 
' partition will be "<pwszPartitionPath>,DC=test,DC=com".
' 
' Username - Contains the user name to be used for authentication.
' 
' Password - Contains the password to be used for authentication.
' 
' PartitionPath - Contains the relative distinguished name of the 
' partition. This must be in the form of "DC=dynamicdata".
' 
' Description - Contains a string that will be used for the 
' description property for the domainDNS object.

Sub CreateApplicationPartitionVBNet(ByVal DCADsPath As String, 
                                    ByVal Username As String, 
                                    ByVal Password As String, 
                                    ByVal PartitionPath As String, 
                                    ByVal Description As String)
    Dim parent As DirectoryEntry
    Dim domainDNS As DirectoryEntry

    ' Bind to the specified domain controller. The path must be in the 
    ' form "LDAP://<server DNS name>/<partition path>", in most cases, 
    ' the <partition path> will be an invalid path, so  
    ' AuthenticationTypes.FastBind is used to enable the bind to
    ' succeed even if the path is invalid. 
    ' AuthenticationTypes.Delegation is used to enable the LDAP 
    ' provider to use the credentials to contact the Domain Naming
    ' FSMO role holder to create or modify the crossRef object.
    parent = New DirectoryEntry(DCADsPath, _
        Username, _
        Password, _
        AuthenticationTypes.Secure Or _
            AuthenticationTypes.FastBind Or _
            AuthenticationTypes.Delegation)

    ' Create the domainDNS object.
    domainDNS = parent.Children.Add(PartitionPath, "domainDNS")

    ' Set the instanceType property.
    domainDNS.Properties("instanceType").Value = 5

    ' Set the description property.
    domainDNS.Properties("description").Value = Description

    ' Commit the new object to the server.
    domainDNS.CommitChanges()
End Sub
```



The following C# code example shows how to create a new application directory partition using [System.DirectoryServices](/dotnet/api/system.directoryservices).


```CSharp
using System;
using System.DirectoryServices;

/********************************************************************

    CreateApplicationPartitionCS()

    Description: Creates an application directory partition.

    Parameters:

    DCADsPath - Contains the ADsPath of the partition. This must also 
    contain the DNS name of the domain controller that the partition  
    will be created on. For example, the ADsPath 
    "LDAP://DC01.fabrikam.com/DC=test,DC=com" would cause the 
    partition to be created on DC01.fabrikam.com. The distinguished
    name of the partition will be 
    "<pwszPartitionPath>,DC=test,DC=com".

    Username - Contains the user name to be used for authentication.

    Password - Contains the password to be used for authentication.

    PartitionPath - Contains the relative distinguished name of the 
    partition. This must be in the form of "DC=dynamicdata".

    Description - Contains a string that will be used for the 
    description property for the domainDNS object.

*******************************************************************/

static void CreateApplicationPartitionCS(string DCADsPath, 
    string Username, 
    string Password,
    string PartitionPath,
    string Description)
{
    /* 
    Bind to the specified domain controller. The path must be in the
    form "LDAP://<server DNS name>/<partition path>", in most cases, 
    the <partition path> will be an invalid path, so 
    AuthenticationTypes.FastBind is used to enable the bind to 
    succeed even if the path is invalid. 
    AuthenticationTypes.Delegation is used to allow the LDAP 
    provider to use the credentials to contact the Domain Naming
    FSMO role holder to create or modify the crossRef object.
    */
    DirectoryEntry parent = new DirectoryEntry(DCADsPath, 
        Username, 
        Password, 
        AuthenticationTypes.Secure | 
        AuthenticationTypes.FastBind | 
        AuthenticationTypes.Delegation);

    // Create the domainDNS object.
    DirectoryEntry domainDNS = parent.Children.Add(PartitionPath, 
                                                   "domainDNS");

    // Set the instanceType property.
    domainDNS.Properties["instanceType"].Value = 5;

    // Set the description property.
    domainDNS.Properties["description"].Value = Description;

    // Commit the new object to the server.
    domainDNS.CommitChanges();
}
```



 

 