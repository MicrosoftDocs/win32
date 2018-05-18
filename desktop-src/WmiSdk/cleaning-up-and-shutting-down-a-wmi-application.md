---
Description: 'After you set the security levels for your IWbemServices pointer, you can access the various capabilities of WMI. After you finish using WMI, you must shut down your application.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '32bc7dd8-cb05-4354-bf46-f4359ac1f0d8'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: Cleaning up and Shutting Down a WMI Application
---

# Cleaning up and Shutting Down a WMI Application

After you set the security levels for your [**IWbemServices**](iwbemservices.md) pointer, you can access the various capabilities of WMI. After you finish using WMI, you must shut down your application.

The following procedure describes how to clean up and shut down a WMI application.

**To clean up and shut down a WMI application**

1.  Release any open COM interfaces.

    The two primary interfaces you must remember to release are [**IWbemServices**](iwbemservices.md) and [**IWbemLocator**](iwbemlocator.md).

2.  Call [**CoUninitialize**](_com_couninitialize).

    As with all COM applications, you must call [**CoUninitialize**](_com_couninitialize) at the end of your application.

3.  Exit your application.

    The following code example shows how to exit a WMI client application.

    ```C++
        // The following #include and #define statements need
        // to be used with this code:
        // #define _WIN32_DCOM
        // #include <wbemidl.h>  
        // #pragma comment(lib, "wbemuuid.lib")
        
        // pSvc was declared as IWbemServices *pSvc;
        // pLoc was declared as IWbemLocator *pLoc;

        pSvc->Release();
        pLoc->Release();     
        CoUninitialize();
        return 0;   // Program successfully completed.
    ```

    

    > [!Note]  
    > The `pSvc` variable is of type [**IWbemServices**](iwbemservices.md)\*, and the pLoc variable is of type [**IWbemLocator**](iwbemlocator.md)\*.

     

You have now successfully initialized COM, accessed WMI, and exited your application. For more information, see [Example: Creating a WMI Application](example-creating-a-wmi-application.md).

## Related topics

<dl> <dt>

[Creating a WMI Application Using C++](creating-a-wmi-application-using-c-.md)
</dt> </dl>

 

 



