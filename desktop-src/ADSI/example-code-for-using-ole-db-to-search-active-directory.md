---
title: Example Code for Using OLE DB to Search Active Directory
description: The following code example shows how to search Active Directory using C++, COM, and OLE DB.
ms.assetid: 71812a4b-5e27-4389-b949-3d96c87b222d
ms.tgt_platform: multiple
keywords:
- Example Code for Using OLE DB to Search Active Directory ADSI
- ADSI ADSI , example code C/C++ , using OLE DB to access Active Directory
- queries ADSI , searching with OLE DB, example code for using OLE DB to access Active Directory
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Using OLE DB to Search Active Directory

The following code example shows how to search Active Directory using C++, COM, and OLE DB. This is an example of a function that takes the distinguished name of the container to search under and the credentials to use for the search. The example will perform a subtree search under the specified container for all objects that have an **objectClass** of "user". The example will print the **name** and **ADsPath** attributes of each user to the console window.

There are two query dialects that can be used with the ADSI OLE DB provider, LDAP and SQL. The dialect is specified in the [ICommandText::SetCommandText](/previous-versions/windows/desktop/ms709757(v=vs.85)) method with one of the following GUIDs:

-   **DBGUID\_SQL** for the SQL dialect.
-   **DBGUID\_LDAPDialect** for the LDAP dialect.

This example uses the LDAP dialect.

The [ICommandText::SetCommandText](/previous-versions/windows/desktop/ms709757(v=vs.85)) method can also accept the **DBGUID\_DEFAULT** GUID for the dialect. In this case, ADSI will attempt to use the SQL dialect first; if that fails, ADSI will attempt to use the LDAP dialect. For more information, see [LDAP dialect](ldap-dialect.md) and [SQL dialect](sql-dialect.md).

For more information about OLE DB, see the OLE DB Programmer's Guide.



```C++

//********************************************************************
//    #include statements
//********************************************************************

#include <atlbase.h>
#include <oledb.h>
#include <adsiid.h>
#include <oledberr.h>

//********************************************************************
//    function prototypes
//********************************************************************

void PrintRowData(DBBINDING *rgBind, 
                  DBCOLUMNINFO *pDBColumnInfo, 
                  ULONG ulNumColsBind, 
                  BYTE *pData);

//********************************************************************
//    global variables and definitions
//********************************************************************

typedef struct 
{
    DBLENGTH dwLength;
    DBSTATUS dwStatus;
    BYTE bData[1];
}DBCOLUMNDATA, *PDBCOLUMNDATA;

#define NUMROWS_CHUNK 500

/*********************************************************************

    PrintAllUsers()

*********************************************************************/

HRESULT PrintAllUsers(LPCWSTR pwszDN, 
                      LPCWSTR pwszUsername, 
                      LPCWSTR pwszPassword)
{
    HRESULT hr;
    DBCOLUMNINFO *rgDBColumnInfo = NULL;
    LPWSTR pStringsBuffer = NULL;
    DBBINDING *rgBind = NULL;
    CComPtr<IDBInitialize> spDBInitialize;
    CComPtr<IDBProperties> spDBProperties;
    DBPROP InitProperties[3];
    CComBSTR sbstrUsername;
    CComBSTR sbstrPassword;
    DBPROPSET InitPropSet;
    CComPtr<IDBCreateSession> spCreateSession;
    CComPtr<IDBCreateCommand> spCreateCommand;
    CComPtr<ICommandText> spCommandText;
    CComBSTR sbstrCommand;
    CComPtr<IRowset> spRowset;
    DBROWCOUNT cRows;
    CComPtr<IColumnsInfo> spColumnsInfo;
    DBORDINAL cColumns;
    DWORD dwOffset;
    DWORD cMaxRowSize;
    HACCESSOR hAccessor;
    BYTE *pRowData = NULL;
    ULONG cRowsObtained;
    CComPtr<IAccessor> spAccessor;
    
    // Get a memory allocator for allocating and freeing memory.
    CComPtr<IMalloc> spMalloc;
    hr = CoGetMalloc(1, &spMalloc);
    if(S_OK != hr)
    {
        return hr;
    }

    // Create an instance of the OLE DB - ODBC provider.
    hr = CoCreateInstance(CLSID_ADsDSOObject, 
        NULL, 
        CLSCTX_INPROC_SERVER, 
        IID_IDBInitialize, 
        (void**)&spDBInitialize);
    if(S_OK != hr)
    {
        return hr;
    }

    // Get the IDBProperties interface.
    hr = spDBInitialize->QueryInterface(IID_IDBProperties, 
        (void**)&spDBProperties);
    if(S_OK != hr)
    {
        return hr;
    }

    // Initialize the OLE DB property initializer structures.
    for(UINT i = 0; i < 3; i++ )
    {
        VariantInit(&InitProperties[i].vValue);
        InitProperties[i].dwOptions = DBPROPOPTIONS_REQUIRED;
        InitProperties[i].colid = DB_NULLID;
    }
        
    // Level of prompting performed for the connection process.
    InitProperties[0].dwPropertyID = DBPROP_INIT_PROMPT;
    InitProperties[0].vValue.vt = VT_I2;
    InitProperties[0].vValue.iVal = DBPROMPT_NOPROMPT;

    // Set the user ID.
    sbstrUsername = pwszUsername;
    InitProperties[1].dwPropertyID = DBPROP_AUTH_USERID;
    InitProperties[1].vValue.vt = VT_BSTR;
    InitProperties[1].vValue.bstrVal = sbstrUsername;

    // Set the password.
    sbstrPassword = pwszPassword;
    InitProperties[2].dwPropertyID = DBPROP_AUTH_PASSWORD;
    InitProperties[2].vValue.vt = VT_BSTR;
    InitProperties[2].vValue.bstrVal = sbstrPassword;

    // Set the InitProperties array into the property set. 
    InitPropSet.guidPropertySet = DBPROPSET_DBINIT;
    InitPropSet.cProperties = 3;
    InitPropSet.rgProperties = InitProperties;
     
    // Set initialization properties.
    hr = spDBProperties->SetProperties(1, &InitPropSet);
    if(S_OK != hr)
    {
        return hr;
    }

    // Initialize the connection.
    hr = spDBInitialize->Initialize();
    if(S_OK != hr)
    {
        return hr;
    }

    // Get the IDBCreateSession interface.
    hr = spDBInitialize->QueryInterface(IID_IDBCreateSession, 
        (void**)&spCreateSession);
    if(S_OK != hr)
    {
        return hr;
    }

    // Create an IDBCreateCommand object.
    hr = spCreateSession->CreateSession(NULL, 
        IID_IDBCreateCommand, 
        (IUnknown**)&spCreateCommand);
    if(S_OK != hr)
    {
        return hr;
    }

    // Create an ICommandText Interface from 
    // the ICreateCommand Interface.
    hr = spCreateCommand->CreateCommand(NULL, 
        IID_ICommandText, 
        (IUnknown**)&spCommandText);
    if(S_OK != hr)
    {
        return hr;
    }

    // Build the command string.
    sbstrCommand = "<LDAP://";
    sbstrCommand += pwszDN;
    sbstrCommand += ">;(objectClass=user);name,adspath;subtree";
    /*
    Before executing the query, pass the command text for 
    the query along with the dialect of the command text. 
    In this case, use the LDAP dialect. You can also pass 
    DBGUID_DBSQL, providing the query text is in that format.
    */
    hr = spCommandText->SetCommandText(DBGUID_LDAPDialect, 
                                       sbstrCommand);
    if(S_OK != hr)
    {
        return hr;
    }

    /*
    Instruct the Active Directory OLE DB provider 
    to execute the statement. If successful, an 
    IRowset interface is returned.
    */
    hr= spCommandText->Execute(NULL, 
        IID_IRowset,
        NULL, 
        &cRows,
        (IUnknown**)&spRowset);

    if(DB_SEC_E_PERMISSIONDENIED == hr)
    {
        return hr;
    }
    if(S_OK != hr)
    {
        return hr;
    }

    // Retrieve the search results.

    /*
    An IRowset object is now available. Send a query 
    for the IColumnsInfo interface to obtain the column 
    data of the result set.
    */
    hr = spRowset->QueryInterface(IID_IColumnsInfo, 
                                  (void**)&spColumnsInfo);
    if(S_OK != hr)
    {
        return hr;
    }

    /*
    Use the IColumnsInfo::GetColumnInfo method to get 
    the column data from the command object.
    */
    hr = spColumnsInfo->GetColumnInfo(&cColumns, 
        &rgDBColumnInfo, 
        &pStringsBuffer);
    if(S_OK != hr)
    {
        goto PrintAllUsers_cleanup;
    }
    
    /*
    Create column bindings for the result set. 
    This code example instructs the IAccessor to return
    column data as Unicode strings.
    */
    rgBind = (DBBINDING*)spMalloc->Alloc(sizeof(DBBINDING) * cColumns);
    if(!rgBind)
    {
        goto PrintAllUsers_cleanup;
    }

    dwOffset = 0;
    for(ULONG ulBind = 0; ulBind < cColumns; ulBind++)
    {
        // Binding structure.
        rgBind[ulBind].dwPart      = DBPART_VALUE | DBPART_LENGTH | DBPART_STATUS;
        rgBind[ulBind].eParamIO    = DBPARAMIO_NOTPARAM;
        rgBind[ulBind].iOrdinal    = rgDBColumnInfo[ulBind].iOrdinal;
        rgBind[ulBind].wType       = DBTYPE_WSTR;
        rgBind[ulBind].pTypeInfo   = NULL;
        rgBind[ulBind].obValue     = dwOffset + offsetof(DBCOLUMNDATA, bData);
        rgBind[ulBind].obLength    = dwOffset + offsetof(DBCOLUMNDATA, dwLength);
        rgBind[ulBind].obStatus    = dwOffset + offsetof(DBCOLUMNDATA, dwStatus);
        rgBind[ulBind].cbMaxLen    = rgDBColumnInfo[ulBind].ulColumnSize;
        rgBind[ulBind].pObject     = NULL;
        rgBind[ulBind].pBindExt    = NULL;
        rgBind[ulBind].dwFlags     = 0;
        rgBind[ulBind].dwMemOwner  = DBMEMOWNER_CLIENTOWNED;
        rgBind[ulBind].bPrecision  = 0;
        rgBind[ulBind].bScale      = 0;
     
        dwOffset += rgBind[ulBind].cbMaxLen + offsetof(DBCOLUMNDATA, bData);
    } 
    cMaxRowSize = dwOffset;

    // Get the IAccessor interface from the rowset.
    hr = spRowset->QueryInterface(IID_IAccessor, (void**)&spAccessor);
    if(S_OK != hr)
    {
        goto PrintAllUsers_cleanup;
    }
 
    /*
    Call the IAccessor::CreateAccessor method, which returns an 
    array of accessor handles. This is an array of handles 
    to the rows in the result set.
    */
    hr = spAccessor->CreateAccessor(DBACCESSOR_ROWDATA, 
        ulBind, 
        rgBind, 
        0, 
        &hAccessor,
        NULL);
    if(S_OK != hr)
    {
        goto PrintAllUsers_cleanup;
    }
     
    // Allocate a block of memory that will hold one 
    // row of the result set.
    pRowData = (BYTE*)spMalloc->Alloc(cMaxRowSize);
    if(!pRowData)
    {
        goto PrintAllUsers_cleanup;
    }
     
    // Process all the rows, one by one, NUMROWS_CHUNK rows at a time.
    do 
    {
        HROW *rgRowHandles = NULL;
        cRowsObtained = 0;
         
        /*
        Call the IRowset::GetNextRows method to specify
        the number of rows desired, pointers to the return row data,
        and the number of rows returned.
        */
        hr = spRowset->GetNextRows(
            0,
            0,
            NUMROWS_CHUNK,
            &cRowsObtained,
            &rgRowHandles);
        if(SUCCEEDED(hr) && (cRowsObtained > 0))
        {
            // Loop through the rows obtained,
            // getting the data for each.
            for(ULONG ulRow = 0; ulRow < cRowsObtained; ulRow++)
            {
                // Retrieve the row.
                hr = spRowset->GetData(rgRowHandles[ulRow],
                    hAccessor,
                    pRowData);
     
                // Print to screen.
                PrintRowData(rgBind, rgDBColumnInfo, ulBind, pRowData);
            }
        
            // Release the row handles.
            hr = spRowset->ReleaseRows(cRowsObtained, rgRowHandles, 0, 0, 0);
        }

        // Free the row handles.
        if(rgRowHandles)
        {
            spMalloc->Free(rgRowHandles);
        }

    }while(cRowsObtained > 0);


PrintAllUsers_cleanup:
    if(rgDBColumnInfo)
    {
        spMalloc->Free(rgDBColumnInfo);
    }

    if(pStringsBuffer)
    {
        spMalloc->Free(pStringsBuffer);
    }

    if(rgBind)
    {
        spMalloc->Free(rgBind);
    }

    if(pRowData)
    {
        spMalloc->Free(pRowData);
    }
}

/********************************************************************

    PrintRowData()

********************************************************************/

void PrintRowData(DBBINDING *rgBind, 
                  DBCOLUMNINFO pDBColumnInfo[], 
                  ULONG ulNumColsBind, 
                  BYTE *pData)
{
    ULONG ulCurrentCol;
    DBCOLUMNDATA *pColumn;
 
    // Print each column that is bound to.
    for(ulCurrentCol = 0; 
        ulCurrentCol < ulNumColsBind; 
        ulCurrentCol++)
    {
        /*
        Get a pointer to the column data. The obLength member of 
        the DBBINDING structure contains the offset, in bytes, to 
        the column data.
        */
        pColumn = (DBCOLUMNDATA*)(pData + 
                                  rgBind[ulCurrentCol].obLength);
 
        // Only print columns that have a column name.
        if(pDBColumnInfo[ulCurrentCol].pwszName)
        {
            // Print the column name.
            wprintf(pDBColumnInfo[ulCurrentCol].pwszName);
            wprintf(L": ");

            // Print the column data.
            switch(pColumn->dwStatus)
            {
                case DBSTATUS_S_ISNULL:
                    wprintf(L"<NULL>");
                    break;

                case DBSTATUS_S_OK:
                case DBSTATUS_S_TRUNCATED:
                    if((LPWSTR)pColumn->bData)
                    {
                        wprintf((LPWSTR)pColumn->bData);
                    }
                    else
                    {
                        wprintf(L"<no data>");
                    }
                    break;

                case DBSTATUS_E_CANTCONVERTVALUE:
                    wprintf(L"<cannot convert value>");
                    break;
                
                default:
                    wprintf(L"<unknown>");
                    break;
            }

            wprintf(L"\n");
        }
    }
    
    wprintf(L"\n");
}
```



 

 