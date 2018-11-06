---
Description: The Local Security Authority (LSA) provides functions to translate between user, group, and local group names and their corresponding security identifier (SID) values.
ms.assetid: 8845b709-a8f9-4d0f-a4a6-86d23d6b01d5
title: Translating Between Names and SIDs
ms.topic: article
ms.date: 05/31/2018
---

# Translating Between Names and SIDs

The [*Local Security Authority*](https://msdn.microsoft.com/library/windows/desktop/ms721592#-security-local-security-authority-gly) (LSA) provides functions to translate between user, group, and local group names and their corresponding [*security identifier*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-identifier-gly) (SID) values. To locate account names, call the [**LsaLookupNames**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsalookupnames) function. This function returns the SID as a RID/Domain index pair. To get the SID as a single element, call the [**LsaLookupNames2**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsalookupnames2) function. To locate SIDs, call [**LsaLookupSids**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsalookupsids).

These functions can translate name and SID information from any domain trusted by the local system.

Before you can translate between account names and SIDs, your application must get a handle to the local [**Policy**](policy-object.md) object, as demonstrated in [Opening a Policy Object Handle](opening-a-policy-object-handle.md).

The following example looks up the SID for an account, given the account name.


```C++
void GetSIDInformation (LPWSTR AccountName,LSA_HANDLE PolicyHandle)
{
  LSA_UNICODE_STRING lucName;
  PLSA_TRANSLATED_SID ltsTranslatedSID;
  PLSA_REFERENCED_DOMAIN_LIST lrdlDomainList;
  LSA_TRUST_INFORMATION myDomain;
  NTSTATUS ntsResult;
  PWCHAR DomainString = NULL;

  // Initialize an LSA_UNICODE_STRING with the name.
  if (!InitLsaString(&lucName, AccountName))
  {
         wprintf(L"Failed InitLsaString\n");
         return;
  }

  ntsResult = LsaLookupNames(
     PolicyHandle,     // handle to a Policy object
     1,                // number of names to look up
     &lucName,         // pointer to an array of names
     &lrdlDomainList,  // receives domain information
     &ltsTranslatedSID // receives relative SIDs
  );
  if (STATUS_SUCCESS != ntsResult) 
  {
    wprintf(L"Failed LsaLookupNames - %lu \n",
      LsaNtStatusToWinError(ntsResult));
    return;
  }

  // Get the domain the account resides in.
  myDomain = lrdlDomainList->Domains[ltsTranslatedSID->DomainIndex];
  DomainString = (PWCHAR) LocalAlloc(LPTR, myDomain.Name.Length + 1);
  wcsncpy_s(DomainString,
     myDomain.Name.Length + 1, 
     myDomain.Name.Buffer, 
     myDomain.Name.Length);

  // Display the relative Id. 
  wprintf(L"Relative Id is %lu in domain %ws.\n",
    ltsTranslatedSID->RelativeId,
    DomainString);

  LocalFree(DomainString);
  LsaFreeMemory(ltsTranslatedSID);
  LsaFreeMemory(lrdlDomainList);
}
```



In the preceding example, the function **InitLsaString** converts a Unicode string to an [**LSA\_UNICODE\_STRING**](/windows/desktop/api/lsalookup/ns-lsalookup-_lsa_unicode_string) structure. The code for this function is shown in [Using LSA Unicode Strings](using-lsa-unicode-strings.md).

> [!Note]  
> These translation functions are primarily provided for use by permissions editors to display [*access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-control-list-gly) (ACL) information. A permission editor should always call these functions using the [**Policy**](policy-object.md) object for the system where the name or [*security identifier*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-identifier-gly) SID is located. This ensures that the proper set of trusted domains is referenced during the translation.

 

Windows Access Control also provides functions that perform translations between SIDs and account names: [**LookupAccountName**](https://msdn.microsoft.com/library/windows/desktop/aa379159) and [**LookupAccountSid**](https://msdn.microsoft.com/library/windows/desktop/aa379166). If your application needs to look up an account name or SID and does not use additional LSA Policy functionality, use the Windows Access Control functions instead of the LSA Policy functions. For more information about these functions, see [Access Control](https://msdn.microsoft.com/library/windows/desktop/aa374860).

 

 



