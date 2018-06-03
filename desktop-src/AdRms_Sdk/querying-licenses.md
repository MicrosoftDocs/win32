---
Description: You can use the Active Directory Rights Management Services (AD RMS) SDK to access the underlying eXtensible Rights Markup Language (XrML) in an end-user or owner license.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 7496380a-2848-4353-a672-27fc5a9eed92
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Querying Licenses
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Querying Licenses

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

You can use the Active Directory Rights Management Services (AD RMS) SDK to access the underlying eXtensible Rights Markup Language (XrML) in an end-user or owner license. The SDK hides the complexity of the XrML and makes it easier to create, retrieve, and modify rights, conditions, users, and other XrML structures. The license, as seen by the application, consists of objects, such as rights and principals, and attributes, such as object name or ID.

> [!Note]  
> An application can query an issuance license only for distribution point nodes.

 

When an application first obtains an end-user license, it gets the unbound license which contains all license information that is applicable to all users and environments. This license can be examined, but the rights cannot be exercised.

To use the license, an application must bind to it by calling the [**DRMCreateBoundLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmcreateboundlicense) function. The bound license that is returned has had the licensor chain verified, principals verified, duplicate information removed, and all rights or groups not pertaining to that specific user and environment removed. A bound license is much flatter than an unbound license, which can have a very deeply nested object structure.

The AD RMS SDK presents the license as a hierarchy of attributes and objects that can contain nested objects and their corresponding attributes. This hierarchy can be navigated by querying each object for any nested object, and further querying this object. The following table lists the corresponding bound and unbound license navigation functions.



| Unbound license function                                                         | Bound license function                                                       |
|----------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| [**DRMParseUnboundLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmparseunboundlicense)                         | [**DRMCreateBoundLicense**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmcreateboundlicense)                       |
| [**DRMGetUnboundLicenseAttribute**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetunboundlicenseattribute)           | [**DRMGetBoundLicenseAttribute**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetboundlicenseattribute)           |
| [**DRMGetUnboundLicenseAttributeCount**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetunboundlicenseattributecount) | [**DRMGetBoundLicenseAttributeCount**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetboundlicenseattributecount) |
| [**DRMGetUnboundLicenseObject**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetunboundlicenseobject)                 | [**DRMGetBoundLicenseObject**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetboundlicenseobject)                 |
| [**DRMGetUnboundLicenseObjectCount**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetunboundlicenseobjectcount)       | [**DRMGetBoundLicenseObjectCount**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetboundlicenseobjectcount)       |
| [**DRMCloseQueryHandle**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmclosequeryhandle)                               | [**DRMCloseHandle**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmclosehandle)                                     |



 

The **DRMGetBound\_xxx** and **DRMGetUnbound\_xxx** functions take a parameter that indicates which object to retrieve. After you retrieve the object, you can obtain information about it by calling [**DRMGetBoundLicenseAttribute**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetboundlicenseattribute) or [**DRMGetUnboundLicenseAttribute**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetunboundlicenseattribute). Not all objects or attributes are required to be present in an XrML certificate, and some (ADDRESS, for example) may have more than one value. Therefore, you should enable robust error trapping, and also call the appropriate **DRMGet\_xxx\_Count** function to determine how many values of an attribute or instances of an object exist.

The Msdrmgetinfo.h file included with this SDK contains a list of defined constants that represent most objects and attributes that can be retrieved from a license. The comments in the Msdrmgetinfo.h file indicate whether an item is an object or an attribute, and whether it is found in the bound or unbound license.

When searching for an object in a license or certificate, the [**DRMGetBoundLicenseObject**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetboundlicenseobject) and [**DRMGetUnboundLicenseObject**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmgetunboundlicenseobject) functions only return an object from the top level of the root that was passed in. More deeply nested objects will not be retrieved. Therefore, if passing in a license root object, you cannot attempt to get a right object directly, but must first obtain a work and a rights group.

The only object you can query for in an issuance license is g\_wszQUERY\_DISTRIBUTIONPOINT. The only attributes you can query for are g\_wszQUERY\_IDTYPE, g\_wszQUERY\_IDVALUE, g\_wszQUERY\_NAME, g\_wszQUERY\_ADDRESSTYPE, and g\_wszQUERY\_ADDRESSVALUE.

The following example shows how to enumerate all the attributes and objects of an end-user license.


```C++
#include <stdio.h>
#include <tchar.h>
#include <Wtypes.h>
#include <msdrm.h>
#include <msdrmgetinfo.h>

//--------------------------------------------------------------------
// The DRMCreateUnBoundLicenseQuery function shows how to create a
// license query.
//
// Parameters:
//   wszSecurityProvider -             ID of the security provider.
//   wszManifest -                     Signed XrML manifest.
//   wszMachineChain -                 The machine certificate.
//   wszUnBoundLicenseQueryChain -     The license leaf certificate.
//   
HRESULT DRMCreateUnBoundLicenseQuery(
   PWSTR wszSecurityProvider,
   PWSTR wszManifest,
   PWSTR wszMachineChain,
   PWSTR wszUnBoundLicenseQueryChain)
{
//--------------------------------------------------------------------
// Declare variables.
//
// hLibrary -     Handle to library used to create principal object.
// hEnv -         Handle to the secure environment.
// cTab -         Tab count.
// hQueryRoot -   Handle to the root object of a license.
// 
HRESULT hr = E_FAIL;
DRMHANDLE hLibrary;
DRMENVHANDLE hEnv;
UINT cTab = 0;
DRMQUERYHANDLE hQueryRoot = DRMQUERYHANDLE_INVALID;

//--------------------------------------------------------------------
// Initialize the environment.
//
hr = DRMInitEnvironment(
       DRMSECURITYPROVIDERTYPE_SOFTWARESECREP,  // software security
       DRMSPECTYPE_FILENAME,                    // file name
       wszSecurityProvider,                     // provider ID
       wszManifest,                             // XrML manifest
       wszMachineChain,                         // machine certificate
       &amp;hEnv,                                   // environment handle
       &amp;hLibrary);                              // library handle
if(FAILED(hr))
{
  wprintf(L"\nDRMInitEnvironment failed. " \
          L"hr = 0x%x\n", hr);
  goto e_Exit;
}

//--------------------------------------------------------------------
// Retrieve a handle to an unbound license so that you can navigate
// the license attributes and objects.
//
hr = DRMParseUnboundLicense(
       wszUnBoundLicenseQueryChain, // license leaf certificate
       &amp;hQueryRoot);                // handle of the license root
if(FAILED(hr))
{
  wprintf(L"\nDRMParseUnboundLicense failed. " \
          L"hr = 0x%x\n", hr);
  goto e_Exit;
}

//--------------------------------------------------------------------
// Call the ExtractAllInfo local function to retrieve information
// from the license.
//
hr = ExtractAllInfo(hQueryRoot, cTab);
if(FAILED(hr))
{
  wprintf(L"\nExtractAllInfo failed. " \
          L"hr = 0x%x\n", hr);
  goto e_Exit;
}

//--------------------------------------------------------------------
// Perform cleanup.
//
e_Exit:
DRMCloseHandle(hLibrary); 
DRMCloseEnvironmentHandle(hEnv); 
DRMCloseQueryHandle(hQueryRoot); 

return hr;  
}

//--------------------------------------------------------------------
// The ExtractAllInfo function retrieves attributes and objects
// from a license.
//
// Parameters:
//   hQuery -  Handle to a license root.
//   cTab -    Tab count.
//   
HRESULT ExtractAllInfo(DRMQUERYHANDLE hQuery, UINT cTab)
{

PWSTR  rgszAttributes[] = {g_wszQUERY_NAME,
   g_wszQUERY_ADDRESSTYPE,
   g_wszQUERY_ADDRESSVALUE,
   g_wszQUERY_APPDATANAME,
   g_wszQUERY_APPDATAVALUE,
   g_wszQUERY_CONDITIONLIST,
   g_wszQUERY_FROMTIME,
   g_wszQUERY_IDTYPE,
   g_wszQUERY_IDVALUE,
   g_wszQUERY_ISSUEDTIME,
   g_wszQUERY_INTERVALTIMECONDITION,
   g_wszQUERY_INTERVALTIMEINTERVAL,
   g_wszQUERY_MAXVERSION,
   g_wszQUERY_MINVERSION,
   g_wszQUERY_REFRESHPERIOD,
   g_wszQUERY_RIGHTSPARAMETERNAME,
   g_wszQUERY_RIGHTSPARAMETERVALUE,
   g_wszQUERY_SKUTYPE,
   g_wszQUERY_SKUVALUE,
   g_wszQUERY_TIMEINTERVAL,
   g_wszQUERY_UNTILTIME,
   g_wszQUERY_VALIDITYFROMTIME,
   g_wszQUERY_VALIDITYUNTILTIME      
}; 
PWSTR rgszObjects[] = { g_wszQUERY_ACCESSCONDITION,
   g_wszQUERY_DISTRIBUTIONPOINT,
   g_wszQUERY_OBJECTTYPE,
   g_wszQUERY_WORK, 
   g_wszQUERY_GROUPIDENTITYPRINCIPAL,
   g_wszQUERY_FIRSTUSETAG,
   g_wszQUERY_ISSUEDPRINCIPAL,
   g_wszQUERY_ISSUER,
   g_wszQUERY_OWNER,
   g_wszQUERY_PRINCIPAL,
   g_wszQUERY_RANGETIMECONDITION,
   g_wszQUERY_OSEXCLUSIONCONDITION,
   g_wszQUERY_REVOCATIONCONDITION,
   g_wszQUERY_RIGHT,
   g_wszQUERY_RIGHTSGROUP
};

UINT  cAttributes = sizeof(rgszAttributes) / sizeof(PWSTR);  
UINT  cObjects = sizeof(rgszObjects) / sizeof(PWSTR);  
UINT  iAttribute, i, cSub, cBuffer, iObject;
BYTE* pbBuffer = NULL;  
HRESULT   hr = S_OK;
DRMENCODINGTYPE eType;    
DRMQUERYHANDLE  hSub = NULL;

//--------------------------------------------------------------------
// Retrieve the attributes.
//
for (iAttribute = 0 ; iAttribute < cAttributes ; iAttribute++)
{
   if (S_OK == (hr = DRMGetUnboundLicenseAttributeCount(
                        hQuery,
                        rgszAttributes[iAttribute],
                        &amp;cSub)))
   {
      for (i = 0 ; i < cSub ; i++)
      {
         hr = DRMGetUnboundLicenseAttribute(
                 hQuery,
                 rgszAttributes[iAttribute],
                 i,
                 &amp;eType,
                 &amp;cBuffer,
                 NULL);
         if(FAILED(hr))
         {
            wprintf(L"\nDRMGetUnboundLicenseAttribute failed. " \
            L"hr = 0x%x\n", hr);
            goto e_Exit;
         }

         pbBuffer = new BYTE[cBuffer]; 

         hr = DRMGetUnboundLicenseAttribute(
                 hQuery,
                 rgszAttributes[iAttribute],
                 i,
                 &amp;eType,
                 &amp;cBuffer,
                 pbBuffer);
          if(FAILED(hr))
         {
            wprintf(L"\nDRMGetUnboundLicenseAttribute failed. " \
            L"hr = 0x%x\n", hr);
            goto e_Exit;
         }
         switch(eType)
         {
            case DRMENCODINGTYPE_STRING:
               break;

            case DRMENCODINGTYPE_TIME:
               break;

            case DRMENCODINGTYPE_UINT:
               break;

            case DRMENCODINGTYPE_LONG:                        
               break;

            case DRMENCODINGTYPE_RAW:
               break;

            default:
               break;
         }

         delete[] pbBuffer;
         pbBuffer = NULL;                            
         }
     } 
 } 

//--------------------------------------------------------------------
// Retrieve the objects.
//
for (iObject = 0 ; iObject < cObjects ; iObject++)
{
   if (S_OK == (hr = DRMGetUnboundLicenseObjectCount(
                        hQuery,  
                        rgszObjects[iObject],
                        &amp;cSub))) 
   {
      for (i = 0 ; i < cSub ; i++)
      {
          hr = DRMGetUnboundLicenseObject(
                 hQuery,   
                 rgszObjects[iObject],
                 i,
                 &amp;hSub);
         if(FAILED(hr))
         {
            wprintf(L"\nDRMGetUnboundLicenseObject failed. " \
            L"hr = 0x%x\n", hr);
            goto e_Exit;
         }
         hr = ExtractAllInfo(hSub,cTab+4);
         if(FAILED(hr))
         {
            wprintf(L"\nExtractAllInfo failed. " \
            L"hr = 0x%x\n", hr);
            goto e_Exit;
         }
         hr = DRMCloseQueryHandle(hSub);
         if(FAILED(hr))
         {
            wprintf(L"\nDRMCloseQueryHandle failed. " \
            L"hr = 0x%x\n", hr);
            goto e_Exit;
         }
         hSub = NULL;
      }
  } 
}

e_Exit:
delete[] pbBuffer;
DRMCloseQueryHandle(hSub);
return hr;
}

```



## Related topics

<dl> <dt>

[Binding to a License](binding-to-a-license.md)
</dt> <dt>

[Bound License Structure](bound-license-structure.md)
</dt> <dt>

[Unbound License Structure](unbound-license-structure.md)
</dt> <dt>

[Working with Licenses and Templates](working-with-licenses-and-templates.md)
</dt> </dl>

 

 



