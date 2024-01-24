---
description: A class object path describes the location of a class within a namespace.
ms.assetid: 5ae95707-d023-4102-9b41-140c54b0c5b7
ms.tgt_platform: multiple
title: Describing a Class Object Path
ms.topic: article
ms.date: 05/31/2018
---

# Describing a Class Object Path

A class object path describes the location of a class within a namespace.

You can use the following methods to specify an object path:

-   A full object path to a class appends the class name to a namespace path.

    The following example shows the location of the [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) class within the \\root\\cimv2 namespace on the server named Admin.

    ``` syntax
    \\Admin\Root\CimV2:Win32_LogicalDisk
    ```

-   A relative object path represents a class that resides in the current namespace. A relative object path to a class contains only the class name.

    The following example shows the relative path to the [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) class.

    ``` syntax
    Win32_LogicalDisk
    ```

When you query for a class name but specify no instances, WMI returns the class definition. The following procedure describes how to retrieve a class definition in VBScript.

**To retrieve a class definition in VBScript**

-   You can use the moniker connection either with a query or [**GetObject**](https://msdn.microsoft.com/library/ebdktb00(v=VS.71).aspx). You can also use [**SWbemServices.Get**](swbemservices-get.md).

    The following example shows how to use [GetObject](/previous-versions//kdccchxa(v=vs.85)) to get a class definition.

    ```VB
    strComputer = "."
    Set objWMIService = GetObject("winmgmts:" _
       & "{impersonationLevel=impersonate}!\\" _
       & strComputer & "\root\cimv2:Win32_Printer")
    ```

    

    The following example shows how to query for a class definition.

    ```VB
    strComputer = "."
    Set objWMIService = GetObject("winmgmts:" _
        & "{impersonationLevel=impersonate}!\\" _
        & strComputer & "\root\cimv2")
    Set colInstalledPrinters =  objWMIService.ExecQuery _
        ("Select * from Win32_Printer")
    ```

    

You can retrieve a class definition in C++ by specifying only the class name and no path to a particular instance. The following procedure describes how to retrieve a class definition in C++.

**To retrieve a class definition in C++**

-   Make a call to the [**IWbemServices::GetObject**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobject) or [**IWbemServices::GetObjectAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobjectasync) functions.

    The following example shows how to call the[**IWbemServices::GetObject**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobject) function.

    ```C++
    IWbemServices* pSvcs = 0;

    BSTR Path = SysAllocString(L"Win32_LogicalDisk");
    IWbemClassObject *pDiskClass = 0;
    pSvcs->GetObject(Path, 0, 0, &pDiskClass, 0);
    ```

    

    The previous code example requires the following \#include statement to compile correctly.

    ```C++
    #include <wbemidl.h>
    ```

    

 

 
