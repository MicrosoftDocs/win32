---
title: Example Code for Reading Attributes
description: The following code example enumerates the properties of the specified user in the current domain, by searching for the user and then using IADsPropertyList to enumerate its properties.
ms.assetid: f5541e9b-e149-4d22-9ff6-a32bd8239f57
ms.tgt_platform: multiple
keywords:
- Example Code for Reading Attributes ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Reading Attributes

The following code example enumerates the properties of the specified user in the current domain, by searching for the user and then using [**IADsPropertyList**](/windows/desktop/api/Iads/nn-iads-iadspropertylist) to enumerate its properties. Be aware that time and date values, as large integers, are handled and how octet strings for **objectSID** and **objectGUID** are handled.


```C++
//  Add adsiid.lib to the project.
//  Add activeds.lib to the project.
//  Add msvcrt.dll to the project.

#include "stdafx.h"
// For the pow function to calculate powers of 2.
#include <windows.h>
#include <ole2.h>
#include <math.h>
#include <wchar.h>
#include <objbase.h>
#include <activeds.h>
#include <atlbase.h>

//  Ensure that you define UNICODE
//  Define version 5 for Windows 2000
#define _WIN32_WINNT 0x0500
//  For SID conversion API.
#include <sddl.h>

//  The EnumeratePropertyValue function
HRESULT EnumeratePropertyValue(IADsPropertyEntry *pEntry)
{
    HRESULT hr = E_FAIL;
    IADsPropertyValue *pValue = NULL;
    IADsLargeInteger *pLargeInt = NULL;
    long lType, lValue;
    BSTR bstr,szString;
    VARIANT var;
    CHAR *pszBOOL = NULL;
    FILETIME filetime;
    SYSTEMTIME systemtime;
    IDispatch *pDisp = NULL;
    DATE date;

    //  For Octet Strings
    void HUGEP *pArray;
    ULONG dwSLBound;
    ULONG dwSUBound;

    VariantInit(&var);
    hr = pEntry->get_Values(&var);
    if (SUCCEEDED(hr))
    {
        //  Should be a safe array that contains variants
        if (var.vt == (VT_VARIANT | VT_ARRAY))
        {
            VARIANT *pVar;
            long lLBound, lUBound;

            hr = SafeArrayAccessData((SAFEARRAY*)(var.pparray), (void HUGEP* FAR*)&pVar);

            //  One-dimensional array. Get the bounds for the array.
            hr = SafeArrayGetLBound((SAFEARRAY*)(var.pparray), 1, &lLBound);
            hr = SafeArrayGetUBound((SAFEARRAY*)(var.pparray), 1, &lUBound);

            //  Get the count of elements.
            long cElements = lUBound-lLBound + 1;

            //  Get the array elements.
            if (SUCCEEDED(hr))
            {
                for (int i = 0; i < cElements; i++ ) 
                {
                    switch (pVar[i].vt)
                    {
                    case VT_BSTR:
                        wprintf(L"%s ", pVar[i].bstrVal);
                        break;

                    case VT_DISPATCH:
                        hr = V_DISPATCH(&pVar[i])->QueryInterface(IID_IADsPropertyValue, (void**)&pValue);
                        if (SUCCEEDED(hr))
                        {
                            hr = pValue->get_ADsType(&lType);
                            switch (lType)
                            {
                            case ADSTYPE_DN_STRING:
                                hr = pValue->get_DNString(&bstr);
                                wprintf(L"%s ",bstr);
                                SysFreeString(bstr);
                                break;

                            case ADSTYPE_CASE_IGNORE_STRING:
                                hr = pValue->get_CaseIgnoreString(&bstr);
                                wprintf(L"%s ",bstr);
                                SysFreeString(bstr);
                                break;

                            case ADSTYPE_BOOLEAN:
                                hr = pValue->get_Boolean(&lValue);
                                pszBOOL = lValue ? "TRUE" : "FALSE";
                                wprintf(L"%s ",pszBOOL);
                                break;

                            case ADSTYPE_INTEGER:
                                hr = pValue->get_Integer(&lValue);
                                wprintf(L"%d ",lValue);
                                break;

                            case ADSTYPE_OCTET_STRING:
                                {
                                    VARIANT varOS;

                                    VariantInit(&varOS);

                                    //  Get the name of the property to handle
                                    //  the required properties.
                                    pEntry->get_Name(&szString);
                                    hr = pValue->get_OctetString(&varOS);

                                    //  Get a pointer to the bytes in the octet string.
                                    if (SUCCEEDED(hr))
                                    {
                                        hr = SafeArrayGetLBound( V_ARRAY(&varOS),
                                            1,
                                            (long FAR *) &dwSLBound );

                                        hr = SafeArrayGetUBound( V_ARRAY(&varOS),
                                            1,
                                            (long FAR *) &dwSUBound );

                                        if (SUCCEEDED(hr))
                                        {
                                            hr = SafeArrayAccessData( V_ARRAY(&varOS), &pArray );
                                        }

                                        if (0==wcscmp(L"objectGUID", szString))
                                        {
                                            LPOLESTR szDSGUID = new WCHAR [39];

                                            //  Cast to LPGUID
                                            LPGUID pObjectGUID = (LPGUID)pArray;

                                            //  Convert GUID to string.
                                            ::StringFromGUID2(*pObjectGUID, szDSGUID, 39); 

                                            //  Print the GUID
                                            wprintf(L"%s ",szDSGUID);
                                        }
                                        else if (0==wcscmp(L"objectSid", szString))
                                        {
                                            PSID pObjectSID = (PSID)pArray;
                                            //  Convert SID to string.
                                            LPOLESTR szSID = NULL;
                                            ConvertSidToStringSid(pObjectSID, &szSID);
                                            wprintf(L"%s ",szSID);
                                            LocalFree(szSID);
                                        }
                                        else
                                        {
                                            wprintf(L"Value of type Octet String. No Conversion.");
                                        }
                                        SafeArrayUnaccessData( V_ARRAY(&varOS) );
                                        VariantClear(&varOS);
                                    }

                                    SysFreeString(szString);
                                }
                                break;

                            case ADSTYPE_UTC_TIME:
                                //  wprintf(L"Value of type UTC_TIME\n");
                                hr = pValue->get_UTCTime(&date);
                                if (SUCCEEDED(hr)) 
                                {
                                    VARIANT varDate;

                                    //  Pack in variant.vt
                                    varDate.vt = VT_DATE;
                                    varDate.date = date;

                                    VariantChangeType(&varDate, &varDate, VARIANT_NOVALUEPROP, VT_BSTR);
                                    wprintf(L"%s ",varDate.bstrVal);
                                    VariantClear(&varDate);
                                }
                                break;

                            case ADSTYPE_LARGE_INTEGER:
                                //  wprintf(L"Value of type Large Integer\n");
                                //  Get the name of the property to handle
                                //  the required properties.
                                pEntry->get_Name(&szString);
                                hr = pValue->get_LargeInteger(&pDisp);
                                if (SUCCEEDED(hr))
                                {
                                    hr = pDisp->QueryInterface(IID_IADsLargeInteger, (void**)&pLargeInt);
                                    if (SUCCEEDED(hr))
                                    {
                                        hr = pLargeInt->get_HighPart((long*)&filetime.dwHighDateTime);
                                        hr = pLargeInt->get_LowPart((long*)&filetime.dwLowDateTime);
                                        if((filetime.dwHighDateTime==0) && (filetime.dwLowDateTime==0))
                                        {
                                            wprintf(L"No Value ");
                                        }
                                        else
                                        {
                                            //  Verify properties of type LargeInteger that represent time
                                            //  if TRUE, then convert to variant time.
                                            if ((0==wcscmp(L"accountExpires", szString))||
                                                (0==wcscmp(L"badPasswordTime", szString))||
                                                (0==wcscmp(L"lastLogon", szString))||
                                                (0==wcscmp(L"lastLogoff", szString))||
                                                (0==wcscmp(L"lockoutTime", szString))||
                                                (0==wcscmp(L"pwdLastSet", szString))
                                                )
                                            {
                                                //  Handle special case for Never Expires where low part is -1.
                                                if (filetime.dwLowDateTime==-1)
                                                {
                                                    wprintf(L"Never Expires ");
                                                }
                                                else
                                                {
                                                    if (FileTimeToLocalFileTime(&filetime, &filetime) != 0) 
                                                    {
                                                        if (FileTimeToSystemTime(&filetime, &systemtime) != 0)
                                                        {
                                                            if (SystemTimeToVariantTime(&systemtime, &date) != 0) 
                                                            {
                                                                VARIANT varDate;

                                                                //  Pack in variant.vt
                                                                varDate.vt = VT_DATE;
                                                                varDate.date = date;

                                                                VariantChangeType(&varDate, &varDate, VARIANT_NOVALUEPROP, VT_BSTR);

                                                                wprintf(L"%s ",varDate.bstrVal);

                                                                VariantClear(&varDate);
                                                            }
                                                            else
                                                            {
                                                                wprintf(L"FileTimeToVariantTime failed ");
                                                            }
                                                        }
                                                        else
                                                        {
                                                            wprintf(L"FileTimeToSystemTime failed ");
                                                        }

                                                    }
                                                    else
                                                    {
                                                        wprintf(L"FileTimeToLocalFileTime failed ");
                                                    }
                                                }
                                            }
                                            //  Print the LargeInteger.
                                            else
                                            {
                                                wprintf(L"Large Integer: high: %d low: %d ",filetime.dwHighDateTime, filetime.dwLowDateTime);
                                            }
                                        }
                                    }
                                    if (pLargeInt)
                                        pLargeInt->Release();
                                }
                                else
                                {
                                    wprintf(L"Cannot get Large Integer");
                                }

                                if (pDisp)
                                    pDisp->Release();

                                break;

                            case ADSTYPE_NT_SECURITY_DESCRIPTOR:
                                wprintf(L"Value of type NT Security Descriptor ");
                                break;

                            case ADSTYPE_PROV_SPECIFIC:
                                wprintf(L"Value of type Provider Specific ");
                                break;

                            default:
                                wprintf(L"Unhandled ADSTYPE for property value: %d ",lType);
                                break;
                            }
                        }
                        else
                        {
                            wprintf(L"QueryInterface failed for IADsPropertyValue. HR: %x\n", hr);
                        }

                        if (pValue)
                        {
                            pValue->Release();
                        }
                        break;

                    default:
                        wprintf(L"Unhandled Variant type for property value array: %d\n",pVar[i].vt);
                        break;
                    }
                }
                wprintf(L"\n");
            }

            //  Decrement the access count for the array.
            SafeArrayUnaccessData((SAFEARRAY*)(var.pparray));
        }

        VariantClear(&var);
    }

    return hr;
}

//  The GetUserProperties function gets a property list for a user.
HRESULT GetUserProperties(IADs *pObj)
{
    HRESULT hr = E_FAIL;
    LPOLESTR szDSPath = new OLECHAR [MAX_PATH];
    long lCount = 0L;
    long lCountTotal = 0L;
    long lPType = 0L;

    if (!pObj)
    {
        return E_INVALIDARG;
    }

    //  Call GetInfo to load all object properties into the cache
    //  because IADsPropertyList methods read from the cache.
    hr = pObj->GetInfo();
    if (SUCCEEDED(hr))
    {
        IADsPropertyList *pObjProps = NULL;

        //  QueryInterface for an IADsPropertyList pointer.
        hr = pObj->QueryInterface(IID_IADsPropertyList, (void**)&pObjProps);
        if (SUCCEEDED(hr))
        {
            VARIANT var;

            //  Enumerate the properties of the object.
            hr = pObjProps->get_PropertyCount(&lCountTotal);
            wprintf(L"Property Count: %d\n",lCountTotal);

            VariantInit(&var);
            hr = pObjProps->Next(&var);
            if (SUCCEEDED(hr))
            {
                lCount = 1L;
                while (hr == S_OK)
                {
                    if (var.vt == VT_DISPATCH)
                    {
                        IADsPropertyEntry *pEntry = NULL;

                        hr = V_DISPATCH(&var)->QueryInterface(IID_IADsPropertyEntry, (void**)&pEntry);
                        if (SUCCEEDED(hr))
                        {
                            BSTR bstrString;

                            hr = pEntry->get_Name(&bstrString);
                            wprintf(L"%s: ", bstrString);
                            SysFreeString(bstrString);

                            hr = pEntry->get_ADsType(&lPType);
                            if (lPType != ADSTYPE_INVALID)
                            {
                                hr = EnumeratePropertyValue(pEntry);
                                if(FAILED(hr))
                                {
                                    printf("EnumeratePropertyValue failed. hr: %x\n",hr);
                                }
                            }
                            else
                            {
                                wprintf(L"Invalid type\n");
                            }
                        }
                        else
                        {
                            printf("IADsPropertyEntry QueryInterface call failed. hr: %x\n",hr);
                        }

                        // Cleanup.
                        if (pEntry)
                        {
                            pEntry->Release();
                        }
                    }
                    else
                    {
                        printf("Unexpected returned type for VARIANT: %d",var.vt);
                    }
                    VariantClear(&var);
                    hr = pObjProps->Next(&var);
                    if (SUCCEEDED(hr))
                    {
                        lCount++;
                    }
                }
            }
            //  Cleanup.
            pObjProps->Release();
        }

        wprintf(L"Total properties retrieved: %d\n",lCount); 
    }

    //  Return S_OK if all properties were retrieved.
    if (lCountTotal == lCount)
    {
        hr = S_OK;
    }

    return hr;
}


//  The FindUserByName function searches for users.
#define NUM_ATTRIBUTES 1

HRESULT FindUserByName(IDirectorySearch *pSearchBase, //  Container to search.
    LPOLESTR szFindUser, //  Name of user to find.
    IADs **ppUser) //  Return a pointer to the user.
{
    if ((!pSearchBase) || (!szFindUser))
    {
        return E_INVALIDARG;
    }

    HRESULT hrObj = E_FAIL;
    HRESULT hr = E_FAIL;
    ADS_SEARCHPREF_INFO SearchPrefs;
    //  COL for iterations
    ADS_SEARCH_COLUMN col;
    //  Handle used for searching
    ADS_SEARCH_HANDLE hSearch;

    //  Search entire subtree from root.
    SearchPrefs.dwSearchPref = ADS_SEARCHPREF_SEARCH_SCOPE;
    SearchPrefs.vValue.dwType = ADSTYPE_INTEGER;
    SearchPrefs.vValue.Integer = ADS_SCOPE_SUBTREE;

    //  Set the search preference.
    DWORD dwNumPrefs = 1;
    hr = pSearchBase->SetSearchPreference(&SearchPrefs, dwNumPrefs);
    if (FAILED(hr))
    {
        return hr;
    }

    //  Create search filter.
    LPWSTR pszFormat = L"(&(objectCategory=person)(objectClass=user)(cn=%s))";
    LPWSTR pszSearchFilter = new WCHAR[wcslen(pszFormat) + wcslen(szFindUser) + 1];
    if(NULL == pszSearchFilter)
    {
        return E_OUTOFMEMORY;
    }

#ifdef _MBCS
    swprintf_s(pszSearchFilter, pszFormat, szFindUser);
#endif _MBCS

    //  Set attributes to return.
    LPWSTR pszAttribute[NUM_ATTRIBUTES] = {L"ADsPath"};

    //  Execute the search.
    hr = pSearchBase->ExecuteSearch(pszSearchFilter,
                                    pszAttribute,
                                    NUM_ATTRIBUTES,
                                    &hSearch);
    if (SUCCEEDED(hr))
    {    
        //  Call IDirectorySearch::GetNextRow() to retrieve the next row of data.
        while(pSearchBase->GetNextRow(hSearch) != S_ADS_NOMORE_ROWS)
        {
            //  Loop through the array of passed column names and
            //  print the data for each column.
            for (DWORD x = 0; x < NUM_ATTRIBUTES; x++)
            {
                //  Get the data for this column.
                hr = pSearchBase->GetColumn(hSearch, pszAttribute[x], &col);
                if (SUCCEEDED(hr))
                {
                    //  Print the data for the column and free the column.
                    //  Be aware that the requested attribute is type CaseIgnoreString.
                    if (ADSTYPE_CASE_IGNORE_STRING == col.dwADsType)
                    {
                        hr = ADsOpenObject( col.pADsValues->CaseIgnoreString,
                            NULL,
                            NULL,
                            ADS_SECURE_AUTHENTICATION,
                            IID_IADs,
                            (void**)ppUser);
                        if (SUCCEEDED(hr))
                        {
                            wprintf(L"Found User.\n",szFindUser); 
                            wprintf(L"%s: %s\r\n",pszAttribute[x],col.pADsValues->CaseIgnoreString); 
                            hrObj = S_OK;
                        }
                    }

                    pSearchBase->FreeColumn( &col );
                }
                else
                {
                    hr = E_FAIL;
                }
            }
        }
        //  Close the search handle to cleanup.
        pSearchBase->CloseSearchHandle(hSearch);
    }

    delete pszSearchFilter;

    if (FAILED(hrObj))
    {
        hr = hrObj;
    }

    return hr;
}

//  Entry point for the application.
#define BUFFER_SIZE (MAX_PATH * 2)

void wmain(int argc, wchar_t *argv[])
{
    //  Handle the command line arguments.
    WCHAR szBuffer[BUFFER_SIZE];
    if (argv[1] == NULL)
    {
        wprintf(L"This program finds a user in the current Windows 2000 domain\n");
        wprintf(L"and displays its properties.\n");
        wprintf(L"Enter Common Name of the user to find:");
        fgetws(szBuffer, BUFFER_SIZE, stdin);
    }
    else
    {
        wcsncpy_s(szBuffer, argv[1], BUFFER_SIZE);
    }

    //  If the string is empty, then exit.
    if (0==wcscmp(L"", szBuffer))
    {
        return;
    }

    wprintf(L"\nFinding user: %s...\n", szBuffer);

    //  Initialize COM.
    CoInitialize(NULL);
    HRESULT hr = S_OK;

    //  Get rootDSE and the domain container DN.
    IADs *pObject = NULL;
    IDirectorySearch *pDS = NULL;
    LPOLESTR szPath = new OLECHAR[MAX_PATH];
    hr = ADsOpenObject(L"LDAP://rootDSE",
        NULL,
        NULL,
        ADS_SECURE_AUTHENTICATION, //  Use Secure Authentication.
        IID_IADs,
        (void**)&pObject);
    if(SUCCEEDED(hr))
    {
        VARIANT var;
        VariantInit(&var);
        hr = pObject->Get(CComBSTR(L"defaultNamingContext"), &var);
        if (SUCCEEDED(hr))
        {
#ifdef _MBCS
            wcscpy_s(szPath, L"LDAP://");
            wcscat_s(szPath, var.bstrVal);
            VariantClear(&var);
#endif _MBCS
            if (pObject)
            {
                pObject->Release();
                pObject = NULL;
            }

            //  Bind to the root of the current domain.
            hr = ADsOpenObject(szPath,
                NULL,
                NULL,
                ADS_SECURE_AUTHENTICATION, //  Use Secure Authentication.
                IID_IDirectorySearch,
                (void**)&pDS);
            if (SUCCEEDED(hr))
            {
                hr =  FindUserByName(pDS, //  Container to search
                    szBuffer,   //  Name of user to find
                    &pObject); //  Return a pointer to the user
                if (SUCCEEDED(hr))
                {
                    wprintf (L"----------------------------------------------\n");
                    wprintf (L"--------Call GetUserProperties-----------\n");
                    hr = GetUserProperties(pObject);
                    wprintf (L"GetUserProperties HR: %x\n", hr);
                }
                else
                {
                    wprintf(L"User \"%s\" not Found.\n", szBuffer);
                    wprintf (L"FindUserByName failed with the following HR: %x\n", hr);
                }

                pDS->Release();
            }

            pObject->Release();
        }
    }         

    //  Uninitialize COM.
    CoUninitialize();

    return;
}
```



The following Visual Basic code example shows how to get the properties of a user object. To use this code example, create a reference to the Active DS Type Library and the Microsoft ActiveX Data Objects Library in your Visual Basic project.


```VB
Const ADS_SCOPE_BASE = 0
Const ADS_SCOPE_ONELEVEL = 1
Const ADS_SCOPE_SUBTREE = 2

Const ADS_CHASE_REFERRALS_NEVER = 0
Const ADS_CHASE_REFERRALS_SUBORDINATE = &H20
Const ADS_CHASE_REFERRALS_EXTERNAL = &H40
Const ADS_CHASE_REFERRALS_ALWAYS = ADS_CHASE_REFERRALS_SUBORDINATE Or ADS_CHASE_REFERRALS_EXTERNAL

Dim sUserName As String
Dim sMsg As String
Dim sSearchFilter As String
Dim lScope As Integer
Dim iIndex As Integer
iIndex = 0
Dim v, j, i
Dim rootDSE As IADs
Dim con As New Connection, rs As New Recordset
Dim Com As New Command
Dim oIADs As IADs
Dim sObjectDN As String
Dim sUserADsPath As String

sMsg = "This script enumerates the properties of a user on a domain."
sMsg = sMsg & vbCrLf & vbCrLf & "Specify the name of the user:"
sUserName = InputBox(sMsg)

If sUserName = "" Then
   Exit Sub
End If

' Bind to the Active Directory with the RootDSE object.
Set rootDSE = GetObject("LDAP://RootDSE")
sObjectDN = "LDAP://" & rootDSE.Get("defaultNamingContext")
Set rootDSE = Nothing
Set oIADs = GetObject(sObjectDN)

' Search for entries with the specified name.
sSearchFilter = "CN='" & sUserName & "'"

' Open a Connection object.
con.Provider = "ADsDSOObject"

' Open the connection.
con.Open "Active Directory Provider"

' Create a command object on this connection.
Set Com.ActiveConnection = con

' Set the query string using SQL Dialect.
sMsg = "select name,AdsPath from '" & oIADs.ADsPath
sMsg = sMsg & "' where " & sSearchFilter & " ORDER BY NAME"
Com.CommandText = sMsg

' Notify the user of what the search filter is.
' MsgBox "Search Filter = " & Com.CommandText

'---------------------------------------------------
' Or you can use LDAP Dialect, for example,
'---------------------------------------------------
' Ex Com.CommandText="<LDAP://ldapsvr/dc=Fabrikam,DC=com>;(objectClass=*);name"
' For LDAP Dialect, the valid search scope are base, oneLevel and subtree
' Com.CommandText = "<" & adDomainPath & ">;(objectClass=*);name;subtree"
' For LDAP Dialect (<LDAP:...>), cannot specify sort order in the string,
' However, you can use this SORT ON property to specify sort order.
' for SQL Dialect you can use ORDER BY in the SQL Statement
' Ex. Com.Properties("Sort On") = "Name"

' Set the preferences for Search
Com.Properties("Page Size") = 1000
Com.Properties("Timeout") = 30 'seconds
Com.Properties("searchscope") = ADS_SCOPE_SUBTREE
Com.Properties("Chase referrals") = ADS_CHASE_REFERRALS_EXTERNAL

' Do not cache the result, it results in less memory requirements.
Com.Properties("Cache Results") = False
Com.Properties("Size Limit") = 1 ' Limit to 1 Result

' Execute the query.
Set rs = Com.Execute

' Navigate the record set.
If Not rs.EOF Then
   rs.MoveFirst
End If

On Error Resume Next
If Not rs.EOF Then
   ' Display the LDAP path for the row.
   MsgBox "Found the user " & sUserName & " at " & rs.Fields("AdsPath")
   sUserADsPath = rs.Fields("AdsPath")
   rs.MoveNext
Else
   MsgBox "Cannot find user name " & sUserName & " in the directory"
   Exit Sub
End If

Set ds = Nothing
Set con = Nothing
Set rs = Nothing
Set Com = Nothing
Set oIADs = Nothing

' Now, enumerate the properties
Dim propList As IADsPropertyList
Dim propEnty As IADsPropertyEntry
Dim propVal As IADsPropertyValue
Dim count As Long

Dim sOutput As String
Dim currentcount As Long

Const NumToDisplayAtAtime As Integer = 10

' Bind to the user.
Set propList = GetObject(sUserADsPath)

' Put the properties into the cache.
propList.GetInfo

count = propList.PropertyCount
sOutput = "No of Property Found: " & Str(count) & vbCrLf & vbCrLf

For i = 0 To count - 1
   currentcount = currentcount + 1
   ' Each item in property list has a property entry
   Set propEntry = propList.Item(i)

   ' Append to outputstring.
   sOutput = sOutput & "PROPERTYENTRY NAME:" & propEntry.Name
   sOutput = sOutput & vbCrLf & " ------" & vbCrLf

   ' Each value in property entry has property values

   For Each v In propEntry.Values
      Set propVal = v
      ' Append to outputstring.
      sOutput = sOutput & propVal.CaseIgnoreString & vbCrLf
   Next

   If currentcount = NumToDisplayAtAtime Then
      MsgBox sOutput
      sOutput = ""
      currentcount = 0
   End If
Next

Set propList = Nothing
Set propEnty = Nothing
Set propVal = Nothing
```



 

 




