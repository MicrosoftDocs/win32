---
title: Composing the SPNs for a Service with an SCP
description: The following code example composes an SPN for a service that uses a service connection point (SCP).
ms.assetid: cbaa11ba-d32b-46cf-86a4-9050bb1be3a6
ms.tgt_platform: multiple
keywords:
- Composing the SPNs for a Service with an SCP AD
- Service Principal Name AD , Composing SPNs for a Service with an SCP
ms.topic: article
ms.date: 05/31/2018
---

# Composing the SPNs for a Service with an SCP

The following code example composes an SPN for a service that uses a service connection point (SCP). The returned SPN has the following format.


```C++
<service class>/<host>/<service name>
```



"&lt;service class&gt;" and "&lt;service name&gt;" correspond to the *pszDNofSCP* and *pszServiceClass* parameters. "&lt;host&gt;" defaults to the DNS name of the local computer.


```C++
DWORD
SpnCompose(
    TCHAR ***pspn,          // Output: an array of SPNs
    unsigned long *pulSpn,  // Output: the number of SPNs returned
    TCHAR *pszDNofSCP,      // Input: DN of the service's SCP
    TCHAR* pszServiceClass) // Input: the name of the service class
{
DWORD   dwStatus;    
 
dwStatus = DsGetSpn(
    DS_SPN_SERVICE, // Type of SPN to create (enumerated type)
    pszServiceClass, // Service class - a name in this case
    pszDNofSCP, // Service name - DN of the service SCP
    0, // Default: omit port component of SPN
    0, // Number of entries in hostnames and ports arrays
    NULL, // Array of hostnames. Default is local computer
    NULL, // Array of ports. Default omits port component
    pulSpn, // Receives number of SPNs returned in array
    pspn // Receives array of SPN(s)
    );
 
return dwStatus;
}
```



 

 




