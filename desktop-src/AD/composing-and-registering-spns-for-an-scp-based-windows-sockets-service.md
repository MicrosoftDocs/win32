---
title: Composing and registering SPNs for SCP-based Windows Sockets Service
description: The following code example shows how to compose and register the SPNs for a service. Call this code from your service installer after calling CreateService and creating the service's service connection point (SCP).
ms.assetid: 3957af10-974a-415f-b8fb-d9b52ac5a82d
ms.tgt_platform: multiple
keywords:
- service principal names AD ,composing and registering SPNs for an SCP-based Windows sockets service
ms.topic: article
ms.date: 05/31/2018
---

# Composing and registering SPNs for SCP-based Windows Sockets Service

The following code example shows how to compose and register the SPNs for a service. Call this code from your service installer after calling [**CreateService**](/windows/desktop/api/winsvc/nf-winsvc-createservicea) and creating the service's service connection point (SCP).

The following code example calls the **SpnCompose** and **SpnRegister** example functions that compose and register the SPN. For more information and the **SpnCompose** source code, see [Composing the SPNs for a Service with an SCP](composing-the-spns-for-a-service-with-an-scp.md). For more information and the **SpnRegister** source code, see [Registering the SPNs for a Service](registering-the-spns-for-a-service.md).

This example uses the service class name and the distinguished name of its SCP to create its service principal name. For more information and a code example that shows how the client binds to the service SCP to retrieve these name strings, see [How Clients Find and Use a Service Connection Point](how-clients-find-and-use-a-service-connection-point.md). Be aware that the code for composing an SPN varies depending on the type of service and the mechanisms used to publish the service.

The service registers its SPN by storing it in the **servicePrincipalName** attribute of the service's account object in the directory. If the service runs under the LocalSystem account instead of under a service account, it registers its SPN under the local computer account's object in the directory.


```C++
TCHAR szDNofSCP[MAX_PATH]; // DN of SCP. Initialize by querying SCP.
TCHAR szServiceClass[]=TEXT("ADSockAuth");
LPCTSTR szServiceAccountDN;   // DN of a service logon account. 
 
DWORD dwStatus;
TCHAR **pspn = NULL;
ULONG ulSpn = 1;
 
// Compose the SPNs.
dwStatus = SpnCompose(
        &pspn,              // Receives pointer to the SPN array.
        &ulSpn,             // Receives number of SPNs returned.
        szDNofSCP,          // Input: DN of the SCP.
        szServiceClass);    // Input: the service class string.
 
// Register the SPNs
if (dwStatus == NO_ERROR) 
    dwStatus = SpnRegister(
       szServiceAccountDN,  // Logon account to register SPNs on
       pspn,                // Array of SPNs
       ulSpn,               // Number of SPNs in array
       DS_SPN_ADD_SPN_OP);  // Add SPNs to the account
 
// Free the array of SPNs returned by SpnCompose.
DsFreeSpnArray(ulSpn, pspn); 
```



You can use similar code to unregister your SPNs when your service is uninstalled. Specify the **DS\_SPN\_DELETE\_SPN\_OP** operation instead of **DS\_SPN\_ADD\_SPN\_OP**.

 

 