---
title: Installing a Service on a Host Computer
description: The following code example shows the basic steps of installing a directory-enabled service on a host computer.
ms.assetid: 35a3b261-d499-4154-a022-1e33a9ef7ba8
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Installing a Service on a Host Computer

The following code example shows the basic steps of installing a directory-enabled service on a host computer. It performs the following operations:

1.  Calls the [**OpenSCManager**](/windows/desktop/api/winsvc/nf-winsvc-openscmanagera) function to open a handle to the service control manager (SCM) on the local computer.
2.  Calls the [**CreateService**](/windows/desktop/api/winsvc/nf-winsvc-createservicea) function to install the service in the SCM database. This call specifies the service's logon account and password, as well as the service's executable and other information about the service. **CreateService** fails if the specified logon account is invalid. However, **CreateService** does not check the validity of the password. It also does not verify that the account has the logon as a service right on the local computer. For more information, see [Granting Logon as Service Right on the Host Computer](granting-logon-as-service-right-on-the-host-computer.md).
3.  Calls the service's **ScpCreate** subroutine that creates a service connection point object (SCP) in the directory to publish the location of this instance of the service. For more information, see [How Clients Find and Use a Service Connection Point](how-clients-find-and-use-a-service-connection-point.md). This routine also stores the service's binding information in the SCP, sets an ACE on the SCP so the service can access it at run time, caches the distinguished name of the SCP in the local registry, and returns the distinguished name of the new SCP.
4.  Calls the service's **SpnCompose** subroutine that uses the service's class string and the distinguished name of the SCP to compose a service principal name (SPN). For more information, see [Composing the SPNs for a Service with an SCP](composing-the-spns-for-a-service-with-an-scp.md). The SPN uniquely identifies this instance of the service.
5.  Calls the service's **SpnRegister** subroutine that registers the SPN on the account object associated with service's logon account. For more information, see [Registering the SPNs for a Service](registering-the-spns-for-a-service.md). Registration of the SPN enables client applications to authenticate the service.

This code example works correctly regardless of whether the logon account is a local or domain user account or the LocalSystem account. For a domain user account, the *szServiceAccountSAM* parameter contains the *Domain***\\***UserName* name of the account, and the *szServiceAccountDN* parameter contains the distinguished name of the user account object in the directory. For the LocalSystem account, *szServiceAccountSAM* and *szPassword* are **NULL**, and *szServiceAccountSN* is the distinguished name of the local computer's account object in the directory. If *szServiceAccountSAM* specifies a local user account (name format is ".\\*UserName*"), the code example skips the SPN registration because mutual authentication is not supported for local user accounts.

Be aware that the default security configuration allows only domain administrators to execute this code.

Also, be aware that this code example, as written, must be executed on the computer where the service is being installed. Consequently, it is typically in a separate installation executable from your service installation code, if any, that extends the schema, extends the UI, or sets up group policy. Those operations install service components for an entire a forest, whereas this code installs the service on a single computer.


```C++
void InstallServiceOnLocalComputer(
            LPTSTR szServiceAccountDN,  // Distinguished name of logon account.
            LPTSTR szServiceAccountSAM, // SAM name of logon account.
            LPTSTR szPassword)          // Password of logon account.
{
SC_HANDLE   schService = NULL;
SC_HANDLE   schSCManager = NULL;
TCHAR szPath[512];
LPTSTR lpFilePart;
TCHAR szDNofSCP[MAX_PATH];
TCHAR szServiceClass[]=TEXT("ADSockAuth");
 
DWORD dwStatus;
TCHAR **pspn=NULL;
ULONG ulSpn=1;
 
// Get the full path of the service's executable.
// The code example assumes that the executable is in the current directory.
dwStatus = GetFullPathName(TEXT("service.exe"), 512, szPath, &lpFilePart);
if (dwStatus == 0) {
    _tprintf(TEXT("Unable to install %s - %s\n"), 
            TEXT(SZSERVICEDISPLAYNAME), GetLastErrorText(szErr, 256));
    return;
}
_tprintf(TEXT("path of service.exe: %s\n"), szPath);
 
// Open the Service Control Manager on the local computer.
schSCManager = OpenSCManager(
                NULL,                   // Computer (NULL == local)
                NULL,                   // Database (NULL == default)
                SC_MANAGER_ALL_ACCESS   // Access required
                );
if (! schSCManager) {
    _tprintf(TEXT("OpenSCManager failed - %s\n"), 
                   GetLastErrorText(szErr,256));
    goto cleanup;
}
        
// Install the service in the SCM database.
schService = CreateService(
            schSCManager,               // SCManager database
            TEXT(SZSERVICENAME),        // Name of service
            TEXT(SZSERVICEDISPLAYNAME), // Name to display
            SERVICE_ALL_ACCESS,         // Desired access
            SERVICE_WIN32_OWN_PROCESS,  // Service type
            SERVICE_DEMAND_START,       // Start type
            SERVICE_ERROR_NORMAL,       // Error control type
            szPath,                     // Service binary
            NULL,                       // No load ordering group
            NULL,                       // No tag identifier
            TEXT(SZDEPENDENCIES),       // Dependencies
            szServiceAccountSAM,        // Service account
            szPassword);                // Account password
if (! schService) {
    _tprintf(TEXT("CreateService failed - %s\n"), 
                   GetLastErrorText(szErr,256));
    goto cleanup;
}
 
_tprintf(TEXT("%s installed.\n"), TEXT(SZSERVICEDISPLAYNAME) );
 
// Create the service's Service Connection Point (SCP).
dwStatus = ScpCreate(
        2000,                 // Service default port number
        szServiceClass,       // Specifies the service class string
        szServiceAccountSAM,  // SAM name of logon account for ACE
        szDNofSCP             // Buffer returns the DN of the SCP
        );
if (dwStatus != 0) {
    _tprintf(TEXT("ScpCreate failed: %d\n"), dwStatus );
    DeleteService(schService);
    goto cleanup;
}
 
// Compose and register a service principal name for this service.
// This is performed on the install path because this requires elevated
// privileges for updating the directory.
// If a local account of the format ".\user name", skip the SPN.
if ( szServiceAccountSAM[0] == '.' ) 
{
    _tprintf(TEXT("Do not register SPN for a local account.\n"));
    goto cleanup;
}
 
dwStatus = SpnCompose(
        &pspn,            // Receives pointer to the SPN array.
        &ulSpn,           // Receives number of SPNs returned.
        szDNofSCP,        // Input: DN of the SCP.
        szServiceClass);  // Input: the service's class string.
 
if (dwStatus == NO_ERROR) 
    dwStatus = SpnRegister(
        szServiceAccountDN,  // Account on which SPNs are registered.
        pspn,                // Array of SPNs to register.
        ulSpn,               // Number of SPNs in array.
        DS_SPN_ADD_SPN_OP);  // Operation code: Add SPNs.
 
if (dwStatus != NO_ERROR) 
{
    _tprintf(TEXT("Failed to compose SPN: Error was %X\n"), 
                  dwStatus);
    DeleteService(schService);
    ScpDelete(szDNofSCP, szServiceClass, szServiceAccountDN);
    goto cleanup;
}
 
cleanup:
if (schSCManager)
    CloseServiceHandle(schSCManager);
if (schService)
    CloseServiceHandle(schService);
DsFreeSpnArray(ulSpn, pspn);
return;
}
```



For more information about the previous code example, see [Composing the SPNs for a Service with an SCP](composing-the-spns-for-a-service-with-an-scp.md) and [Registering the SPNs for a Service](registering-the-spns-for-a-service.md).

 

 