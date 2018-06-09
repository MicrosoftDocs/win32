---
title: Domain Browser
description: Using the IDsBrowseDomainTree interface, an application can display a domain browser dialog box and obtain the DNS name of the domain selected by the user.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 26793c61-469e-4e99-9056-b9fc04336b69
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- domain browser AD
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Domain Browser

Using the [**IDsBrowseDomainTree**](/windows/desktop/api/Dsclient/) interface, an application can display a domain browser dialog box and obtain the DNS name of the domain selected by the user. An application can also use the **IDsBrowseDomainTree** interface to obtain data about all domain trees and domains within a forest.

An instance of the [**IDsBrowseDomainTree**](/windows/desktop/api/Dsclient/) interface is created by calling [**CoCreateInstance**](7295a55b-12c7-4ed0-a7a4-9ecee16afdec) with the **CLSID\_DsDomainTreeBrowser** class identifier as shown below.

The [**IDsBrowseDomainTree::SetComputer**](/windows/desktop/api/Dsclient/) method can be used to specify which computer and credentials are used as the basis for retrieving the domain data. When **SetComputer** is called on a particular [**IDsBrowseDomainTree**](/windows/desktop/api/Dsclient/) instance, [**IDsBrowseDomainTree::FlushCachedDomains**](/windows/desktop/api/Dsclient/) must be called before **SetComputer** is called again.

The [**IDsBrowseDomainTree::BrowseTo**](/windows/desktop/api/Dsclient/) method is used to display the domain browser dialog box. When the user selects a domain and clicks the **OK** button, the **IDsBrowseDomainTree::BrowseTo** returns **S\_OK** and the *ppszTargetPath* parameter contains the name of the selected domain. When the name string is no longer required, the caller must free the string by calling [**CoTaskMemFree**](3d0af12e-fc74-4ef7-b2dd-e9da5d0483c7).

The following code example shows how to use the [**IDsBrowseDomainTree**](/windows/desktop/api/Dsclient/) interface to display the domain browser dialog box.


```C++
#include <shlobj.h>
#include <dsclient.h>

void main(void)
{
    HRESULT     hr;

    hr = CoInitialize(NULL);
    if(FAILED(hr)) 
    {
        return;
    }

    IDsBrowseDomainTree *pDsDomains = NULL;

    hr = ::CoCreateInstance(    CLSID_DsDomainTreeBrowser,
                                NULL,
                                CLSCTX_INPROC_SERVER,
                                IID_IDsBrowseDomainTree,
                                (void **)(&amp;pDsDomains));
    
    if(SUCCEEDED(hr))
    {
        LPOLESTR    pstr;        

        hr = pDsDomains->BrowseTo(  GetDesktopWindow(),
                                    &amp;pstr,
                                    0);
        
        if(S_OK == hr)
        {
            wprintf(pstr);
            wprintf(L"\n");
            CoTaskMemFree(pstr);
        }

        pDsDomains->Release();
    }

    CoUninitialize();
}
```



The [**IDsBrowseDomainTree::GetDomains**](/windows/desktop/api/Dsclient/) method is used to obtain domain tree data. The domain data is supplied in a [**DOMAINTREE**](/windows/desktop/api/Dsclient/ns-dsclient-domain_tree) structure. The **DOMAINTREE** structure contains the size of the structure and the number of domain elements in the tree. The **DOMAINTREE** structure also contains one or more [**DOMAINDESC**](/windows/desktop/api/Dsclient/ns-dsclient-_domaindesc) structures. The **DOMAINDESC** contains data about a single element in the domain tree, including child and sibling data. The siblings of a domain can be enumerated by accessing the **pdNextSibling** member of each subsequent **DOMAINDESC** structure. The children of the domain can be retrieved in a similar manner by accessing the **pdChildList** member of each subsequent **DOMAINDESC** structure.

The following code example shows how to obtain and access the domain tree data using the [**IDsBrowseDomainTree::GetDomains**](/windows/desktop/api/Dsclient/) method.


```C++
//  Add dsuiext.lib to the project.

#include "stdafx.h"
#include <shlobj.h>
#include <dsclient.h>

//The PrintDomain() function displays the domain name
void PrintDomain(DOMAINDESC *pDomainDesc, DWORD dwIndentLevel)
{
    DWORD i;

    // Display the domain name.
    for(i = 0; i < dwIndentLevel; i++)
    {
        wprintf(L"  ");
    }
    wprintf(pDomainDesc->pszName);
    wprintf(L"\n");
}

//The WalkDomainTree() function traverses the domain tree and prints the current domain name
void WalkDomainTree(DOMAINDESC *pDomainDesc, DWORD dwIndentLevel = 0)
{
    DOMAINDESC  *pCurrent;

    // Walk through the current item and any siblings it may have.
    for(pCurrent = pDomainDesc; 
        NULL != pCurrent; 
        pCurrent = pCurrent->pdNextSibling)
    {
        // Print the current domain name.
        PrintDomain(pCurrent, dwIndentLevel);

        // Walk the child tree, if one exists.
        if(NULL != pCurrent->pdChildList)
        {
            WalkDomainTree(pCurrent->pdChildList, 
                           dwIndentLevel + 1);
        }
    }
}

//  Entry point for application
int main(void)
{
    HRESULT hr;
    IDsBrowseDomainTree *pBrowseTree;
    CoInitialize(NULL);

    hr = CoCreateInstance(CLSID_DsDomainTreeBrowser,
                          NULL,
                          CLSCTX_INPROC_SERVER,
                          IID_IDsBrowseDomainTree,
                          (void**)&amp;pBrowseTree);

    if(SUCCEEDED(hr))
    {
        DOMAINTREE  *pDomTreeStruct;
        hr = pBrowseTree->GetDomains(&amp;pDomTreeStruct, 
                                     DBDTF_RETURNFQDN);
        if(SUCCEEDED(hr))
        {
            WalkDomainTree(&amp;pDomTreeStruct->aDomains[0]);
            hr = pBrowseTree->FreeDomains(&amp;pDomTreeStruct);
        }
        pBrowseTree->Release();
    }
    CoUninitialize();
}
```



 

 




