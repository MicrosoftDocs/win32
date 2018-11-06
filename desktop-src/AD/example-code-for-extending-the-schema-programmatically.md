---
title: Example Code for Extending the Schema Programmatically
description: This topic includes a C++ code example that programmatically extends the Active Directory Schema.
ms.assetid: e84678c5-ac12-424b-ba6c-c6cba23e4ff6
ms.tgt_platform: multiple
keywords:
- Example Code for Extending the Schema Programmatically AD
- Extending the Schema Programmatically AD , Example Code for
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Extending the Schema Programmatically

This topic includes a C++ code example that programmatically extends the Active Directory Schema.


```C++
/*
**  schema.cxx: The following C++ code example installs an Active 
**              Directory Schema extension.
**
**    This example creates six new attributes, one new class, and 
**    modifies two existing classes by adding new MAY HAVE attributes.
**
**    Attributes:    courseTugboat          integer
**                   speedTugboat           integer
**                   maxPayloadTugboat      integer
**                   allowedTugboat         integer
**                   consistencyGUID        octet string
**                   consistencyChildCount  integer
**
**                Class:    policyParametersTugboat
**
**                Classes Modified: container, groupPolicyContainer
**
**                The modified classes have the two consistency 
**                attributes added.
**
**  Notes:        Must run on a DC which is the current Schema Master 
**                and has schema updates enabled using the registry key 
**                and value:
**
**          KEY:  HKEY_LOCAL_MACHINE\CurrentControlSet\Services\NTDS\Parameters
**          Value:    Schema Update Allowed, REG_DWORD, 1
**
**  Libraries:  activeds.lib, adsiid.lib
**
*/
 
#include <windows.h>
#include <ole2.h>
#include <iads.h>
#include <activeds.h>
#include <stdio.h>
#include <atlbase.h>

#define COURSE_ATTR_NAME L"Course-Tugboat"
#define COURSE_ATTR_RDN L"CN=Course-Tugboat"
#define COURSE_ATTR_LDAP_NAME L"courseTugboat"

#define SPEED_ATTR_NAME L"Speed-Tugboat"
#define SPEED_ATTR_RDN L"CN=Speed-Tugboat"
#define SPEED_ATTR_LDAP_NAME L"speedTugboat"

#define MAX_PAYLOAD_ATTR_NAME L"Max-Payload-Tugboat"
#define MAX_PAYLOAD_ATTR_RDN L"CN=Max-Payload-Tugboat"
#define MAX_PAYLOAD_ATTR_LDAP_NAME L"maxPayloadTugboat"

#define ALLOWED_ATTR_NAME L"Allowed-Tugboat"
#define ALLOWED_ATTR_RDN L"CN=Allowed-Tugboat"
#define ALLOWED_ATTR_LDAP_NAME L"allowedTugboat"

#define CONSISTENCY_GUID_ATTR_NAME L"Consistency-GUID"
#define CONSISTENCY_GUID_ATTR_RDN L"CN=Consistency-GUID"
#define CONSISTENCY_GUID_ATTR_LDAP_NAME L"consistencyGUID"

#define CONSISTENCY_CHILD_ATTR_NAME L"Consistency-Child-Count"
#define CONSISTENCY_CHILD_ATTR_RDN L"CN=Consistency-Child-Count"
#define CONSISTENCY_CHILD_ATTR_LDAP_NAME L"consistencyChildCount"

#define TUGBOAT_CLASS_NAME L"Policy-Parameters-Tugboat" 
#define TUGBOAT_CLASS_RDN L"CN=Policy-Parameters-Tugboat" 

// Forward declaration of the error report.
 
void ReportErrorW(LPCWSTR pwszDefaultMsg, DWORD dwErr);
 
// GUIDs for schema extensions. Provide your own GUID for each 
// extension so they are the same in every installation. If the 
// DS assigns them your GUIDs will be different in every installation; 
// this will affect system performance when moving to an 
// identity-based schema.
 
// GUIDS for the policy attributes
 
// {C45F05B2-4D16-11d2-800E-0080C76670C0}
static const GUID attrGuid1 = 
{ 0xc45f05b2, 0x4d16, 0x11d2, { 0x80, 0xe, 0x0, 0x80, 0xc7, 0x66, 0x70, 0xc0 } };
// {C45F05B3-4D16-11d2-800E-0080C76670C0}
static const GUID attrGuid2 = 
{ 0xc45f05b3, 0x4d16, 0x11d2, { 0x80, 0xe, 0x0, 0x80, 0xc7, 0x66, 0x70, 0xc0 } };
// {C45F05B4-4D16-11d2-800E-0080C76670C0}
static const GUID attrGuid3 = 
{ 0xc45f05b4, 0x4d16, 0x11d2, { 0x80, 0xe, 0x0, 0x80, 0xc7, 0x66, 0x70, 0xc0 } };
// {C45F05B6-4D16-11d2-800E-0080C76670C0}
static const GUID attrGuid4 = 
{ 0xc45f05b6, 0x4d16, 0x11d2, { 0x80, 0xe, 0x0, 0x80, 0xc7, 0x66, 0x70, 0xc0 } };
 
// GUIDs for Consistency checking attributes
 
// {7707464B-4D9D-11d2-AF2D-00C04FB9624E}
static const GUID attrGuid5 = 
{ 0x7707464b, 0x4d9d, 0x11d2, { 0xaf, 0x2d, 0x0, 0xc0, 0x4f, 0xb9, 0x62, 0x4e } };
// {7707464C-4D9D-11d2-AF2D-00C04FB9624E}
static const GUID attrGuid6 = 
{ 0x7707464c, 0x4d9d, 0x11d2, { 0xaf, 0x2d, 0x0, 0xc0, 0x4f, 0xb9, 0x62, 0x4e } };
 
 
// {C45F05B5-4D16-11d2-800E-0080C76670C0}
static const GUID classGuid1 = 
{ 0xc45f05b5, 0x4d16, 0x11d2, { 0x80, 0xe, 0x0, 0x80, 0xc7, 0x66, 0x70, 0xc0 } };
 
 
void main(void)
{
    HRESULT hr;
    IADs    *pRoot = NULL;
    VARIANT varDSRoot, 
            varSchemaUpdate;
    LPWSTR  pwszDSPath = NULL;
    LPWSTR  pwszGPCPath = NULL;
    LPWSTR  pwszContPath = NULL;
 
    // Returned by CreateDSObject
    IDispatch *pDisp = NULL;
 
    // Pointers to schema objects
    IDirectoryObject    *pSchema = NULL, 
                        *pGpc = NULL;
 
    // Data structures for creating schema objects
    //
    // attribute values: These are unions and cannot be 
    // statically initialized.
    //
    ADSVALUE        cn,
                    singleValued,
                    oid,
                    syntax,
                    omSyntax,
                    ldapname,
                    idGuid,
                    objectClass,
                    objectClassCategory,
                    subClassOf,
                    defaultSecurityDesc,
                    defaultHidingValue,
                    mayContain[6];
 
    // ATTR_INFO for creating an attributeSchema object
    // Each ADS_ATTR_INFO describes one attribute of an object to be
    // stored in the DS.
 
    ADS_ATTR_INFO   attrArray[] = {
        {L"cn", ADS_ATTR_UPDATE, ADSTYPE_CASE_IGNORE_STRING, &cn, 1},
        {L"isSingleValued", ADS_ATTR_UPDATE, ADSTYPE_BOOLEAN, &singleValued, 1},
        {L"objectClass", ADS_ATTR_UPDATE, ADSTYPE_CASE_IGNORE_STRING, &objectClass, 1},
        {L"attributeID", ADS_ATTR_UPDATE, ADSTYPE_CASE_IGNORE_STRING, &oid, 1},
        {L"attributeSyntax", ADS_ATTR_UPDATE, ADSTYPE_INTEGER, &syntax, 1},
        {L"oMSyntax", ADS_ATTR_UPDATE, ADSTYPE_INTEGER, &omSyntax, 1},
        {L"lDAPDisplayName", ADS_ATTR_UPDATE, ADSTYPE_CASE_IGNORE_STRING, &ldapname, 1},
        {L"schemaIdGUID", ADS_ATTR_UPDATE, ADSTYPE_OCTET_STRING, &idGuid, 1},
    };
 
    // ATTR_INFO for creating a classSchema object
 
    ADS_ATTR_INFO   classArray[] = {
        {L"cn", ADS_ATTR_UPDATE, ADSTYPE_CASE_IGNORE_STRING, &cn, 1},
        {L"objectClass", ADS_ATTR_UPDATE, ADSTYPE_CASE_IGNORE_STRING, &objectClass, 1},
        {L"governsID", ADS_ATTR_UPDATE, ADSTYPE_CASE_IGNORE_STRING, &oid, 1},
        {L"objectClassCategory", ADS_ATTR_UPDATE, ADSTYPE_INTEGER, &objectClassCategory, 1},
        {L"schemaIdGUID", ADS_ATTR_UPDATE, ADSTYPE_OCTET_STRING, &idGuid, 1},
        {L"defaultSecurityDescriptor", ADS_ATTR_UPDATE, ADSTYPE_CASE_IGNORE_STRING, &defaultSecurityDesc, 1},
        {L"defaultHidingValue", ADS_ATTR_UPDATE, ADSTYPE_BOOLEAN, &defaultHidingValue, 1},
        {L"subClassOf", ADS_ATTR_UPDATE, ADSTYPE_CASE_IGNORE_STRING, &subClassOf, 1},
        {L"mayContain", ADS_ATTR_UPDATE, ADSTYPE_CASE_IGNORE_STRING, &mayContain[0], 6},
    };
 
    // ATTR_INFO for adding attributes to Group Policy Container
    ADS_ATTR_INFO gpcUpdate[] = {{L"mayContain", ADS_ATTR_APPEND, ADSTYPE_CASE_IGNORE_STRING, &mayContain[0], 2},};
 
 
    DWORD           dwAttrs;
    ULONG           iAttrsMod;
 
    hr = CoInitializeEx(NULL, COINIT_MULTITHREADED | COINIT_DISABLE_OLE1DDE);
 
    //  Get the name of the schema container for this domain. 
    //  Read the Root DSE from the default DS,  which will be 
    //  the DS for the local domain. This will get the name of the 
    //  schema container, stored in the "schemaNamingContext" 
    // operational attribute. 

    hr = ADsGetObject(L"LDAP://RootDSE",
                      IID_IADs,
                      (void**)&pRoot);
    if(FAILED(hr))
    {
        goto cleanup;
    }
 
    // Get IDirectoryObject on the root DSE as well; use this for 
    // forcing a schema update later.
 
    VariantInit(&varDSRoot);
    hr = pRoot->Get(CComBSTR("schemaNamingContext"), &varDSRoot);
    if(FAILED(hr))
    {
        goto cleanup;
    }
    wprintf(L"\nDS Root:%S\n", varDSRoot.bstrVal);
    
    // ADsPath of the schema container
    pwszDSPath = new WCHAR[7 + lstrlenW(varDSRoot.bstrVal) + 1];
    if(!pwszDSPath)
    {
        goto cleanup;
    }
    wcscpy_s(pwszDSPath, L"LDAP://");
    wcscat_s(pwszDSPath, varDSRoot.bstrVal);
 
    // ADsPath of the Group Policy Container class-schema object
    pwszGPCPath = new WCHAR[33 + lstrlenW(varDSRoot.bstrVal) + 1];
    if(!pwszGPCPath)
    {
        goto cleanup;
    }
    wcscpy_s(pwszGPCPath, L"LDAP://CN=Group-Policy-Container,");
    wcscat_s(pwszGPCPath, varDSRoot.bstrVal);
 
    // ADsPath of the Container class-schema object
    pwszContPath = new WCHAR[20 + lstrlenW(varDSRoot.bstrVal) + 1];
    if(!pwszContPath)
    {
        goto cleanup;
    }
    wcscpy_s(pwszContPath, L"LDAP://CN=Container,");
    wcscat_s(pwszContPath, varDSRoot.bstrVal);
 
    // Bind to the schema container and get the IDirectoryObject 
    // interface for it.
    hr = ADsGetObject(pwszDSPath,
                      IID_IDirectoryObject,
                      (void**)&pSchema);
    if(FAILED(hr))
    {
        goto cleanup;
    }
 
 
    //***************************************************************
    // Consistency-Child-Count
    //***************************************************************
 
    // Create a new attribute object. Set the values into the 
    // attribute unions, then call the method to create the object.
    //

    // Calculate attribute count:
    dwAttrs = sizeof(attrArray)/sizeof(ADS_ATTR_INFO); 
 
    cn.dwType = ADSTYPE_CASE_IGNORE_STRING;
    cn.CaseIgnoreString = CONSISTENCY_CHILD_ATTR_NAME;
    singleValued.dwType = ADSTYPE_BOOLEAN;
    singleValued.Boolean = VARIANT_TRUE;
    oid.dwType = ADSTYPE_CASE_IGNORE_STRING;

    // Reserved. Test OID:
    oid.CaseIgnoreString = L"1.2.840.113556.1.4.7000.161"; 
    objectClass.dwType = ADSTYPE_CASE_IGNORE_STRING;
    objectClass.CaseIgnoreString = L"attributeSchema";
    syntax.dwType = ADSTYPE_CASE_IGNORE_STRING;
    syntax.CaseIgnoreString = L"2.5.5.9";    // 2.5.5.9 = Integer
    omSyntax.dwType = ADSTYPE_INTEGER;
    omSyntax.Integer = 2;
    //
    // The LDAP display name is defaulted by the server and 
    // should not be provided unless different than the name 
    // computed from the CN attribute - the LDAP name is the CN  
    // with the hyphens removed and case delimiting substituted. 
    // The initial character is always lowercase. For this example, 
    // an explicit LDAP display name is provided to show 
    // how it is done.
    ldapname.dwType = ADSTYPE_CASE_IGNORE_STRING;
    ldapname.CaseIgnoreString = CONSISTENCY_CHILD_ATTR_LDAP_NAME;
    //
    // Schema-ID-Guid is provided by the server is the client 
    // does not provide it. This is a good example of how to 
    // write an Octet String to the DS.
    idGuid.dwType = ADSTYPE_OCTET_STRING;
    idGuid.OctetString.dwLength = sizeof(attrGuid6);
    idGuid.OctetString.lpValue = (LPBYTE)&attrGuid6;
 
    hr = pSchema->CreateDSObject(CONSISTENCY_CHILD_ATTR_RDN,
                                 attrArray,
                                 dwAttrs,
                                 &pDisp);
    if (FAILED(hr)) 
    {
        ReportErrorW(L"CreateDSObject failed.", hr);
    } 
    else 
    {
        wprintf(L"\n");
        wprintf(CONSISTENCY_CHILD_ATTR_NAME);
        wprintf(L" Attribute defined.\n");
 
        // The IDispatch interface returned by the CreateDSObject 
        // call is not used. Release it now.
        pDisp->Release();
        pDisp = NULL;
    }
 
 
    //***************************************************************
    // Consistency-GUID
    //***************************************************************
 
    // Create a new attribute object. Set the values into the 
    // attribute unions, then call the method to create the object.
    //
 
    cn.dwType = ADSTYPE_CASE_IGNORE_STRING;
    cn.CaseIgnoreString = L"Consistency-GUID";
    singleValued.dwType = ADSTYPE_BOOLEAN;
    singleValued.Boolean = VARIANT_TRUE;
    oid.dwType = ADSTYPE_CASE_IGNORE_STRING;
    // Reserved. Test OID:
    oid.CaseIgnoreString = L"1.2.840.113556.1.4.7000.160"; 
    objectClass.dwType = ADSTYPE_CASE_IGNORE_STRING;
    objectClass.CaseIgnoreString = L"attributeSchema";
    syntax.dwType = ADSTYPE_CASE_IGNORE_STRING;
    syntax.CaseIgnoreString = L"2.5.5.10"; // 2.5.5.10 = Octet String
    omSyntax.dwType = ADSTYPE_INTEGER;
    omSyntax.Integer = 4;
    //
    // The LDAP display name will be defaulted by the server and 
    // should not be provided unless different than the name 
    // computed from the CN attribute - the LDAP name is the CN  
    // with the hyphens removed and case delimiting substituted.
    // The initial character is always lowercase. For this example,
    // an explicit LDAP display name is provided to show
    // how it is done.
    ldapname.dwType = ADSTYPE_CASE_IGNORE_STRING;
    ldapname.CaseIgnoreString = CONSISTENCY_GUID_ATTR_LDAP_NAME;
    //
    // Schema-ID-Guid is provided by the server is the client does
    // not provide it. This is a good example of how to write an 
    // Octet String to the DS.
    idGuid.dwType = ADSTYPE_OCTET_STRING;
    idGuid.OctetString.dwLength = sizeof(attrGuid5);
    idGuid.OctetString.lpValue = (LPBYTE)&attrGuid5;
 
    hr = pSchema->CreateDSObject(CONSISTENCY_GUID_ATTR_RDN,
                                 attrArray,
                                 dwAttrs,
                                 &pDisp);
    if (FAILED(hr)) 
    {
        ReportErrorW(L"CreateDSObject failed.", hr);
    } 
    else 
    {
        wprintf(L"\n");
        wprintf(CONSISTENCY_GUID_ATTR_NAME);
        wprintf(L" Attribute defined.\n");
 
        // The IDispatch interface, returned by the CreateDSObject
        // call, is not used. Release it now.
        pDisp->Release();
        pDisp = NULL;
    }
 
    //****************************************************************
    // Course-Tugboat
    //****************************************************************
 
    // Create a new attribute object. Set the values into the 
    // attribute unions, then call the method to create the object.
 
    // Calculate attribute count:
    dwAttrs = sizeof(attrArray)/sizeof(ADS_ATTR_INFO); 
 
    cn.dwType = ADSTYPE_CASE_IGNORE_STRING;
    cn.CaseIgnoreString = COURSE_ATTR_NAME;
    singleValued.dwType = ADSTYPE_BOOLEAN;
    singleValued.Boolean = VARIANT_TRUE;
    oid.dwType = ADSTYPE_CASE_IGNORE_STRING;

    // Reserved. Test OID:
    oid.CaseIgnoreString = L"1.2.840.113556.1.4.7000.155"; 
    objectClass.dwType = ADSTYPE_CASE_IGNORE_STRING;
    objectClass.CaseIgnoreString = L"attributeSchema";
    syntax.dwType = ADSTYPE_CASE_IGNORE_STRING;
    syntax.CaseIgnoreString = L"2.5.5.9";   // 2.5.5.9 = Integer
    omSyntax.dwType = ADSTYPE_INTEGER;
    omSyntax.Integer = 2;
    //
    // The LDAP display name is defaulted by the server and should 
    // not be provided unless different than the name computed from 
    // the CN attribute - the LDAP name is the CN with the hyphens 
    // removed and case delimiting substituted. The initial character 
    // is always lowercase. For this example, an explicit LDAP display 
    // name is provided to show how it is done.
    ldapname.dwType = ADSTYPE_CASE_IGNORE_STRING;
    ldapname.CaseIgnoreString = COURSE_ATTR_LDAP_NAME;
    //
    // Schema-ID-Guid is provided by the server is the client does 
    // not provide it. This is a good example of how to write an 
    // Octet String to the DS.
    idGuid.dwType = ADSTYPE_OCTET_STRING;
    idGuid.OctetString.dwLength = sizeof(attrGuid1);
    idGuid.OctetString.lpValue = (LPBYTE)&attrGuid1;
 
    hr = pSchema->CreateDSObject(COURSE_ATTR_RDN,
                                 attrArray,
                                 dwAttrs,
                                 &pDisp);
    if (FAILED(hr)) 
    {
        ReportErrorW(L"CreateDSObject failed.", hr);
    } 
    else 
    { 
        wprintf(L"\n");
        wprintf(COURSE_ATTR_NAME);
        wprintf(L" Attribute defined.\n");
 
        // Do not use the IDispatch interface returned by the 
        // CreateDSObject call. Release it now.
        pDisp->Release();
        pDisp = NULL;
    }
 
 
    //**********************************************************************
    // Speed-Tugboat
    //**********************************************************************
 
    // Create a new attribute object. Set the values into the 
    // attribute unions, then call the method to create the object.
 
    // Calculate attribute count:
    dwAttrs = sizeof(attrArray)/sizeof(ADS_ATTR_INFO); 
 
    cn.dwType = ADSTYPE_CASE_IGNORE_STRING;
    cn.CaseIgnoreString = SPEED_ATTR_NAME;
    singleValued.dwType = ADSTYPE_BOOLEAN;
    singleValued.Boolean = VARIANT_TRUE;
    oid.dwType = ADSTYPE_CASE_IGNORE_STRING;

    // Reserved. Test OID:
    oid.CaseIgnoreString = L"1.2.840.113556.1.4.7000.156";
    objectClass.dwType = ADSTYPE_CASE_IGNORE_STRING;
    objectClass.CaseIgnoreString = L"attributeSchema";
    syntax.dwType = ADSTYPE_CASE_IGNORE_STRING;
    syntax.CaseIgnoreString = L"2.5.5.9"; // 2.5.5.9 = Integer
    omSyntax.dwType = ADSTYPE_INTEGER;
    omSyntax.Integer = 2;
    //
    // The LDAP display name is defaulted by the server and should 
    // not be provided unless different than the name computed 
    // from the CN attribute - the LDAP name is the CN with the  
    // hyphens removed and case delimiting substituted. The initial
    // character is always lowercase. For this example, an explicit
    //  LDAP display name is provided to show how it is done.
    ldapname.dwType = ADSTYPE_CASE_IGNORE_STRING;
    ldapname.CaseIgnoreString = SPEED_ATTR_LDAP_NAME;
    //
    // Schema-ID-Guid is provided by the server if the client does 
    // not provide it. This is a good example of how to write an 
    // Octet String to the DS.
    idGuid.dwType = ADSTYPE_OCTET_STRING;
    idGuid.OctetString.dwLength = sizeof(attrGuid2);
    idGuid.OctetString.lpValue = (LPBYTE)&attrGuid2;
 
    hr = pSchema->CreateDSObject(SPEED_ATTR_RDN,
                                 attrArray,
                                 dwAttrs,
                                 &pDisp);
    if (FAILED(hr)) 
    {
        ReportErrorW(L"CreateDSObject failed.", hr);
    } 
    else 
    {
        wprintf(L"\n");
        wprintf(SPEED_ATTR_NAME);
        wprintf(L" Attribute defined.\n");
 
        // Do not use the IDispatch interface returned by the 
        // CreateDSObject call. Release it now.
        pDisp->Release();
        pDisp = NULL;
    }
 
 
    //****************************************************************
    // Max-Payload-Tugboat
    //****************************************************************

    // Create a new attribute object. Set the values into the 
    // attribute unions, then call the method to create the object.
    //
 
    // Calculate attribute count:
    dwAttrs = sizeof(attrArray)/sizeof(ADS_ATTR_INFO); 
 
    cn.dwType = ADSTYPE_CASE_IGNORE_STRING;
    cn.CaseIgnoreString = MAX_PAYLOAD_ATTR_NAME;
    singleValued.dwType = ADSTYPE_BOOLEAN;
    singleValued.Boolean = VARIANT_TRUE;
    oid.dwType = ADSTYPE_CASE_IGNORE_STRING;
    oid.CaseIgnoreString = L"1.2.840.113556.1.4.7000.157";
    objectClass.dwType = ADSTYPE_CASE_IGNORE_STRING;
    objectClass.CaseIgnoreString = L"attributeSchema";
    syntax.dwType = ADSTYPE_CASE_IGNORE_STRING;
    syntax.CaseIgnoreString = L"2.5.5.9"; // 2.5.5.9 = Integer
    omSyntax.dwType = ADSTYPE_INTEGER;
    omSyntax.Integer = 2;
    //
    // The LDAP display name is defaulted by the server and should
    // not be provided unless different than the name computed from 
    // the CN attribute - the LDAP name is the CN with the hyphens 
    // removed and case delimiting substituted. The initial character 
    // is always lowercase. For this example, an explicit LDAP  
    // display name is provided to show how it is done.
    ldapname.dwType = ADSTYPE_CASE_IGNORE_STRING;
    ldapname.CaseIgnoreString = MAX_PAYLOAD_ATTR_LDAP_NAME;
    //
    // Schema-ID-Guid is provided by the server is the client 
    // does not provide it. This is a good example of how to write 
    // an Octet String to the DS.
    idGuid.dwType = ADSTYPE_OCTET_STRING;
    idGuid.OctetString.dwLength = sizeof(attrGuid3);
    idGuid.OctetString.lpValue = (LPBYTE)&attrGuid3;
 
    hr = pSchema->CreateDSObject(MAX_PAYLOAD_ATTR_RDN,
                                 attrArray,
                                 dwAttrs,
                                 &pDisp);
    if (FAILED(hr)) 
    {
        ReportErrorW(L"CreateDSObject failed.", hr);
    } 
    else 
    {
        wprintf(L"\n");
        wprintf(MAX_PAYLOAD_ATTR_NAME);
        wprintf(L" Attribute defined.\n");
 
        // Do not use the IDispatch interface returned by the 
        // CreateDSObject call. Release it now.
        pDisp->Release();
        pDisp = NULL;
    }
 
 
    //*************************************************************
    // Allowed-Tugboat
    //*************************************************************
 
    // Create a new attribute object. Set the values into the 
    // attribute unions, then call the method to create the object.
    //
 
    // Calculate attribute count:
    dwAttrs = sizeof(attrArray)/sizeof(ADS_ATTR_INFO); 
 
    cn.dwType = ADSTYPE_CASE_IGNORE_STRING;
    cn.CaseIgnoreString = ALLOWED_ATTR_NAME;
    singleValued.dwType = ADSTYPE_BOOLEAN;
    singleValued.Boolean = VARIANT_TRUE;
    oid.dwType = ADSTYPE_CASE_IGNORE_STRING;
    oid.CaseIgnoreString = L"1.2.840.113556.1.4.7000.159"; 
    objectClass.dwType = ADSTYPE_CASE_IGNORE_STRING;
    objectClass.CaseIgnoreString = L"attributeSchema";
    syntax.dwType = ADSTYPE_CASE_IGNORE_STRING;
    syntax.CaseIgnoreString = L"2.5.5.8";    // 2.5.5.8 = Boolean
    omSyntax.dwType = ADSTYPE_INTEGER;
    omSyntax.Integer = 1;
    //
    // The LDAP display name is defaulted by the server and should
    // not be provided unless different than the name computed 
    // from the CN attribute - the LDAP name is the CN with the 
    // hyphens removed and  case delimiting substituted. The initial 
    // character is always lowercase. For this example, an explicit 
    // LDAP display name is provided to show how it is done.
    ldapname.dwType = ADSTYPE_CASE_IGNORE_STRING;
    ldapname.CaseIgnoreString = ALLOWED_ATTR_LDAP_NAME;
    //
    // Schema-ID-Guid is provided by the server is the client does not
    // provide it. This is a good example of how to write an 
    // Octet String to the DS.

    idGuid.dwType = ADSTYPE_OCTET_STRING;
    idGuid.OctetString.dwLength = sizeof(attrGuid4);
    idGuid.OctetString.lpValue = (LPBYTE)&attrGuid4;
 
    hr = pSchema->CreateDSObject(ALLOWED_ATTR_RDN,
                                 attrArray,
                                 dwAttrs,
                                 &pDisp);
    if (FAILED(hr)) 
    {
        ReportErrorW(L"CreateDSObject failed.", hr);
    } 
    else 
    {
        wprintf(L"\n");
        wprintf(ALLOWED_ATTR_NAME);
        wprintf(L" Attribute defined.\n");
 
        // Do not use the IDispatch interface returned by the 
        // CreateDSObject call. Release it now.
        pDisp->Release();
        pDisp = NULL;
    }
 
 
    // Force an update of the schema cache to create the class that 
    // includes these attributes. Force a synchronous schema update 
    // by writing the operational attribute "schemaUpdateNow" to 
    // the Root DSE.
    varSchemaUpdate.vt = VT_I4;
    varSchemaUpdate.intVal = 1;
    hr = pRoot->Put(CComBSTR("schemaUpdateNow"), varSchemaUpdate);
    hr = pRoot->SetInfo();
    if (FAILED(hr)) 
    {
        ReportErrorW(L"Force Schema Recalc failed.", hr);
    }
 
 
    //***************************************************************
    // Policy-Parameters-Tugboat
    //***************************************************************
    //
    // Create a new class object and add attributes 
    // (including the new ones) to the class.
    //
    cn.dwType = ADSTYPE_CASE_IGNORE_STRING;
    cn.CaseIgnoreString = TUGBOAT_CLASS_NAME;
    objectClass.dwType = ADSTYPE_CASE_IGNORE_STRING;
    objectClass.CaseIgnoreString = L"classSchema";
    oid.dwType = ADSTYPE_CASE_IGNORE_STRING;
    oid.CaseIgnoreString = L"1.2.840.113556.1.5.7000.92";
    subClassOf.dwType = ADSTYPE_CASE_IGNORE_STRING;
    subClassOf.CaseIgnoreString = L"serviceConnectionPoint";
    defaultSecurityDesc.dwType = ADSTYPE_CASE_IGNORE_STRING;
    defaultSecurityDesc.CaseIgnoreString = L"D:(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)(A;;RPLCLORC;;;AU)S:(AU;SAFA;WDWOSDDTWPCRCCDCSW;;;WD)";
    defaultHidingValue.dwType = ADSTYPE_BOOLEAN;
    defaultHidingValue.Boolean = -1;
    mayContain[0].dwType = ADSTYPE_CASE_IGNORE_STRING;
    mayContain[0].CaseIgnoreString = COURSE_ATTR_LDAP_NAME;
    mayContain[1].dwType = ADSTYPE_CASE_IGNORE_STRING;
    mayContain[1].CaseIgnoreString = SPEED_ATTR_LDAP_NAME;
    mayContain[2].dwType = ADSTYPE_CASE_IGNORE_STRING;
    mayContain[2].CaseIgnoreString = MAX_PAYLOAD_ATTR_LDAP_NAME;
    mayContain[3].dwType = ADSTYPE_CASE_IGNORE_STRING;
    mayContain[3].CaseIgnoreString = ALLOWED_ATTR_LDAP_NAME;
    mayContain[4].dwType = ADSTYPE_CASE_IGNORE_STRING;
    mayContain[4].CaseIgnoreString = CONSISTENCY_GUID_ATTR_LDAP_NAME;
    mayContain[5].dwType = ADSTYPE_CASE_IGNORE_STRING;
    mayContain[5].CaseIgnoreString = CONSISTENCY_CHILD_ATTR_LDAP_NAME;
 
    // Object-Class-Category=
    // 88_CLASS           0
    // STRUCTURAL_CLASS   1
    // ABSTRACT_CLASS     2
    // AUXILIARY_CLASS    3
    objectClassCategory.dwType = ADSTYPE_INTEGER;
    objectClassCategory.Integer = 1; 
    
     // Calculate attribute count:
    dwAttrs = sizeof(classArray)/sizeof(ADS_ATTR_INFO);
 
    hr = pSchema->CreateDSObject(TUGBOAT_CLASS_RDN,
                                 classArray,
                                 dwAttrs,
                                 &pDisp);
    if (FAILED(hr)) 
    {
        ReportErrorW(L"CreateDSObject failed.", hr);
    } 
    else 
    {
        wprintf(L"\nClass defined.\n");
 
        // Do not use the IDispatch interface returned by the 
        // CreateDSObject call. Release it now.
        pDisp->Release();
        pDisp = NULL;
    }
 
    //************************************************************
    // Add the consistency attributes to Group-Policy-Container
    // and Container
    //************************************************************
 
    hr = ADsGetObject(pwszGPCPath,
                      IID_IDirectoryObject,
                      (void**)&pGpc);
 
    if (FAILED(hr)) 
    {
        ReportErrorW(L"Read GPC class object failed.", hr);
        goto cleanup;
    } 
    else 
    {
        wprintf(L"\nRetrieved GPC class object.\n");
 
        mayContain[0].dwType = ADSTYPE_CASE_IGNORE_STRING;
        mayContain[0].CaseIgnoreString = 
               CONSISTENCY_GUID_ATTR_LDAP_NAME;
        mayContain[1].dwType = ADSTYPE_CASE_IGNORE_STRING;
        mayContain[1].CaseIgnoreString = 
               CONSISTENCY_CHILD_ATTR_LDAP_NAME;
        hr = pGpc->SetObjectAttributes(gpcUpdate,
                                       1,
                                       &iAttrsMod);
        if (FAILED(hr)) 
        {
            ReportErrorW(L"Update GPC Class object failed.", 
                         hr);
        } 
        else 
        {
            wprintf(L"\nUpdated GPC Class object.\n");
        }
    }
 
    // Done with class object.
    pGpc->Release();
    pGpc = NULL;
 
    //
    // Apply the consistency attributes to Container. The 
    // ATTR_INFO required is filled in. Apply it.
    //
    hr = ADsGetObject(pwszContPath,
                      IID_IDirectoryObject,
                      (void**)&pGpc);
 
    if (FAILED(hr)) 
    {
        ReportErrorW(L"Read Container class object failed.",
                     hr);
        goto cleanup;
    } 
    else 
    {
        wprintf(L"\nRetrieved Container class object.\n");
 
        hr = pGpc->SetObjectAttributes(gpcUpdate,1,&iAttrsMod);
        if (FAILED(hr)) 
        {
            ReportErrorW(L"Update Container Class object failed.", 
                         hr);
        } 
        else 
        {
            wprintf(L"\nUpdated Container Class object.\n");
        }
    }
 
    // Force an update of the schema cache to use the changes
    // immediately. Force a synchronous schema update by writing 
    // the operational attribute "schemaUpdateNow" to 
    // the Root DSE.
    varSchemaUpdate.vt = VT_I4;
    varSchemaUpdate.intVal = 1;
    hr = pRoot->Put(CComBSTR("schemaUpdateNow"), 
                    varSchemaUpdate);
    hr = pRoot->SetInfo();
    if (FAILED(hr)) 
    {
        ReportErrorW(L"Force Schema Recalc failed.", hr);
    }
 
cleanup:
    VariantClear(&varDSRoot);
    VariantClear(&varSchemaUpdate);

    if(pwszDSPath)
    {
        delete pwszDSPath;
    }

    if(pwszGPCPath)
    {
        delete pwszGPCPath;
    }

    if(pwszContPath)
    {
        delete pwszContPath;
    }
    
    if(pDisp)
    {
        pDisp->Release();
    }
    
    if(pSchema)
    {
        pSchema->Release();
    }
    
    if(pRoot)
    {
        pRoot->Release();
    }
 

    CoUninitialize();
}
 
// Simple error message reporter
 
void ReportErrorW(LPCWSTR pwszDefaultMsg, DWORD dwErr)
{
    DWORD   dwStatus;
    LPWSTR  pwszMsg;
 
    dwStatus = FormatMessageW(FORMAT_MESSAGE_FROM_SYSTEM |
                              FORMAT_MESSAGE_ALLOCATE_BUFFER |
                              FORMAT_MESSAGE_IGNORE_INSERTS,
                              NULL,
                              dwErr,
                              LANG_NEUTRAL,
                              (LPWSTR)&pwszMsg,
                              64,
                              NULL); 
    if (dwStatus != 0) 
    {
        wprintf(L"%s %s", pwszDefaultMsg, pwszMsg);
        LocalFree(pwszMsg);
    } 
    else 
    {
        wprintf(L"%s %X\n", pwszDefaultMsg, dwErr);
    }
}
```



 

 




