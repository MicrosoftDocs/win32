---
title: How to Get a Specific Instance of a Class (C/C++)
description: This topic provides step-by-step instructions for getting a specific (keyed) instance of a specified CIM class using the Windows Management Infrastructure (MI) native API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 581895DF-04B7-4FED-94B3-0A207E462E74
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# How to: Get a Specific Instance of a Class (C/C++)

This topic provides step-by-step instructions for getting a specific (keyed) instance of a specified CIM class using the [Windows Management Infrastructure (MI) native API](Http://Go.Microsoft.Com/FWLink/p/?LinkID=308914). In addition to the steps, a full source code example is provided at the end of the topic.

> [!Note]  
> To see the [MI .NET API](Http://Go.Microsoft.Com/FWLink/p/?LinkID=308910) and Microsoft Visual C# version of this topic, refer to [How to: Get a Specific Instance of a Class (C)](how-to-get-a-specific-instance-of-a-class.md)

 

## Step-by-step Instructions

1.  Insert an include directive for the MI header file. (This file ships as part of the [Windows Software Development Kit (SDK) for Windows 8](Http://Go.Microsoft.Com/FWLink/p/?LinkID=306595).)

    ```C++
    #include <mi.h>
    ```

    

2.  Add the MI import library (**mi.lib**) to the project's linker dependencies. (This file ships as part of the [Windows Software Development Kit (SDK) for Windows 8](Http://Go.Microsoft.Com/FWLink/p/?LinkID=306595).)

3.  Initialize the application via [**MI\_Application\_Initialize**](/windows/previous-versions/Mi/nf-mi-mi_application_initializev1?branch=master). It is recommended to have only one [**MI\_Application**](/windows/previous-versions/Mi/ns-mi-_mi_application?branch=master) per process. The **MI\_Application** returned from this function should always be closed, or de-initialized, via [**MI\_Application\_Close**](/windows/previous-versions/Mi/nf-mi-mi_application_close?branch=master).

    ```C++
    MI_RESULT miResult = MI_Application_Initialize(0,               // Flags - Must be 0
                                                   NULL,            // Application ID
                                                   NULL,            // Extended error
                                                   &amp;miApplication); // Application 
    if (miResult != MI_RESULT_OK)
    { /* Handle error */ }
    ```

    

4.  Create an MI session against the specified destination (computer) with the specified protocol (WinRM, in this example) via [**MI\_Application\_NewSession**](/windows/previous-versions/Mi/nf-mi-mi_application_newsession?branch=master). The session must be closed via [**MI\_Session\_Close**](/windows/previous-versions/Mi/nf-mi-mi_session_close?branch=master).

    ```C++
    MI_RESULT miResult = MI_Application_NewSession(&amp;miApplication, // Application 
                                                   L"WINRM",       // WimRM Protocol
                                                   L"localhost",   // Machine destination
                                                   NULL,           // Options
                                                   NULL,           // Callbacks
                                                   NULL,           // Extended error
                                                   &amp;miSession);    // Session 
    if (miResult != MI_RESULT_OK)
    { /* Handle error */ }  
    ```

    

5.  Create an [**MI\_Instance**](/windows/previous-versions/Mi/ns-mi-_mi_instance?branch=master) that represents the class name and keys of the instance to be retrieved from the server via [**MI\_Session\_GetInstance**](/windows/previous-versions/Mi/nf-mi-mi_session_getinstance?branch=master). The following example function creates an instance with a hard-coded element (property) name of **Handle** and a value of **0**. For the [**Win32\_Process**](https://msdn.microsoft.com/library/aa394372) class (the class being used in this example), the **Handle** property is the process ID (PID) and the process with a PID of 0 is the System Idle Process. In a real-world scenario, you will want to specify the appropriate elements and values pursuant to the class you are attempting to obtain.

    ```C++
    MI_Result CreateSearchInstance(MI_Session *miSession, 
                                   _In_z_ const wchar_t *namespaceName, 
                                   _In_z_ const wchar_t *className, 
                                   MI_Boolean keysOnly, 
                                   MI_Instance **inboundInstance)
    {
        MI_Result miResult;

        MI_Operation miOperation = MI_OPERATION_NULL;
        MI_Class *miClass = NULL;
        MI_Boolean moreResults;
        MI_Char *errorMessage = NULL;
        MI_Instance *completionDetails = NULL;
        MI_Instance *miInstance = NULL;

        *inboundInstance = NULL;

        MI_Session_GetClass(miSession, 0, NULL, namespaceName, className, NULL, &amp;miOperation);
        MI_Operation_GetClass(&amp;miOperation, 
                              (const MI_Class**)&amp;miClass, 
                              &amp;moreResults, 
                              &amp;miResult, 
                              (const MI_Char**)&amp;errorMessage, 
                              (const MI_Instance**)&amp;completionDetails);

        if (miResult == MI_RESULT_OK)
        {
            MI_Application miApplication = MI_APPLICATION_NULL;
            miResult = MI_Session_GetApplication(miSession, &amp;miApplication);
            if (miResult == MI_RESULT_OK)
            {
                miResult = MI_Application_NewInstanceFromClass(&amp;miApplication, 
                                                               className, 
                                                               miClass, 
                                                               &amp;miInstance);
                if (miResult == MI_RESULT_OK)
                {
                    MI_Value miValue;
                    miValue.string = L"0";
                    miResult = MI_Instance_SetElement(miInstance, 
                                                      L"Handle", 
                                                      &amp;miValue, 
                                                      MI_STRING, 
                                                      0);
                }
            }
        }

        // Cleanup in case of error
        if ((miResult != MI_RESULT_OK) &amp;&amp; miInstance)
        {
            MI_Result _tmpResult = MI_Instance_Delete(miInstance);
            if (_tmpResult != MI_RESULT_OK)
            {
                wprintf(L"Failed to delete key instance. MI_Result: %ld\n", _tmpResult);
            }
        }

        {
            MI_Result _tmpResult = MI_Operation_Close(&amp;miOperation);
            if (_tmpResult != MI_RESULT_OK)
            {
                wprintf(L"MI_Operation_Close failed. MI_Result: %ld\n", _tmpResult);
            }
        }
            
        if (miResult == MI_RESULT_OK)
        {
            *inboundInstance = miInstance;
        }
        return miResult;
    }
    ```

    

6.  Call [**MI\_Session\_GetInstance**](/windows/previous-versions/Mi/nf-mi-mi_session_getinstance?branch=master) passing the key, or search, instance from the previous step.

    > [!Note]  
    > The following code uses a loop to enumerate the results of the [**MI\_Session\_GetInstance**](/windows/previous-versions/Mi/nf-mi-mi_session_getinstance?branch=master) function. While not technically necessary for this particular example - as this example will always return one instance - it's included to illustrate how you would enumerate the results of a call to **MI\_Session\_GetInstance** that returns multiple instances.

     

    ```C++
    void GetInstance(MI_Session* miSession, 
                     _In_z_ const wchar_t* namespaceName, 
                     const wchar_t* className,
                     MI_Instance* searchInstance)
    {
        MI_Result miResult = MI_RESULT_OK;

        MI_Operation miOperation = MI_OPERATION_NULL;
        MI_Session_GetInstance(miSession, 
                               0, 
                               NULL, 
                               namespaceName, 
                               searchInstance, 
                               NULL, 
                               &amp;miOperation);

        MI_Instance *miInstance = NULL;
        MI_Boolean moreResults;
        MI_Char *errorMessage = NULL;
        MI_Instance *completionDetails = NULL;
        do
        {
            miResult = MI_Operation_GetInstance(&amp;miOperation, 
                                                (const MI_Instance**)&amp;miInstance, 
                                                &amp;moreResults, 
                                                &amp;miResult, 
                                                (const MI_Char**)&amp;errorMessage, 
                                                (const MI_Instance**)&amp;completionDetails);
            if (miResult != MI_RESULT_OK)
            {
                wprintf(L"MI_Operation_GetInstance failed. MI_Result: %ld\n", miResult);
            }
            else
            {
                if (miResult != MI_RESULT_OK)
                {
                    wprintf(L"Operation failed: MI_Result=%ld, errorString=%s, errorDetails=\n", 
                            miResult, errorMessage);
                }
                else if (miInstance)
                {
                    MI_Value value;
                    MI_Type type;
                    MI_Uint32 flags;

                    miResult = MI_Instance_GetElement(miInstance,  // Instance
                                                      L"Name",     // Element (property) name
                                                      &amp;value,      // Element value
                                                      &amp;type,       // Element type
                                                      &amp;flags,      // Flags
                                                      NULL);       // Index
                    if (miResult != MI_RESULT_OK)
                    {
                        wprintf(L"MI_Instance_GetElement failed. MI_RESULT: %ld)\n", miResult);
                        return;
                    }
                    wprintf(L"Process Name: %s\n", value.string);
                }
                else if (moreResults == MI_TRUE)
                {
                    wprintf(L"More results are due and we have no instance, we will keep trying!\n");
                }
            }
        } while (moreResults == MI_TRUE);

        miResult = MI_Operation_Close(&amp;miOperation);
        if (miResult != MI_RESULT_OK)
        {
            wprintf(L"MI_Operation_Close failed. MI_Result: %ld\n", miResult);
        }
    }
    ```

    

7.  Delete key, or search, instance created earlier.

    ```C++
    miResult = MI_Instance_Delete(searchInstance);
    if (miResult != MI_RESULT_OK)
    { /* Handle error */ }
    ```

    

8.  Close the operation via [**MI\_Operation\_Close**](/windows/previous-versions/Mi/nf-mi-mi_operation_close?branch=master). All operations must be closed. If an operation is not closed, [**MI\_Session\_Close**](/windows/previous-versions/Mi/nf-mi-mi_session_close?branch=master) will block until all of its operations are closed. Also note that **MI\_Operation\_Close** will cancel an operation if it is still running. However, results must be consumed before **MI\_Operation\_Close** can complete. For synchronous operations (such as the example in this topic), **MI\_Operation\_Close** is blocked until the final result has been consumed (i.e., until the **moreResults** output parameters is set to **MI\_FALSE**).

    ```C++
    miResult = MI_Operation_Close(&amp;miOperation);
    if (miResult != MI_RESULT_OK)
    { /* Handle error */ }
    ```

    

9.  Close the MI session via [**MI\_Session\_Close**](/windows/previous-versions/Mi/nf-mi-mi_session_close?branch=master). If this function fails (reflected in the [**MI\_Result**](/windows/previous-versions/Mi/ne-mi-_mi_result?branch=master) return code), it is likely due to an invalid parameter, out of memory errors, or access denied. Invalid parameter means a programming error happened. When an out of memory error happens, the session will shut down as best it can. Access denied means the security context while calling the **MI\_Session\_Close** function is different than the one used when the session was created. This could happen if closing from a different thread and neglecting to impersonate.

    ```C++
    MI_RESULT miResult = MI_Session_Close(&amp;miSession, // Session
                                          NULL,       // Completion context
                                          NULL);      // Completion callback
    if (miResult != MI_RESULT_OK)
    { /* Handle error */ }
    ```

    

10. The last MI call that should be made is a call to [**MI\_Application\_Close**](/windows/previous-versions/Mi/nf-mi-mi_application_close?branch=master). Note that this call will block until all operations and sessions are fully closed.

    ```C++
    MI_RESULT miResult = MI_Application_Close(&amp;miApplication);
    if (miResult != MI_RESULT_OK)
    { /* Handle error */ }
    ```

    

## Example

The following code sample attempts to get the instance of the [**Win32\_Process**](https://msdn.microsoft.com/library/aa394372) class (which represents active processes) with a PID of 0 on the local machine, and if found, prints the name of process.

> [!Note]  
> In a real application you would define as parameters the computer name ("localhost"), CIM namespace ("root\\cimv2"), and class name ("Win32\_Process"). For purposes of simplicity, these have been hardcoded in this example.

 


```C++
#include "stdafx.h"
#include <mi.h>

MI_Result CreateSearchInstance(MI_Session *miSession, 
                               _In_z_ const wchar_t *namespaceName, 
                               _In_z_ const wchar_t *className, 
                               MI_Boolean keysOnly, 
                               MI_Instance **inboundInstance)
{
    MI_Result miResult;

    MI_Operation miOperation = MI_OPERATION_NULL;
    MI_Class *miClass = NULL;
    MI_Boolean moreResults;
    MI_Char *errorMessage = NULL;
    MI_Instance *completionDetails = NULL;
    MI_Instance *miInstance = NULL;

    *inboundInstance = NULL;

    MI_Session_GetClass(miSession, 0, NULL, namespaceName, className, NULL, &amp;miOperation);
    MI_Operation_GetClass(&amp;miOperation, 
                          (const MI_Class**)&amp;miClass, 
                          &amp;moreResults, 
                          &amp;miResult, 
                          (const MI_Char**)&amp;errorMessage, 
                          (const MI_Instance**)&amp;completionDetails);

    if (miResult == MI_RESULT_OK)
    {
        MI_Application miApplication = MI_APPLICATION_NULL;
        miResult = MI_Session_GetApplication(miSession, &amp;miApplication);
        if (miResult == MI_RESULT_OK)
        {
            miResult = MI_Application_NewInstanceFromClass(&amp;miApplication, 
                                                           className, 
                                                           miClass, 
                                                           &amp;miInstance);
            if (miResult == MI_RESULT_OK)
            {
                MI_Value miValue;
                miValue.string = L"0";
                miResult = MI_Instance_SetElement(miInstance, 
                                                  L"Handle", 
                                                  &amp;miValue, 
                                                  MI_STRING, 
                                                  0);
            }
        }
    }

    // Cleanup in case of error
    if ((miResult != MI_RESULT_OK) &amp;&amp; miInstance)
    {
        MI_Result _tmpResult = MI_Instance_Delete(miInstance);
        if (_tmpResult != MI_RESULT_OK)
        {
            wprintf(L"Failed to delete key instance. MI_Result: %ld\n", _tmpResult);
        }
    }

    {
        MI_Result _tmpResult = MI_Operation_Close(&amp;miOperation);
        if (_tmpResult != MI_RESULT_OK)
        {
            wprintf(L"MI_Operation_Close failed. MI_Result: %ld\n", _tmpResult);
        }
    }
        
    if (miResult == MI_RESULT_OK)
    {
        *inboundInstance = miInstance;
    }
    return miResult;
}

void GetInstanceAndPrintProperty(MI_Session* miSession, 
                 _In_z_ const wchar_t* namespaceName, 
                 const wchar_t* className,
                 MI_Instance* searchInstance)
{
    MI_Result miResult = MI_RESULT_OK;

    MI_Operation miOperation = MI_OPERATION_NULL;
    MI_Session_GetInstance(miSession, 
                           0, 
                           NULL, 
                           namespaceName, 
                           searchInstance, 
                           NULL, 
                           &amp;miOperation);

    MI_Instance *miInstance = NULL;
    MI_Boolean moreResults;
    MI_Char *errorMessage = NULL;
    MI_Instance *completionDetails = NULL;
    do
    {
        miResult = MI_Operation_GetInstance(&amp;miOperation, 
                                            (const MI_Instance**)&amp;miInstance, 
                                            &amp;moreResults, 
                                            &amp;miResult, 
                                            (const MI_Char**)&amp;errorMessage, 
                                            (const MI_Instance**)&amp;completionDetails);

            if (miResult != MI_RESULT_OK)
            {
                wprintf(L"Operation failed: MI_Result=%ld, errorString=%s, errorDetails=\n", 
                        miResult, errorMessage);
            }
            else if (miInstance)
            {
                MI_Value value;
                MI_Type type;
                MI_Uint32 flags;

                miResult = MI_Instance_GetElement(miInstance,  // Instance
                                                  L"Name",     // Element (property) name
                                                  &amp;value,      // Element value
                                                  &amp;type,       // Element type
                                                  &amp;flags,      // Flags
                                                  NULL);       // Index
                if (miResult != MI_RESULT_OK)
                {
                    wprintf(L"MI_Instance_GetElement failed. MI_RESULT: %ld)\n", miResult);
                    return;
                }
                wprintf(L"Process Name: %s\n", value.string);
            }
            else if (moreResults == MI_TRUE)
            {
                wprintf(L"More results are due and we have no instance, we will keep trying!\n");
            }
    } while (moreResults == MI_TRUE);

    miResult = MI_Operation_Close(&amp;miOperation); 
    if (miResult != MI_RESULT_OK)
    {
        wprintf(L"MI_Operation_Close failed. MI_Result: %ld\n", miResult);
    }
}

int _tmain(int argc, _TCHAR* argv[])
{
    MI_Result miResult = MI_RESULT_OK;

    MI_Application miApplication = MI_APPLICATION_NULL;
    miResult = MI_Application_Initialize(0,                   // Flags - Must be 0
                                         NULL,                // Application ID
                                         NULL,                // Extended error
                                         &amp;miApplication);     // Application
    if (miResult != MI_RESULT_OK)
    {
        wprintf(L"MI_Application_Initialize failed. MI_RESULT: %ld\n", miResult);
        return -1;
    }

    MI_Session miSession = MI_SESSION_NULL;
    miResult = MI_Application_NewSession(&amp;miApplication, // Application 
                                         L"WINRM",       // WimRM Protocol
                                         L"localhost",   // Machine destination
                                         NULL,           // Options
                                         NULL,           // Callbacks
                                         NULL,           // Extended error
                                         &amp;miSession);    // Session 
    if (miResult != MI_RESULT_OK)
    {
        wprintf(L"MI_Application_NewSession failed. MI_RESULT: %ld\n", miResult);
        return -1;
    }

    MI_Instance* searchInstance = NULL;
    miResult = CreateSearchInstance(&amp;miSession, L"root\\cimv2", L"Win32_Process", MI_TRUE, &amp;searchInstance);
    if (miResult != MI_RESULT_OK)
    {
        wprintf(L"Failed to create a keyed instance for the operation. MI_Result: %ld\n", miResult);
        return -1;
    }

    GetInstance(&amp;miSession, L"root\\cimv2", L"Win32_Process", searchInstance);    

    miResult = MI_Instance_Delete(searchInstance);
    if (miResult != MI_RESULT_OK)
    {
        wprintf(L"MI_Instance_Delete failed. MI_Result: %ld\n", miResult);
        return -1;
    }

    miResult = MI_Session_Close(&amp;miSession, NULL, NULL);
    if (miResult != MI_RESULT_OK)
    {
        wprintf(L"MI_Session_Close failed. MI_Result: %ld\n", miResult);
        return -1;
    }

    miResult = MI_Application_Close(&amp;miApplication);
    if (miResult != MI_RESULT_OK) 
    {
        wprintf(L"MI_Application_Close failed. MI_RESULT: %ld\n", miResult);
        return -1;
    }

    return 0;
}
```



 

 




