---
description: After you set the security levels for your IWbemServices pointer, you can access the various capabilities of WMI. After you finish using WMI, you must shut down your application.
ms.assetid: 32bc7dd8-cb05-4354-bf46-f4359ac1f0d8
ms.tgt_platform: multiple
title: Cleaning up and Shutting Down a WMI Application
ms.topic: article
ms.date: 05/31/2018
---

# Cleaning up and Shutting Down a WMI Application

After you set the security levels for your [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) pointer, you can access the various capabilities of WMI. After you finish using WMI, you must shut down your application.

The following procedure describes how to clean up and shut down a WMI application.

**To clean up and shut down a WMI application**

1.  Release any open COM interfaces.

    The two primary interfaces you must remember to release are [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) and [**IWbemLocator**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemlocator).

2.  Call [**CoUninitialize**](/windows/win32/api/combaseapi/nf-combaseapi-couninitialize).

    As with all COM applications, you must call [**CoUninitialize**](/windows/win32/api/combaseapi/nf-combaseapi-couninitialize) at the end of your application.

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
    > The `pSvc` variable is of type [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices)\*, and the pLoc variable is of type [**IWbemLocator**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemlocator)\*.

     

You have now successfully initialized COM, accessed WMI, and exited your application. For more information, see [Example: Creating a WMI Application](example-creating-a-wmi-application.md).

## Related topics

<dl> <dt>

[Creating a WMI Application Using C++](creating-a-wmi-application-using-c-.md)
</dt> </dl>

 

 
