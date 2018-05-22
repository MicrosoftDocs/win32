---
title: How to Test an MI Provider Using Windows PowerShell
description: PowerShell includes a cmdlet - Get-CimClass - that makes easy work of exercising an MI provider's classes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '15F435C7-E365-43F0-AD86-15DDFE717051'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
---

# How to: Test an MI Provider Using Windows PowerShell

PowerShell includes a cmdlet - [Get-CimClass](Http://Go.Microsoft.Com/FWLink/p/?LinkID=308964) - that makes easy work of exercising an MI provider's classes. This topic illustrates how to determine if a provider's class has been successfully registered on the local machine and how to test some of its intrinsic functions.

At this point, you should have a fully functional MI provider. If you created the provider, but did not add any logic, you won't be able to do much with it as most of the intrinsic functions - such as **Enumerate**, **Get**, **Delete**, **Modify**, and **Create** - post an **MI\_RESULT\_NOT\_SUPPORTED** value. This essentially means that it's just not implemented yet.

1.  On the target machine, open an **elevated** instance of PowerShell.
2.  Enter the following command to use the [Get-CimClass](Http://Go.Microsoft.Com/FWLink/p/?LinkID=308964) to list all the classes defined within the **root/StandardCimv2/sample** namespace. If a different namespace was used when the provider was registered, you'll need to modify the following accordingly.

    ```PowerShell
    Get-CimClass -Namespace root/StandardCimv2/sample
    ```

    

3.  To find a specific class - or group of classes - within a given namespace you would call the same [Get-CimClass](Http://Go.Microsoft.Com/FWLink/p/?LinkID=308964) cmdlet and specify a search string for the **ClassName** parameter. For example, the sample MOF file introduced in the [Generate an MI Provider from a MOF File](how-to-generate-an-mi-provider-from-a-mof-file.md) topic defined a class called **MSFT\_WindowsProcess**. To verify that this class was successfully registered, you can use the following command.

    ```PowerShell
    Get-CimClass -Namespace root/StandardCimv2/sample -ClassName MSFT_WindowsProcess
    ```

    

4.  Once you've determined that the provider has been registered successfully, you can start testing its intrinsic functions via the [Get-CimClass](Http://Go.Microsoft.Com/FWLink/p/?LinkID=308964) cmdlet. As mentioned earlier, if you have not implemented the intrinsic functions in your provider, attempting to run the following commands will return **MI\_RESULT\_NOT\_SUPPORTED**. To see an example of implementing the **MSFT\_WindowsProcess** class, download the [MI API Samples](Http://Go.Microsoft.Com/FWLink/p/?LinkID=306594) and look at the **MSFT\_WindowsProcess.c** and **WindowsProcess.c** files.

    > [!Note]  
    > Some of the following commands are split across multiple lines for display purposes. You should enter each call on a single line.

     

    ```PowerShell
    #Enumerate instances
    Get-CimInstance -ClassName MSFT_WindowsProcess -Namespace root/StandardCimv2/sample

    #Enumerate instances with keys only 
    Get-CimInstance -ClassName MSFT_WindowsProcess -Namespace root/StandardCimv2/sample -KeyOnly

    #Query Instances
    Get-CimInstance -query 'Select * from MSFT_WindowsProcess Where name like "svc%"' 
    -Namespace root/StandardCimv2/sample 

    #Query Instances with filter
    Get-CimInstance -ClassName MSFT_WindowsProcess -Namespace root/StandardCimv2/sample 
    -Filter 'name like "s%"' | Select Name

    #Get Instance
    $a,$b = Get-CimInstance -ClassName MSFT_WindowsProcess -Namespace root/StandardCimv2/sample
    Get-CimInstance -InputObject $a
    ```

    

> [!Note]  
> To learn how to write a Microsoft Visual C++ native MI client that will interface to an MI provider, see [How to: Implement a Native MI Client](how-to-implement-a-native-mi-client.md). To learn how to write a Microsoft Visual C# managed MI client that interfaces to an MI provider, see [How to: Implement a Managed MI Client](how-to-implement-a-managed-mi-client.md).

 

 

 




