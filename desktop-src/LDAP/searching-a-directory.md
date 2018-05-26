---
title: Searching a Directory
description: Search is the most common directory activity.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 38482501-faa1-4055-9758-e1e0a4199688
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- Searching a Directory LDAP
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Searching a Directory

Search is the most common directory activity. The LDAP API includes a variety of search criteria and result-retrieval methods to find directory data. As with other LDAP operations, you can perform a search synchronously or asynchronously. Extensions to the base LDAP API enable you to add sorting criteria and other extensions to your search request. Three settings in the [**LDAP**](/windows/previous-versions/Winldap/ns-winldap-ldap?branch=master) structure affect a search:

-   The **LDAP\_OPT\_SIZELIMIT** option limits the number of results returned from a search.
-   The **LDAP\_OPT\_TIMELIMIT** option limits the amount of time to spend on a search.
-   The **LDAP\_OPT\_DEREF** option determines when, or if, aliases are dereferenced during a search.

The [**ldap\_search**](/windows/previous-versions/Winldap/nf-winldap-ldap_search?branch=master) and [**ldap\_search\_s**](/windows/previous-versions/Winldap/nf-winldap-ldap_search_s?branch=master) functions are the original (LDAP 2) asynchronous and synchronous search functions. To specify a local timeout for a synchronous search, use [**ldap\_search\_st**](/windows/previous-versions/Winldap/nf-winldap-ldap_search_st?branch=master). The extended functions [**ldap\_search\_ext**](/windows/previous-versions/Winldap/nf-winldap-ldap_search_ext?branch=master) and [**ldap\_search\_ext\_s**](/windows/previous-versions/Winldap/nf-winldap-ldap_search_ext_s?branch=master) support LDAP 3 server controls and client controls, and enable you to specify varying size and time limits for each search operation.

For more information, see [Synchronous and Asynchronous Calls](synchronous-vs--asynchronous-calls.md), [**ldap\_search\_init\_page**](/windows/previous-versions/Winldap/nf-winldap-ldap_search_init_page?branch=master), and [**ldap\_search\_abandon\_page**](/windows/previous-versions/Winldap/nf-winldap-ldap_search_abandon_page?branch=master).

The following C++ code example shows how to use LDAP functions to initialize, connect to, and perform a synchronous search of an Active Directory, and it outputs the search results to a command prompt window. It lists the first ten, or fewer, users and the names and values of a selected subset of attributes for the user. To retrieve the value of an attribute whose type is a null-terminated character string, use [**ldap\_get\_values**](/windows/previous-versions/Winldap/nf-winldap-ldap_get_values?branch=master), but for an attribute which contains binary data you should use [**ldap\_get\_values\_len**](/windows/previous-versions/Winldap/nf-winldap-ldap_get_values_len?branch=master). Determining the type for each attribute can become complex, and is not shown in this code example. Due to the complexity of this operation, it is recommended that, when possible, you use the ADSI interface for searching Active Directory, where much of the complexity has been minimized. However, if you must use LDAP in your application, the following code example should help.

The following code example:

-   Receives validated credentials (name and password) from its two parameters.
-   Initializes the session parameters for the connection.

    Provide the host name and set up the options for the session. In this example, a host name of "fabrikam.com" is provided, the LDAP version is set to 3.0, and the maximum number of entries, that is objects, to return is set to 10.

-   Connects to the server.
-   Binds to the server with credentials.

    This step provides the credentials that determine how much on the server you have access to. In this example an Administrator credential is used.

-   Searches the Active Directory.

    Here, a filter is supplied that determines what kind of objects to search for, in this case, the "user" class. The search returns the requested objects, called entries, to the [**LDAPMessage**](/windows/previous-versions/Winldap/ns-winldap-ldapmsg?branch=master) structure. The parsing of the results is done on this returned message.

-   Retrieves the number of entries in the returned message.

    This number is used later for looping through the message entries.

-   Loops through entries in the returned message.

    For each entry, all the requested attribute names and values are output.


```C++
//----------------------------------------------
// Performing an LDAP Synchronous Search.
//
// Be aware that you must set the command prompt screen buffer 
// height to 350 and the width to 90.
//-------------------------------------------------------------

#include <windows.h>
#include <winldap.h>
#include <winber.h>
#include <rpc.h>
#include <rpcdce.h>
#include <stdio.h>

//-----------------------------------------------------------
// This subroutine must have validated credentials (name and
// password) passed to it.
//-----------------------------------------------------------
int MyLDAPSearch(PCHAR pUserName, PCHAR pPassword)
{
    //---------------------------------------------------------
    // Initialize a session. LDAP_PORT is the default port, 389.
    //---------------------------------------------------------
    PCHAR hostName = "fabrikam.com";
    LDAP* pLdapConnection = NULL;
    
    pLdapConnection = ldap_init(hostName, LDAP_PORT);
    
    if (pLdapConnection == NULL)
    {
        printf("ldap_init failed with 0x%x.\n",LdapGetLastError());
        ldap_unbind(pLdapConnection);
        return -1;
    }
    else
        printf("ldap_init succeeded \n");
    
    
    //-------------------------------------------------------
    // Set session options.
    //-------------------------------------------------------
    ULONG version = LDAP_VERSION3;
    ULONG numReturns = 10;
    ULONG lRtn = 0;
    
    // Set the version to 3.0 (default is 2.0).
    lRtn = ldap_set_option(
                    pLdapConnection,           // Session handle
                    LDAP_OPT_PROTOCOL_VERSION, // Option
                    (void*) &amp;version);         // Option value

    if(lRtn == LDAP_SUCCESS)
        printf("ldap version set to 3.0 \n");
    else
    {
        printf("SetOption Error:%0lX\n", lRtn);
        ldap_unbind(pLdapConnection);
        return -1;
    }

    // Set the limit on the number of entries returned to 10.
    lRtn = ldap_set_option(
                    pLdapConnection,       // Session handle
                    LDAP_OPT_SIZELIMIT,    // Option
                    (void*) &amp;numReturns);  // Option value

    if(lRtn == LDAP_SUCCESS)
        printf("Max return entries set to 10 \n");
    else
    {
        printf("SetOption Error:%0lX\n", lRtn);
        ldap_unbind(pLdapConnection);
        return -1;
    }
    
    
    //--------------------------------------------------------
    // Connect to the server.
    //--------------------------------------------------------
    
    lRtn = ldap_connect(pLdapConnection, NULL);
    
    if(lRtn == LDAP_SUCCESS)
        printf("ldap_connect succeeded \n");
    else
    {
        printf("ldap_connect failed with 0x%lx.\n",lRtn);
        ldap_unbind(pLdapConnection);
        return -1;
    }
    
    
    //--------------------------------------------------------
    // Bind with credentials.
    //--------------------------------------------------------
    PCHAR pMyDN = "DC=fabrikam,DC=com";
    SEC_WINNT_AUTH_IDENTITY secIdent;
 
    secIdent.User = (unsigned char*)pUserName;
    secIdent.UserLength = strlen(pUserName);
    secIdent.Password = (unsigned char*)pPassword;
    secIdent.PasswordLength = strlen(pPassword);
    secIdent.Domain = (unsigned char*)hostName;
    secIdent.DomainLength = strlen(hostName);
    secIdent.Flags = SEC_WINNT_AUTH_IDENTITY_ANSI;
    
    lRtn = ldap_bind_s(
                pLdapConnection,      // Session Handle
                pMyDN,                // Domain DN
                (PCHAR)&amp;secIdent,     // Credential structure
                LDAP_AUTH_NEGOTIATE); // Auth mode
    if(lRtn == LDAP_SUCCESS)
    {
        printf("ldap_bind_s succeeded \n");
        secIdent.Password = NULL; // Remove password pointer
        pPassword = NULL;         // Remove password pointer
    }
    else
    {
        printf("ldap_bind_s failed with 0x%lx.\n",lRtn);
        ldap_unbind(pLdapConnection);
        return -1;
    }
  
    //----------------------------------------------------------
    // Perform a synchronous search of fabrikam.com for 
    // all user objects that have a "person" category.
    //----------------------------------------------------------
    ULONG errorCode = LDAP_SUCCESS;
    LDAPMessage* pSearchResult;
    PCHAR pMyFilter = "(&amp;(objectCategory=person)(objectClass=user))";
    PCHAR pMyAttributes[6];

    pMyAttributes[0] = "cn";
    pMyAttributes[1] = "company";
    pMyAttributes[2] = "department";
    pMyAttributes[3] = "telephoneNumber";
    pMyAttributes[4] = "memberOf";
    pMyAttributes[5] = NULL;
    
    errorCode = ldap_search_s(
                    pLdapConnection,    // Session handle
                    pMyDN,              // DN to start search
                    LDAP_SCOPE_SUBTREE, // Scope
                    pMyFilter,          // Filter
                    pMyAttributes,      // Retrieve list of attributes
                    0,                  // Get both attributes and values
                    &amp;pSearchResult);    // [out] Search results
    
    if (errorCode != LDAP_SUCCESS)
    {
        printf("ldap_search_s failed with 0x%0lx \n",errorCode);
        ldap_unbind_s(pLdapConnection);
        if(pSearchResult != NULL)
            ldap_msgfree(pSearchResult);
        return -1;
    }
    else
        printf("ldap_search succeeded \n");
    
    //----------------------------------------------------------
    // Get the number of entries returned.
    //----------------------------------------------------------
    ULONG numberOfEntries;
    
    numberOfEntries = ldap_count_entries(
                        pLdapConnection,    // Session handle
                        pSearchResult);     // Search result
    
    if(numberOfEntries == NULL)
    {
        printf("ldap_count_entries failed with 0x%0lx \n",errorCode);
        ldap_unbind_s(pLdapConnection);
        if(pSearchResult != NULL)
            ldap_msgfree(pSearchResult);
        return -1;
    }
    else
        printf("ldap_count_entries succeeded \n");
    
    printf("The number of entries is: %d \n", numberOfEntries);
    
    
    //----------------------------------------------------------
    // Loop through the search entries, get, and output the
    // requested list of attributes and values.
    //----------------------------------------------------------
    LDAPMessage* pEntry = NULL;
    PCHAR pEntryDN = NULL;
    ULONG iCnt = 0;
    char* sMsg;
    BerElement* pBer = NULL;
    PCHAR pAttribute = NULL;
    PCHAR* ppValue = NULL;
    ULONG iValue = 0;
    
    for( iCnt=0; iCnt < numberOfEntries; iCnt++ )
    {
        // Get the first/next entry.
        if( !iCnt )
            pEntry = ldap_first_entry(pLdapConnection, pSearchResult);
        else
            pEntry = ldap_next_entry(pLdapConnection, pEntry);
        
        // Output a status message.
        sMsg = (!iCnt ? "ldap_first_entry" : "ldap_next_entry");
        if( pEntry == NULL )
        {
            printf("%s failed with 0x%0lx \n", sMsg, LdapGetLastError());
            ldap_unbind_s(pLdapConnection);
            ldap_msgfree(pSearchResult);
            return -1;
        }
        else
            printf("%s succeeded\n",sMsg);
        
        // Output the entry number.
        printf("ENTRY NUMBER %i \n", iCnt);
                
        // Get the first attribute name.
        pAttribute = ldap_first_attribute(
                      pLdapConnection,   // Session handle
                      pEntry,            // Current entry
                      &amp;pBer);            // [out] Current BerElement
        
        // Output the attribute names for the current object
        // and output values.
        while(pAttribute != NULL)
        {
            // Output the attribute name.
            printf("     ATTR: %s",pAttribute);
            
            // Get the string values.

            ppValue = ldap_get_values(
                          pLdapConnection,  // Session Handle
                          pEntry,           // Current entry
                          pAttribute);      // Current attribute

            // Print status if no values are returned (NULL ptr)
            if(ppValue == NULL)
            {
                printf(": [NO ATTRIBUTE VALUE RETURNED]");
            }

            // Output the attribute values
            else
            {
                iValue = ldap_count_values(ppValue);
                if(!iValue)
                {
                    printf(": [BAD VALUE LIST]");
                }
                else
                {
                    // Output the first attribute value
                    printf(": %s", *ppValue);

                    // Output more values if available
                    ULONG z;
                    for(z=1; z<iValue; z++)
                    {
                        printf(", %s", ppValue[z]);
                    }
                }
            } 

            // Free memory.
            if(ppValue != NULL)  
                ldap_value_free(ppValue);
            ppValue = NULL;
            ldap_memfree(pAttribute);
            
            // Get next attribute name.
            pAttribute = ldap_next_attribute(
                            pLdapConnection,   // Session Handle
                            pEntry,            // Current entry
                            pBer);             // Current BerElement
            printf("\n");
        }
        
        if( pBer != NULL )
            ber_free(pBer,0);
        pBer = NULL;
    }
    
    //----------------------------------------------------------
    // Normal cleanup and exit.
    //----------------------------------------------------------
    ldap_unbind(pLdapConnection);
    ldap_msgfree(pSearchResult);
    ldap_value_free(ppValue);
    return 0;
    
}


```



 

 




