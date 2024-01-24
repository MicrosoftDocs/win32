---
description: Interpreting Error Codes
ms.assetid: df2fe03b-2f5f-4958-926f-17e3a025a9b5
title: Interpreting Error Codes
ms.topic: article
ms.date: 05/31/2018
---

# Interpreting Error Codes

After you have determined which application is the source of a problem, you need to find out what error has occurred. Errors are raised and reported in different formats, depending on the language your application uses.

In Microsoft Visual C++, success, warning, and failure values are returned using a 32-bit number known as a **HRESULT**. For a list of system-defined **HRESULT** values, see the header file Winerror.h included with the Windows SDK. This file includes all COM+ error codes and descriptions. For more information about **HRESULT** values, see [Error Handling](/windows/desktop/com/error-handling-in-com).

In the Java language, an instance of com.ms.com.ComFailException is thrown to indicate failure, where the ComFailException object specifies an **HRESULT**. An instance of com.ms.com.ComSuccessException indicates success with a return value of False. For information about interpreting these exceptions, see the Microsoft Visual J++ documentation.

> [!Note]  
> COM+ application server processes that are hosting Visual J++ objects will not idle down (even with zero active objects) unless you turn off JIT debugging in the VJ6 IDE. For information on how to do so, see the Visual J++ documentation.

 

In Visual Basic, you can retrieve **HRESULT** values by examining the Err.Number property. A description of the error can be retrieved with the Err.Description property.

You can also use the ERRLOOK utility in Microsoft Visual Studio to retrieve a system error message or module error message. ERRLOOK retrieves the error message text automatically if you drag-and-drop a hexadecimal or decimal value from the Visual Studio debugger or other Automation-enabled application. You can also enter a value by either typing it in or pasting it from the IDE clipboard and clicking the **Look Up** option.

The following C++ method prints a description of the error, based upon the input **HRESULT**.


```C++
#include <stdio.h>
#include <windows.h>
#include <tchar.h>

void ErrorDescription(HRESULT hr) 
{ 
     if(FACILITY_WINDOWS == HRESULT_FACILITY(hr)) 
         hr = HRESULT_CODE(hr); 
     TCHAR* szErrMsg; 

     if(FormatMessage( 
       FORMAT_MESSAGE_ALLOCATE_BUFFER|FORMAT_MESSAGE_FROM_SYSTEM, 
       NULL, hr, MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT), 
       (LPTSTR)&szErrMsg, 0, NULL) != 0) 
     { 
         _tprintf(TEXT("%s"), szErrMsg); 
         LocalFree(szErrMsg); 
     } else 
         _tprintf( TEXT("[Could not find a description for error # %#x.]\n"), hr); 
}
```



The following table provides descriptions of common error codes in COM+.



| Error codes                                                   | Definitions                                                                                                                                                                                                      |
|---------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| COMADMIN\_E\_ALREADYINSTALLED<br/>                      | The object is already registered.<br/>                                                                                                                                                                     |
| COMADMIN\_E\_APP\_FILE\_READFAIL<br/>                   | Error occurred reading the application file.<br/>                                                                                                                                                          |
| COMADMIN\_E\_APP\_FILE\_VERSION<br/>                    | Invalid version number in application file.<br/>                                                                                                                                                           |
| COMADMIN\_E\_APP\_FILE\_WRITEFAIL<br/>                  | Error occurred writing to the application file.<br/>                                                                                                                                                       |
| COMADMIN\_E\_APPDIRNOTFOUND<br/>                        | Application install directory was not found.<br/>                                                                                                                                                          |
| COMQC\_E\_APPLICATION\_NOT\_QUEUED<br/>                 | Only COM+ applications marked "queued" can be created using the "queue" moniker.<br/>                                                                                                                      |
| COMADMIN\_E\_APPLICATIONEXISTS<br/>                     | The application is already installed.<br/>                                                                                                                                                                 |
| COMADMIN\_E\_APPLID\_MATCHES\_CLSID<br/>                | A CLSID with the same GUID as the new application ID is already installed on this machine.<br/>                                                                                                            |
| COMADMIN\_E\_APP\_NOT\_RUNNING<br/>                     | The specified application is not currently running.<br/>                                                                                                                                                   |
| COMADMIN\_E\_AUTHENTICATIONLEVEL<br/>                   | Unable to set required authentication level for update request.<br/>                                                                                                                                       |
| COMADMIN\_E\_BADPATH<br/>                               | The file path is invalid.<br/>                                                                                                                                                                             |
| COMADMIN\_E\_BADREGISTRYLIBID<br/>                      | The registered type library ID is invalid.<br/>                                                                                                                                                            |
| COMADMIN\_E\_BADREGISTRYPROGID<br/>                     | The component's ProgID is missing or corrupt.<br/>                                                                                                                                                         |
| COMADMIN\_E\_CAN\_NOT\_EXPORT\_APP\_PROXY<br/>          | The application proxy is not exportable.<br/>                                                                                                                                                              |
| COMADMIN\_E\_CAN\_NOT\_START\_APP<br/>                  | Failed to start application because it is either a library application or an application proxy.<br/>                                                                                                       |
| COMADMIN\_E\_CAN\_NOT\_EXPORT\_SYS\_APP<br/>            | The system application is not exportable.<br/>                                                                                                                                                             |
| COMADMIN\_E\_CANT\_SUBSCRIBE\_TO\_COMPONENT<br/>        | The user cannot subscribe to this component because the component may have been imported.<br/>                                                                                                             |
| COMADMIN\_E\_CANTCOPYFILE<br/>                          | An error occurred copying the file.<br/>                                                                                                                                                                   |
| COMADMIN\_E\_CLSIDORIIDMISMATCH<br/>                    | Application file CLSIDs or IIDs do not match corresponding DLLs.<br/>                                                                                                                                      |
| COMADMIN\_E\_COMP\_MOVE\_BAD\_DEST<br/>                 | The component move failed because the destination application no longer exists.<br/>                                                                                                                       |
| COMADMIN\_E\_COMP\_MOVE\_LOCKED<br/>                    | The component move was disallowed because the source or destination application either is a system application or is currently locked against changes.<br/>                                                |
| COMADMIN\_E\_COMPFILE\_BADTLB<br/>                      | The type library could not be loaded.<br/>                                                                                                                                                                 |
| COMADMIN\_E\_COMPFILE\_CLASSNOTAVAIL<br/>               | The DLL does not support the components listed in the type library.<br/>                                                                                                                                   |
| COMADMIN\_E\_COMPFILE\_DOESNOTEXIST<br/>                | This file does not exist.<br/>                                                                                                                                                                             |
| COMADMIN\_E\_COMPFILE\_GETCLASSOBJ<br/>                 | The [**GetClassObject**](/windows/desktop/api/objidl/nf-objidl-iclassactivator-getclassobject) method failed in the DLL.<br/>                                                                                                                |
| COMADMIN\_E\_COMPFILE\_LOADDLLFAIL<br/>                 | The DLL could not be loaded.<br/>                                                                                                                                                                          |
| COMADMIN\_E\_COMPFILE\_NOREGISTRAR<br/>                 | The component registrar referenced in this file is not available.<br/>                                                                                                                                     |
| COMADMIN\_E\_COMPFILE\_NOTINSTALLABLE<br/>              | The file does not contain components or component information.<br/>                                                                                                                                        |
| COMADMIN\_E\_COREQCOMPINSTALLED<br/>                    | A component in the same DLL is already installed.<br/>                                                                                                                                                     |
| COMADMIN\_E\_DLLLOADFAILED<br/>                         | The DLL could not be loaded.<br/>                                                                                                                                                                          |
| COMADMIN\_E\_DLLREGISTERSERVER<br/>                     | The [**DllRegisterServer**](/windows/desktop/api/olectl/nf-olectl-dllregisterserver) function failed when the component was installed.<br/>                                                                                                  |
| COMADMIN\_E\_EVENTCLASS\_CANT\_BE\_SUBSCRIBER<br/>      | An event class cannot be configured as a subscriber component. When an attempt is made to create a subscription with an event class as a subscriber, this error is returned.<br/>                          |
| COMADMIN\_E\_INVALIDUSERIDS<br/>                        | One or more users in the application file are not valid.<br/>                                                                                                                                              |
| COMADMIN\_E\_KEYMISSING<br/>                            | The object was not found in the catalog.<br/>                                                                                                                                                              |
| COMADMIN\_E\_LIB\_APP\_PROXY\_INCOMPATIBLE<br/>         | Library applications and application proxies are incompatible. This error is returned when an attempt is made to export an application proxy and the application's activation property is a library. <br/> |
| COMADMIN\_E\_NOREGISTRYCLSID<br/>                       | The component's CLSID is missing or corrupt.<br/>                                                                                                                                                          |
| COMADMIN\_E\_NOSERVERSHARE<br/>                         | No server file share is available.<br/>                                                                                                                                                                    |
| COMADMIN\_E\_NOTCHANGEABLE<br/>                         | Changes to this object and its sub-objects have been disabled.<br/>                                                                                                                                        |
| COMADMIN\_E\_NOTDELETEABLE<br/>                         | The delete function has been disabled for this object.<br/>                                                                                                                                                |
| COMADMIN\_E\_NOTINREGISTRY<br/>                         | Object was not found in registry.<br/>                                                                                                                                                                     |
| COMADMIN\_E\_NOUSER<br/>                                | One or more users are not valid.<br/>                                                                                                                                                                      |
| COMADMIN\_E\_OBJECT\_DOES\_NOT\_EXIST<br/>              | One of the specified objects cannot be found.<br/>                                                                                                                                                         |
| COMADMIN\_E\_OBJECT\_PARENT\_MISSING<br/>               | One of the objects being inserted or updated does not belong to a valid parent collection.<br/>                                                                                                            |
| COMADMIN\_E\_OBJECTERRORS<br/>                          | Errors occurred accessing one or more objects. For more information, see the [**ErrorInfo**](errorinfo.md) collection.<br/>                                                                               |
| COMADMIN\_E\_OBJECTEXISTS<br/>                          | The object you are attempting to add or rename already exists.<br/>                                                                                                                                        |
| COMADMIN\_E\_OBJECTINVALID<br/>                         | One or more of the object's properties are missing or invalid.<br/>                                                                                                                                        |
| COMADMIN\_E\_OBJECTNOTPOOLABLE<br/>                     | This object is cannot be pooled.<br/>                                                                                                                                                                      |
| COMADMIN\_E\_PROPERTYSAVEFAILED<br/>                    | One or more property settings are either invalid or in conflict with each other.<br/>                                                                                                                      |
| COMADMIN\_E\_PROPERTY\_OVERFLOW<br/>                    | The property value is too large.<br/>                                                                                                                                                                      |
| COMADMIN\_E\_REGFILE\_CORRUPT<br/>                      | The registration file is corrupt.<br/>                                                                                                                                                                     |
| COMADMIN\_E\_REGISTERTLB<br/>                           | The system was unable to register the type library.<br/>                                                                                                                                                   |
| COMADMIN\_E\_REGISTRARFAILED<br/>                       | Errors occurred while in the component registrar.<br/>                                                                                                                                                     |
| COMADMIN\_E\_REMOTEINTERFACE<br/>                       | Interface information is either missing or changed.<br/>                                                                                                                                                   |
| COMADMIN\_E\_REQUIRES\_DIFFERENT\_PLATFORM<br/>         | This operation is not enabled on this platform.<br/>                                                                                                                                                       |
| COMADMIN\_E\_ROLE\_DOES\_NOT\_EXIST<br/>                | A role assigned to a component, interface, or method does not exist in the application.<br/>                                                                                                               |
| COMADMIN\_E\_ROLEEXISTS<br/>                            | The role already exists.<br/>                                                                                                                                                                              |
| COMADMIN\_E\_SERVICENOTINSTALLED<br/>                   | The service is not installed.<br/>                                                                                                                                                                         |
| COMADMIN\_E\_SESSION<br/>                               | The server catalog version is not supported.<br/>                                                                                                                                                          |
| COMADMIN\_S\_SOMEALREADYPAUSED<br/>                     | One or more of the specified application processes were already paused.<br/>                                                                                                                               |
| COMADMIN\_S\_SOMEALREADYRUNNING<br/>                    | One or more of the specified application processes were already running.<br/>                                                                                                                              |
| COMADMIN\_E\_START\_APP\_NEEDS\_COMPONENTS<br/>         | To start the application, you must have components in an application.<br/>                                                                                                                                 |
| COMADMIN\_E\_SVCAPP\_NOT\_POOLABLE\_OR\_RECYCLABLE<br/> | The COM+ applications running as an NT service may not be marked as pooled or recycled.<br/>                                                                                                               |
| COMADMIN\_E\_SYSTEMAPP<br/>                             | This operation cannot be performed on the system application.<br/>                                                                                                                                         |
| COMADMIN\_E\_USER\_IN\_SET<br/>                         | One or more users are already assigned to a local partition set.<br/>                                                                                                                                      |
| COMADMIN\_E\_USERPASSWDNOTVALID<br/>                    | The identity or password set on the application is not valid.<br/>                                                                                                                                         |



 

## Related topics

<dl> <dt>

[Fault Isolation and Failfast Policy](fault-isolation-and-failfast-policy.md)
</dt> <dt>

[Finding the Source of an Error](finding-the-source-of-an-error.md)
</dt> <dt>

[How COM+ Modifies Return Values](how-com--modifies-return-values.md)
</dt> <dt>

[Strategies for Handling Errors in COM+](strategies-for-handling-errors-in-com-.md)
</dt> <dt>

[Troubleshooting](troubleshooting-the-com--crm.md)
</dt> </dl>

 

