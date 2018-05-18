---
Description: 'If you do not know the names of the head nodes in a domain, you can use Active Directory to search for the names.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'cacdcba2-98e8-4306-b289-ef90393a925e'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Using Active Directory to Find the Head Nodes
---

# Using Active Directory to Find the Head Nodes

If you do not know the names of the head nodes in a domain, you can use Active Directory to search for the names. If you used Active Directory with Microsoft Compute Cluster Server 2003 to find the head nodes, you must change your filter to include the following keyword to find all Windows HPC Server 2008 head nodes:

`(keywords=*Version2*)`

For example,

`(&(objectClass=ServiceConnectionPoint)(serviceClassName=MicrosoftComputeCluster)(keywords=*Version2*))`

The following C# example shows how to retrieve all Microsoft HPC Server 2008 and later head nodes in the domain.


```CSharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.DirectoryServices;

namespace Using_AD_to_Find_the_Head_Node
{
    class Program
    {
        static void Main(string[] args)
        {
            LoadHeadNodes();
        }

        private static void LoadHeadNodes()
        {
            DirectoryEntry searchRoot;
            DirectoryEntry domain;
            DirectorySearcher searcher;
            string dnsName;

            // Bind to current domain
            searchRoot = new DirectoryEntry("LDAP://rootDSE");
            domain = new DirectoryEntry("LDAP://" + searchRoot.Properties["defaultNamingContext"][0]);
            searchRoot.Dispose();

            string domainName = domain.Name.Substring(3);  // DC=name

            // Search for all v2 head nodes in current domain.
            string[] propsToLoad = new string[] { "servicednsname" };
            string filterForAllHeadNodes = "(&amp;(objectClass=ServiceConnectionPoint)(serviceClassName=MicrosoftComputeCluster)(keywords=*Version2*))";

            searcher = new DirectorySearcher(domain, filterForAllHeadNodes, propsToLoad);

            SearchResultCollection results = searcher.FindAll();

            Console.WriteLine("Found the following {0} head nodes:", results.Count);

            // Enumerate head nodes
            foreach (SearchResult result in results)
            {
                dnsName = (string)result.Properties["servicednsname"][0];
                Console.WriteLine(dnsName);
            }

            results.Dispose();
            domain.Dispose();
        }
    }
}
```



The following C++ example shows how to retrieve all Microsoft HPC Server 2008 and later head nodes in the domain.


```C++
#include <windows.h>
#include <stdio.h>
#include <vector>
#include <activeds.h>
#include <strsafe.h>
#include <comutil.h>

// Link to Activeds.lib and Adsiid.lib
#pragma comment(lib, "activeds.lib")
#pragma comment(lib, "adsiid.lib")
#pragma comment(lib, "comsuppw.lib")

void FindConnectionPoints(std::vector<LPWSTR>&amp; pHeadNodes);
void ClearConnectionPoints(std::vector<LPWSTR>&amp; pHeadNodes);


void wmain(void)
{
    std::vector<LPWSTR> pHeadNodes;
    DWORD size = 0;

    CoInitializeEx(NULL, COINIT_APARTMENTTHREADED);

    FindConnectionPoints(pHeadNodes);

    if (!pHeadNodes.empty())
    {
        size = (DWORD) pHeadNodes.size();
        wprintf(L"Found the following %d head nodes.\n", size);

        for (DWORD i=0; i<size; i++)
        {
        wprintf(L"%s\n", pHeadNodes[i]);
    }

    ClearConnectionPoints(pHeadNodes);
    }

    CoUninitialize();
}

// Use Active Directory to find the head nodes of the compute clusters 
// in a domain.
void FindConnectionPoints(std::vector<LPWSTR>&amp; pHeadNodes)
{
    HRESULT hr = S_OK;
    IADs* pObject = NULL;
    IDirectorySearch* pSearch = NULL;
    ADS_SEARCH_HANDLE hSearch;
    WCHAR szPath[MAX_PATH];
    VARIANT var;
    LPWSTR pNodeName = NULL;
    BOOL fAllocationError = FALSE;
    size_t length = 0;


    // Bind to LDAP://rootDSE.
    hr = ADsOpenObject(L"LDAP://rootDSE",
                     NULL,
                     NULL,
                     ADS_SECURE_AUTHENTICATION, // Use Secure Authentication.
                     IID_IADs,
                     (void**)&amp;pObject);
    if (FAILED(hr))
    {
        wprintf(L"Cannot execute query. Cannot bind to LDAP://rootDSE.\n");
        return;
    }

    hr = pObject->Get(_bstr_t(L"defaultNamingContext"), &amp;var);
    if (SUCCEEDED(hr))
    {
        // Build path to the domain container.
        StringCchPrintf(szPath, MAX_PATH, L"LDAP://");
        StringCchCatN(szPath, MAX_PATH, var.bstrVal, MAX_PATH - wcslen(szPath));
        VariantClear(&amp;var);

        // Get the DirectorySearch object used to search Active Directory.
        hr = ADsOpenObject(szPath,
                       NULL,
                       NULL,
                       ADS_SECURE_AUTHENTICATION, // Use Secure Authentication.
                       IID_IDirectorySearch,
                       (void**)&amp;pSearch);
        if (FAILED(hr))
        {
            wprintf(L"Failed to create DirectorySearch object, 0x%x.\n", hr);
        }
        else
        {
            // This attribute contains the FQDN of the head node.
            LPWSTR pszAttrs[] = { L"servicednsname" }; 
            DWORD dwCount = sizeof(pszAttrs)/sizeof(LPWSTR);
            ADS_SEARCH_COLUMN DnsNameColumn;

            // Search for all v2 head nodes in current domain.
            hr = pSearch->ExecuteSearch(L"(&amp;(objectClass=ServiceConnectionPoint)(serviceClassName=MicrosoftComputeCluster)(keywords=*Version2*))",
                                  pszAttrs, 
                                  dwCount, 
                                  &amp;hSearch);
            if (FAILED(hr))
            {
                wprintf(L"pSearch->ExecuteSearch failed, 0x%x\n", hr);
            }
            else
            {
                hr = pSearch->GetFirstRow(hSearch);
                if (SUCCEEDED(hr))
                {
                    while( hr != S_ADS_NOMORE_ROWS &amp;&amp; !fAllocationError)
                    {
                        hr = pSearch->GetColumn(hSearch, L"servicednsname", &amp;DnsNameColumn );
                        if ( SUCCEEDED(hr) )
                        {
                            length = wcslen(DnsNameColumn.pADsValues->CaseIgnoreString) + 1;
                            pNodeName = (LPWSTR) malloc(length * sizeof(WCHAR));
                            if (pNodeName)
                            {
                                StringCchCopy(pNodeName, length+1, DnsNameColumn.pADsValues->CaseIgnoreString);
                                pHeadNodes.push_back( pNodeName );
                            }
                            else
                            {
                                wprintf(L"Failed to allocate memory for node name.\n");
                                pSearch->FreeColumn( &amp;DnsNameColumn );
                                fAllocationError = TRUE;
                                ClearConnectionPoints(pHeadNodes);
                                continue;
                            }

                            pSearch->FreeColumn( &amp;DnsNameColumn );
                        }

                        // Get the next row.
                        hr = pSearch->GetNextRow( hSearch);
                    }
                }
   
                pSearch->CloseSearchHandle(hSearch);
            }

            pSearch->Release();
        }
    }

    pObject->Release();
}


// Free the node names in the vector and clear the vector.
void ClearConnectionPoints(std::vector<LPWSTR>&amp; pHeadNodes)
{
    DWORD size = 0;

    if (!pHeadNodes.empty())
    {
        size = (DWORD) pHeadNodes.size();

        for (DWORD i=0; i<size; i++)
        {
            if (pHeadNodes[i])
                free(pHeadNodes[i]);
        }

        pHeadNodes.clear();
    }
}
```



 

 



