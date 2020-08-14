---
title: Example Code for Receiving Change Notifications
description: The following code example shows how to use the LDAP change notification control to receive notifications of changes to an object in Active Directory Domain Services.
ms.assetid: e1d36d1c-ee50-4c2f-92f6-eee1dae1c5af
ms.tgt_platform: multiple
keywords:
- Active Directory examples Active Directory ,receiving change notifications
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Receiving Change Notifications

The following code example shows how to use the LDAP change notification control to receive notifications of changes to an object in Active Directory Domain Services. The example registers for notifications, reads the initial state of the object, and then uses a loop to wait for and process changes to the object.

First, the code example calls the [**ldap\_search\_ext**](/previous-versions/windows/desktop/api/winldap/nf-winldap-ldap_search_ext) function, which is an asynchronous search operation that returns after registering a notification request. Second, after setting up the notification request, the example calls the [**ldap\_search\_s**](/previous-versions/windows/desktop/api/winldap/nf-winldap-ldap_search_s) function, which is a synchronous search operation that reads the current state of the object. Third, the example, uses a loop that calls ldap\_result to wait for results of the asynchronous search operation. When the [**ldap\_result**](/previous-versions/windows/desktop/api/winldap/nf-winldap-ldap_result) function returns, the example processes the search results and repeats the loop.

Be aware that if the example read the current state and then set up the notification request, there would be a period of time during which changes could occur before the notification request was registered. By reading the object after setting up the notification request, the window works in reverse–you could receive notifications of changes that occurred before reading the initial state. To handle this, the example caches the object [**uSNChanged**](/windows/desktop/ADSchema/a-usnchanged) attribute value when it reads the object's initial state. Then, when [**ldap\_result**](/previous-versions/windows/desktop/api/winldap/nf-winldap-ldap_result) returns with a change notification, the example compares the cached **uSNChanged** attribute value with the value reported by **ldap\_result**. If the new **uSNChanged** attribute value is less than or equal to the cached value, the example discards the results because they indicate a change that occurred prior to the initial read operation.

This example performs a base level search that monitors a single object. You can specify the **LDAP\_SCOPE\_ONELEVEL** scope to monitor all child objects of the specified object. You can also modify the code to register up to five notification requests and then use the [**ldap\_result**](/previous-versions/windows/desktop/api/winldap/nf-winldap-ldap_result) function to wait for notifications from any of the requests. Remember that change notification requests impact the performance of the server. For more information about how to improve performance, see [Change Notifications in Active Directory Domain Services](change-notifications-in-active-directory-domain-services.md).


```C++
//  Add Wldap32.lib to the project

#include <stdafx.h>
#include <windows.h>
#include <winldap.h>
#include <ntldap.h>
#include <stdio.h>
#include <rpcdce.h>
#include <wchar.h>

// Forward declarations
VOID BuildGUIDString(WCHAR *szGUID, LPBYTE pGUID);
BOOL ProcessResult(LDAP *pldapConnection, LDAPMessage *message, __int64 *piUSNChanged);

//  GetChangeNotifications Function
//
//  Description:
//   The function binds to an LDAP server,
//   registers for change notifications,
//   retrieves the current state, and
//   processes change notifications.
//
//  Input Parameters:
//   szSearchBaseDN  The distinguished name of the object monitored.
//
//  Return Values
//   0   The function was successful.
//   1   An error occurred.
INT GetChangeNotifications (LPWSTR szSearchBaseDN)  
{
    INT             err = LDAP_OPERATIONS_ERROR;//  Return value for LDAP operations.
    INT             iretVal = 1;                //  Return value of this function.
    INT             inumberOfChanges = 3;       //  The number of changes to monitor.
    BOOL            bSuccess = FALSE;           //  Results from processing search results.
    ULONG           version = LDAP_VERSION3;    //  LDAP version 3.
    LDAP*           pldapConnection = NULL;     //  Pointer to the connection handle.
    LDAPControl     simpleControl;              //  Structure used to represent both
                                                //  client and server controls.
    PLDAPControl    controlArray[2];            //  Pointer to the LDAPControl.
    LONG            msgId;                      //  Used to identify the message.
    LDAPMessage*    presults = NULL;            //  Pointer to LDAPMessage data structure 
                                                //  used to contain the search results.
    LDAPMessage*    pmessage = NULL;            //  Pointer to an LDAPMessage data
                                                //  structure used to contain each
                                                //  entry of the search results.
    LPWSTR          szAttribs[] = {             //  Array of attributes whose value will 
                                                 //  be displayed when the attribute
                                                //  changes to a different value.
        {L"telephoneNumber"},
        {L"isDeleted"},
        {L"objectGUID"},
        {L"uSNChanged"},
        NULL
    };

    __int64 iUSNChanged = 0;                    //  Stores the latest USNChanged value for the object.

    //  Connect to the default LDAP server. If successful, the function returns a handle to the
    //  connection.
    pldapConnection = ldap_open(NULL, //  Connect to the default LDAP server.
                                0);   //  TCP port number.

    //  If the connect function fails, show an error message and go to the error section.
    if (pldapConnection == NULL)
    {
        wprintf(L"ldap_open failed to connect. Error: 0x%x.\n", GetLastError());
        goto FatalExit0;
    }

    //  The function succeeded in opening a connection to an LDAP server.    
    wprintf(L"Connected to server.\n");

    //  Set the options on connection blocks to specify LDAP version 3.
    pldapConnection->ld_lberoptions = 0;    

    ldap_set_option(pldapConnection, LDAP_OPT_VERSION, &version);

    //  Asynchronously authenticate a client to the LDAP server using the current credentials.
    err = ldap_bind_s(pldapConnection,        //  Connection handle
                      NULL,                   //  Null pointer
                      NULL,                   //  Use the current credential.
                      LDAP_AUTH_NEGOTIATE);     //  Use the most appropriate authentication method.

    //  If the bind function fails, show an error message and go to the error section. 
    if (LDAP_SUCCESS != err)
    {
        wprintf(L"Bind failed: 0x%x\n", err);
        goto FatalExit0;
    }

    //  The function succeeded in binding to the default LDAP server.
    wprintf(L"Successful bind.\n");

    //  Set up the control to search the directory for objects that have 
    //  changed from a previous state.
    simpleControl.ldctl_oid = LDAP_SERVER_NOTIFICATION_OID_W;
    simpleControl.ldctl_iscritical = TRUE;

    //  Set up the control to specify a BER-encoded sequence of parameters to the
    //  length of the binary data and to initialize a pointer.
    simpleControl.ldctl_value.bv_len = 0;
    simpleControl.ldctl_value.bv_val = NULL;

    //  Initialize the control array values.
    controlArray[0] = &simpleControl;
    controlArray[1] = NULL;

    //  Start a persistent asynchronous search.
    err = ldap_search_ext(pldapConnection,              //  Connection handle.
                           (PWCHAR) szSearchBaseDN,        //  Distinguished name of the object to monitor.
                        LDAP_SCOPE_BASE,                //  Monitor the specified object.
                        L"ObjectClass=*",               //  The search filter.
                        szAttribs,                      //  Attributes to retrieve.
                        0,                              //  Retrieve attributes and values.
                        (PLDAPControl *) &controlArray, //  Server control.
                        NULL,                           //  Client controls.
                        0,                              //  No timeout. 
                        0,                              //  No size limit.
                        (PULONG)&msgId);                //  Receives identifier for results.

    //  If the search function fails, show an error message and go to the error section.                     
    if (LDAP_SUCCESS != err)
    {
        wprintf(L" The asynch search failed. Error: 0x%x \n", err);
        goto FatalExit0;
    }

    //  The asynchronous search function succeeded.
    wprintf(L"Registered for change notifications on %s.\n", szSearchBaseDN);
    wprintf(L"Message identifier is %d.\n", msgId); 

    //  After starting the persistent search, perform a synchronous search 
    //  to retrieve the current state of the monitored object.
    err = ldap_search_s(pldapConnection,            //  Connection handle.
                        (PWCHAR) szSearchBaseDN,    //  Distinguished name of the object to monitor.
                        LDAP_SCOPE_BASE,            //  Monitor the specified object.
                        L"ObjectClass=*",           //  The search filter.
                        szAttribs,                  //  List of attributes to retrieve.
                        0,                          //  Retrieve attributes and values.
                        &presults);                   //  Receives the search results.

    //  If the synchronous search function fails, show an error message and go to
    //  the error section.
    if (LDAP_SUCCESS != err)
    {
        wprintf(L"ldap_search_s error: 0x%x\n", err);
        goto FatalExit0;
    }

    //  The synchronous search function succeeded.
    wprintf(L"\nGot current state\n");

    //  Process the search results by retrieving the first entry of a message
    //  and calling the function that processes the message. As long as the
    //  message contains an entry that is not null, retrieve and process the 
    //  the next entry.
    pmessage = ldap_first_entry(pldapConnection, presults);    

    while (pmessage != NULL) 
    {
        bSuccess = ProcessResult(pldapConnection, pmessage, &iUSNChanged);
        pmessage = ldap_next_entry(pldapConnection, pmessage);
    }

    //  After processing the message, frees the results of the synchronous search routine. 
    ldap_msgfree(presults);
    presults = NULL;

    //  Begin checking for changes on the specified object.
    wprintf(L"Waiting for change notifications...\n");

    //  This loop monitors for changes on the specified object. The number of 
    //  returned changes is specified.
    for (INT icounter = 0;                   //  Lower limit.
         icounter < inumberOfChanges;        //  Upper limit.
         icounter++)                         //  Increment the counter after each loop.
    {
        //  Wait for the results of the asynchronous search.
        presults = NULL;
        err = ldap_result(pldapConnection, //  Connection handle.
                          LDAP_RES_ANY,   //  Message identifier.
                          LDAP_MSG_ONE,   //  Retrieve one message at a time.
                          NULL,           //  No timeout.
                          &presults);       //  Receives the search results. 

        if ((err == (ULONG) -1) || (presults) == NULL)
        {
            wprintf(L"ldap_result error: 0x%x\n", pldapConnection->ld_errno);
            break;
        }

        wprintf(L"\nGot a notification. Message ID: %d\n", presults->lm_msgid);

        //  Process the search results by retrieving the first entry of a message
        //  and calling the function that processes the message. As long as the
        //  message contains an entry that is not null, retrieve and process the 
        //  the next entry.
        pmessage = ldap_first_entry(pldapConnection, presults);

        while (pmessage != NULL) 
        {
            bSuccess = ProcessResult(pldapConnection, pmessage, &iUSNChanged);
            pmessage = ldap_next_entry(pldapConnection, pmessage);
        }

        // Free the resources used by the results.
        ldap_msgfree(presults);

        // Set the pointer to null.
        presults = NULL;
    }

    iretVal = 0;
    wprintf(L"The program returned the last %d changes.\n", inumberOfChanges);

    //  Error Section.
FatalExit0:

    //  If a connection succeeds, frees resources associated with an LDAP session.
    if (pldapConnection) ldap_unbind(pldapConnection);

    //  Free resources used by the results.
    if (presults) ldap_msgfree(presults);

    return iretVal;
}


// BuildGUIDString
//
// Description:
// The function turns the GUID into a string.
//
// Input parameters:
//  szGUID  Pointer to a null-terminated string that will contain the
//          the string version of the GUID.
//  pGUID   Pointer to the GUID to be converted to a string.
VOID BuildGUIDString(WCHAR* szGUID,LPBYTE pGUID)
{
    DWORD i = 0;
    DWORD dwlen = sizeof(GUID);
    WCHAR buf[4];
    wcscpy_s(szGUID,dwlen, L"");
    for (i; i < dwlen; i++)
    {
        swprintf_s(buf, L"%02x", pGUID[i]);
        wcscat_s(szGUID,dwlen,buf);
    }

}

//  ProcessResult
//
//  Description:
//  This function processes and displays the search results.
//
//  Input Parameters:
//   pldapConnection     Pointer to the connection handle.
//   pmessage            Pointer to the result entry to process.
//   piUSNChanged        Pointer to the latest USNChanged value.
//
//  Return Values:
//   True    The function succeeded.
//   False   The function failed.
BOOL ProcessResult(LDAP* pldapConnection,
    LDAPMessage* pmessage,
    __int64* piUSNChanged)
{

    PWCHAR* value = NULL;
    __int64 iNewUSNChanged;
    PWCHAR dn = NULL, attribute = NULL;
    BerElement *opaque = NULL;
    berval **pbvGUID=NULL;
    WCHAR szGUID[40];      //  String version of the objectGUID attribute.
    ULONG count, total;

    //  Get the uSNChanged attribute to determine if this result is new data.
    value = ldap_get_values(pldapConnection, pmessage, L"uSNChanged");

    //  The attempt to get the attribute value failed so the function fails.
    if (!value)
    {
        wprintf(L"ldap_get_values error\n");
        return FALSE;
    }

    //  Convert the attribute value from a string to an integer.
    iNewUSNChanged = _wtoi64(value[0]);

    //  If this attribute value is less than or equal to the previous value, the result
    //  contains out-of-date data. Therefore, discard the attribute value.
    if (iNewUSNChanged <= *piUSNChanged)
    {
        wprintf(L"Discarding outdated search results.\n");
        ldap_value_free(value);

        return TRUE;
    }
    else
    {
        *piUSNChanged = iNewUSNChanged;
        ldap_value_free(value);
    }

    //  The search results are newer than the previous state; process 
    //  the results.
    dn = ldap_get_dn(pldapConnection, pmessage);

    //  If the function does not return a distinguished name, then an
    //  error occurred.
    if (!dn)
    {
        wprintf(L"ldap_get_dn error\n");
        return FALSE;
    }

    //  Display the distinguished name of the object.
    wprintf(L"    Distinguished Name is : %s\n", dn);

    //  Free the resources used to get the distinguished name.
    ldap_memfree(dn);

    //  Display the new values of the specified attributes
    attribute = ldap_first_attribute(pldapConnection, pmessage, &opaque);

    while (attribute != NULL) 
    {
        //  Handle objectGUID as a binary value.
        if (_wcsicmp(L"objectGUID", attribute)==0)
        {  
            wprintf(L"    %s: ", attribute);
            pbvGUID = ldap_get_values_len (pldapConnection, pmessage, attribute);
            if (pbvGUID)
            {
                BuildGUIDString(szGUID, (LPBYTE) pbvGUID[0]->bv_val);
                wprintf(L"%s\n", szGUID);
            }
            ldap_value_free_len(pbvGUID);
        }
        else
        {
            //  Handle other attributes as string values.
            value = ldap_get_values(pldapConnection, pmessage, attribute);
            wprintf(L"    %s: ", attribute);
            if (total = ldap_count_values(value) > 1)
            {
                for (count = 0; count < total; count++)
                    wprintf(L"        %s\n", value[count]);
            }
            else
            {
                wprintf(L"%s\n", value[0]);
                ldap_value_free(value);
            }
        }
        ldap_memfree(attribute);
        attribute = ldap_next_attribute(pldapConnection, pmessage, opaque);
    } 

    return TRUE;
}

//  Entry point for the application.
int wmain(int   cArgs,WCHAR  *pArgs[])
{
    PWCHAR szSearchBaseDN = NULL;
    wprintf(L"\n");
    if (cArgs < 2)
    {
        wprintf(L"Missing the distinguished name of the search base.\n");
        wprintf(L"Usage: getchanges <distinguished name of search base>\n");
        return 0;
    }
    szSearchBaseDN = (PWCHAR) pArgs[1];
    return GetChangeNotifications(szSearchBaseDN);
}
```



 

 