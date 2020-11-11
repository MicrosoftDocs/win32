---
title: Example Code for Deleting an Application Directory Partition
description: This topic includes code examples used to delete an application directory partition.
ms.assetid: 74eb46a1-9300-452a-86b6-a19aff58a4f0
ms.tgt_platform: multiple
keywords:
- example code for deleting an application directory partition Active Directory
- application directory partitions Active Directory , example code for deleting
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Deleting an Application Directory Partition

The following C++ code example can be used to delete an application directory partition using ADSI. This example uses one of the **GetPartitionsDN\*** example functions described in [Example Code for Locating the Partitions Container](example-code-for-locating-the-partitions-container.md).


```C++
/********************************************************************

    GetCrossRefDNFromPartitionDN()

    Description: Gets the distinguished name of the crossRef object 
    that represents the specified application directory partition.

    Parameters:

    pwszPartitionDN - Contains the distinguished name of the 
    application directory partition for which to find the crossRef 
    object.

    pwszUsername - Contains the user name to be used for 
    authentication.

    pwszPassword - Contains the password to be used for 
    authentication.

    ppwszCrossRefDN - Pointer to an LPWSTR that receives the 
    distinguished name string. The caller must free this memory 
    with FreeADsMem when it is no longer required.

********************************************************************/

HRESULT GetCrossRefDNFromPartitionDN(LPCWSTR pwszPartitionDN,
                                     LPCWSTR pwszUsername, 
                                     LPCWSTR pwszPassword, 
                                     LPWSTR *ppwszCrossRefDN)
{
    *ppwszCrossRefDN = NULL;
    
    HRESULT hr;
    LPWSTR pwszPartitionsDN;

    // Get the distinguished name of the Partitions container.
    hr = GetPartitionsDN(&pwszPartitionsDN);
    if(SUCCEEDED(hr))
    {
      /*
      Search the Partitions container for an object that is of
      type crossRef and has an nCName that matches the distinguished 
      name of the partition. This will be the crossRef object that 
      represents the partition and the one to delete.
      */
      IDirectorySearch *pdsPartitions;

      CComBSTR sbstrADsPath = "LDAP://";
      sbstrADsPath += pwszPartitionsDN;

      // Bind to the Partitions container.
      hr = ADsOpenObject( sbstrADsPath,
                          pwszUsername,
                          pwszPassword,
                          ADS_SECURE_AUTHENTICATION,
                          IID_IDirectorySearch, 
                          (LPVOID*)&pdsPartitions);
      if(SUCCEEDED(hr))
      {
        ADS_SEARCHPREF_INFO SearchPref[1];

        // Set the search scope.
        SearchPref[0].dwSearchPref = ADS_SEARCHPREF_SEARCH_SCOPE;
        SearchPref[0].vValue.dwType = ADSTYPE_INTEGER;
        SearchPref[0].vValue.Integer = ADS_SCOPE_ONELEVEL;
            
        hr = pdsPartitions->SetSearchPreference(
              SearchPref, 
              sizeof(SearchPref)/sizeof(ADS_SEARCHPREF_INFO)
             );
        if(SUCCEEDED(hr))
        {
          ADS_SEARCH_HANDLE hSearch = NULL;
          LPWSTR pwszAttributes[1] = {L"distinguishedName"};
              
          CComBSTR sbstrSearchFilter;
          sbstrSearchFilter = "(&(objectClass=crossRef)(nCName=";
          sbstrSearchFilter += pwszPartitionDN;
          sbstrSearchFilter += "))";

          // Execute the search.
          hr = pdsPartitions->ExecuteSearch(
                sbstrSearchFilter, 
                pwszAttributes, 
                sizeof(pwszAttributes)/sizeof(LPWSTR), 
                &hSearch
               );
          if(SUCCEEDED(hr))
          {
            // Get the first result row. There should never be more
            // than one result.
            hr = pdsPartitions->GetFirstRow(hSearch);
            if(S_OK == hr)
            {
              ADS_SEARCH_COLUMN col;

              // Get the search result. The distinguishedName 
              // attribute will be a string.
              hr = pdsPartitions->GetColumn(hSearch,
                                            pwszAttributes[0], 
                                            &col);
              if(SUCCEEDED(hr))
              {
                // Allocate and copy the returned
                // distinguished name buffer.
                DWORD dwChars = 
                  lstrlenW(col.pADsValues[0].DNString) + 1;
                            
                *ppwszCrossRefDN = 
                   (LPWSTR)AllocADsMem(dwChars * 
                                       sizeof(WCHAR));
                            
                if(*ppwszCrossRefDN)
                {
                   wcsncpy_s(*ppwszCrossRefDN, 
                             col.pADsValues[0].DNString,
                             dwChars);
                }
                else
                {
                   hr = E_OUTOFMEMORY;
                }

                // Free the column.
                pdsPartitions->FreeColumn(&col);
              }
            }
            else
            {
               hr = HRESULT_FROM_WIN32(ERROR_NOT_FOUND);
            }
                    
            // Close the search handle to cleanup.
            pdsPartitions->CloseSearchHandle(hSearch);
          }
        }
      }
        
      FreeADsMem(pwszPartitionsDN);
    }

    return hr;
}

/********************************************************************

    DeleteAppPartition()

    Description - Deletes an application directory partition by
    finding the crossRef object for the partition and then deleting 
    the crossRef object.

********************************************************************/

HRESULT DeleteAppPartition( LPCWSTR pwszPartitionDN, 
                            LPCWSTR pwszUsername, 
                            LPCWSTR pwszPassword)
{
    LPWSTR pwszCrossRefDN;
    HRESULT hr;
        
    // Get the distinguished name of the crossRef object.
    hr = GetCrossRefDNFromPartitionDN(pwszPartitionDN, 
        pwszUsername, 
        pwszPassword, 
        &pwszCrossRefDN);

    if(SUCCEEDED(hr))
    {
        CComBSTR sbstrADsPath;
        IADsDeleteOps *pDelete;

        // Bind to the crossRef object and delete it.
        sbstrADsPath = "LDAP://";
        sbstrADsPath += pwszCrossRefDN;
        hr = ADsOpenObject( sbstrADsPath,
                            NULL,
                            NULL,
                            ADS_SECURE_AUTHENTICATION,
                            IID_IADsDeleteOps, 
                            (LPVOID*)&pDelete);
        if(SUCCEEDED(hr))
        {
            hr = pDelete->DeleteObject(0);
            
            pDelete->Release();
        }
        
        FreeADsMem(pwszCrossRefDN);
    }

    return hr;
}
```



The following Visual Basic Scripting Edition code example can be used to delete an application directory partition using ADSI. This example uses one of the **GetPartitionsDN\*** example functions described in [Example Code for Locating the Partitions Container](example-code-for-locating-the-partitions-container.md).


```VB
Const ADS_SECURE_AUTHENTICATION = 1

'
'   GetCrossRefDNFromPartitionDN()
'
'   Description: Gets the distinguished name of the crossRef object 
'   that represents the specified application directory partition.
'
'Parameters:
'
'   PartitionDN - Contains the distinguished name of the application
'   directory partition for which to find the crossRef object.
'
'   Username - Contains the user name to be used for authentication.
'
'   Password - Contains the password to be used for authentication.
'
Function GetCrossRefDNFromPartitionDN(PartitionDN, Username, Password)
    ' Search the Partitions container for an object that is of type 
    ' crossRef and has an nCName that matches the distinguished name 
    ' of the partition. This will be the crossRef object that represents 
    ' the partition.
    
    partitionsDN = GetPartitionsDN()
    
    commandString = "<LDAP://" + partitionsDN + ">;(&(objectClass=crossRef)(nCName=" + PartitionDN + "));distinguishedName;onelevel"
    
    Set oConn = CreateObject("ADODB.Connection")
    Set oComm = CreateObject("ADODB.Command")
     
    oConn.Provider = "ADsDSOObject"

    ' Set the binding options for the search.
    oConn.Properties("ADSI Flag") = ADS_SECURE_AUTHENTICATION
    
    If Username <> vbNullString And Username <> "" Then
        oConn.Properties("User ID") = strUsername
        oConn.Properties("Password") = strPassword
    End If
    
    oConn.Open
    oComm.ActiveConnection = oConn
    
    oComm.CommandText = commandString
    
    ' Execute the query.
    Set oResults = oComm.Execute
    
    ' Get the first result. This should be the only result.
    Set oField = oResults(0)
    
    GetCrossRefDNFromPartitionDN = oField.Value
End Function

'
'   DeleteAppPartition()
'
'   Description: Deletes the specified application directory 
'   partition.
'
'Parameters:
'
'   PartitionDN - Contains the distinguished name of the 
'   application directory partition to delete.
'
'   Username - Contains the user name to be used for authentication.
'
'   Password - Contains the password to be used for authentication.
'
Sub DeleteAppPartition(PartitionDN, Username, Password)
    ' Get the distinguished name of the crossRef object that 
    ' represents the application directory partition.
    CrossRefADsPath = "LDAP://" + GetCrossRefDNFromPartitionDN(PartitionDN, Username, Password)
    
    Set oNSP = GetObject("LDAP:")
    
    ' Bind to the crossRef object.
    If Username = "" Then
        Set oCrossRef = GetObject(CrossRefADsPath)
    Else
        Set oCrossRef = oNSP.OpenDSObject(CrossRefADsPath, _
            Username, _
            Password, _
            ADS_SECURE_AUTHENTICATION)
    End If
    
    ' Delete the crossRef object using IADsDeleteOps.DeleteObject().
    oCrossRef.DeleteObject(0)
End Sub
```



The following C# code example can be used to delete an application directory partition using [System.DirectoryServices](/dotnet/api/system.directoryservices). This example uses one of the **GetPartitionsDN\*** example functions described in [Example Code for Locating the Partitions Container](example-code-for-locating-the-partitions-container.md).


```CSharp
/********************************************************************

    GetCrossRefDNFromPartitionDN()

    Description: Gets the distinguished name of the crossRef object 
    that represents the specified application directory partition.

    Parameters:

    PartitionDN - Contains the distinguished name of the application 
    directory partition for which to find the crossRef object.

    Username - Contains the user name to be used for authentication.

    Password - Contains the password to be used for authentication.

********************************************************************/

static string GetCrossRefDNFromPartitionDN(
    string PartitionPath, 
    string Username, 
    string Password)
{
    string PartitionsDN = GetPartitionsDN();

    /*
    Search the Partitions container for an object that is of type crossRef 
    application and has an nCName that matches the distinguished name  
    of the partition. This will be the crossRef object that represents 
    the partition and the one to delete.
    */
    DirectoryEntry PartitionsContainer = 
      new DirectoryEntry("LDAP://" + PartitionsDN, 
                         Username, 
                         Password, 
                         AuthenticationTypes.Secure);
    DirectorySearcher PartitionsSearcher = 
      new DirectorySearcher(PartitionsContainer);
    
    // Build the search filter.
    PartitionsSearcher.Filter = "(&(objectClass=crossRef)(nCName=";
    PartitionsSearcher.Filter += PartitionPath;
    PartitionsSearcher.Filter += "))";
    
    // Request the distinguishedName.
    PartitionsSearcher.PropertiesToLoad.Add("distinguishedName");

    // Search only one level.
    PartitionsSearcher.SearchScope = SearchScope.OneLevel;

    SearchResult result = PartitionsSearcher.FindOne();
    return result.Properties["distinguishedName"][0].ToString();
}

/********************************************************************

    DeleteAppPartition()

    Description: Deletes an application directory partition.

********************************************************************/

static void DeleteAppPartition(
    string PartitionPath, 
    string Username, 
    string Password)
{
    /*
    Get the distinguished name of the crossRef object that represents
    the specified application directory partition.
    */
    string CrossRefDN = GetCrossRefDNFromPartitionDN(PartitionPath, 
                                                     Username,
                                                     Password);

    // Bind to the crossRef object.
    DirectoryEntry Partition = 
      new DirectoryEntry("LDAP://" + CrossRefDN, 
                         Username, 
                         Password, 
                         AuthenticationTypes.Secure);
    
    // Delete the crossRef object.
    /*
    To avoid a problem in DirectoryEntry.DeleteTree(), it is necessary
    to access a property value before calling DeleteTree(). If this is
    not done, DeleteTree() will fail.
    */
    object CommonName = Partition.Properties["cn"].Value;
    Partition.DeleteTree();
}
```



The following Visual Basic .NET code example can be used to delete an application directory partition using [System.DirectoryServices](/dotnet/api/system.directoryservices). This example uses one of the **GetPartitionsDN\*** example functions described in [Example Code for Locating the Partitions Container](example-code-for-locating-the-partitions-container.md).


```VB
'********************************************************************
'
'   GetCrossRefDNFromPartitionDN()
'
'   Description: Gets the distinguished name of the crossRef object 
'   that represents the specified application directory partition.
'
'   Parameters:
'
'   PartitionDN - Contains the distinguished name of the application 
'   directory partition for which to find the crossRef object.
'
'   Username - Contains the user name to be used for authentication.
'
'   Password - Contains the password to be used for authentication.
'
'*********************************************************************

Function GetCrossRefDNFromPartitionDN(ByVal PartitionPath As String, _
        ByVal Username As String, _
        ByVal Password As String) _
        As String
    Dim PartitionsDN As String
    PartitionsDN = GetPartitionsDN()

    ' Search the Partitions container for an object that is of type 
    ' crossRef and has an nCName that matches the distinguished name of 
    ' the partition. This will be the crossRef object that represents  
    ' the partition and the one to delete.

    Dim Path As String = "LDAP://" + PartitionsDN
    Dim PartitionsContainer _
        As New DirectoryEntry(Path, _
                              Username, _
                              Password, _
                              AuthenticationTypes.Secure)
    Dim PartitionsSearcher _
        As New DirectorySearcher(PartitionsContainer)

    ' Set the search filter.
    PartitionsSearcher.Filter = "(&(objectClass=crossRef)(nCName="
    PartitionsSearcher.Filter += PartitionPath
    PartitionsSearcher.Filter += "))"

    ' Retrieve the distinguishedName property.
    PartitionsSearcher.PropertiesToLoad.Add("distinguishedName")

    ' Search only one level.
    PartitionsSearcher.SearchScope = SearchScope.OneLevel

    ' Perform the search.
    Dim result As SearchResult = PartitionsSearcher.FindOne()

    ' Form and return the distinguished name of the crossRef object.
    Return result.Properties("distinguishedName")(0).ToString()
End Function

'********************************************************************
'
'   DeleteAppPartition()
'
'   Description: Deletes an application directory partition.
'
'********************************************************************

Sub DeleteAppPartition(ByVal PartitionPath As String, _
        ByVal Username As String, _
        ByVal Password As String)
    ' Get the distinguished name of the crossRef object that 
    ' represents the specified application directory partition.
    Dim CrossRefDN _
       As String = GetCrossRefDNFromPartitionDN(PartitionPath, _
                                                Username, _
                                                Password)

    ' Bind to the crossRef object.
    Dim Path As String = "LDAP://" + CrossRefDN
    Dim Partition As New DirectoryEntry(Path, _
                                        Username, _
                                        Password, _
                                        AuthenticationTypes.Secure)

    ' Delete the crossRef object.
    ' To avoid a problem in DirectoryEntry.DeleteTree(), it is necessary to 
    ' access a property value before calling DeleteTree(). If this is not 
    ' done, DeleteTree() will fail.
    Dim CommonName As Object = Partition.Properties("cn").Value
    Partition.DeleteTree()
End Sub
```



 

 