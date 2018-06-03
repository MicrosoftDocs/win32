---
title: How to Enumerate All Instances of a Class (C/C++)
description: This topic provides step-by-step instructions for enumerating the instances of a specified CIM class using the Windows Management Infrastructure (MI) native API. In addition to the steps, a full source code example is provided at the end of the topic.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: FD5E9DD9-2B1A-4987-89A4-E397E69624B8
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# How to: Enumerate All Instances of a Class (C/C++)

This topic provides step-by-step instructions for enumerating the instances of a specified CIM class using the [Windows Management Infrastructure (MI) native API](Http://Go.Microsoft.Com/FWLink/p/?LinkID=308914). In addition to the steps, a full source code example is provided at the end of the topic.

> [!Note]  
> To see the [MI .NET API](Http://Go.Microsoft.Com/FWLink/p/?LinkID=308910) and Microsoft Visual C# version of this topic, refer to [How to: Enumerate All Instances of a Class (C)](how-to-enumerate-all-instances-of-a-class.md)

 

## Step-by-step Instructions

1.  Insert an include directive for the MI header file. (This file ships as part of the [Windows Software Development Kit (SDK) for Windows 8](Http://Go.Microsoft.Com/FWLink/p/?LinkID=306595).)

    ```C++
    #include <mi.h>
    ```

    

2.  Add the MI import library (**mi.lib**) to the project's linker dependencies. (This file ships as part of the [Windows Software Development Kit (SDK) for Windows 8](Http://Go.Microsoft.Com/FWLink/p/?LinkID=306595).)
3.  Initialize the application via [**MI\_Application\_Initialize**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_application_initializev1). It is recommended to have only one [**MI\_Application**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_application) per process. The **MI\_Application** returned from this function should always be closed, or de-initialized, via [**MI\_Application\_Close**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_application_close).

    ```C++
    MI_RESULT miResult = MI_Application_Initialize(0,               // Flags - Must be 0
                                                   NULL,            // Application ID
                                                   NULL,            // Extended error
                                                   &amp;miApplication); // Application 
    if (miResult != MI_RESULT_OK)
    { /* Handle error */ }
    ```

    

4.  Create an MI session against the specified destination (computer) with the specified protocol (WinRM, in this example) via [**MI\_Application\_NewSession**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_application_newsession). The session must be closed via [**MI\_Session\_Close**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_session_close).

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

    

5.  Enumerate the instances of the desired class via [**MI\_Session\_EnumerateInstances**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_session_enumerateinstances). In the following example, the code has hardcoded values for both the **namespaceName** and the **className** parameters.

    ```C++
    MI_Operation miOperation = MI_OPERATION_NULL;

    MI_Session_EnumerateInstances(miSession,       // Session 
                                  0,               // Flags
                                  NULL,            // Options
                                  "root\\cimv2",   // CIM Namespace
                                  "Win32_Process", // Class name
                                  MI_FALSE,        // Retrieve only keys
                                  NULL,            // Callbacks
                                  &amp;miOperation);   // Operation
    ```

    

6.  The [**MI\_Session\_EnumerateInstances**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_session_enumerateinstances) function (called in the previous step) returns an [**MI\_Operation**](/previous-versions/windows/desktop/api/Mi/ns-mi-_mi_operation). To retrieve the enumerated instances from that struct, you must call [**MI\_Operation\_GetInstance**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operation_getinstance) in a loop until it returns a **moreResults** value of **MI\_FALSE**. For each instances that is returned via **MI\_Operation\_GetInstance**, [**MI\_Instance\_GetElement**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_instance_getelement) is called to retrieve the desired property. The following code uses a simple do/while loop and outputs the **Name** property for all instances of the [**Win32\_Process**](https://msdn.microsoft.com/library/aa394372) class (representing all running processes).

    ```C++
    MI_Result miResult = MI_RESULT_OK;
    MI_Boolean moreResults;
    const MI_Char* errorString = NULL;
    MI_Uint32 instanceCount = 0;
    MI_Instance *miInstance;
    const MI_Instance* errorDetails = NULL;

    do {    
        miResult = MI_Operation_GetInstance(&amp;miOperation,                     // Operation
                                            (const MI_Instance**)&amp;miInstance, // Instance
                                            &amp;moreResults,                     // More results? 
                                            &amp;miResult,                        // Result
                                            &amp;errorString,                     // Error message
                                            &amp;errorDetails);                   // Completion details
        if (miResult != MI_RESULT_OK) {
            wprintf(L"MI_Operation_GetInstance failed. MI_RESULT: %ld\n", miResult);
            break;
        }

        if (miInstance) {
            MI_Value value;
            MI_Type type;   
            MI_Uint32 flags;

            miResult = MI_Instance_GetElement(miInstance,  // Instance
                                              L"Name",     // Element (property) name
                                              &amp;value,      // Element value
                                              &amp;type,       // Element type
                                              &amp;flags,      // Flags
                                              NULL);       // Index
            if (miResult != MI_RESULT_OK) {
               wprintf(L"MI_Instance_GetElement failed. MI_RESULT: %ld)\n", miResult);
               return;
            }

            wprintf(L"Process Name: %s\n", value.string);
            
            instanceCount++;
        }

    } while (miResult == MI_RESULT_OK &amp;&amp; moreResults == MI_TRUE);
    ```

    

7.  Close the operation via [**MI\_Operation\_Close**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_operation_close). All operations must be closed. If an operation is not closed, [**MI\_Session\_Close**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_session_close) will block until all of its operations are closed. Also note that **MI\_Operation\_Close** will cancel an operation if it is still running. However, results must be consumed before **MI\_Operation\_Close** can complete. For synchronous operations (such as the example in this topic), **MI\_Operation\_Close** is blocked until the final result has been consumed (i.e., until the **moreResults** output parameters is set to **MI\_FALSE**).

    ```C++
    miResult = MI_Operation_Close(&amp;miOperation);
    if (miResult != MI_RESULT_OK)
    { /* Handle error */ }
    ```

    

8.  Close the MI session via [**MI\_Session\_Close**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_session_close). If this function fails (reflected in the [**MI\_Result**](/previous-versions/windows/desktop/api/Mi/ne-mi-_mi_result) return code), it is likely due to an invalid parameter, out of memory errors, or access denied. Invalid parameter means a programming error happened. When an out of memory error happens, the session will shut down as best it can. Access denied means the security context while calling the **MI\_Session\_Close** function is different than the one used when the session was created. This could happen if closing from a different thread and neglecting to impersonate.

    ```C++
    MI_RESULT miResult = MI_Session_Close(&amp;miSession, // Session
                                          NULL,       // Completion context
                                          NULL);      // Completion callback
    if (miResult != MI_RESULT_OK)
    { /* Handle error */ }
    ```

    

9.  The last MI call that should be made is a call to [**MI\_Application\_Close**](/previous-versions/windows/desktop/api/Mi/nf-mi-mi_application_close). Note that this call will block until all operations and sessions are fully closed.

    ```C++
    MI_RESULT miResult = MI_Application_Close(&amp;miApplication);
    if (miResult != MI_RESULT_OK)
    { /* Handle error */ }
    ```

    

## Example

The following code sample enumerates all instances of the [**Win32\_Process**](https://msdn.microsoft.com/library/aa394372) class (which represents active processes) on the local machine, and prints the name of each process.

> [!Note]  
> In a real application you would define as parameters the computer name ("localhost"), CIM namespace ("root\\cimv2"), and class name ("Win32\_Process"). For purposes of simplicity, these have been hardcoded in this example.

 


```C++
#include "stdafx.h"
#include <mi.h>

void EnumerateAndPrintInstanceNames(MI_Session* miSession, 
                        _In_z_ const wchar_t* namespaceName, 
                        const wchar_t* className)
{
    MI_Operation miOperation = MI_OPERATION_NULL;

    MI_Session_EnumerateInstances(miSession,      // Session 
                                  0,              // Flags
                                  NULL,           // Options
                                  namespaceName,  // CIM Namespace
                                  className,      // Class name
                                  MI_FALSE,       // Retrieve only keys
                                  NULL,           // Callbacks
                                  &amp;miOperation);  // Operation

    MI_Result miResult = MI_RESULT_OK;
    MI_Boolean moreResults;
    const MI_Char* errorString = NULL;
    MI_Uint32 instanceCount = 0;
    MI_Instance *miInstance;
    const MI_Instance* errorDetails = NULL;

    do
    {
        //Note that each instance becomes invalid after getting the next instance in the loop or
        //after closing the operation. Call the MI_Instance_Clone function to use an instance 
        //past this. Be sure to MI_Instance_Delete to close the cloned instance when finished.

        miResult = MI_Operation_GetInstance(&amp;miOperation,                     // Operation 
                                            (const MI_Instance**)&amp;miInstance, // Instance
                                            &amp;moreResults,                     // More results?
                                            &amp;miResult,                        // Result
                                            &amp;errorString,                     // Error message
                                            &amp;errorDetails);                   // Completion details
        if (miResult != MI_RESULT_OK)
        {
            wprintf(L"MI_Operation_GetInstance failed. MI_RESULT: %ld\n", miResult);
            break;
        }
        //The following demonstrates using the instance just received.
        if (miInstance)  
        {
            MI_Value value;
            MI_Type type;
            MI_Uint32 flags;

            //Athough the Name property is shown here to demonstrate, you could substitute another property
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

            instanceCount++;
        }

    } while (miResult == MI_RESULT_OK &amp;&amp; moreResults == MI_TRUE);

    if (miResult != MI_RESULT_OK)
    {
        wprintf(L"Operation failed: MI_Result=%ld, errorString=%s\n", 
                miResult, errorString);
    }
    else
    {
        wprintf(L"Operation succeeded. Number of instances = %u\n", instanceCount);
    }

    miResult = MI_Operation_Close(&amp;miOperation);
    if (miResult != MI_RESULT_OK)
    {
        wprintf(L"MI_Operation_Close failed. MI_RESULT: %ld\n", miResult);
    }
}

int _tmain(int argc, _TCHAR* argv[])
{
    MI_Result miResult = MI_RESULT_OK;
    MI_Application miApplication = MI_APPLICATION_NULL;
    MI_Session miSession = MI_SESSION_NULL;
    MI_Operation miOperation = MI_OPERATION_NULL;

    miResult = MI_Application_Initialize(0,                   // Flags - Must be 0
                                         NULL,                // Application ID
                                         NULL,                // Extended error
                                         &amp;miApplication);     // Application
    if (miResult != MI_RESULT_OK)
    {
        wprintf(L"MI_Application_Initialize failed. MI_RESULT: %ld\n", miResult);
        return -1;
    }

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

    EnumerateAndPrintInstanceNames(&amp;miSession, L"root\\cimv2", L"Win32_Process");    

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



 

 




