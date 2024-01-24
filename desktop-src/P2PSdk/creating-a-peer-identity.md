---
description: The Identity Manager API allows you to create a peer identity to use in a peer network.
ms.assetid: 44b85bbc-9594-4f68-b930-51a28422b571
title: Creating a Peer Identity
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Peer Identity

The Identity Manager API allows you to create a peer identity to use in a peer network.

When you create a peer identity, you can provide the following optional information:

-   [Classifier](peer-names.md)
-   Friendly name
-   Cryptographic service provider

> [!Note]  
> Whenever possible, re-use a peer identity.

 

## Example of Creating and Deleting a Peer Identity

The following code snippet shows you how to create and delete a peer identity by using a classifier and friendly name.


```C++
#define UNICODE
#include <p2p.h>
#include <stdio.h>

#pragma comment(lib, "p2p.lib")

//-----------------------------------------------------------------------------
// Function: CreateIdentity
//
// Purpose:  Creates a new Identity.
//
// Returns:  HRESULT
//
HRESULT CreateIdentity(PWSTR pwzFriendlyName)
{
    HRESULT     hr              = S_OK;   
    PWSTR       pwzClassifier   = L"GroupMember";
    PWSTR       pwzIdentity     = NULL;

    hr = PeerIdentityCreate(pwzClassifier, pwzFriendlyName, 0, &pwzIdentity);
    if (FAILED(hr))
    {            
        printf("Failed to create identity.");
    }
    else
    {
        printf("Identity: %s", pwzFriendlyName);
    }
       
    PeerFreeData(pwzIdentity);    

    return hr;
}


//-----------------------------------------------------------------------------
// Function: DeleteIdentity
//
// Purpose:  Delete the identity created by CreateIdentity
//
// Returns:  HRESULT
//
HRESULT DeleteIdentity()
{
    HRESULT hr = S_OK;

    if (g_pwzIdentity)
    {
        hr = PeerIdentityDelete(g_pwzIdentity);
        g_pwzIdentity = NULL;
    }

    return hr;
}
```



 

 



