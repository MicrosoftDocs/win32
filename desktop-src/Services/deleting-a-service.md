---
description: A service configuration program uses the OpenService function to get a handle to an installed service object. The program can then use the service object handle in the DeleteService function to delete the service from the SCM database.
ms.assetid: 3bfe4d42-a8a0-4613-9b0f-a80eef54b622
title: Deleting a Service
ms.topic: article
ms.date: 05/31/2018
---

# Deleting a Service

A [service configuration program](service-configuration-programs.md) uses the [**OpenService**](/windows/desktop/api/Winsvc/nf-winsvc-openservicea) function to get a handle to an installed service object. The program can then use the service object handle in the [**DeleteService**](/windows/desktop/api/Winsvc/nf-winsvc-deleteservice) function to delete the service from the SCM database.

The DoDeleteSvc function in the following example shows how to delete a service from the SCM database. The szSvcName variable is a global variable that contains the name of the service to be deleted. For the complete example that sets this variable, see [SvcConfig.cpp](svcconfig-cpp.md).


```C++
//
// Purpose: 
//   Deletes a service from the SCM database
//
// Parameters:
//   None
// 
// Return value:
//   None
//
VOID __stdcall DoDeleteSvc()
{
    SC_HANDLE schSCManager;
    SC_HANDLE schService;
    SERVICE_STATUS ssStatus; 

    // Get a handle to the SCM database. 
 
    schSCManager = OpenSCManager( 
        NULL,                    // local computer
        NULL,                    // ServicesActive database 
        SC_MANAGER_ALL_ACCESS);  // full access rights 
 
    if (NULL == schSCManager) 
    {
        printf("OpenSCManager failed (%d)\n", GetLastError());
        return;
    }

    // Get a handle to the service.

    schService = OpenService( 
        schSCManager,       // SCM database 
        szSvcName,          // name of service 
        DELETE);            // need delete access 
 
    if (schService == NULL)
    { 
        printf("OpenService failed (%d)\n", GetLastError()); 
        CloseServiceHandle(schSCManager);
        return;
    }

    // Delete the service.
 
    if (! DeleteService(schService) ) 
    {
        printf("DeleteService failed (%d)\n", GetLastError()); 
    }
    else printf("Service deleted successfully\n"); 
 
    CloseServiceHandle(schService); 
    CloseServiceHandle(schSCManager);
}
```



## Related topics

<dl> <dt>

[Service Installation, Removal, and Enumeration](service-installation-removal-and-enumeration.md)
</dt> <dt>

[The Complete Service Sample](the-complete-service-sample.md)
</dt> </dl>

 

 



