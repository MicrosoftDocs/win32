---
title: Windows Remote Management and WMI
description: Windows Remote Management can be used to retrieve data exposed by Windows Management Instrumentation.
ms.assetid: a625440b-a839-487d-b862-e35934f24e1f
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Windows Remote Management and WMI

Windows Remote Management can be used to retrieve data exposed by Windows Management Instrumentation ([WMI](/windows/desktop/WmiSdk/wmi-start-page) and [MI](/previous-versions/windows/desktop/wmi_v2/windows-management-infrastructure)). You can obtain WMI data with scripts or applications that use the [WinRM Scripting API](winrm-scripting-api.md) or through the **Winrm** command-line tool.

WinRM supports most of the familiar WMI classes and operations, including embedded objects. WinRM can leverage WMI to collect data about [*resources*](windows-remote-management-glossary.md) or to manage resources on a Windows-based operating system. That means that you can obtain data about objects such as disks, network adapters, services, or processes in your enterprise through the existing set of [WMI classes](/windows/desktop/WmiSdk/wmi-classes). You can also access the hardware data that is available from the standard WMI [IPMI provider](/previous-versions/windows/desktop/ipmiprv/ipmi-provider).

## Identifying a WMI Resource

You can reference a WMI class as a [*resource*](windows-remote-management-glossary.md) in WinRM and in the WS-Management protocol: a type of managed entity, like a service or a disk.

A WMI class or method is identified by a [*URI*](windows-remote-management-glossary.md), just as any other resource is when using the WS-Management protocol. The URI can specify a WMI resource (class), a WMI action (method), or identify a specific instance of a class in [*messages*](windows-remote-management-glossary.md) sent over a network. For more information, see [Resource URIs](resource-uris.md).

## Constructing the URI Prefix for WMI Classes

The URI prefix contains a fixed part and the WMI namespace. For example, the URI prefix in Windows Server that contains the fixed part of the prefix is: `http://schemas.microsoft.com/wbem/wsman/1/wmi/<WmiNamespace>`. This allows the URI prefix to be generated for any WMI namespace. For example, to access the **root\\default** WMI namespace, use the following URI prefix: `http://schemas.microsoft.com/wbem/wsman/1/wmi/root/default/`.

The majority of the WMI classes for management are in the **root\\cimv2** namespace. To access classes and instances in **root\\cimv2** namespace, use the URI prefix: `http://schemas.microsoft.com/wbem/wsman/1/wmi/root/cimv2/`. For more information, see [Resource URIs](resource-uris.md).

## Generating a Complete URI for WMI Classes

The URI that you supply, either to the **Winrm** command-line tool or to a script, consists of the prefix plus the resource specification.

The following procedure describes how to generate a resource URI either to get a WMI class or to use in an enumerate operation.

**To generate a resource URI for a WMI class**

1.  Start with the prefix that indicates the WS-Management protocol schema should be used.

    https://schemas.microsoft.com/wbem/wsman/1

    The resource URI prefix for WMI classes is always the same. For more information, see [URI Prefixes](uri-prefixes.md).

2.  Add the WMI namespace to the prefix.

    `http://schemas.microsoft.com/wbem/wsman/1/wmi/root/cimv2/`

3.  Add the class name.

    `http://schemas.microsoft.com/wbem/wsman/1/wmi/root/cimv2/Win32\_Service`

4.  To set the value of a property, or to invoke a specific method, add the required key value or values for the class.

    `http://schemas.microsoft.com/wbem/wsman/1/wmi/root/cimv2/Win32\_Service?Name=Winmgmt`

    If you leave the key value blank, you will not alter the original property value.

    > [!Note]  
    > Leaving the key value blank sets the property value to **NULL**.

     

## Locating a WMI Resource with WinRM

You can obtain WMI data either through the command-line tool, **Winrm**, or through a Visual Basic script that uses the [WinRM Scripting API](winrm-scripting-api.md). You do not use a [WMI path](/windows/desktop/WmiSdk/describing-the-location-of-a-wmi-object) to locate a resource. Instead, you convert the WMI namespace and hierarchy to a [*URI*](windows-remote-management-glossary.md).

The WinRM URI for a WMI class contains two parts: the [URI prefix](uri-prefixes.md) and the class that you want to access.

For example, the following URI can be supplied to the [**Session.Enumerate**](session-enumerate.md) method to list all the services on a computer. The URI prefix is `http://schemas.microsoft.com/wbem/wsman/1/wmi/root/cimv2/`, and the class is [**Win32\_Service**](/windows/desktop/CIMWin32Prov/win32-service).

`strResourceUri = "http://schemas.microsoft.com/wbem/wsman/1/wmi/root/cimv2/Win32_CurrentTime"`

In WMI, list the data for all of the instances of a resource or class in several ways:

-   A query for all the instances of that resource.

    `Set colServices = objWMIService.ExecQuery("Select * from Win32_Service")`

-   A call to [**SWbemServices.InstancesOf**](/windows/desktop/WmiSdk/swbemservices-instancesof) or [**SWbemObject.Instances\_**](/windows/desktop/WmiSdk/swbemobject-instances-).

    `Set colServices = InstancesOf("Win32_Service")`

In WinRM, there is one way to list all of the instances of a resource: [**Session.Enumerate**](session-enumerate.md).


```VB
strResource = "http://schemas.microsoft.com/wbem/wsman/1/wmi/root/cimv2/Win32_Service"
Set colServices = objSession.Enumerate( strResource )
```



## Locating a Specific Instance of a WMI Resource

In WMI, you can designate a particular instance of a class either by specifying values for the key properties or by querying for an instance that matches a list of property values. Key properties have the WMI [**Key qualifier**](/windows/desktop/WmiSdk/key-qualifier).

You can obtain a specific instance of a class in several ways:

-   A call to [**Session.Enumerate**](session-enumerate.md) with the *filter* and *dialect* parameters to create a query.

    ```VB
    RemoteComputer = "servername.domain.com"
    strDialect = "http://schemas.microsoft.com/wbem/wsman/1/WQL"
    strResource = "http://schemas.microsoft.com/wbem/wsman/1/wmi/root/cimv2/*"
    Set objWsman = CreateObject("Wsman.Automation")
    Set objSession = objWsman.CreateSession("https://" & RemoteComputer)

    strFilter = "SELECT * FROM Win32_Share WHERE Name='Admin$'"
    Set objResultSet = objSession.Enumerate(strResource, strFilter, strDialect)
    ```

    

-   A call to [**SWbemServices.Get**](/windows/desktop/WmiSdk/swbemservices-get). For [**Session.Get**](session-get.md), you must supply one or more specific key values, preceded by a question mark (?).

    The format of the URI for a specific instance is `http://schemas.microsoft.com/wbem/wsman/1/wmi/root/cimv2/WMI\_Class?Key1=Value`.

    ```VB
    strResourceUri = "http://schemas.microsoft.com/wbem/wsman/1/wmi/root/cimv2/Win32_Service?Name=winmgmt"
    ```

    

    A WMI class may have more than one key. Key name-value pairs are separated by a "+" sign. In that case, the format is: `http://schemas.microsoft.com/wbem/wsman/1/wmi/root/cimv2/Win32\_Service?Key1=Value1+Key2=Value2`.

    The WinRM syntax to obtain a singleton WMI object is different from WMI. A singleton is a WMI class defined so that only one instance is allowed. [**Win32\_CurrentTime**](/previous-versions/windows/desktop/wmitimepprov/win32-currenttime) or [**Win32\_WMISetting**](/windows/desktop/CIMWin32Prov/win32-wmisetting) are examples of a WMI singleton class.

    The WMI syntax for singletons is shown in the following VBScript code example.

    ```VB
    Set TimeObject = objWMIService.Get("Win32_CurrentTime=@")
    ```

    

    The following example shows the WinRM singleton syntax which does not use "@".

    ```VB
    strResourceUri = "http://schemas.microsoft.com/wbem/wsman/1/wmi/root/cimv2/Win32_CurrentTime"
    ```

    

-   Adding a [*selector*](windows-remote-management-glossary.md) to a [**ResourceLocator**](resourcelocator.md) or [**IWSManResourceLocator**](/windows/desktop/api/WSManDisp/nn-wsmandisp-iwsmanresourcelocator) object.

    The following VBScript code example shows how to use a selector to get a specific instance of [**Win32\_Processor**](/windows/desktop/CIMWin32Prov/win32-processor).

    ```VB
    strUri = "http://schemas.microsoft.com/wbem/wsman/1/wmi/root/cimv2/Win32_Processor"
    Set objWsman = CreateObject("Wsman.Automation")
    Set Session = objWsman.CreateSession
    Set Locator = objWsman.CreateResourceLocator(strUri)
    Locator.AddSelector "DeviceID", "CPU0"
    ```

    

## Related topics

<dl> <dt>

[About Windows Remote Management](about-windows-remote-management.md)
</dt> <dt>

[URI Prefixes](uri-prefixes.md)
</dt> <dt>

[Resource URIs](resource-uris.md)
</dt> <dt>

[Scripting in Windows Remote Management](scripting-in-windows-remote-management.md)
</dt> </dl>
