---
description: LSA Policy provides two functions that you can use to set and retrieve private data.
ms.assetid: 7b6e63d4-ce8f-4279-85d9-da6b2b589afa
title: Storing Private Data
ms.topic: article
ms.date: 05/31/2018
---

# Storing Private Data

LSA Policy provides two functions that you can use to set and retrieve private data. This data is stored as an encrypted string in the registry. For example, you can use these functions to store server account passwords and other sensitive information.

Call the [**LsaStorePrivateData**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsastoreprivatedata) function to store and encrypt private data. As described in [Private Data Object](private-data-object.md), private data objects include three specialized types: local, global, and machine. To create a specialized object, add a prefix to the key name passed to **LsaStorePrivateData**: "L$" for local objects, "G$" for global objects, and "M$" for machine objects. If you are not creating one of these specialized types, you do not need to specify a key name prefix.

To retrieve and decode previously stored private data, call [**LsaRetrievePrivateData**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsaretrieveprivatedata). Note that you cannot retrieve machine private data objects; machine objects can be retrieved only by the operating system.

Before you can store or retrieve private data, your application must get a handle to the local [**Policy**](policy-object.md) object, as demonstrated in [Opening a Policy Object Handle](opening-a-policy-object-handle.md).

The following example creates a local private data object. Note that the function InitLsaString converts a [*Unicode*](/windows/desktop/SecGloss/u-gly) string to an [**LSA\_UNICODE\_STRING**](/windows/desktop/api/lsalookup/ns-lsalookup-lsa_unicode_string) structure. The code for this function is shown in [Using LSA Unicode Strings](using-lsa-unicode-strings.md).


```C++
#include <windows.h>
#include <stdio.h>

BOOL CreatePrivateDataObject(LSA_HANDLE PolicyHandle)
{
  NTSTATUS ntsResult;
  LSA_UNICODE_STRING lucKeyName;
  LSA_UNICODE_STRING lucPrivateData;
  // The L$ prefix specifies a local private data object
  WCHAR wszKeyName[] = L"L$MyPrivateKey";
  WCHAR wszPrivateData[] = L"Something secret.";

  // Initializing PLSA_UNICODE_STRING structures
  if (!InitLsaString(&lucKeyName, wszKeyName))
  {
         wprintf(L"Failed InitLsaString\n");
         return FALSE;
  }
  if (!InitLsaString(&lucPrivateData, wszPrivateData))
  {
         wprintf(L"Failed InitLsaString\n");
         return FALSE;
  }

  // Store the private data.
  ntsResult = LsaStorePrivateData(
    PolicyHandle,   // handle to a Policy object
    &lucKeyName,    // key to identify the data
    &lucPrivateData // the private data
  );
  if (ntsResult != STATUS_SUCCESS)
  {
    wprintf(L"Store private object failed %lu\n",
      LsaNtStatusToWinError(ntsResult));
    return FALSE;
  }
  return TRUE;
}
```



> [!Note]  
> The data stored by the [**LsaStorePrivateData**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsastoreprivatedata) function is not absolutely protected. The key, however, has a [*discretionary access control list*](/windows/desktop/SecGloss/d-gly) (DACL) that allows only the creator and administrators to read the data.

 

 

 
