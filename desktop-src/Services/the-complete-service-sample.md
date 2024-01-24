---
description: "Learn more about: The Complete Service Sample"
ms.assetid: a3aeea9b-09c0-4834-892a-c378b67402f4
title: The Complete Service Sample
ms.topic: article
ms.date: 05/31/2018
---

# The Complete Service Sample

The topics in this section form a complete service sample:

-   [Sample.mc](sample-mc.md) (contains error messages)
-   [Svc.cpp](svc-cpp.md) (contains the service code)
-   [SvcConfig.cpp](svcconfig-cpp.md) (contains service configuration code)
-   [SvcControl.cpp](svccontrol-cpp.md) (contains service control code)

## Building the Service

The following procedure describes how to build the service and register the event message DLL.

**To build the service and register the event message DLL**

1.  Build the message DLL from Sample.mc using the following steps:
    1.  **mc -U sample.mc**
    2.  **rc -r sample.rc**
    3.  **link -dll -noentry -out:sample.dll sample.res**
2.  Build Svc.exe, SvcConfig.exe, and SvcControl.exe from Svc.cpp, SvcConfig.cpp, and SvcControl.cpp, respectively.
3.  Create the registry key **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\EventLog\\Application\\SvcName** and add the following registry values to this key.

    | Value                              | Type       | Description                                                                                                        |
    |------------------------------------|------------|--------------------------------------------------------------------------------------------------------------------|
    | **EventMessageFile** = *dll\_path* | REG\_SZ    | The path to the resource-only DLL that contains strings that the service can write to the event log.               |
    | **TypesSupported** = 0x00000007    | REG\_DWORD | A bit mask that specifies the supported event types. The value 0x000000007 indicates that all types are supported. |

    

     

## Testing the Service

The following procedure describes how to test the service.

**To test the service**

1.  In Control Panel, start the **Services** application. (In the following steps, use the F5 key to refresh the display after executing a command that modifies the information in the **Services** application.)
2.  Run the following command to install the service:

    **svc install**

    The service writes "Service installed successfully" to the console if the operation succeeds or an error message otherwise.

    If the service installation succeeds, the service is displayed in the **Services** application. Note that **Name** is set to "SvcName", **Description** and **Status** are blank, and **Startup Type** is set to "Manual".

3.  Run the following command to start the service:

    **svccontrol start SvcName**

    If the operation succeeds, the service control program writes "Service start pending..." and then "Service started successfully" to the console. Otherwise, the program writes an error message to the console.

    If the service starts successfully, **Status** is set to "Started". The code in the [*ServiceMain*](/windows/win32/api/winsvc/nc-winsvc-lpservice_main_functiona) function is executed by the SCM. If an error occurs, the service will write an error message to the event log. This message includes the name of the function that failed and the error code that was returned on failure.

4.  Run the following command to update the service description:

    **svcconfig describe SvcName**

    The service configuration program writes "Service description updated successfully" to the console if the operation succeeds or an error message otherwise.

    If the update succeeds, **Description** is set to "This is a test description".

5.  Run the following command to query the service configuration:

    **svcconfig query SvcName**

    The service configuration program writes the service configuration information to the console if the operation succeeds or an error message otherwise.

6.  Run the following command to change the service DACL:

    **svccontrol dacl SvcName**

    The service configuration program writes "Service DACL updated successfully" to the console if the operation succeeds or an error message otherwise.

7.  Run the following command to disable the service:

    **svcconfig disable SvcName**

    The service configuration program writes "Service disabled successfully" to the console if the operation succeeds or an error message otherwise.

    If the service is disabled successfully, **Startup Type** is set to "Disabled".

8.  Run the following command to enable the service:

    **svcconfig enable SvcName**

    The service configuration program writes "Service enabled successfully" to the console if the operation succeeds or an error message otherwise.

    If the service is enabled successfully, **Startup Type** is set to "Manual".

9.  Run the following command to stop the service:

    **svccontrol stop SvcName**

    If the operation succeeds, the service control program writes "Service stop pending..." and then "Service stopped successfully" to the console. Otherwise, the program writes an error message to the console.

    If the service stops successfully, **Status** is blank.

    If the service fails to stop, the service control program writes an error message to the event log that includes the name of the function that failed and the error code that was returned on failure.

10. Run the following command to delete the service:

    **svcconfig delete SvcName**

    The service configuration program writes "Service deleted successfully" to the console if the operation succeeds or an error message otherwise.

    If the service is deleted successfully, it is no longer displayed in the **Services** application. (Note that if you attempt to delete a service that is not stopped, the operation succeeds but **Startup Type** is set to "Disabled" and the service entry will be deleted at system restart or when the service is terminated using Task Manager.)

## Related topics

<dl> <dt>

[Using Services](using-services.md)
</dt> </dl>

 

 
