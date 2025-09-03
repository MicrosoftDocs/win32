---
title: Launch an AppContainer
description: Learn about launching an AppContainer,  security feature introduced in Windows 8 to enhance the isolation and control of application processes.
ms.assetid: C70A2F8C-27CB-4298-AA31-8F5099616625
ms.topic: concept-article
ms.date: 07/20/2023
---

# Launch an AppContainer

This article describes the steps necessary to launch an AppContainer or Less-Privileged AppContainer including relevant code examples. AppContainers are a security feature introduced in Windows 8 to enhance the isolation and control of application processes. They provide a sandboxed environment for applications, restricting their ability to access system or each other’s resources, as well as user data unless explicitly permitted. AppContainers leverage existing Windows security mechanisms, such as security identifiers (SIDs), tokens, and security descriptor discretionary access control list (DACL), to enforce these restrictions. 

## Terminology

The following table defines terms and concepts referenced in this article.

| Term | Description |
|------|-------------|
| Package identity | A package identity is a logical construct, uniquely identifying a package. For more information, see [An overview of Package Identity in Windows apps](/windows/apps/desktop/modernize/package-identity-overview).|
| Security identifier (SID) | A SID is used to uniquely identify a security principal or security group. Security principals can represent any entity that the operating system can authenticate. Examples include a user account, a computer account, or a thread or process that runs in the security context of a user or computer account. For more information, see [Security identifiers](/windows-server/identity/ad-ds/manage/understand-security-identifiers) |
| Capability SIDs | Capability SIDs serve as unique and immutable identifiers for capabilities. A capability represents an unforgeable token of authority that grants an application access to resources (for example, documents, cameras, and locations). For more information, see [App capability declarations](/windows/uwp/packaging/app-capability-declarations) |
| Discretionary Access Control List (DACL) | A list that identifies the users and groups who can perform various operations on an object. For more information, see [Security descriptor components](/windows/win32/ad/security-descriptor-components). |
| Less Privileged AppContainers (LPAC) | A type of AppContainer that is more isolated than a regular AppContainer. It requires explicit capability declarations to access resources that are accessible to AppContainers. |


## AppContainer overview

When an application runs as an AppContainer, its access token includes a unique application package identity (Package SID) and one or more capability SIDs. For AppContainers, capabilities are used to ensure that AppContainers can run with the least privilege possible and only be granted access to potentially sensitive resources if needed. For example, without the *network* capability, an AppContainer cannot access the network, without the *webcam* capability it can’t access a camera. AppContainer SIDs (Package and Capability SIDs) are separate from the traditional user and group SIDs with both portions of the token being required to grant access to a protected resource via the object's discretionary access control list (DACL). This dual-principal model ensures that access to sensitive resources is tightly controlled and can be managed independently for different applications. It also ensures that AppContainers must be explicitly granted access to a given resource. Furthermore, the permitted access is the intersection of that granted by the user/group SIDs and AppContainer SIDs so if the User has full access, but the AppContainer only has read access, the AppContainer can only be granted read access. Similarly, if the user has read & execute access but the AppContainer has full access the AppContainer can only be granted read & execute access.

AppContainers run with a Low Integrity Level (IL), which further limits their ability to interact with higher-integrity objects on the system. However, if a resource has a mandatory label of Medium IL or lower and the DACL grants access through to the AppContainer (through a Package SID or Capability SID) then the AppContainer can read, write, or execute depending on the access granted to both principals in the DACL. This approach provides both flexibility and security, allowing access to necessary resources while restricting potentially harmful actions from untrusted or compromised applications.

AppContainers are isolated from accessing processes and windows belonging to other applications as well as from devices, files/directories, registry keys, the network, and credentials. Thus, they provide a mechanism for sandboxing potential risky operations such as parsing untrusted data safely.

Regular AppContainers are granted access to certain system files/directories, common registry keys and COM objects, however, LPAC needs specific capabilities to access resources that regular AppContainers can access. Less Privileged AppContainers (LPAC) are even more isolated than regular AppContainers and require further capabilities to gain access to resources that regular AppContainers already have access to such as the registry, files, and others. For example, LPAC cannot open any keys in the registry unless it has the *registryRead* capability and cannot use COM unless it has the *lpacCom* capability.

## Launching an AppContainer

As mentioned earlier, AppContainers have a unique Package SID that ensures that their own resources are protected from other applications. The Package SID is derived from a string name (moniker) for the given AppContainer. In the case of AppContainers spawned through an AppX manifest, this is the Package Family Name (PFN) but in the case of an application launching an AppContainer process itself, the application needs to determine the name (moniker) it wishes to give the AppContainer.

There are several steps involved in launching an AppContainer. The necessary capabilities to grant need to be determined, the profile needs to be created for the AppContainer so that there is a location where the AppContainer can create/read/write files, process and thread attributes need to be included to inform Windows that it needs to create an AppContainer.

## Constructing the capabilities

An AppContainer (or LPAC) may need capabilities to access different resources such as the network, location or in the case of an LPAC even the registry or COM object. Constructing the capabilities can be achieved through the [DeriveCapabilitySidsFromName](/windows/win32/api/securitybaseapi/nf-securitybaseapi-derivecapabilitysidsfromname) API, although it’s better to wrap this API in a helper function, such as **GetCapabilitySidFromName** shown in the example code below, since Group SIDs are only used for services and the API only ever returns a single capability.

```cpp
BOOL GetCapabilitySidFromName( 
    PCWSTR CapabilityName, 
    PSID* CapabilitySid) 
{ 
    PSID* CapabilitySids; 
    DWORD CapabilitySidCount; 
    PSID* GroupSids; 
    DWORD GroupSidCount; 

    *CapabilitySid = NULL; 

    if (DeriveCapabilitySidsFromName(CapabilityName, &GroupSids, &GroupSidCount, & CapabilitySids, &CapabilitySidCount)) 
    { 
        LocalFree(GroupSids[0]); 
        LocalFree(GroupSids); 

        *CapabilitySid = CapabilitySids[0]; 
        LocalFree(CapabilitySids); 
        return TRUE; 

    }

    return FALSE; 
} 
```

The following example code demonstrates using the **GetCapabilitySidFromName** helper function defined in the previous example to construct the *internetClient* and *location* capabilities.

```cpp
BOOL BuildAppContainerCapabilities( 
    PSID_AND_ATTRIBUTES* Capabilities, 
    DWORD* NumberOfCapabilities 
) 
{
    DWORD CapabilityCount; 
    PSID CapabilitySids[2]; 
    PSID_AND_ATTRIBUTES LocalCapabilities; 

    *Capabilities = NULL; 
    *NumberOfCapabilities = 0; 

    CapabilityCount = 0; 

    if (GetCapabilitySidFromName(L"internetClient", &CapabilitySids[CapabilityCount++]) == FALSE) 
    { 
        return FALSE; 
    } 

    if (GetCapabilitySidFromName(L"location", &CapabilitySids[CapabilityCount++]) == FALSE) 
    { 
        for (DWORD i = 0; i < CapabilityCount; ++i) 
        { 
            LocalFree(CapabilitySids[i]); 
        } 

        return FALSE; 
    } 

    LocalCapabilities =  
        (PSID_AND_ATTRIBUTES)HeapAlloc(GetProcessHeap(), 
        0, 
        CapabilityCount * sizeof(SID_AND_ATTRIBUTES)); 

    if (LocalCapabilities != NULL) 
    { 
        for (DWORD i = 0; i < CapabilityCount; ++i) 
        { 
            LocalCapabilities[i].Sid = CapabilitySids[i]; 
            LocalCapabilities[i].Attributes = SE_GROUP_ENABLED; 
        } 
    }
    else 
    { 
        for (DWORD i = 0; i < CapabilityCount; ++i) 
        {
            LocalFree(CapabilitySids[i]); 
        } 

        return FALSE; 
    } 

    *Capabilities = LocalCapabilities; 
    *NumberOfCapabilities = CapabilityCount; 

    return TRUE; 
} 
```

## Creating the Profile

Create the AppContainer by calling [CreateAppContainerProfile](/windows/win32/api/userenv/nf-userenv-createappcontainerprofile), with the profile being accessible to the AppContainer via the **LOCALAPPDATA** environment variable or by calling [GetAppContainerFolderPath](/windows/win32/api/userenv/nf-userenv-getappcontainerfolderpath). For a new AppContainer this also returns the Package SID for the AppContainer. However, for an existing AppContainer it is necessary to derive the package SID from the moniker using the [DeriveAppContainerSidFromAppContainerName](/windows/win32/api/userenv/nf-userenv-deriveappcontainersidfromappcontainername) API. Both the **TMP** and **TEMP** environment variables are also rerouted to a directory accessible to the AppContainer under the profile location:

`LOCALAPPDATA=C:\Users\TestUser\AppData\Local\Packages\TestAppContainer\AC`

`TEMP=C:\Users\TestUser\AppData\Local\Packages\TestAppContainer\AC\Temp`

`TMP=C:\Users\TestUser\AppData\Local\Packages\TestAppContainer\AC\Temp`

The following example code demonstrates the use of **CreateAppContainerProfile** function to create an AppContainer profile and retrieve the SID for a new or an existing AppContainer.

```cpp
HRESULT
CreateProfileForAppContainer(
    PCWSTR AppContainerName,
    PSID_AND_ATTRIBUTES Capabilities,
    ULONG NumberOfCapabilities,
    PCWSTR DisplayName,
    PCWSTR Description,
    PSID* AppContainerSid
    )
{
    HRESULT hr;
    PSID LocalAppContainerSid = NULL;

    *AppContainerSid = NULL;

    hr = CreateAppContainerProfile(AppContainerName,
                                   DisplayName,
                                   Description,
                                   Capabilities,
                                   NumberOfCapabilities,
                                   &LocalAppContainerSid);

    if (FAILED(hr)) {
        if (hr == HRESULT_FROM_WIN32(ERROR_ALREADY_EXISTS)) {

            //
            // Obtain the AppContainer SID based on the AppContainer name.
            //

            hr = AppContainerDeriveSidFromMoniker(AppContainerName,
                                                  &LocalAppContainerSid);
            
            if (FAILED(hr)) {   
                return hr;
            }

        } else {
            return hr;
        }        
    } 

    //
    // Since this is successful, set the output AppContainer SID accordingly.
    //
    
    *AppContainerSid = LocalAppContainerSid;

    return S_OK;
}
```

## Launching the AppContainer (or LPAC)

 To launch the AppContainer or LPAC process, it is necessary to include certain fields in the startup information structure, [STARTUPINFOEX](/windows/win32/api/winbase/ns-winbase-startupinfoexw). Specifically the *lpAttributeList* field is required as this allows additional information that instructs [CreateProcess](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw) to create the environment for the AppContainer which includes the object namespace and token. The *lpAttributeList* field is of type LPPROC_THREAD_ATTRIBUTE_LIST and is set up as follows. 

The following example shows how to launch a regular app container.

```cpp
STARTUPINFOEX si = {0}; 
LPPROC_THREAD_ATTRIBUTE_LIST AttributeList = NULL; 
SECURITY_CAPABILITIES SecurityCapabilities; 
DWORD AttributeCount = 1; 
SIZE_T AttributesLength = 0; 

if (!InitializeProcThreadAttributeList(NULL, AttributeCount, 0, &AttributesLength)) 
{
    if (GetLastError() != ERROR_INSUFFICIENT_BUFFER)  
    { 
        return GetLastError(); 
    }
} 

AttributeList = (LPPROC_THREAD_ATTRIBUTE_LIST)HeapAlloc(GetProcessHeap(), 
    0, 
    AttributesLength); 

if (AttributeList == NULL) 
{ 
    return ERROR_OUTOFMEMORY; 
} 

if (!InitializeProcThreadAttributeList(AttributeList, AttributeCount, 0, &AttributesLength)) 
{ 
    if (GetLastError() != ERROR_SUCCESS) 
    {
        return GetLastError(); 
    }
} 

SecurityCapabilities.CapabilityCount = NumberOfCapabilities; 
SecurityCapabilities.Capabilities = Capabilities; 
SecurityCapabilities.AppContainerSid = PackageSid; 
SecurityCapabilities.Reserved = 0; 

if (!UpdateProcThreadAttribute(AttributeList, 
        0,
        PROC_THREAD_ATTRIBUTE_SECURITY_CAPABILITIES, 
        &SecurityCapabilities, 
        sizeof(SecurityCapabilities), 
        NULL, 
        NULL 
        )) 
{ 
    return GetLastError(); 
} 

si.StartupInfo.cb = sizeof(si); 
si.lpAttributeList = AttributeList; 
```

The following example shows how to launch a less privileged AppContainer (LPAC), which requires an additional process/thread attribute:

```cpp
STARTUPINFOEX si = {0}; 
LPPROC_THREAD_ATTRIBUTE_LIST AttributeList = NULL; 
SECURITY_CAPABILITIES SecurityCapabilities; 
DWORD AttributeCount = 2; 
SIZE_T AttributesLength = 0; 
DWORD AllApplicationPackagesPolicy; 

if (!InitializeProcThreadAttributeList(NULL, AttributeCount, 0, &AttributesLength)) 
{ 
    if (GetLastError() != ERROR_INSUFFICIENT_BUFFER) 
    { 
        return GetLastError(); 
    } 
} 

AttributeList = (LPPROC_THREAD_ATTRIBUTE_LIST)HeapAlloc(GetProcessHeap(), 
    0, 
    AttributesLength); 

if (AttributeList == NULL) 
{ 
    return ERROR_OUTOFMEMORY; 
} 

if (!InitializeProcThreadAttributeList(AttributeList, AttributeCount, 0, &AttributesLength)) 
{ 
    if (GetLastError() != ERROR_SUCCESS) 
    { 
        return GetLastError(); 
    } 
} 

SecurityCapabilities.CapabilityCount = NumberOfCapabilities; 
SecurityCapabilities.Capabilities = Capabilities; 
SecurityCapabilities.AppContainerSid = PackageSid; 
SecurityCapabilities.Reserved = 0; 

if (!UpdateProcThreadAttribute(AttributeList, 
    0, 
    PROC_THREAD_ATTRIBUTE_SECURITY_CAPABILITIES, 
    &SecurityCapabilities, 
    sizeof(SecurityCapabilities), 
    NULL, 
    NULL 
    )) 
{
    return GetLastError(); 
} 

AllApplicationPackagesPolicy = PROCESS_CREATION_ALL_APPLICATION_PACKAGES_OPT_OUT; 

if (!UpdateProcThreadAttribute(AttributeList, 
    0, 
    PROC_THREAD_ATTRIBUTE_ALL_APPLICATION_PACKAGES_POLICY, 
    &AllApplicationPackagesPolicy, 
    sizeof(AllApplicationPackagesPolicy), 
    NULL, 
    NULL 
    )) 
{ 
    return GetLastError(); 
} 

si.StartupInfo.cb = sizeof(si); 
si.lpAttributeList = AttributeList; 
```

## Creating the AppContainer/LPAC process 

The final step is to launch the process using the startup information, which includes the process/thread attributes constructed in the previous steps. This will include the package SID, capabilities, if any, as well as if this should be an LPAC, which is specified by opting out of All Application Packages.

```cpp
if (!CreateProcess(NULL, 
    <path to executable>, 
    NULL, 
    NULL, 
    FALSE, 
    EXTENDED_STARTUPINFO_PRESENT, 
    NULL, 
    NULL, 
    (LPSTARTUPINFOW)&si, 
    &pi)) 
{ 
    return GetLastError(); 
}
```



## Related topics

[Security identifiers](/windows-server/identity/ad-ds/manage/understand-security-identifiers)

[Security descriptor components](/windows/win32/ad/security-descriptor-components)